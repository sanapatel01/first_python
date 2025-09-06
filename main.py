import streamlit as st
#import pandas as pd


name = st.text_input("Enter your name: ")
fname = st.text_input("Enter your  father's name: ")
adr = st.text_area("Enter your Address: ")
classdata = st.selectbox("Enter your class :",("B.Tech","M.Tech","MBA","BBA"))

button = st.button("Done")
if button :
    st.markdown(f"""
                Name : {name}
                Fathers Name : {fname}
                address : {adr}    
               """ )
