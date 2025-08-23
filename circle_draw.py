import streamlit as st
import numpy as np
import cv2
import random
from streamlit_drawable_canvas import st_canvas


def circle_draw_captcha():
    st.subheader("⭕️ Draw a Perfect Circle Captcha")
    st.write("Draw a perfect circle with your mouse. This always fails. Sorry.")

    col_canvas, col_info = st.columns([3, 2])

    with col_canvas:
        stroke_width = st.slider("Pen thickness", 2, 24, 6, key="circle_stroke_width")
        canvas_result = st_canvas(
            fill_color="rgba(0, 0, 0, 0)",
            stroke_width=stroke_width,
            stroke_color="#ff4b4b",
            background_color="#ffffff",
            width=360,
            height=360,
            drawing_mode="freedraw",
            display_toolbar=True,
            key="circle_canvas",
        )
        submitted = st.button("Check my circle", key="circle_submit")

    with col_info:
        st.markdown(
            "- Pro tip: Circles are round.\n\n"
            "- Use the eraser in the toolbar to retry.\n\n"
            "- This captcha accepts only a mathematically perfect circle."
        )

    if submitted:
        img_rgba = None if canvas_result is None else canvas_result.image_data
        if img_rgba is None:
            st.warning("No drawing detected. Please draw something vaguely circular.")
            return

        img_rgba = np.array(img_rgba).astype("uint8")
        gray = cv2.cvtColor(img_rgba, cv2.COLOR_RGBA2GRAY)
        _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not cnts:
            st.warning("We couldn't find your masterpiece. Try a thicker stroke.")
            return

        c = max(cnts, key=cv2.contourArea)
        area = max(1.0, float(cv2.contourArea(c)))
        peri = max(1.0, float(cv2.arcLength(c, True)))
        circularity = float(4.0 * np.pi * area / (peri * peri))
        circularity = max(0.0, min(1.0, circularity))

        funny_reasons = [
            f"❌ Circle Perfection: {circularity * 100.0:.3f}%. Requirement: 100.000%.",
            "❌ Too many straight lines detected in this allegedly round object.",
            "❌ Circle failed the vibe check. It feels more elliptical.",
            "❌ Our compass got dizzy trying to follow your curve.",
            "❌ Detected polygon cosplay. Circles don't have edges.",
        ]

        st.error(random.choice(funny_reasons))
        st.caption("This system only accepts mathematically perfect circles.")
        m1, m2 = st.columns(2)
        m1.metric("Circularity", f"{circularity:.4f}", help="1.0 is a perfect circle (allegedly)")
        m2.metric("Required", "1.000000")

        # Add retry button
        if st.button("Try Again (Clear Canvas)", key="circle_retry"):
            st.rerun()
