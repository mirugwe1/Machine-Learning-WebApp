import streamlit as st

with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("AutoML")
    choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
    st.info("This project application helps you build and explore your data.")

if choice == "Upload":
    file = st.file_uploader("Upload Your Dataset Here")
    if file:
        #activity
        pass


if choice == "Profiling":
    pass

if choice == "Modelling":
    pass

if choice == "Download":
    pass