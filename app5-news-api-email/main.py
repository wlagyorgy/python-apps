import requests

api_key = "f13d0d99d61946cea6248448e17fba50"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-12-23&sortBy=publishedAt\
        &apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
# print(content)
for article in content["articles"]:
    print(article["title"])
    print(article["description"])


