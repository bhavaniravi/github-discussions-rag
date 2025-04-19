import os
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

from embeddings import Embedding
from test import data

load_dotenv()

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
token = os.environ["GITHUB_TOKEN"]
embedding_obj = Embedding(data)


client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

query = input('query>')

prompt = f"""
use the following CONTEXT to answer the QUESTION at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

CONTEXT: {embedding_obj.fetch_document(query)}
QUESTION: {query}

"""

response = client.complete(
    messages=[
        SystemMessage("You're an Q and A agent who answers questions based on the rag"),
        UserMessage(prompt)
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

print(response.choices[0].message.content)

