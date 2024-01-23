const title = document.querySelector("h1.title");
const title2 = document.querySelector("h1.artTitle.font_faus");
const summary = document.querySelector("h2.summary");

if (title && summary) {
  requestBody = { title: title.innerText, summary: summary.innerText };
} else if (title2 && summary) {
  requestBody = { title: title2.innerText, summary: summary.innerText };
}
// if (summary) {
//   requestBody_sum = { title: summary.innerText };
// }

if (title2 || title) {
  (async () => {
    try {
      const response = await fetch(
        "https://newsic-server.vercel.app/process-title",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(requestBody),
        }
      );

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      const generatedContent = data.generatedContent;
      const generatedTitle = data.title;
      console.log(generatedContent);
      console.log(generatedTitle);

      const generatedContentDiv = document.getElementById(
        "generatedContentDiv"
      );
      if (generatedContentDiv) {
        generatedContentDiv.innerHTML = generatedContent;
      }

      if (summary) {
        summary.innerHTML = generatedContent;
      }

      if (title) {
        title.innerHTML = generatedTitle;
      } else if (title2) {
        title2.innerHTML = generatedTitle;
      }
    } catch (error) {
      console.error("Error:", error);
    }
  })();
}
