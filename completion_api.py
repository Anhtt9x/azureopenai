import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_type = "azure"
openai.api_version = "2023-09-15-preview",
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

response = openai.completions.create(
    prompt="",
    temperature=1,
    max_tokens=100,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)


print(response)