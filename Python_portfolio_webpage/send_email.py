import smtplib, ssl
import os

import requests

topic = "tesla"
api_key = "f13d0d99d61946cea6248448e17fba50"
url = "https://newsapi.org/v2/everything?"\
        f"q={topic}&" \
        "from=2023-11-04&sortBy=publishedAt&"\
        "apiKey=f13d0d99d61946cea6248448e17fba50&"\
        "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
full_message = ""
for article in content["articles"][:20]:
    if article['title'] is not None:
        full_message += f"Subject: Today's news\
                        {article['title']} \n \
                        {article['description']} \n {article['url']} \n\n "


def send_email(message):
    host = "smtp.gmail.com"
    port = 456

    username = "don.georgleone@gmail.com"
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()
    receiver = "wlagyorgy@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)

        server.sendmail(username, receiver, message)


send_email(full_message)
