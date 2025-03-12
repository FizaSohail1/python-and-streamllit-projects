import streamlit as st
import string 
import random

st.title("Password Generator")
st.write("Just select your password length and click on generate!")

value = st.slider("Select a length",0,100)

def password_generator(len,isnumbers,isspecialchrac):
    chracters = string.ascii_letters

    if isnumbers:
        isnumbers = string.digits
        chracters += isnumbers
    elif isspecialchrac:
        specialChrac = string.punctuation
        chracters += specialChrac

    return ''.join(random.choice(chracters) for _ in range(len))    

length =  value 
use_digit = st.checkbox("Do you want to add digits?")          
use_specialchracters = st.checkbox("Do you want to add special chracters?")

if st.button("Generate"):
  result =  password_generator(length,use_digit,use_specialchracters)
  st.write(result)

    
