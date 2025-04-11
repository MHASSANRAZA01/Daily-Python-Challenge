import streamlit as st

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "Encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

def main():
    st.title("🔐 Caesar Cipher Encoder & Decoder")
    
    mode = st.radio("Select Mode", ["Encrypt", "Decrypt"])
    text = st.text_area("Enter your message:")
    shift = st.slider("Select Shift Value", 1, 25, 3)
    
    if st.button("Run Cipher"):
        output = caesar_cipher(text, shift, mode)
        st.text_area("Result:", output, height=100)

if __name__ == "__main__":
    main()
