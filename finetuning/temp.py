from openai import OpenAI
client = OpenAI(api_key="openai_api_key")

response = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-1106:personal::8eovJ1Vq",
  messages=[
    {"role": "system", "content": "You are a Bollywood lyricist and will generate Bollywood songs lyrics and title based on the user input, which is news content of an article. The song lyrics need to be mostly in Hindi and might include English in between. Do not include the translation to these lyrics. The song title should be based on a Bolywood Movie name."},
    {"role": "user", "content": "Ex-Indian high commissioner Ajay Bisaria has revealed the inside story of how India's post-Pulwama coercive diplomacy spooked Pakistan, forcing it to rethink its terror policy. The Pakistan government, spooked by 9 Indian missiles apparently pointed at them, reached out to Ajay Bisaria, the Indian high commissioner, to facilitate a conversation between Imran Khan and PM Narendra Modi. Bisaria checked with people in Delhi and got back to the Pakistanis, saying PM Modi wasn’t available at that hour and that any urgent message could be conveyed to the high commissioner himself. Bisaria didn’t hear from them again that night."}
  ],
)



content = response.choices[0].message.content

song_title_start = content.find("Song Title: '") + len("Song Title: '")
song_title_end = content.find("'", song_title_start)
song_title = content[song_title_start:song_title_end]



print(content)
print("Song Title:", song_title)