""" this is the main file for the web app """

import streamlit as st
import functions as fn


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    if todo:
        fn.add_todos(todos)


st.title("My todo app")
st.subheader("This is a simple todo app")
st.write("This app is for increasing productivity")

todos = fn.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(
    label="Add new todo",
    placeholder="Type new todo...",
    key="new_todo",
    on_change=add_todo,
)
