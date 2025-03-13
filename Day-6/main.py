# 📢 Day 6 – Daily Python Challenge 🐍
# 🚀 Challenge:# Aisa Python program likhna hai jo user se ek integer number lega aur uska binary (0s aur 1s) me conversion karega, phir check karega ke ye palindrome hai ya nahi! 🔄✨

# 🔥 Example:
# 📌 Input: 9
# 📌 Binary: 1001
# 📌 Output: Palindrome ✅

# 📌 Input: 13
# 📌 Binary: 1101
# 📌 Output: Not a Palindrome ❌

# User se ek integer number input lete hain
number = int(input("Enter an integer number: "))

# Number ko binary string me convert karte hain (bin() function se) aur '0b' prefix ko hata dete hain
binary_representation = bin(number)[2:]

# Binary string ko reverse karke check karte hain ki palindrome hai ya nahi
if binary_representation == binary_representation[::-1]:
    print(f"Binary: {binary_representation}")
    print("Output: Palindrome ")
else:
    print(f"Binary: {binary_representation}")
    print("Output: Not a Palindrome ")



# Answer

# Enter an integer number: 7 
# Binary: 111 
# Output: Palindrome 

# Enter an integer number: 10 
# Binary: 1010 
# Output: Not a Palindrome 
