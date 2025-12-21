import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Ladda .env
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": "Svara med exakt text: OK – Azure OpenAI fungerar."},
        {"role": "user", "content": "test"}
    ]
)

print(response.choices[0].message.content)
