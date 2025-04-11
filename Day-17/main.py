import streamlit as st
import qrcode
from io import BytesIO

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    return img

def main():
    st.title("📱 QR Code Generator 🔗")
    
    data = st.text_input("Enter text or URL:")
    
    if st.button("Generate QR Code"):
        if data:
            img = generate_qr_code(data)
            buf = BytesIO()
            img.save(buf, format="PNG")
            st.image(buf, caption="Your QR Code", use_container_width=True)  # Updated parameter
            
            st.download_button(
                label="Download QR Code",
                data=buf.getvalue(),
                file_name="qrcode.png",
                mime="image/png"
            )
        else:
            st.warning("Please enter some text or URL to generate a QR code.")

if __name__ == "__main__":
    main()
