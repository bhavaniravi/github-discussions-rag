import os
from dotenv import load_dotenv()
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

prompt = input()

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

