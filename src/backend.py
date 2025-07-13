from src.embeddings import chroma_embedding
from src.github.fetch_data import fetch_discussions
from src.utils import (
    get_project_name_from_github_url,
    get_project_owner_from_github_url,
)
from dotenv import load_dotenv
import os
import openai


load_dotenv()
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1", api_key=os.environ.get("GROQ_TOKEN")
)


def add_github_project(url: str, force_embed=False) -> bool:
    project_name = get_project_name_from_github_url(url)
    owner = get_project_owner_from_github_url(url)
    embedding = chroma_embedding.ChromaEmbedding(collection_name=project_name)

    if not embedding.embedding_exists or force_embed:
        data = fetch_discussions(owner, project_name)
        embedding.create_embedding(data)
        print(
            f"Project {owner}/{project_name} added with {len(data.questions)} questions."
        )
    if not os.path.exists(f"data/{project_name}/name.txt"):
        os.makedirs(f"data/{project_name}", exist_ok=True)
        with open(f"data/{project_name}/name.txt", "w") as f:
            f.write(f"{owner}/{project_name}")
    return True


def list_projects():
    import os

    return os.listdir("data")


def construct_prompt(project_name, query):
    embedding_obj = chroma_embedding.ChromaEmbedding(collection_name=project_name)
    prompt = f"""
    use the following CONTEXT to answer the QUESTION at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    CONTEXT: {embedding_obj.fetch_document(query)}
    QUESTION: {query}

    """
    return prompt


def get_answer(project_name, query) -> str:
    prompt = construct_prompt(project_name, query)

    print(prompt)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    answer = response.choices[0].message.content
    return answer
