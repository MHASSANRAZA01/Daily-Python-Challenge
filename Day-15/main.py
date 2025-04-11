import streamlit as st
import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4 characters."
    
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_chars, k=length))
    return password

def main():
    st.title("🔐 Random Password Generator")
    
    length = st.slider("Select Password Length", 4, 50, 12)
    
    if st.button("Generate Password"):
        password = generate_password(length)
        st.text_area("Your Secure Password:", password, height=70)  # Fixed height issue

if __name__ == "__main__":
    main()
