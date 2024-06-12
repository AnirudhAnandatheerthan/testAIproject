import streamlit as st
from PIL import Image
st.title("Trial")
st.header("Header")
st.subheader("This is a trial website using Streamlit")
st.write("Hello World")

black_hole =  Image.open(r"C:\Users\aniru\OneDrive\Desktop\School\black-hole-artwork-royalty-free-illustration-1616081355_.jpg")
st.image(black_hole)

st.text_input("Give me a review")

