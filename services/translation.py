from deepl import Translator
from dotenv import load_dotenv
import os
import langdetect

def translate(text):
    '''日本語から英語に翻訳'''
    load_dotenv('.env')
    translator = Translator(os.getenv('DEEPL_API_KEY'))
    
    # テキストが英語かどうかを判定
    detected_lang = langdetect.detect(text)
    if detected_lang == 'en':
        return text
    
    result = translator.translate_text(text, source_lang='JA', target_lang='EN-US')
    return result