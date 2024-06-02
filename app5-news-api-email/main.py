import requests

api_key = "f13d0d99d61946cea6248448e17fba50"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-03&sortBy=publishedAt\
        &apiKey=f13d0d99d61946cea6248448e17fba50"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])


