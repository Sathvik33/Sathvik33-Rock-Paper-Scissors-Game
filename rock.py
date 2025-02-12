import random
import streamlit as st


st.title("Rock-Paper-Scissors")
st.write("Welcome to the Rock, Paper, Scissors game!")

def rock_paper_scissors(user_choice):
    choices = ['rock', 'paper', 'scissors']
    
    com_choice = random.choice(choices)
    st.write(f"The computer has chosen: {com_choice}")
    if user_choice == com_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and com_choice == 'scissors') or \
         (user_choice == 'scissors' and com_choice == 'paper') or \
         (user_choice == 'paper' and com_choice == 'rock'):
        result = "You win!"
    else:
        result = "You lost."
    
    return result
user_choice = st.selectbox("Choose your option:", ['rock', 'paper', 'scissors'])

if st.button('Play'):
    result = rock_paper_scissors(user_choice)
    st.write(f"Result: {result}")
