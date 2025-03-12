import streamlit as st
from datetime import date
import random

quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Your only limit is your mind.",
    "Do something today that your future self will thank you for.",
    "Growth and comfort do not coexist.",
    "Every day is a new opportunity to grow and improve."
]

principles = [
    "Learn from Mistakes: Mistakes are lessons. Each one is an opportunity to grow.",
    "Persist Through Difficulties: Challenges are stepping stones. Keep pushing forward.",
    "Embrace Challenges: Growth happens when you step out of your comfort zone.",
    "Seek Feedback: Constructive criticism helps you improve.",
    "Celebrate Small Wins: Every step forward is progress worth recognizing."
]


st.title("🌱 Growth Mindset Tracker")
st.write("Welcome to your personal growth journey!")
st.subheader("✨ Daily Motivation")

st.subheader(f"{random.choice(principles)}")

if "goals" not in st.session_state:
    st.session_state.goals = []

st.header("Set Your Goals 🎯")

new_goal = st.text_input("Enter your goal:")

if st.button("Add Goal"):
    if new_goal:
        st.session_state.goals.append(new_goal)
        st.success("Goal added successfully!")
    else:
        st.warning("Please enter a goal.")

st.subheader("Your Goals:")
for i, goal in enumerate(st.session_state.goals, 1):
    st.write(f"{i}. {goal}")

if st.button("Clear Goals"):
    st.session_state.goals = []
    st.success("Goals cleared!")

st.header("📖 Reflect on Learning")
reflection = st.text_area("What are the tasks that you have completed today?")
if st.button("Save Reflection"):
    st.session_state.reflections.append((date.today(), reflection))
    st.success("Reflection saved!")

st.header("📈 Progress Tracker")
if "reflections" in st.session_state and st.session_state.reflections:
    for entry in st.session_state.reflections:
        st.write(f"📅 {entry[0]}: {entry[1]}")
else:
    st.write("No reflections recorded yet.")


if "reflections" not in st.session_state:
    st.session_state.reflections = []
if "goal" not in st.session_state:
    st.session_state.goal = ""


