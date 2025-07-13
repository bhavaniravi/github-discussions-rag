from dotenv import load_dotenv
from src.backend import add_github_project, get_answer

load_dotenv()

project_url = "https://github.com/apache/airflow"
add_github_project(project_url)

while True:
    query = input("\nquery> ")
    answer = get_answer("airflow", query)
    print(answer)
