import streamlit as st
st.write('# Streamlit calcuator')



# input field for two numbers

number1 = st.number_input('Enter first number')
number2 = st.number_input('Enter second number')

# perform the calculation
sum_result = number1 + number2
sub_result = number1 - number2
mul_result = number1 * number2
div_result = number1 / number2 if number2 != 0 else  "undefined (Cannot divide by zero)"


# display the results

st.write('### Results')
st.write(f'**addition:**{number1}={number2}={sum_result}')
st.write(f'**subtraction:**{number1}-{number2}={sub_result}')
st.write(f'**multiplication:**{number1}*{number2}={mul_result}')
st.write(f'**division:**{number1}/{number2}={div_result}')

