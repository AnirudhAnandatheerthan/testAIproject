import streamlit as st
import pandas as pd
from pandasai import Agent
from PIL import Image
import os

st.title("PandasAI chat")
# st.header("Header")
st.subheader("Here is a dataframe:")
os.environ['PANDASAI_API_KEY'] = '$2a$10$fG0XgS85l0mYxtWXCU/AaOlrShJVq.WIAtOpjkEUmimlbV9Utk/Ve'
addresses = pd.read_csv(
    'https://raw.githubusercontent.com/codeforamerica/ohana-api/master/data/sample-csv/addresses.csv')

st.write(addresses)

black_hole = Image.open(
    r"C:\Users\aniru\OneDrive\Desktop\School\black-hole-artwork-royalty-free-illustration-1616081355_.jpg")
st.image(black_hole)

prompt = st.chat_input("Ask the Chat bot anything from the dataframe")


def response():
    if prompt:
        st.write("Pandas AI chat:", {prompt})
        agent = Agent(addresses)
        reply = agent.chat(prompt)
        # st.write_stream(Reply)
        st.write(reply)


response()
