import streamlit as st

st.set_page_config(page_title="Password Strength Meter", page_icon="🔏")

st.title("🔏 Password Strength Meter")
st.write("Enter your password to check its strength.")

password = st.text_input("Enter Your Password:", type="password")

score = 0
feedback = []

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Use at least one uppercase letter.")

    if any(char in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~" for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    st.progress((score + 1) / 5)

    if feedback:
        st.warning("Suggestions to improve your password:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")

st.write("Made By Fiza 💖 ")            


