from flask import Flask, render_template, request, send_file
import openai
import os
from dotenv import load_dotenv
import requests
from io import BytesIO

app = Flask(__name__)
load_dotenv('.env')

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        selected_size = request.form.get('size')
        selected_style = request.form.get('style')
        
        if prompt:
            response = openai.Image.create(
                prompt=f"{prompt}, {selected_style}",
                n=1,
                size=selected_size
            )
            image_url = response['data'][0]['url']
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