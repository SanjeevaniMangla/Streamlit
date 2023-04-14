import streamlit as st

def largest(a, b, c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    else:
        return c

st.title("Find the Largest Number")

# Get user input
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

# Call the function to find the largest number
result = largest(num1, num2, num3)

# Display the result
st.write("The largest number is:", result)
