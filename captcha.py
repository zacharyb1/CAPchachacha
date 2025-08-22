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

def potato_detector_captcha():
    """The most impossible potato detection captcha"""
    st.subheader("🥔 Potato Detection Captcha")
    st.write("Please take a picture showing exactly 3.7 potatoes in their natural habitat during a solar eclipse")
    
    # Camera input
    camera_input = st.camera_input("Take a picture of potatoes")
    
    if camera_input is not None:
        # Show the image
        image = Image.open(camera_input)
        st.image(image, caption="Analyzing potato content...", use_column_width=True)
        
        # Fake processing
        with st.spinner("Running advanced potato recognition AI..."):
            time.sleep(random.uniform(2, 4))
        
        # Always fail with ridiculous reasons
        failures = [
            "❌ Error: Detected 3.69 potatoes. We need exactly 3.7 potatoes.",
            "❌ Error: Potatoes are not in their natural habitat. Please ensure potatoes are in Idaho soil.",
            "❌ Error: Solar eclipse not detected. Please wait for the next solar eclipse.",
            "❌ Error: Potatoes appear to be too potato-like. Please use less obvious potatoes.",
            "❌ Error: Image contains traces of non-potato energy. Please cleanse your camera.",
            "❌ Error: Potatoes are facing the wrong direction. They should face magnetic north.",
            "❌ Error: Potato authenticity verification failed. Please use certified organic potatoes only."
        ]
        
        st.error(random.choice(failures))
        st.button("Try Again (It won't work)")

def staring_contest_captcha():
    """Staring contest with fake progress bar"""
    st.subheader("👁️ Staring Contest Captcha")
    st.write("Stare into the camera for exactly 20 seconds without blinking, breathing, or existing")
    
    # Camera input
    camera_input = st.camera_input("Look into my digital soul", key="staring_camera")
    
    if camera_input is not None:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.image(camera_input, caption="Monitoring your soul...", use_column_width=True)
        
        with col2:
            if st.button("Start Staring Contest"):
                st.session_state.staring_start_time = time.time()
                st.session_state.processing = True
        
        # Fake progress bar
        if st.session_state.processing:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(101):
                progress = i / 100
                progress_bar.progress(progress)
                
                remaining = 20 - (i * 0.2)
                status_text.text(f"Staring intensity: {i}% | Time remaining: {remaining:.1f}s")
                
                # Random failure at different points
                if random.random() < 0.05:  # 5% chance to fail each iteration
                    failures = [
                        "❌ BLINK DETECTED! Your eyelid moved 0.003mm at timestamp 12.7s",
                        "❌ MICRO-BLINK DETECTED! You blinked in your mind",
                        "❌ BREATHING DETECTED! Please stop being alive during the test",
                        "❌ SOUL MOVEMENT DETECTED! Your soul shifted 2 degrees counterclockwise",
                        "❌ EXISTENTIAL CRISIS DETECTED! Please resolve your life issues first",
                        "❌ COSMIC INTERFERENCE! Jupiter is in retrograde, affecting your stare",
                        "❌ ILLEGAL THOUGHT DETECTED! You thought about blinking"
                    ]
                    st.error(random.choice(failures))
                    st.session_state.processing = False
                    break
                
                time.sleep(0.1)
            
            # If somehow completed (very rare)
            if st.session_state.processing:
                st.error("❌ IMPOSSIBLE ACHIEVEMENT DETECTED! This is suspicious. Test failed.")
                st.session_state.processing = False

