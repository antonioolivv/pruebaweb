import streamlit as st 
import pandas as pd 
st.write("My First Streamlit Web App")
df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)
weight=st.slider('How fat are you in kgs?', 0, 130, 10)
height=st.slider('How tall are you in kgs?', 0, 200, 10)
size=pd.dataframe("height":[],"weight":[])
session_state = SessionState.get(df=size)

if st.button("Save it"):
  session_state.df=session_state.df.append({"height": height,"weight":weight}ignore_index=True)
  st.text("Updated dataframe")
  st.dataframe(session_state.df)
                                           
                                            
  
st.bar_chart(size)
