import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv('.env')

openai.api_key = os.getenv('OPENAI_API_KEY')

st.title("画像生成App")

prompt = st.text_input("どのような画像を生成したいですか:")

# サイズ選択オプション
size_options = ["256x256", "512x512", "1024x1024"]
selected_size = st.selectbox("画像のサイズを選択:", size_options)

# スタイル選択オプション
style_options = ["リアル", "アニメ", "抽象", "幻想的"]
selected_style = st.selectbox("画像のスタイルを選択:", style_options)

if st.button("画像を生成"):
    if prompt:
        with st.spinner("画像を生成中..."):
            response = openai.Image.create(
                prompt=f"{prompt}, {selected_style}",
                n=1,
                size=selected_size
            )
            image_url = response['data'][0]['url']
            st.image(image_url, caption='Generated Image')

            # ダウンロードボタン
            st.download_button("画像をダウンロード", image_url, "generated_image.png", "image/png")
    else:
        st.error("プロンプトを入力してください")
