import os
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from fetch_data import fetch_discussions
import os
from embeddings.embeddings import Embedding
from embeddings.chroma_embedding import ChromaEmbedding
# from test import data

load_dotenv()

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
token = os.environ["GITHUB_TOKEN"]

print ("constructing embedding object")

embedding = "chroma"
if embedding == "chroma":
    embedding_obj = ChromaEmbedding()
else:
    embedding_obj = Embedding()

data = fetch_discussions()
embedding_obj.create_embedding(data)

print ("embedding object constructed")

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

while True:
    query = input('\nquery> ')

    prompt = f"""
    use the following CONTEXT to answer the QUESTION at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    CONTEXT: {embedding_obj.fetch_document(query)}
    QUESTION: {query}

    """

    print ("document fetched", prompt)

    response = client.complete(
        messages=[
            SystemMessage("You're an Q and A agent who answers questions based on the rag"),
            UserMessage(prompt)
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )
    print ("fetching llm response...")
    print(response.choices[0].message.content)

