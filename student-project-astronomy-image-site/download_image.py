import requests

# Set url and API key
API_KEY = "ltsk3Njpl5QVggBtvU8ijhYeRa6Jrh5fopBRNhDc"
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"


def get_data():
    # Get data through the API
    response = requests.get(URL)
    content = response.json()

    # Get the image url, the text and the title
    image_url = content['hdurl']
    text = content["explanation"]
    title = content["title"]

    #Download the image as raw content and save it as a jpg and return the values
    response = requests.get(image_url)
    with open("apod.jpg", "wb") as file:
        file.write(response.content)
    return text, title
