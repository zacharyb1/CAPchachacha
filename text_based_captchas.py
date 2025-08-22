import streamlit as st
import random
import time

def impossible_math_captcha():
    """Solve an impossible math problem"""
    st.subheader("🧮 Impossible Math Captcha")
    st.write("Please solve the following equation: `2 + 2 = ?` (Hint: It's not 4)")
    
    answer = st.text_input("Your Answer", key="math_captcha")
    
    if answer:
        with st.spinner("Validating your mathematical genius..."):
            time.sleep(random.uniform(2, 4))
        
        failures = [
            "❌ Error: Answer is too logical. Please think outside the box.",
            "❌ Error: Detected traces of common sense. Please remove all logic.",
            "❌ Error: The answer is not a number. Please try again.",
            "❌ Error: Your answer is too correct. We need incorrect creativity.",
            "❌ Error: Quantum fluctuations suggest your answer is from another dimension."
        ]
        
        st.error(random.choice(failures))

def philosophical_question_captcha():
    """Answer a deep philosophical question"""
    st.subheader("🤔 Philosophical Question Captcha")
    st.write("What is the meaning of life, the universe, and everything?")
    
    answer = st.text_input("Your Answer", key="philosophy_captcha")
    
    if answer:
        with st.spinner("Analyzing your philosophical depth..."):
            time.sleep(random.uniform(2, 4))
        
        failures = [
            "❌ Error: Answer is too shallow. Please provide more existential depth.",
            "❌ Error: Detected traces of optimism. Please remove all hope.",
            "❌ Error: Your answer is too accurate. We need more ambiguity.",
            "❌ Error: The meaning of life cannot be expressed in words. Try again.",
            "❌ Error: Your answer suggests you are a robot. Please prove your humanity."
        ]
        
        st.error(random.choice(failures))

def random_trivia_captcha():
    """Answer a random trivia question"""
    st.subheader("🎲 Random Trivia Captcha")
    question = "What is the airspeed velocity of an unladen swallow?"
    st.write(f"Question: {question}")
    
    answer = st.text_input("Your Answer", key="trivia_captcha")
    
    if answer:
        with st.spinner("Checking your trivia knowledge..."):
            time.sleep(random.uniform(2, 4))
        
        failures = [
            "❌ Error: African or European swallow? Please specify.",
            "❌ Error: Your answer lacks sufficient detail. Please elaborate.",
            "❌ Error: Trivia answer is too correct. We need more creativity.",
            "❌ Error: Detected sarcasm in your response. Please be serious.",
            "❌ Error: Your answer suggests you are overthinking this."
        ]
        
        st.error(random.choice(failures))

def main():
    """Main application for text-based captchas"""
    st.title("🤖 Text-Based Captcha Challenges")
    st.write("*Test your creativity and patience with these text-based challenges!*")
    
    # Captcha selection
    captcha_options = {
        "🧮 Impossible Math": impossible_math_captcha,
        "🤔 Philosophical Question": philosophical_question_captcha,
        "🎲 Random Trivia": random_trivia_captcha
    }
    
    selected_captcha = st.selectbox("Choose a Captcha Challenge", list(captcha_options.keys()))
    
    # Run the selected captcha function
    captcha_function = captcha_options[selected_captcha]
    captcha_function()
    
    # Footer
    st.write("---")
    st.write("*If you somehow pass any of these captchas, please contact our emergency response team immediately.*")
    st.write("*Warning: Side effects may include existential dread, questioning reality, and uncontrollable laughter.*")

if __name__ == "__main__":
    main()