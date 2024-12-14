import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="",
    api_key=os.environ["AZURE_OPENAI_API_KEY"]
)

result = client.images.generate(
    model="dall-e-3",
    prompt="",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)