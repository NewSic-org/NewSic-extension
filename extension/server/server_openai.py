import pathlib
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os
from openai import OpenAI
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

env_path = pathlib.Path('.') / '.local.env'
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MONGO_DB_URI = os.getenv('MONGO_DB_URI')

#Database connection
client = OpenAI(api_key=OPENAI_API_KEY)
client_db = MongoClient(MONGO_DB_URI)
db = client_db.get_database('newsic')
records = db.articles

@app.route('/process-title', methods=['POST'])
def process_title():
    data = request.get_json()
    title = data.get('title', '')
    summary = data.get('summary', '')
    if records.find_one({'art_title':title}):
        db_song_title = records.find_one({'art_title':title})['song_title']
        db_song = records.find_one({'art_title':title})['song']
        return jsonify({'title': db_song_title, 'generatedContent': db_song})
    generated_content = generate_content_with_openai(summary, title)
    #sending the title and summary to the function to be used in db
    return generated_content

def generate_content_with_openai(summary, art_title):
    response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-1106:personal::8eovJ1Vq",
    messages=[
        {"role": "system", "content": "You are a Bollywood lyricist and will generate Bollywood songs lyrics and title based on the user input, which is news content of an article. The song lyrics need to be mostly in Hindi and might include English in between. Do not include the translation to these lyrics."},
        {"role": "user", "content": f"{summary}"}
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

    #putting the data int the database, every time the model is called
    new_song = {
        'summary': summary,
        'art_title': art_title,
        'song': content,
        'song_title': song_title
    }
    records.insert_one(new_song)
    return jsonify({'title': song_title, 'generatedContent': content})

@app.route('/api/data', methods=['GET'])
def get_data():
    articles = db.articles.find({}, {"_id": 0})
    articles_list = list(articles)
    return jsonify(articles_list)

@app.route('/api/data/headlines' ,methods=['GET'])
def headlines():
    headlines = db.articles.find({}, {"art_title": 1, "_id": 0})
    headlines_list = [article["art_title"] for article in headlines]
    return jsonify({"headlines": headlines_list})

@app.route("/", methods=['GET'])
def home():
    return "Connection Succesful"

if __name__ == '__main__':
    app.run()
