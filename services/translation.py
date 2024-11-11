import requests
from dotenv import load_dotenv
import os

def translate(text):
    load_dotenv('.env')
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        "auth_key": os.getenv('DEEPL_API_KEY'),
        "text": text,
        "source_lang": "JA",
        "target_lang": "EN"
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        result = response.json()
        return result.get('translations')[0].get('text')
    else:
        response.raise_for_status()