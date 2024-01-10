# NewSic

![Newsic](https://github.com/gSayak/NewSic/assets/88048601/aa8bf995-ec61-41a4-9380-ab3cfdd60d56)

## Overview

**NewSic** is a browser extension that transforms any news article into a Bollywood/Indian song. The title of the article is replaced with the name of a fictional Bollywood movie based on the content of the article.

## Features

- Convert news articles into Bollywood songs.
- Replace article titles with fictional Bollywood movie names.
- Add a touch of entertainment to your news reading experience.

## How it Works

The extension utilizes powerful language models, specifically a fine-tuned version of OpenAI's GPT-3.5-turbo, to generate Bollywood-style song lyrics and movie titles based on the content of news articles.

### Backend

- The backend of NewSic runs on a custom fine-tuned OpenAI GPT-3.5-turbo model, providing more accurate and personalized Bollywood-style content.
- For now I am hosting the backend using a Flask server, as making the API call using just the JS directly to openAI had the chance of my API getting exhausted(and I did have to beg someone for the credit card.. so that would not be ideal)

## Installation

1. Download the extension files or clone the repository.

2. Open your Chrome browser and go to `chrome://extensions/`.

3. Enable "Developer mode" in the top right corner.

4. Click on "Load unpacked" and select the folder containing the extension files. `(extension -> NewSic)`

6. The NewSic extension will be added to your Chrome browser.

7. Open `server -> server-openai.py` and add the details of your model which can be trained using the `dataLLM.jsonl` data provided.

8. Run the `server-openai.py` and open to `https://economictimes.indiatimes.com/` and click on any article.

## Usage

1. Open `https://economictimes.indiatimes.com/` (currently only that site is added)

2. Read a news article.

3. Witness the magic as the article is transformed into a fictional Bollywood song.

## Disclaimer

This extension is for entertainment purposes only and may not accurately represent Bollywood song styles. The generated content is fictional and not associated with real Bollywood productions.

## License

This project is licensed under the [MIT License](LICENSE).


Feel free to contribute or report issues! 🚀

