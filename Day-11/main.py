import streamlit as st
import emoji

# Page Config
st.set_page_config(page_title="Emoji Sentiment Analyzer", page_icon="🤖")

st.title("Emoji Sentiment Analyzer 🤖")
st.write("Type a message with emojis to detect mood")

# User Input
user_input = st.text_input("Your Sentence:")

# Function to Extract Emojis
def extract_emojis(text):
    return [char for char in text if char in emoji.EMOJI_DATA]

# Button to Detect Mood
if st.button("🟢 Detect Mood", help="Click to analyze the mood"):
    emojis_found = extract_emojis(user_input)
    
    if user_input:
        if emojis_found:
            st.success(f"**Mood Detected:** {''.join(emojis_found)}")
        else:
            st.warning("⚠ No emoji found, can't detect mood!")
    else:
        st.warning("⚠ Please enter a sentence!")

