import streamlit as st

def are_anagrams(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    # Check if sorted letters of both words are the same
    return sorted(word1) == sorted(word2)

def main():
    st.title("Anagram Checker 🔄")
    
    # Input fields for the two words
    word1 = st.text_input("Enter the first word:")
    word2 = st.text_input("Enter the second word:")
    
    # Button to check if they are anagrams
    if st.button("Check Anagram"):
        if are_anagrams(word1, word2):
            st.success("✅ Yes, it's an anagram!")
        else:
            st.error("❌ No, it's not an anagram!")

if __name__ == "__main__":
    main()
