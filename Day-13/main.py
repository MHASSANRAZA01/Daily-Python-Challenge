import streamlit as st

# Page Configuration
st.set_page_config(page_title="Encryption & Decryption Tool", page_icon="🔐")

# Custom Styling
st.markdown("""
    <style>
        .main {background-color: #f5f5f5; text-align: center;}
        .stTextInput>div>div>input {font-size: 18px; padding: 10px; border-radius: 8px;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 16px; padding: 10px 20px; border-radius: 8px;}
        .stTextArea>div>textarea {font-size: 18px; border-radius: 8px;}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🔐 Simple Encryption & Decryption Tool</h1>", unsafe_allow_html=True)
st.write("Enter a message below to encrypt or decrypt it.")

# Function to Encrypt Message
def encrypt_message(text, shift=3):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if char.islower() else shift
            new_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift_amount) % 26) + ord('a' if char.islower() else 'A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

# Function to Decrypt Message
def decrypt_message(text, shift=3):
    return encrypt_message(text, -shift)  # Reverse shift for decryption

# User Input
message = st.text_input("Enter Your Message:")

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("🔒 Encrypt"):
        if message:
            encrypted_text = encrypt_message(message)
            st.success(f"**Encrypted Message:** `{encrypted_text}`")
        else:
            st.warning("⚠ Please enter a message!")

with col2:
    if st.button("🔓 Decrypt"):
        if message:
            decrypted_text = decrypt_message(message)
            st.success(f"**Decrypted Message:** `{decrypted_text}`")
        else:
            st.warning("⚠ Please enter a message!")

# Footer
st.markdown("<br><hr><p style='text-align: center;'>Made with ❤️ by Hassan Raza</p>", unsafe_allow_html=True)
