import streamlit as st
from PIL import Image
st.write('This is simple text')

# IMAGE
img = Image.open('logo_js.png')

# CHECKBOX
if st.checkbox('Show/Hide'):
    st.image(img,width=200)

# RADIO
status = st.radio('Select Gender: ',('Male','Female'))
if status == 'Male':
    st.success('Male')
elif status == 'Female':
    st.warning('Female')

# MULTISELECT
hobbies = st.multiselect('Hobbies: ',('Dancing','Singing','Cooking'))
st.write('You Selected', len(hobbies),'Hobbies')

st.button('Click me for a popup')

if(st.button('About')):
    st.text('This is a simple app')
    st.snow()


name = st.text_input('Enter your name: ')
if(st.button('Click')):
    result = name.title()
    st.success(result)

level = st.slider('Select your level: ',1,5)
st.text('Selected: {}'.format(level))


