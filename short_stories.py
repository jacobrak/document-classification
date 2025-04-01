import os
import requests
from bs4 import BeautifulSoup

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

# URL of the Gutenberg Short Stories Collection
gutenberg_url = "https://www.gutenberg.org/files/31554/31554-h/31554-h.htm"

# Fetch the page content
response = requests.get(gutenberg_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all <p> tags inside the text
paragraphs = soup.find_all("p")


story_texts = []
story = []
for para in paragraphs:
    text = para.get_text().strip()
    if text:  
        story.append(text)
        if len(story) >= 5:  
            story_texts.append("\n".join(story))
            story = []
        if len(story_texts) >= 100:  
            break

# Save each story as a separate text file
for i, story in enumerate(story_texts):
    with open(f"data/story_{i+1}.txt", "w", encoding="utf-8") as file:
        file.write(story)

print("done'")
