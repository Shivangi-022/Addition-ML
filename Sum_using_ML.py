# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:41:20 2023

@author: PANDEY
"""

import streamlit as st
import joblib

def main():
    
    html_temp = """
    <div style = "background-color: purple; padding: 16px">
    <h2 style = "color:black";text-align:center> Addition of two number using ML model </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    # load the model
    model = joblib.load('model_AddEqualNumber')
    
    p1 = st.slider("Enter First Number: ",0,500)
    p2 = st.slider("Enter Second Number: ",0,500)
    
    if st.button('Predict'):
        prediction = model.predict([[p1,p2]])
        st.success('Sum = {}'.format(round(prediction[0],0)))

if __name__ == '__main__':
    main()