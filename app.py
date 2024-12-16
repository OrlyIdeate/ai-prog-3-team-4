from flask import Flask, render_template, request, send_file
import requests
from io import BytesIO
from services.openai_client import create_image
from services.translation import translate


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        origin_prompt = request.form.get('prompt')
        selected_size = request.form.get('size')
        selected_style = request.form.get('style')
        
        # 日本語から英語に翻訳
        translated_prompt = translate(origin_prompt)
        
        if translated_prompt:
            image_urls = create_image(translated_prompt, selected_size, selected_style)
            return render_template('result.html', image_urls=image_urls, origin_prompt=origin_prompt, prompt=translated_prompt, size=selected_size, style=selected_style)
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