import streamlit as st
import requests

st.title("🔬 Microscope Madness")

zoomy = st.number_input("Magnification")
picture = st.number_input("Image Size")

if st.button("Reveal Truth"):
    r = requests.post("http://127.0.0.1:5000/micro",
                      json={"mag": zoomy, "img": picture})

    st.write("Real Size:", r.json()["real_size"])