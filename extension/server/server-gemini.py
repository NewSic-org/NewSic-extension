import pathlib
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

env_path = pathlib.Path('.') / '.local.env'
load_dotenv(dotenv_path=env_path)

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the generativeai library with the API key
genai.configure(api_key=GOOGLE_API_KEY)


@app.route('/process-title', methods=['POST'])
def process_title():
    data = request.get_json()
    title = data.get('title', '')
    # summary = data.get('summary', '')

    # Use the title with the Gemini model
    generated_content = generate_content_with_gemini(title)
    title_name = generate_title_with_gemini(title)

    return jsonify({'title': title_name, 'generatedContent': generated_content})

def generate_title_with_gemini(title):
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    model = genai.GenerativeModel('gemini-pro')
    response2 = model.generate_content(f"It should change the title into a fictional Bollywood/Indian movie name. The title is {title}")

    return response2.text


def generate_content_with_gemini(title):
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"Write a Bollywood song based on {title}. The song should be in Hindi language but written in English and based on the contents of the summary.")

    return response.text

if __name__ == '__main__':
    app.run(port=5000)
