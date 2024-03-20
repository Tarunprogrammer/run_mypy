import streamlit as st
import pandas as pd

st.title("WELCOME TO SeeInMatic")
st.header("Feel The Pixel")
st.subheader("Every frame of a video is an opportunity to create something extraordinary.")

name = st.text_input("ENTER YOUR NAME : ")
fathername = st.text_input("ENTER YOUR FATHER NAME : ")
adr = st.text_area("ENTER YOUR ADDRESS : ")
classdata = st.selectbox("ENTER YOUR CLASS :",(1,2,3,4,5,6,7,8,9,10))

button = st.button("DONE")
if button :
     st.markdown(f""""
     name : {name}
     fathername : {fathername}
     address : {adr}
     class : {classdata}""")

