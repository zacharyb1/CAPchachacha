import streamlit as st
import random
import time
from PIL import Image

def potato_detector_captcha():
    """Potato Detection CAPTCHA"""
    st.subheader("🥔 Potato Detection CAPTCHA")
    st.write("Take a picture showing exactly 3.7 potatoes during a solar eclipse.")
    camera_input = st.camera_input("Take a picture")
    
    if camera_input:
        image = Image.open(camera_input)
        st.image(image, caption="Analyzing potato content...", use_column_width=True)
        with st.spinner("Running advanced potato recognition AI..."):
            time.sleep(random.uniform(2, 4))
        st.error("❌ Error: Detected 3.69 potatoes. We need exactly 3.7 potatoes.")

captcha_options = [
    {"name": "Potato Detector", "function": potato_detector_captcha}
]