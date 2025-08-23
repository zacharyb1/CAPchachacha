import streamlit as st
import cv2
import numpy as np
import time
import random
from PIL import Image
import base64
from io import BytesIO
from streamlit_autorefresh import st_autorefresh

THERAPY_QUESTIONS = [
    "If your anxiety could dance, what dance would it do?",
    "On a scale from goldfish to philosopher, how deep are your thoughts right now?",
    "What childhood snack could solve your adult problems if given the chance?",
    "If your self-esteem were a vegetable, which one would it be?",
    "What’s one irrational fear you could beat in a rap battle?",
    "If inner peace had a theme song, would it have cowbells in it?",
    "What’s the dumbest thing that made you cry last year?",
    "If your brain had a loading screen, what would be the tip of the day?",
    "What’s one completely useless talent that still makes you proud?",
    "If stress were a Pokémon, what would it evolve into?",
    "What’s the most dramatic way you could describe your Monday?",
    "If you could unsubscribe from one emotion, which one would it be?",
    "What inanimate object understands you best?",
    "If overthinking were an Olympic sport, what medal would you win?",
    "What conspiracy theory does your cat secretly believe about you?",
    "If your happiness ran on batteries, what brand would they be?",
    "What advice would you give to someone about to argue with a pigeon?",
    "If procrastination had a fashion style, what would it wear?",
    "What’s the weirdest motivational speech you could give yourself right now?",
    "If your life had subtitles, what font would they be in?"
]

# Configure Streamlit page
st.set_page_config(
    page_title="World's Most Stupid Captcha",
    page_icon="🤖",
    layout="wide"
)

def init_session_state():
    """Initialize session state variables"""
    if 'current_captcha' not in st.session_state:
        st.session_state.current_captcha = None
    if 'processing' not in st.session_state:
        st.session_state.processing = False
    if 'progress' not in st.session_state:
        st.session_state.progress = 0
    if 'staring_start_time' not in st.session_state:
        st.session_state.staring_start_time = None

def awkward_wait_captcha():
    # Auto-refresh every 1 second
    st_autorefresh(interval=1000, key="awkward_refresh")
    st.subheader("⏳ 1 Minute Therapy Captcha")
    st.write("Please wait exactly 1 minute. If the countdown reaches 0, it will restart at 59 seconds.")

    # Initialize session state variables before use
    if "awkward_start_time" not in st.session_state:
        st.session_state.awkward_start_time = time.time()
    if "awkward_question" not in st.session_state:
        st.session_state.awkward_question = random.choice(THERAPY_QUESTIONS)
    if "awkward_answer" not in st.session_state:
        st.session_state.awkward_answer = ""

    # Countdown logic
    elapsed = int(time.time() - st.session_state.awkward_start_time)
    countdown = 60 - (elapsed % 60)
    if countdown == 60:
        countdown = 59

    st.write(f"⏳ Time remaining: {countdown} seconds")
    st.write("Therapist question:")
    st.write(st.session_state.awkward_question)

    # Use dynamic key so input box clears each time
    input_key = f"awkward_input_{st.session_state.awkward_question}"
    new_answer = st.text_input(
        "Type your awkward answer here (don’t worry, we won’t save it)",
        key=input_key
    )

    # If user submits a new answer
    if new_answer and new_answer != st.session_state.awkward_answer:
        st.session_state.awkward_answer = new_answer
        st.session_state.awkward_question = random.choice(THERAPY_QUESTIONS)
        st.session_state.awkward_start_time = time.time()
        st.rerun()

def main():
    """Main application"""
    init_session_state()
    
    st.title("🤖 World's Most Stupid Captcha System")
    st.write("*Guaranteed to be unsolvable since 2024*")
    
    # Only use the awkward wait captcha
    captcha_options = {
        "⏳ 1 Minute Therapy": awkward_wait_captcha
    }

    st.write("---")
    st.subheader("Current Challenge: ⏳ 1 Minute Therapy")

    awkward_wait_captcha()
    
    # Footer
    st.write("---")
    st.write("*If you somehow pass any of these captchas, please contact our emergency response team immediately.*")
    st.write("*Warning: Side effects may include existential dread, questioning reality, and uncontrollable laughter.*")

if __name__ == "__main__":
    main()