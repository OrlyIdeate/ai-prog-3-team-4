from flask import Flask, render_template, request, send_file
import openai
import os
from dotenv import load_dotenv
import requests
from io import BytesIO
from services.openai_client import create_image
from services.translation import translate


app = Flask(__name__)
load_dotenv('.env')

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        selected_size = request.form.get('size')
        selected_style = request.form.get('style')
        
        # 日本語から英語に翻訳
        prompt = translate(prompt)
        
        if prompt:
            image_url = create_image(prompt, selected_size, selected_style)
            return render_template('index.html', image_url=image_url)
        else:
            error = "プロンプトを入力してください"
            return render_template('index.html', error=error)
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    image_url = request.args.get('image_url')
    response = requests.get(image_url)
    return send_file(BytesIO(response.content), as_attachment=True, download_name='generated_image.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)