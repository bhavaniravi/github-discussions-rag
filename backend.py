from embeddings import chroma_embedding
import subprocess
from fetch_data import fetch_discussions
from groq import Groq
from dotenv import load_dotenv
from embeddings.chroma_embedding import ChromaEmbedding
from fetch_data import fetch_discussions
import os
import os
import openai

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_TOKEN")
)

def get_project_name_from_github_url(url: str) -> str:
	return url.split('/')[-1]

def get_project_owner_from_github_url(url: str) -> str:
	return url.split('/')[-2]


def add_github_project(url: str) -> bool:
    project_name = get_project_name_from_github_url(url)
    owner = get_project_owner_from_github_url(url)
    embedding = chroma_embedding.ChromaEmbedding(collection_name=project_name)

    if not embedding.embedding_exists:
        data = fetch_discussions(owner, project_name)
        embedding.create_embedding(data)
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

    print (prompt)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    answer = response.choices[0].message.content
    return answer
