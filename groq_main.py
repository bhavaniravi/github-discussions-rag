from groq import Groq
from dotenv import load_dotenv
from embeddings.chroma_embedding import ChromaEmbedding
from backend import add_github_project, get_answer
from fetch_data import fetch_discussions
import os
import os
import openai

load_dotenv()

project_url = "https://github.com/apache/airflow"
add_github_project(project_url)

while True:
    query = input('\nquery> ')
    answer = get_answer('airflow', query)
    print(answer)

