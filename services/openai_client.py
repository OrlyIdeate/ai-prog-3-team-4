import openai
import os
from dotenv import load_dotenv
import requests

load_dotenv('.env')
openai.api_key = os.getenv('OPENAI_API_KEY')

def create_image(prompt: str, size: str, style: str) -> str:
    """
    指定されたプロンプト、サイズ、およびスタイルに基づいて画像を生成します。

    Args:
        prompt (str): 画像生成のためのテキストプロンプト。
        size (str): 生成する画像のサイズ（例: "1024x1024"）。
        style (str): 画像のスタイルを指定するテキスト。

    Returns:
        list: 生成された画像のURLのリスト。
    """
    first_resopnse = openai.Image.create(
        model="dall-e-3",
        prompt=f"{prompt}, {style}",
        n=1,
        size=size
    )
    first_image_url = first_resopnse['data'][0]['url']
    
    image_data = requests.get(first_image_url).content
    
    variation_response = openai.Image.create_variation(
        image=image_data,
        n=3,
        size=size
    )
    
    variation_urls = [variation['url'] for variation in variation_response['data']]
    
    return [first_image_url] + variation_urls