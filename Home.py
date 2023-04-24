# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:08:57 2023

@author: Karsyn
"""

import streamlit as st
from PIL import Image


st.set_page_config(layout="wide")
st.markdown('# Home')
            
image1 = Image.open('Images/HomePage.jpg')

st.image(image1, caption='Image Source: American University')
st.markdown('   Hey! My name is Karsyn Plunkett, and I have completed my Master of Science in Data Science at' +
            ' Eastern University. I have learned so much in this Data Science program and am so thrilled to'+
            ' apply my knowledge to an industry. During my undergrad I studied Industrial and Systems engineering at '+
            'Auburn University (War Eagle!) where I have been working as a systems engineer since. I am hoping this '+
            'degree will help me to make a breakthrough in the Data Science field!')
st.markdown('   In my free time, I enjoy playing tennis with my husband and throwing the frisbee with our adorable dog, Sammy! '
            +'I try to stay active even with my busy schedule and tennis has really made that possible since it is so much fun '
            +'and I spend so much of my time chasing the ball. I also enjoy reading, especially historical fiction or southern lit.'
            + ' If you have any new, interesting reads, send them my way! If you want to connect, my contact information can be found on the \'Contact Me\' tab of my [Resume](Resume)')





col1, col2, col3 = st.columns([1,1,1])

with col1:
        st.write("")

with col2:
        image = Image.open('Images/IMG_9144_copy.jpg')
        st.image(image, width=500)

with col3:
        st.write("")
        
