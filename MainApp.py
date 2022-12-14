import streamlit as st

from PIL import Image

img = Image.open('logo.png')

st.set_page_config(page_icon=img)

st.title("Welcome to Heroku Deployment")

st.markdown("----")
st.subheader("How do we deploy Streamlit applications on Heroku?")

st.image(img)
