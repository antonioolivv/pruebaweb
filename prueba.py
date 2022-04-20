import streamlit as st 
import pandas as pd 
st.write("My First Streamlit Web App")
df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)
weight=st.slider('How fat are you in kgs?', 0, 130, 10)
height=st.slider('How tall are you in kgs?', 0, 200, 10)
st.metric("This is you",weight,height)
