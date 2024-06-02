import streamlit as st
import download_image as di

# Get the data: title, text and image
text, title = di.get_data()

# Add title, image and text to the page
st.title(title)
st.image("apod.jpg")
st.write(text)
