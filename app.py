import streamlit as st
from story_generator import generate_story

st.set_page_config(page_title="AI Story Generator", layout="centered")

st.title("📖 AI Story Generator")
st.markdown("Enter a prompt and let the AI spin a story for you!")

prompt = st.text_input("Story Prompt", placeholder="e.g., A time traveler visits ancient Egypt")

if st.button("Generate Story") and prompt:
    with st.spinner("Generating story..."):
        story = generate_story(prompt)
        st.markdown("### ✨ Your AI-generated Story")
        st.write(story)
