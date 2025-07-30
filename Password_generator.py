# password genrator
import random
import string
import streamlit as st

st.title('Password generator 🧑‍💻')
st.subheader('Create a strong password of 12 digits:')

# Random Charachters

numbers = string.digits
letters = string.ascii_letters
ln = string.ascii_letters + string.digits
mix = string.digits + string.ascii_letters +string.punctuation

# Giving Choice 
numbersf = ''.join (random.choices(numbers,k=12))
letterf = ''.join (random.choices(letters,k=12))
lnf = ''.join(random.choices(ln ,k=12 ))
mixf = ''.join(random.choices(mix,k=12))
 
# Selectbox 
choices = st.selectbox ('TYPE OF PASSWORD--🔴',['Letters','Numbers','Letters + Numbers', 'Letters + Numbers + Special Characters'])

# Applying Things

if st.button('Generate Password'):
    if choices == 'Letters':
       st.success(letterf).code(letterf , language = 'text')
       st.snow()
    elif choices == 'Numbers':
        st.success(numbersf).code(numbersf , language = 'text')
        st.balloons()
    elif choices == 'Letters + Numbers':
        st.success(lnf) .code(lnf , language = 'text')
        st.balloons()
    elif choices == 'Letters + Numbers + Special Characters':
        st.success(mixf) .code (mixf , language = 'text')
        st.snow()
