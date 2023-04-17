import streamlit as st

@st.cache
def reverse_string(string):
    return string[::-1]

def main():
    st.title("Reverse String API")
    string = st.text_input("Enter a string to reverse:")
    if st.button("Reverse"):
        reversed_string = reverse_string(string)
        st.write(f"The reversed string is: {reversed_string}")

if __name__ == "__main__":
    main()
