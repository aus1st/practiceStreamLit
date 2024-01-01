import streamlit as st

st.title('Welcome to BMI Calculator')


# take weight input
weight = st.number_input('Enter your weight in kg')


height_format = st.radio('Choose your height format: ',('meter','centimeter','feet'))

if(height_format == 'centimeter'):
    height = st.number_input('Input your height in cm')

    try:
        bmi = weight / ((height/100))**2
    except ZeroDivisionError:
        st.error('Height cannot be zero')

elif(height_format == 'meter'):
    height = st.number_input('Input your height in meter')
    try:
        bmi = weight / (height)**2
    except ZeroDivisionError:
        st.error('Height cannot be zero')

    
else:
    height = st.number_input('Input your height in Feet')
    try:
        bmi = weight / ((height/3.28))**2
    except ZeroDivisionError:
            st.error('Height cannot be zero')
            
if(st.button('Calculate BMI')):
    st.success('Your BMI is {}'.format(bmi))
    if(bmi < 16):
        st.error('Severe Thinness')
    elif(bmi >=16 and bmi < 18.5):
        st.warning('Moderate Thinness')
    elif(bmi >= 18.5 and bmi < 25):
        st.success('Normal')
    elif(bmi >= 25 and bmi < 30):
        st.warning('Overweight')
    elif(bmi >= 30):
            st.error('Obese')
            



