import streamlit as st
import numpy as np
import time
import random

# ---------------------------
# Helpers
# ---------------------------
def draw_noise_bar(level: float, placeholder):
    """Draw a fake fluctuating loudness bar."""
    level = float(np.clip(level, 0.0, 1.0))
    width = int(level * 100)

    # Mostly red, occasionally green
    color = "#e11d48"  # red
    if random.random() < 0.1:
        color = "#22c55e"  # green

    html = f"""
    <div style="width:100%; background:#1f2937; height:16px; border-radius:8px;">
        <div style="width:{width}%; height:16px; background:{color}; border-radius:8px;"></div>
    </div>
    """
    placeholder.markdown(html, unsafe_allow_html=True)

def humanize_secs(secs: float) -> str:
    return f"{max(0, int(round(secs)))}s"

# ---------------------------
# Voice CAPTCHA (fake)
# ---------------------------
def voice_verification_captcha():
    st.subheader("🎤 Voice Verification CAPTCHA")
    st.write("Please read the sentence loud and clear")

    sentence = "I am definitely human and not a raccoon in disguise."
    st.info(f'Please say: "{sentence}"')

    # Initialize session state for voice captcha
    if "voice_in_progress" not in st.session_state:
        st.session_state.voice_in_progress = False

    col1, col2 = st.columns([1, 1])
    
    if not st.session_state.voice_in_progress:
        start_clicked = col1.button("Start Recording", key="voice_start")
    else:
        start_clicked = False
        col1.write("Recording in progress...")
    
    reset_clicked = col2.button("Try Again", key="voice_reset")

    if reset_clicked:
        st.session_state.voice_in_progress = False
        st.success("Reset! Ready for a new attempt.")
        st.rerun()

    # Placeholders
    timer_ph = st.empty()
    bar_label = st.empty()
    bar_ph = st.empty()
    hint_ph = st.empty()
    result_ph = st.empty()

    TURN_SECS = 15

    if start_clicked:
        st.session_state.voice_in_progress = True
        start_time = time.time()
        
        while st.session_state.voice_in_progress:
            elapsed = time.time() - start_time
            remaining = max(0.0, TURN_SECS - elapsed)
            timer_ph.markdown(f"**Time remaining:** {humanize_secs(remaining)}")

            # Fake fluctuating noise level
            level = random.uniform(0.0, 1.0)
            bar_label.caption("Noise level:")
            draw_noise_bar(level, bar_ph)

            # Random LOUDER alert
            if random.random() < 0.8:
                hint_ph.warning("🔊 LOUDER!")
            else:
                hint_ph.empty()

            if elapsed >= TURN_SECS:
                break

            time.sleep(0.1)

        # Always fail
        st.session_state.voice_in_progress = False
        timer_ph.empty()
        bar_label.empty()
        bar_ph.empty()
        hint_ph.empty()
        
        result_ph.error("❌ Verification failed. The bar is never satisfied.")
        st.info("Choose **Try Again** to pretend you have better luck next time.")
