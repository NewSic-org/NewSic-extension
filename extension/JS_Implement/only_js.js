const title = document.querySelector('h1.title');
const title2 = document.querySelector('h1.artTitle.font_faus');
const summary = document.querySelector('h2.summary');

if (title) {
    title = title;
    
} else if (title2) {
    title = title2;
}

const OPENAI_API_KEY = OPEN_AI_KEY;
const apiUrl = "https://api.openai.com/v1/chat/completions";
// const title = "'Qatal ki Raat': How PM Modi declined Imran Khan’s midnight call"
const requestBody = {
  model: "ft:gpt-3.5-turbo-1106:personal::8eovJ1Vq",
  messages: [
    {
        role: "system", 
        content: "You are a Bollywood lyricist and will generate Bollywood songs lyrics and title based on the user input, which is news content of an article. The song lyrics need to be mostly in Hindi and might include English in between. Do not include the translation to these lyrics. The title should be a fictional bolywood movie name based on the content"
    },
    {
      role: "user",
      content: {title},
    },
    
  ],
  temperature: 1,
  max_tokens: 256,
  top_p: 1,
  frequency_penalty: 0,
  presence_penalty: 0,
};

fetch(apiUrl, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${OPENAI_API_KEY}`,
  },
  body: JSON.stringify(requestBody),
})
  .then((response) => response.json())
  .then((data) => {
    console.log(data);

    const generatedContent = data.generatedContent;
    console.log(generatedContent);
    const generatedTitle = data.title;
    if (title) {
        title.innerHTML = generatedTitle;
    } else if (title2) {
        title2.innerHTML = generatedTitle;
    }

  })
  .catch((error) => console.error("Error:", error));