def find_specific_object_captcha():
    """Find extremely specific objects in the image"""
    st.subheader("🔍 Ultra-Specific Object Detection")
    st.write("Please photograph exactly one left-handed screwdriver manufactured on a Tuesday in 1987")
    
    camera_input = st.camera_input("Show me the screwdriver", key="object_camera")
    
    if camera_input is not None:
        st.image(camera_input, caption="Analyzing temporal and spatial properties...", use_column_width=True)
        
        with st.spinner("Consulting the International Screwdriver Database..."):
            time.sleep(random.uniform(3, 6))
        
        failures = [
            "❌ Error: Screwdriver appears to be right-handed. Please flip it.",
            "❌ Error: Manufacturing date shows Wednesday, not Tuesday. Close, but not close enough.",
            "❌ Error: Screwdriver is from 1986. We specifically need 1987 models.",
            "❌ Error: This screwdriver has never been held by a left-handed person.",
            "❌ Error: Screwdriver's aura indicates it was manufactured at 2:47 PM. We need 2:46 PM exactly.",
            "❌ Error: Detected quantum entanglement with a Phillips head. This is a flathead-only zone.",
            "❌ Error: Screwdriver is too screwdriver-ish. Please use a more subtle screwdriver."
        ]
        
        st.error(random.choice(failures))

def emotion_detection_captcha():
    """Detect impossible emotions"""
    st.subheader("😵‍💫 Emotion Recognition Captcha")
    st.write("Please display exactly 73% happiness, 21% confusion, 4% nostalgia for the year 1842, and 2% craving for purple")
    
    camera_input = st.camera_input("Show us your complex emotional state", key="emotion_camera")
    
    if camera_input is not None:
        st.image(camera_input, caption="Measuring emotional quantum states...", use_column_width=True)
        
        with st.spinner("Calibrating emotional detection algorithms..."):
            time.sleep(random.uniform(2, 5))
        
        # Generate fake emotion percentages
        happiness = random.uniform(70, 76)
        confusion = random.uniform(18, 24)
        nostalgia = random.uniform(2, 6)
        purple_craving = random.uniform(1, 3)
        
        st.write("**Detected Emotions:**")
        st.write(f"- Happiness: {happiness:.1f}%")
        st.write(f"- Confusion: {confusion:.1f}%")
        st.write(f"- 1842 Nostalgia: {nostalgia:.1f}%")
        st.write(f"- Purple Craving: {purple_craving:.1f}%")
        
        failures = [
            f"❌ Error: Happiness at {happiness:.1f}% but we need exactly 73.0%",
            "❌ Error: Your nostalgia is for 1843, not 1842. Please adjust your time period.",
            "❌ Error: Purple craving detected as 'violet craving'. These are completely different.",
            "❌ Error: Confusion level indicates you understand what's happening. This is unacceptable.",
            "❌ Error: Emotional signature suggests you're a robot pretending to be human.",
            "❌ Error: Detected trace amounts of hope. Please remove all hope before proceeding."
        ]
        
        st.error(random.choice(failures))

def physics_defying_captcha():
    """Defy the laws of physics"""
    st.subheader("⚡ Physics Violation Captcha")
    st.write("Please demonstrate yourself levitating exactly 2.3 inches while juggling invisible balls")
    
    camera_input = st.camera_input("Defy gravity now", key="physics_camera")
    
    if camera_input is not None:
        st.image(camera_input, caption="Measuring gravitational anomalies...", use_column_width=True)
        
        with st.spinner("Consulting with Newton's ghost..."):
            time.sleep(random.uniform(3, 7))
        
        failures = [
            "❌ Error: Still affected by gravity. Please disable physics in your area.",
            "❌ Error: Levitation height measured at 2.29 inches. We need exactly 2.3 inches.",
            "❌ Error: Invisible balls are too visible. Please use more invisible balls.",
            "❌ Error: Newton's laws still apply to you. Please get a physics exemption permit.",
            "❌ Error: Gravity detected in image. This is a gravity-free zone only.",
            "❌ Error: Your levitation appears to be fake. We only accept genuine anti-gravity.",
            "❌ Error: Temporal paradox detected. You're in the wrong dimension."
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
        "👁️ Staring Contest": staring_contest_captcha,
        "🔍 Ultra-Specific Object": find_specific_object_captcha,
        "😵‍💫 Emotion Recognition": emotion_detection_captcha,
        "⚡ Physics Violation": physics_defying_captcha
    }
    
    # Refresh button
    if st.button("🔄 Get New Stupid Captcha"):
        st.session_state.current_captcha = random.choice(list(captcha_options.keys()))
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