# Lets create BMI calculator using streamlit

import streamlit as st

# Title of the app
st.title("BMI Calculator")
st.write("This app calculates your Body Mass Index (BMI) based on your weight and height.") 

#Get input from user
weight = st.number_input("Enter your weight in kilograms (kg):", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
height = st.number_input("Enter your height in meters (m):", min_value=0.5, max_value=2.5, value=1.75, step=0.01)

#Button to calculate BMI
if st.button("Calculate BMI"):
    # Calculate BMI
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    # Determine BMI category
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")

#Give a messsage to the user based on the BMI category what he sould do to improve his health
    if bmi < 18.5:
        st.write("Consider eating more nutritious food and consult a healthcare provider for advice.")
    elif 18.5 <= bmi < 24.9:
        st.write("Maintain your current lifestyle and continue to eat a balanced diet.")
    elif 25 <= bmi < 29.9:
        st.write("Consider adopting a healthier diet and increasing physical activity. Consult a healthcare provider for personalized advice.")
    else:
        st.write("It's important to seek guidance from a healthcare provider to develop a plan for weight management and overall health improvement.")      


