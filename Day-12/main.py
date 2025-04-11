import streamlit as st
import re

# Page Configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

# Custom CSS for Styling
st.markdown("""
    <style>
        .main {background-color: #f5f5f5; text-align: center;}
        .stTextInput>div>div>input {font-size: 18px; padding: 10px; border-radius: 8px;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 16px; padding: 10px 20px; border-radius: 8px;}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)
st.write("Enter a password below to analyze its strength.")

# Password Input Field
password = st.text_input("Enter Password:", type="password")

# Function to Analyze Password Strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Use at least one special character (!@#$%^&*).")

    return score, feedback

# Check Password Strength on Button Click
if st.button("🔍 Check Strength"):
    if password:
        score, feedback = check_password_strength(password)

        if score <= 2:
            st.error("🔴 Weak Password: Try making it stronger!")
        elif score <= 4:
            st.warning("🟠 Medium Password: Improve it for better security!")
        else:
            st.success("🟢 Strong Password: Good job!")

        # Display Feedback
        for msg in feedback:
            st.write(msg)
    else:
        st.warning("⚠ Please enter a password!")

