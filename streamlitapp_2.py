# -*- coding: utf-8 -*-
"""streamlitapp_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KQoyAAGBXzn_XABME34nFRG24gn82Ac2
"""

from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('NEWLGBM')

def predict_quality(model, df):
    predictions_data = predict_model(estimator = model, data = df)
    predictions = predictions_data['Label'][0]
    return predictions

def run():
    
    st.title('Prediciting Vehicle Insurance Interest in Customers Web App')
    st.write('This is a web app to predicting whether existing customers interested or not based on\
             several features bellow. Please adjust the value of each feature. After that, click on\
             the Predict button at the bottom to see the prediction.')

    Gender = st.selectbox('Gender', ['Female', 'Male'])

    Age = st.number_input('Input your age', min_value=24, max_value=85, value=35)

    Driving_License  = st.selectbox('Do you have a driving license?', ['No', 'Yes'])

    Region_Code = st.number_input('Input your region code here', min_value=1.0, max_value=51.0, value=10.0)

    Previously_Insured = st.selectbox('Do you have a previously insured?', ['No', 'Yes'])

    Vehicle_Age = st.selectbox('Choose your vehicle age', ['> 2 Years', '1-2 Year', '< 1 Year'])

    Vehicle_Damage = st.selectbox('Do you have a vehicle damage?', ['No', 'Yes'])

    Annual_Premium = st.number_input('Input your annual premium', min_value=2630.0, max_value=540165.0, value=30000.0)

    Policy_Sales_Channel = st.number_input('Input your policy sales channel number', min_value=1.0, max_value=163.0, value=30.0)

    Vintage = st.number_input('How long you have been our customers (in a day)', min_value=10.0, max_value=299.0, value=30.0)

    features = {'Gender': Gender, 'Age': Age,
                 'Driving_License': Driving_License, 'Region_Code': Region_Code,
                 'Previously_Insured' : Previously_Insured, 'Vehicle_Age': Vehicle_Age, 
                 'Vehicle_Damage': Vehicle_Damage, 'Annual_Premium': Annual_Premium, 
                'Policy_Sales_Channel': Policy_Sales_Channel, 'Vintage': Vintage
                }
        
    features_df  = pd.DataFrame([features])

    if st.button('Predict'):
        predictions = predict_quality(model, features_df)
        predictions = str(predictions)
    
        st.success('It is looks like you {} in vehicle insurance'.format(predictions))
       
if __name__ == '__main__':
    run()
