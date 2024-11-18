from deepl import Translator
from dotenv import load_dotenv
import os

def translate(text):
    '''日本語から英語に翻訳'''
    load_dotenv('.env')
    translator = Translator(os.getenv('DEEPL_API_KEY'))
    result = translator.translate_text(text, source_lang='JA', target_lang='EN-US')
    return result