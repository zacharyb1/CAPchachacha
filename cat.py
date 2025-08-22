import streamlit as st
import random
import time
from camera_utils import get_camera_image, clear_camera_widget


def cat_check_captcha():
    st.subheader("🐱 The Cat Check")
    st.write("Please show us a cat on your webcam. No cat → fail.")
    display_width = 240

    cat_bytes = get_camera_image('cat_image_bytes', 'cat_camera', "Show a cat to the camera", display_width)
    if cat_bytes is None:
        return

    with st.spinner("Running state-of-the-art cat recognition model..."):
        time.sleep(random.uniform(1.5, 3.0))

    failures = [
        "❌ Error: No cat detected. Detected only suspicious levels of cuteness.",
        "❌ Error: The animal in the image is too cat-like to be trusted.",
        "❌ Error: Detected a mirror reflection, not a real cat.",
        "❌ Error: Cat detected but not existentially aligned. Try again later.",
        "❌ Error: Detected cat-like pixels: 99.999% confidence of being a plant."
    ]

    st.error(random.choice(failures))

    if st.button("Try Again (Retake)"):
        st.session_state.cat_image_bytes = None
        st.session_state.processing = False
        st.session_state.progress = 0
        clear_camera_widget('cat_camera')
        st.rerun()
