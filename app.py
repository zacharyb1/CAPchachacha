import streamlit as st
import random
from potato import potato_detector_captcha
from cat import cat_check_captcha
from stare import staring_contest_captcha


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
        "🥔 Potato Detector": potato_detector_captcha,
        "🐱 The Cat Check": cat_check_captcha,
    "👀 Staring Contest": staring_contest_captcha,
    }

    if st.button("🔄 Get New Stupid Captcha"):
        st.session_state.current_captcha = random.choice(list(captcha_options.keys()))
        st.session_state.potato_image_bytes = None
        st.session_state.cat_image_bytes = None
        st.session_state.processing = False
        st.session_state.progress = 0
        st.session_state.staring_start_time = None
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
