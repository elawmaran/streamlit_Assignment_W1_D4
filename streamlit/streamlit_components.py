import streamlit as st

# exploring the streamlit components
st.title("Streamlit Components Exploration")
st.write("This is a simple exploration of Streamlit components.")

# Adding a button
if st.button("Click Me"):
    st.write("Button clicked!") 

# Adding a checkbox
if st.checkbox("Check me"):
    st.write("Checkbox is checked!")        

# Adding a selectbox
option = st.selectbox(
    'Select a car:',
    ['BMW', 'Maruthi', 'Hyndai', 'Tata', 'Kia', 'Toyota']
)
st.write(f'You selected: {option}')         

# Adding a slider
age = st.slider('Select your age:', 0, 100, 25)
st.write(f'Your age is: {age}')         

# Adding a text input
name = st.text_input("Enter your name:")
if name:
    st.write(f'Hello, {name}!')             

# Adding a text area
message = st.text_area("Enter your message:")
if message:
    st.write(f'Your message: {message}')        

# Adding a file uploader        
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(f'File uploaded: {uploaded_file.name}')    

# Adding a date input
date = st.date_input("Select a date:")
st.write(f'You selected: {date}')   

# Adding a time input
time = st.time_input("Select a time:")
st.write(f'You selected: {time}')   

# Adding a color picker
color = st.color_picker("Pick a color:")
st.write(f'You picked: {color}')

# Adding a progress bar
import time
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1) 

# Adding a metric
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")       

# Adding a map
import pandas as pd
import numpy as np
# Create a DataFrame with random latitude and longitude values
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(map_data)        

