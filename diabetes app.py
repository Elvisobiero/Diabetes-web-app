#importing our libraries
import numpy as np
import pickle
import streamlit as st

#loading our saved model
model = pickle.load(open('C:/Users/Elvis/Desktop/my python/Diabetes model.sav', 'rb'))

#creating a function
def diabetes_pred(input_data):
    prediction = model.predict([input_data])

    if prediction == 1:
        return 'The person is Diabetic'
    else:
        return 'The person is not diabetic'


def main():
    #giving a title
    st.title('Diabetes Prediction Web App')

    #getting input data from the user
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Level of Glucose')
    Blood_pressure = st.text_input('Blood pressure level')
    Skin_thickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Level of Insulin')
    BMI = st.text_input('BMI value')
    Diabetes_pedigree_function = st.text_input('Diabetes_pedigree_function')
    Age = st.text_input('Age of patient')


    #code for prediction

    diagnosis = ''


    #creating a pattern for prediction

    if st.button('Diabetes test result'):
        diagnosis = diabetes_pred([Pregnancies, Glucose, Blood_pressure, Skin_thickness, Insulin, BMI, Diabetes_pedigree_function, Age])


    st.success(diagnosis)

if __name__ == '__main__':
    main()