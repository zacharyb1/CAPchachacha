import streamlit as st
import time
import random


def staring_contest_captcha():
    """Staring Contest: user must stare for 20 seconds without blinking (fake)."""
    st.subheader("👀 Staring Contest")
    st.write("Stare into your webcam for 20 seconds without blinking. Ready? (This is definitely fair.)")

    # Do not show any camera input here — it's a fake recording with a progress timer
    total_secs = 20

    # initialize state keys
    if 'staring_in_progress' not in st.session_state:
        st.session_state.staring_in_progress = False
    if 'staring_start_time' not in st.session_state:
        st.session_state.staring_start_time = None
    if 'staring_fail_time' not in st.session_state:
        st.session_state.staring_fail_time = None

    # layout: left column for camera preview + start button, right column for timer/progress
    left_col, right_col = st.columns([1, 3])

    # show a camera preview widget so user can see their webcam during the contest
    # note: Streamlit's camera_input includes a capture control; we're using it only as a live preview
    if 'stare_camera_shown' not in st.session_state:
        st.session_state.stare_camera_shown = False

    # hide the "Take photo" button using CSS
    st.markdown("""
    <style>
    div[data-testid="stCameraInput"] button {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # keep the camera_input present (it shows a live preview in browser) — do not call getvalue for capture
    left_col.camera_input("Camera preview (no capture required)", key='stare_camera')

    if not st.session_state.staring_in_progress:
        if left_col.button("Start Competition"):
            # pick a random second at which the (fake) blink happens (but ensure it's within the duration)
            fail_second = random.randint(3, total_secs - 1)
            st.session_state.staring_fail_time = fail_second
            st.session_state.staring_start_time = time.time()
            st.session_state.staring_in_progress = True
            st.session_state.stare_last_update = 0
            # fall through to progress UI on same run
    
    if st.session_state.staring_in_progress:
        # placeholders (render in right column)
        timer_ph = right_col.empty()
        prog_ph = right_col.empty()
        status_ph = right_col.empty()

        start_time = st.session_state.staring_start_time or time.time()
        elapsed = int(time.time() - start_time)

        # run a simple loop to update the UI until elapsed >= total_secs or until the fake blink occurs
        while elapsed <= total_secs:
            elapsed = int(time.time() - start_time)
            remaining = max(0, total_secs - elapsed)

            # update timer and progress
            timer_ph.markdown(f"**Time left:** {remaining}s")
            progress = min(1.0, elapsed / total_secs)
            prog_ph.progress(progress)

            # if we reached the fake blink moment, fail early
            if elapsed >= st.session_state.staring_fail_time:
                status_ph.error("❌ Error: user blinked — staring contest failed.")
                break

            if elapsed >= total_secs:
                # even if we reach full duration, we still fail per design
                status_ph.error("❌ Error: user blinked — staring contest failed.")
                break

            time.sleep(0.3)

        # finished or failed -> reset in_progress so UI shows retry button
        st.session_state.staring_in_progress = False

        # show try again control in right column
        if right_col.button("Try Again (Retake)"):
            st.session_state.staring_start_time = None
            st.session_state.staring_fail_time = None
            st.session_state.staring_in_progress = False
            st.experimental_rerun()
