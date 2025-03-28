import streamlit as st
import re

# Page title and description
st.title("Password Strength Checker by Mariam Faizan")
st.write("Enter your password below to check its security level.")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    # Uppercase & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one uppercase and one lowercase letter**.")

    # Number Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    # Special Character Check
    if re.search(r"[@#$%&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least **one special character (@#$%&*)**.")

    # Display strength level
    if score == 4:
        st.success("✅ **Your password is strong!**")
    elif score == 3:
        st.info("⚠️ **Medium strength password.**")
    else:
        st.error("❌ **Your password is weak!**")

    # Show improvement suggestions
    if feedback:
        with st.expander("💡 **Improve your password:**"):
            for item in feedback:
                st.write(item)
 
# Password input field
password = st.text_input("Enter your password here:", type="password", help="Ensure your password is strong.")

# Check password strength when user inputs a password
if password:
    check_password_strength(password)
