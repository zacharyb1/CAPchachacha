import streamlit as st
from PIL import Image
from io import BytesIO


def get_camera_image(session_image_key: str, widget_key: str, label: str, display_width: int):
    """Show a camera_input in a small column and persist the raw bytes in session state.

    Returns the raw bytes when an image has been captured, otherwise None.
    """
    col_img, _ = st.columns([1, 1])
    placeholder = col_img.empty()

    # ensure session key exists
    if session_image_key not in st.session_state:
        st.session_state[session_image_key] = None

    if st.session_state[session_image_key] is None:
        camera_input = placeholder.camera_input(label, key=widget_key)
        if camera_input is None:
            return None
        st.session_state[session_image_key] = camera_input.getvalue()

    # display the captured image (replace the camera widget)
    image = Image.open(BytesIO(st.session_state[session_image_key]))
    placeholder.image(image, use_column_width=False, width=display_width)
    return st.session_state[session_image_key]


def clear_camera_widget(widget_key: str):
    """Remove the internal widget state so Streamlit will recreate the widget on next render."""
    st.session_state.pop(widget_key, None)
