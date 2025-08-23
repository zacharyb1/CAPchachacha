import streamlit as st
import random
import time
from io import BytesIO
from PIL import Image
from camera_utils import get_camera_image, clear_camera_widget


def nipple_detector_captcha():
    st.subheader("🔍 Nipple Detection Captcha")
    st.write("Please take a picture showing exactly one nipple on your webcam.")
    display_width = 240

    nipple_bytes = get_camera_image('nipple_image_bytes', 'nipple_camera', "Show a nipple to the camera", display_width)
    if nipple_bytes is None:
        return

    # Fake processing
    with st.spinner("Running advanced nipple recognition AI..."):
        time.sleep(random.uniform(2, 4))

    failures = [
        "❌ Error: Detected 0.99 nipples. We need exactly 1.0 nipples.",
        "❌ Error: Nipple appears to be too nipple-like. Please use a less obvious nipple.",
        "❌ Error: Image contains traces of non-nipple energy. Please cleanse your camera.",
        "❌ Error: Nipple is facing the wrong direction. It should face true north.",
        "❌ Error: Nipple authenticity verification failed. Please use certified organic nipples only.",
        "❌ Error: Detected suspicious levels of nipple-ness. Try again with different lighting.",
        "❌ Error: This nipple does not meet our aesthetic standards."
    ]

    st.error(random.choice(failures))

    if st.button("Try Again (Retake)", key="nipple_retry"):
        st.session_state.nipple_image_bytes = None
        st.session_state.processing = False
        st.session_state.progress = 0
        clear_camera_widget('nipple_camera')
        st.rerun()
