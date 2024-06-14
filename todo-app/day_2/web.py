import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This is an app to increase your productivity")

for idx, todo in enumerate(todos):
    st.checkbox(label=todo)

st.text_input(label="", placeholder="Add new todo...")

print("Hello")