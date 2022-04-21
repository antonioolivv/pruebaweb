pip install pillow

import streamlit as st 
import pandas as pd 
import pillow as pil
st.write("My First Streamlit Web App")
df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)
columnnames=["height","weight"]
size=pd.DataFrame(columns=columnnames)

weight=st.slider('How fat are you in kgs?', 0, 130, 10)
height=st.slider('How tall are you in cms?', 0, 200, 10)
if st.button("Save it"):
    size.df=size.append({"height": height,"weight":weight},ignore_index=True)
    st.text("Updated dataframe")
    size=size.df
    st.dataframe(size)
    
st.bar_chart(size)
bmi=weight*10000/height**2

st.header('Are you overweight?')
st.write("Your body mass index is",bmi)                                            
from PIL import Image
  
urllib.request.urlretrieve("https://www.researchgate.net/profile/Bruce-N-Wolfe/publication/236940946/figure/tbl1/AS:614223851814925@1523453786367/WHO-body-mass-index-BMI-Classification-1.png"
  ,
   "bmistats.png")
  
#img = Image.open("bmistats.png")
st.image("bmistats.png")
