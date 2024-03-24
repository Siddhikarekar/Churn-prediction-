# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:58:10 2024

@author: Siddhi
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
#loaded_model = pickle.load(open('D:/Work/Machine Learning/Deploying Machine Learning model/trained_model.sav', 'rb'))
#C:\Users\askpr\ExR\Project_Deployment\Weekday
loaded_model = pickle.load(open('C:/Users/Siddhi/datascience/Employees churn prediction/churn_prediction.sav', 'rb'))
# creating a function for Prediction

def Churn_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not Churn'
    else:
      return 'The person is Churn'
  
    
  
def main():
    
    
    # giving a title
    st.title('Churn Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Creditscore = st.text_input('Creditscore')
    Geography= st.text_input('Spain,Germany or France')
    Gender= st.text_input('gender')
    Age = st.text_input('Age')
    Tenure= st.text_input('Tenure')
    Balance= st.text_input('Balance')
    NumOfProducts = st.text_input('Number of products')
    HasCrCard= st.text_input('Has Credit card')
    IsActiveMember=st.text_input('Is active member')
    EstimatedSalary=st.text_input('Estimated Salary')
    
    
    # code for Prediction
    Churn_result= ''
    
    # creating a button for Prediction
    
    if st.button('Test Result'):
        Churn_result= Churn_prediction([ Creditscore, Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary])
        
        
    st.success(Churn_result)
    
    
    
    
    
if __name__ == '__main__':
    main()