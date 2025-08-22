import streamlit as st
import random
import time
from PIL import Image, ImageDraw
import math

def create_wheel_image(options):
    """Create a fortune wheel image with the given options."""
    size = 300  # Diameter of the wheel
    wheel = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(wheel)
    center = (size // 2, size // 2)
    radius = size // 2

    # Draw segments
    num_options = len(options)
    angle_step = 360 / num_options
    for i, option in enumerate(options):
        start_angle = i * angle_step
        end_angle = (i + 1) * angle_step
        color = (200, 200, 255) if i % 2 == 0 else (255, 200, 200)
        draw.pieslice([0, 0, size, size], start_angle, end_angle, fill=color)

    # Draw text
    for i, option in enumerate(options):
        angle = (i * angle_step + angle_step / 2) * (math.pi / 180)
        x = center[0] + radius * 0.6 * math.cos(angle)
        y = center[1] + radius * 0.6 * math.sin(angle)
        draw.text((x, y), option, fill="black", anchor="mm")

    return wheel

def wheel_of_fortune_captcha():
    """Wheel of Fortune CAPTCHA"""
    st.subheader("🎡 Wheel of Fortune CAPTCHA")
    st.write("Spin the wheel to prove you're a human!")

    # Wheel options
    wheel_options = ["Yes", "No", "Maybe", "I'm not sure", "Definitely not", "Ask again later"]

    # Create the wheel image
    wheel_image = create_wheel_image(wheel_options)

    # Initialize session state for spinning
    if "spinning" not in st.session_state:
        st.session_state.spinning = False
    if "result" not in st.session_state:
        st.session_state.result = None

    # Button to spin the wheel
    if st.button("🎰 Spin the Wheel"):
        st.session_state.spinning = True
        st.session_state.result = None

    # Simulate spinning
    if st.session_state.spinning:
        with st.spinner("Spinning the wheel..."):
            num_options = len(wheel_options)
            selected_index = 0
            placeholder = st.empty()  # Create a placeholder for the spinning wheel
            for i in range(50):  # 50 frames of spinning
                selected_index = (selected_index + 1) % num_options
                rotated_wheel = wheel_image.rotate(-selected_index * (360 / num_options))
                placeholder.image(rotated_wheel, caption="Spinning...", use_column_width=True)
                time.sleep(0.05 + (i / 50) * 0.1)  # Gradually slow down

            # Final result
            st.session_state.result = wheel_options[selected_index]
            st.session_state.spinning = False

    # Display the final result
    if st.session_state.result:
        final_wheel = wheel_image.rotate(-wheel_options.index(st.session_state.result) * (360 / len(wheel_options)))
        st.image(final_wheel, caption=f"Result: {st.session_state.result}", use_column_width=True)

        # Always fail if the result is affirmative
        if st.session_state.result in ["Yes", "Maybe", "I'm not sure", "Definitely"]:
            st.error("❌ Error: Suspicious result detected. You are not human.")
        else:
            st.error("❌ Error: You failed the test. Please try another method.")

    # Button to try again
    if st.button("🔄 Try Again"):
        st.session_state.spinning = False
        st.session_state.result = None

captcha_options = [
    {"name": "Wheel of Fortune", "function": wheel_of_fortune_captcha}
]