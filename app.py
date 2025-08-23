import streamlit as st
import random
from potato import potato_detector_captcha
from cat import cat_check_captcha
from stare import staring_contest_captcha
from age_verify import age_verification_captcha
from voice_verify import voice_verification_captcha
from circle_draw import circle_draw_captcha
from wheel_fortune import wheel_of_fortune_captcha


def init_session_state():
    if 'current_captcha' not in st.session_state:
        st.session_state.current_captcha = None
    if 'processing' not in st.session_state:
        st.session_state.processing = False
    if 'progress' not in st.session_state:
        st.session_state.progress = 0
    if 'staring_start_time' not in st.session_state:
        st.session_state.staring_start_time = None
    if 'potato_image_bytes' not in st.session_state:
        st.session_state.potato_image_bytes = None
    if 'cat_image_bytes' not in st.session_state:
        st.session_state.cat_image_bytes = None


def main():
    # Page config kept minimal here; can be moved back to top-level if needed
    st.set_page_config(
        page_title="World's Most Stupid Captcha",
        page_icon="🤖",
        layout="wide"
    )

    init_session_state()

    st.title("🤖 World's Most Stupid Captcha System")
    st.write("*Guaranteed to be unsolvable since 2024*")

    captcha_options = {
        # "🥔 Potato Detector": potato_detector_captcha,
        # "🐱 The Cat Check": cat_check_captcha,
        # "👀 Staring Contest": staring_contest_captcha,
        # "🔢 Age Verification": age_verification_captcha,
        # "🎤 Voice Verification": voice_verification_captcha,
        # "⭕️ Perfect Circle": circle_draw_captcha,
        "🎡 Wheel of Fortune": wheel_of_fortune_captcha,
    }

    if st.button("🔄 Get New Stupid Captcha"):
        st.session_state.current_captcha = random.choice(list(captcha_options.keys()))
        st.session_state.potato_image_bytes = None
        st.session_state.cat_image_bytes = None
        st.session_state.processing = False
        st.session_state.progress = 0
        st.session_state.staring_start_time = None
        # Reset age verification state
        if 'age_step' in st.session_state:
            st.session_state.age_step = 1
        if 'age_name' in st.session_state:
            st.session_state.age_name = ""
        if 'age_value' in st.session_state:
            st.session_state.age_value = 0
        if 'age_t9_input' in st.session_state:
            st.session_state.age_t9_input = ""
        if 'age_captcha_passed' in st.session_state:
            st.session_state.age_captcha_passed = False
        # Reset voice verification state
        if 'voice_in_progress' in st.session_state:
            st.session_state.voice_in_progress = False
        # Reset wheel of fortune state
        if 'wheel_spinning' in st.session_state:
            st.session_state.wheel_spinning = False
        if 'wheel_result' in st.session_state:
            st.session_state.wheel_result = None
        st.rerun()

    if st.session_state.current_captcha is None:
        st.session_state.current_captcha = list(captcha_options.keys())[0]

    st.write("---")
    st.subheader(f"Current Challenge: {st.session_state.current_captcha}")

    captcha_function = captcha_options[st.session_state.current_captcha]
    captcha_function()

    st.write("---")
    st.write("*If you somehow pass any of these captchas, please contact our emergency response team immediately.*")
    st.write("*Warning: Side effects may include existential dread, questioning reality, and uncontrollable laughter.*")
