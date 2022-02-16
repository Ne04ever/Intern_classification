import streamlit as st
from hr_analytics_functions import *

st.sidebar.image('https://d2lk14jtvqry1q.cloudfront.net/media/large_01_articolo_1200x630_1_1024x538_1024x537_aca1aba709.png', width=250)
st.sidebar.header('HR Analytics: Job Change of Data Scientists')
st.sidebar.markdown('Prediction who will move to a new job')


menu = st.sidebar.radio(
    "Menu:",
    ("Intro", "Data", "Analysis", "Pivot Tables", "Classification Model"),
)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('Project Submitted By: Farrukh Wajahat Ullah and Vaseem Shuaib')
st.sidebar.write('Github Repositories:')
st.sidebar.write('[Farrukh Github Repository Link](https://github.com/Farrukh-Ullah/python_project)')
st.sidebar.write('[Vaseem Github Repository Link](https://github.com/Ne04ever/Intern_classification)')
if menu == 'Intro':
    set_home()
elif menu == 'Data':
    set_data()
elif menu == 'Analysis':
    set_analysis()
elif menu == 'Pivot Tables':
    set_Piyottbl()
elif menu == 'Classification Model':
    set_classmod()
