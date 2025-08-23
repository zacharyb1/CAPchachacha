import streamlit as st
import random
import time
from io import BytesIO
from PIL import Image
from camera_utils import get_camera_image, clear_camera_widget


def potato_detector_captcha():
    st.subheader("🥔 Potato Detection Captcha")
    st.write("Please take a picture showing exactly 3.7 potatoes.")
    display_width = 240

    potato_bytes = get_camera_image('potato_image_bytes', 'potato_camera', "Take a picture of potatoes", display_width)
    if potato_bytes is None:
        return

    # Fake processing
    with st.spinner("Running advanced potato recognition AI..."):
        time.sleep(random.uniform(2, 4))

    failures = [
        "❌ Error: Detected 3.69 potatoes. We need exactly 3.7 potatoes.",
        "❌ Error: Potatoes appear to be too potato-like. Please use less obvious potatoes.",
        "❌ Error: Image contains traces of non-potato energy. Please cleanse your camera.",
        "❌ Error: Potatoes are facing the wrong direction. They should face magnetic north.",
        "❌ Error: Potato authenticity verification failed. Please use certified organic potatoes only."
    ]

    st.error(random.choice(failures))

    if st.button("Try Again (Retake)"):
        st.session_state.potato_image_bytes = None
        st.session_state.processing = False
        st.session_state.progress = 0
        clear_camera_widget('potato_camera')
        st.rerun()
