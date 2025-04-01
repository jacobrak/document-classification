import requests

def get_random_wikipedia_articles(n=2):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": n,  # Number of articles
        "rnnamespace": 0  # 0 = Main articles (excludes talk, user pages, etc.)
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    for article in data["query"]["random"]:
        title = article["title"]
        articles.append(title)
    
    return articles

def get_wikipedia_page(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "explaintext": True
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extract text content
    pages = data["query"]["pages"]
    for page in pages.values():
        if "extract" in page:
            return page["extract"]
    return None

def data_to_text(data: list):
    for i, title in enumerate(data):
        article = get_wikipedia_page(title)
        with open(f"data/wikipedia_{i + 1}", "w", encoding="utf-8") as file:
            file.write(article)

# Main
if __name__ == "__main__":
    titles = get_random_wikipedia_articles(100)
    data_to_text(titles)