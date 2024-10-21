import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv('.env')

openai.api_key = os.getenv('OPENAI_API_KEY')

st.title("画像生成App")

prompt = st.text_input("どのような画像を生成したいですか:")

if st.button("画像を生成"):
    if prompt:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        st.image(image_url, caption='Generated Image')
    else:
        st.error("プロンプトを入力してください")