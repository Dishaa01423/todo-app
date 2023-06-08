import streamlit as st
import python12

todos = python12.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    python12.write_todos(todos)

todos = python12.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to denote the task you have to complete.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder=" Add a new todo...",
              on_change=add_todo, key ="new_todo")

