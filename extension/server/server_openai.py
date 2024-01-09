import pathlib
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os
from openai import OpenAI
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

env_path = pathlib.Path('.') / '.local.env'
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

@app.route('/process-title', methods=['POST'])
def process_title():
    data = request.get_json()
    title = data.get('title', '')
    generated_content = generate_content_with_openai(title)
    return generated_content

def generate_content_with_openai(title):
    response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-1106:personal::8eovJ1Vq",
    messages=[
        {"role": "system", "content": "You are a Bollywood lyricist and will generate Bollywood songs lyrics and title based on the user input, which is news content of an article. The song lyrics need to be mostly in Hindi and might include English in between. Do not include the translation to these lyrics. The title should be a fictional Bollywood/Indian movie name."},
        {"role": "user", "content": f"{title}"}
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    content = response.choices[0].message.content
    song_title_start = content.find("Song Title: '") + len("Song Title: '")
    song_title_end = content.find("'", song_title_start)
    song_title = content[song_title_start:song_title_end]

    return jsonify({'title': song_title, 'generatedContent': content})

if __name__ == '__main__':
    app.run(port=5000)
