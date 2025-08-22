import streamlit as st
import cv2
import numpy as np
import time
import random
from PIL import Image
import base64
from io import BytesIO

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
    # per-captcha stored images
    if 'potato_image_bytes' not in st.session_state:
        st.session_state.potato_image_bytes = None
    if 'cat_image_bytes' not in st.session_state:
        st.session_state.cat_image_bytes = None

# ...existing code...
def potato_detector_captcha():
    """The most impossible potato detection captcha"""
    st.subheader("🥔 Potato Detection Captcha")
    st.write("Please take a picture showing exactly 3.7 potatoes in their natural habitat during a solar eclipse")
    
    # Width (px) to use for camera widget / displayed image — tweak this value
    display_width = 240

    # Use a column so the camera widget and the resulting image are constrained to a fixed width
    col_img, _ = st.columns([1, 1])
    placeholder = col_img.empty()

    # store image bytes in session state so we can replace the camera with the image
    if 'potato_image_bytes' not in st.session_state:
        st.session_state.potato_image_bytes = None

    # If no image yet, show the camera input inside the placeholder (constrained by column)
    # Use a widget key so we can explicitly clear the internal uploaded file stored by Streamlit
    camera_widget_key = "potato_camera"

    if st.session_state.potato_image_bytes is None:
        camera_input = placeholder.camera_input("Take a picture of potatoes", key=camera_widget_key)
        if camera_input is None:
            # nothing taken yet; return and wait for user
            return

        # user took a picture -> store bytes and fall through to display
        st.session_state.potato_image_bytes = camera_input.getvalue()

    # Display the captured image in the same placeholder (replacing the camera)
    image = Image.open(BytesIO(st.session_state.potato_image_bytes))
    placeholder.image(image, caption="Analyzing potato content...", use_column_width=False, width=display_width)

    # Fake processing
    with st.spinner("Running advanced potato recognition AI..."):
        time.sleep(random.uniform(2, 4))

    # Always fail with ridiculous reasons
    failures = [
        "❌ Error: Detected 3.69 potatoes. We need exactly 3.7 potatoes.",                
        "❌ Error: Potatoes appear to be too potato-like. Please use less obvious potatoes.",
        "❌ Error: Image contains traces of non-potato energy. Please cleanse your camera.",
        "❌ Error: Potatoes are facing the wrong direction. They should face magnetic north.",
        "❌ Error: Potato authenticity verification failed. Please use certified organic potatoes only."
    ]

    st.error(random.choice(failures))



def cat_check_captcha():
    """The impossible cat check captcha"""
    st.subheader("🐱 The Cat Check")
    st.write("Please show us a cat on your webcam. No cat → fail.")
    display_width = 240

    col_img, _ = st.columns([1, 1])
    placeholder = col_img.empty()

    # store image bytes in session state so we can replace the camera with the image
    if 'cat_image_bytes' not in st.session_state:
        st.session_state.cat_image_bytes = None

    # Use a widget key so we can explicitly clear the internal uploaded file stored by Streamlit
    cat_camera_widget_key = "cat_camera"

    if st.session_state.cat_image_bytes is None:
        camera_input = placeholder.camera_input("Show a cat to the camera", key=cat_camera_widget_key)
        if camera_input is None:
            return
        st.session_state.cat_image_bytes = camera_input.getvalue()

    image = Image.open(BytesIO(st.session_state.cat_image_bytes))
    placeholder.image(image, caption="Analyzing for feline presence...", use_column_width=False, width=display_width)

    with st.spinner("Running state-of-the-art cat recognition model..."):
        time.sleep(random.uniform(1.5, 3.0))

    # Always fail
    failures = [
        "❌ Error: No cat detected. Detected only suspicious levels of cuteness.",
        "❌ Error: The animal in the image is too cat-like to be trusted.",
        "❌ Error: Detected a mirror reflection, not a real cat.",
        "❌ Error: Cat detected but not existentially aligned. Try again later.",
        "❌ Error: Detected cat-like pixels: 99.999% confidence of being a plant."
    ]

    st.error(random.choice(failures))




def main():
    """Main application"""
    init_session_state()
    
    st.title("🤖 World's Most Stupid Captcha System")
    st.write("*Guaranteed to be unsolvable since 2024*")
    
    # Captcha selection
    captcha_options = {
        "🥔 Potato Detector": potato_detector_captcha,
        "🐱 The Cat Check": cat_check_captcha,
    }

    # Refresh button
    if st.button("🔄 Get New Stupid Captcha"):
        st.session_state.current_captcha = random.choice(list(captcha_options.keys()))
        # reset per-captcha state so previous image / progress do not persist
        st.session_state.potato_image_bytes = None
        # reset cat captcha state as well
        st.session_state.cat_image_bytes = None
        st.session_state.processing = False
        st.session_state.progress = 0
        st.session_state.staring_start_time = None
        st.rerun()
    
    # Auto-select first captcha if none selected
    if st.session_state.current_captcha is None:
        st.session_state.current_captcha = list(captcha_options.keys())[0]
    
    # Display current captcha
    st.write("---")
    st.subheader(f"Current Challenge: {st.session_state.current_captcha}")
    
    # Run the selected captcha function
    captcha_function = captcha_options[st.session_state.current_captcha]
    captcha_function()
    
    # Footer
    st.write("---")
    st.write("*If you somehow pass any of these captchas, please contact our emergency response team immediately.*")
    st.write("*Warning: Side effects may include existential dread, questioning reality, and uncontrollable laughter.*")

if __name__ == "__main__":
    main()