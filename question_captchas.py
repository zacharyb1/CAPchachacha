import streamlit as st
import random
import time

def security_question_captcha():
    """Security Question CAPTCHA"""
    st.subheader("🔒 Security Question CAPTCHA")
    question = random.choice([
        "What is your mother's maiden name?",
        "What was the name of your first pet?",
        "What is the name of the street you grew up on?"
    ])
    st.write(f"Question: {question}")
    answer = st.text_input("Your Answer")
    
    if answer:
        with st.spinner("Validating your answer..."):
            time.sleep(random.uniform(2, 4))
        st.error("❌ Error: Your answer does not match our records.")

captcha_options = [
    {"name": "Security Question", "function": security_question_captcha}
]