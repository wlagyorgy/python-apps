import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This is an app to increase your productivity")

for idx, todo in enumerate(todos):
    st.checkbox(label=todo)

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

print("Hello")

st.session_state