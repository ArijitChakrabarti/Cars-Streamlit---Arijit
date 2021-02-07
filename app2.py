# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 00:12:19 2021
cd  Documents/Python/INSAID Data Science/Insaid Thursdays/Streamlit
@author: ariji
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('rf_random.pkl', 'rb'))

def predict_price(Present_Price, Kms_Driven, Owner, Age, Fuel_Type,Seller_Type, Transmission):
    input = np.array([[Present_Price, Kms_Driven,Owner,Age,Fuel_Type,Seller_Type,Transmission]]).astype(np.float64)
    pred = model.predict(input)
    return float(pred)

def main():
    st.title('The Arijit Car Price Predictor')
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Used Car Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Present_Price = st.text_input('What is the current market value of the car?', 'in INR Lacs only')
    Kms_Driven = st.slider('How many kilometers has the car been used for?',min_value=0, max_value=1000000, step = 10000)
    Owner = st.slider('What are the number of previous owners of the car?',min_value=0,max_value=3,step=1)
    Age = st.slider('How old is the car?',min_value=0, max_value=15,step=1)
    Fuel = st.selectbox('What is the type of fuel the vehicle uses?',('CNG', 'Diesel', 'Petrol'))
    st.write('You selected', Fuel)
    type1 ={ 'CNG': 0, 'Diesel':1, 'Petrol':2}
    Fuel_Type = type1[Fuel]
    Seller = st.selectbox('Are you a dealer or individual?', ('Dealer','Individual'))
    st.write('You selected', Seller)
    type2 = {'Dealer': 0 , 'Individual': 1}
    Seller_Type = type2[Seller]
    Tran = st.selectbox('What type of transmission in your car?', ('Automatic', 'Manual'))
    type3 = {'Automatic': 0, 'Manual': 1}
    Transmission = type3[Tran]
    
    if st.button('Predict'):
        output = predict_price(Present_Price,Kms_Driven, Owner, Age, Fuel_Type,Seller_Type, Transmission)
        st.success('The selling prices of this vehicle in INR Lacs is {} Lacs' .format(round(output,2)))
        
if __name__=='__main__':
    main()
    