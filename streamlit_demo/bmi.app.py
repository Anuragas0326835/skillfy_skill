import streamlit as st

st.title("BMI Calculator")

# Input for weight
weight = st.number_input("Enter your weight in kilograms (kg):", min_value=1.0, value=70.0)

# Input for height
height_unit = st.radio("Select height unit:", ('centimeters (cm)', 'meters (m)', 'feet and inches'))

height_m = 0.0

if height_unit == 'centimeters (cm)':
    height_cm = st.number_input("Enter your height in centimeters (cm):", min_value=1.0, value=175.0)
    height_m = height_cm / 100
elif height_unit == 'meters (m)':
    height_m = st.number_input("Enter your height in meters (m):", min_value=0.1, value=1.75)
else:
    col1, col2 = st.columns(2)
    with col1:
        feet = st.number_input("Feet:", min_value=0, value=5)
    with col2:
        inches = st.number_input("Inches:", min_value=0, value=9)
    height_m = (feet * 0.3048) + (inches * 0.0254)

if st.button("Calculate BMI"):
    if height_m > 0:
        bmi = weight / (height_m ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obesity")
    else:
        st.error("Please enter a valid height.")