import openai
import os
from dotenv import load_dotenv

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
        str: 生成された画像のURL。
    """
    response = openai.Image.create(
        prompt=f"{prompt}, {style}",
        n=1,
        size=size
    )
    return response['data'][0]['url']