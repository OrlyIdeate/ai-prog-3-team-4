import openai
import os
from dotenv import load_dotenv

load_dotenv('.env')
openai.api_key = os.getenv('OPENAI_API_KEY')

def create_image(prompt, size, style):
    response = openai.Image.create(
        prompt=f"{prompt}, {style}",
        n=1,
        size=size
    )
    return response['data'][0]['url']