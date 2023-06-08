import streamlit as st
import python12

todos = python12.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to denote the task you have to complete.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder=" Add a new todo...")

