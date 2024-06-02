import streamlit as st
import pandas
st.set_page_config(layout="wide")


st.title("The Best Company")
content1 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna 
 aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
 ullamco laboris nisi ut aliquip ex ea commodo consequat
"""

st.write(content1)

st.subheader("Our Team")
col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        name = f"{row['first name']} {row['last name']}".title()
        st.header(name)
        st.text(row['role'])
        st.image("images/" + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        name = f"{row['first name']} {row['last name']}".title()
        st.header(name)
        st.text(row['role'])
        st.image("images/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        name = f"{row['first name']} {row['last name']}".title()
        st.header(name)
        st.text(row['role'])
        st.image("images/" + row['image'])

