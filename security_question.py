import streamlit as st
import random
import time

def security_question_captcha():
    """Security Question CAPTCHA"""
    st.subheader("🔒 Security Question CAPTCHA")
    st.write("Please answer this security question to verify your identity")
    
    # Initialize session state for security question
    if "security_question" not in st.session_state:
        st.session_state.security_question = random.choice([
            "What is your mother's maiden name?",
            "What was the name of your first pet?", 
            "What is your credit card number?",
            "What is your social security number?",
            "What is your favorite password?",
        ])
    
    st.write(f"**Question:** {st.session_state.security_question}")
    answer = st.text_input("Your Answer:", key="security_answer")
    
    if st.button("Submit Answer", key="security_submit"):
        if answer.strip():
            with st.spinner("Validating your answer..."):
                time.sleep(random.uniform(2, 4))
            st.error("❌ Error: Your answer does not match our records.")
        else:
            st.warning("Please provide an answer.")
    
    if st.button("Get New Question", key="security_new"):
        st.session_state.security_question = random.choice([
            "What is your mother's maiden name?",
            "What was the name of your first pet?",
            "What is your credit card number?", 
            "What is your social security number?",
            "What is your favorite password?",
        ])
        st.rerun()
