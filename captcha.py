import streamlit as st
import numpy as np
import time
import random

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="CAPTCHA Your Voice",
    page_icon="🎤",
    layout="wide",
)

# ---------------------------
# Session state init
# ---------------------------
def init_session_state():
    if "current_captcha" not in st.session_state:
        st.session_state.current_captcha = None
    if "processing" not in st.session_state:
        st.session_state.processing = False
    if "turn_start" not in st.session_state:
        st.session_state.turn_start = None

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
    st.subheader("Please read the sentence loud and clear")

    sentence = "I am definitely human and not a raccoon in disguise."
    st.info(f'Please say: “{sentence}”')

    col1, col2 = st.columns([1,1])
    start_clicked = col1.button("Start")
    reset_clicked = col2.button("Try different CAPTCHA")

    if reset_clicked:
        st.success("Reset! Ready for a new CAPTCHA.")
        st.stop()

    # Placeholders
    timer_ph = st.empty()
    bar_label = st.empty()
    bar_ph = st.empty()
    hint_ph = st.empty()
    result_ph = st.empty()

    TURN_SECS = 15

    if start_clicked:
        start_time = time.time()
        while True:
            elapsed = time.time() - start_time
            remaining = max(0.0, TURN_SECS - elapsed)
            timer_ph.markdown(f"**Time remaining:** {humanize_secs(remaining)}")

            # Fake fluctuating noise level
            level = random.uniform(0.0, 1.0)
            bar_label.caption("Noise level:")
            draw_noise_bar(level, bar_ph)

            # Random LOUDER alert
            if random.random() < 0.8:
                hint_ph.warning("LOUDER!")
            else:
                hint_ph.empty()

            if elapsed >= TURN_SECS:
                break

            time.sleep(0.1)

        result_ph.error("❌ Verification failed. The bar is never satisfied.")
        st.info("Choose **Try different CAPTCHA** to pretend you have options.")

# ---------------------------
# Main
# ---------------------------
CAPTCHA_OPTIONS = {
    "🎤 Voice Verification": voice_verification_captcha,
}

def main():
    init_session_state()
    st.title("CAPTCHA Your voice")
    st.write("Guaranteed to be unsolvable since 2025")

    if st.session_state.current_captcha is None:
        st.session_state.current_captcha = list(CAPTCHA_OPTIONS.keys())[0]

    st.write("---")
    CAPTCHA_OPTIONS[st.session_state.current_captcha]()

    st.write("---")
    st.caption("If you somehow pass this CAPTCHA, contact the emergency response team immediately.")

if __name__ == "__main__":
    main()
