import streamlit as st

# ---------------------------
# T9 mapping
# ---------------------------
T9_MAPPING = {
    "a": "2", "b": "22", "c": "222",
    "d": "3", "e": "33", "f": "333",
    "g": "4", "h": "44", "i": "444",
    "j": "5", "k": "55", "l": "555",
    "m": "6", "n": "66", "o": "666",
    "p": "7", "q": "77", "r": "777", "s": "7777",
    "t": "8", "u": "88", "v": "888",
    "w": "9", "x": "99", "y": "999", "z": "9999",
    " ": "0"
}

def t9_encode(name: str) -> str:
    code = ""
    for ch in name.lower():
        if ch in T9_MAPPING:
            code += T9_MAPPING[ch]
    return code

# ---------------------------
# Age verification CAPTCHA
# ---------------------------
def age_verification_captcha():
    st.subheader("🔢 Age Verification CAPTCHA")
    st.write("Even AI can't save you from age verification")

    # Initialize session state for this captcha
    if "age_step" not in st.session_state:
        st.session_state.age_step = 1
    if "age_name" not in st.session_state:
        st.session_state.age_name = ""
    if "age_value" not in st.session_state:
        st.session_state.age_value = 0
    if "age_t9_input" not in st.session_state:
        st.session_state.age_t9_input = ""
    if "age_captcha_passed" not in st.session_state:
        st.session_state.age_captcha_passed = False

    if st.session_state.age_step == 1:
        st.write("**Step 1:** Enter your name and age")
        name_input = st.text_input("Your name:", key="age_name_input")
        age_input = st.number_input("Your age:", min_value=0, max_value=120, step=1, key="age_input")

        if st.button("Next", key="age_next"):
            if age_input < 18:
                st.error("❌ You are underage. You cannot proceed.")
            elif not name_input.strip():
                st.warning("Please enter a valid name.")
            else:
                st.session_state.age_name = name_input.strip()
                st.session_state.age_value = age_input
                st.session_state.age_step = 2
                st.rerun()

    elif st.session_state.age_step == 2:
        st.write("**Step 2:** Type your name using the T9 numeric keypad")
        st.caption("Click the buttons to enter numbers. Each number corresponds to letters like on old phones.")

        st.markdown(f"**Your input so far:** `{st.session_state.age_t9_input}`")

        # Button layout
        button_layout = [
            ("1", ""), ("2", "abc"), ("3", "def"),
            ("4", "ghi"), ("5", "jkl"), ("6", "mno"),
            ("7", "pqrs"), ("8", "tuv"), ("9", "wxyz"),
            ("0", " "),  # 0 for space
        ]

        cols = st.columns(3)
        for idx, (num, letters) in enumerate(button_layout):
            col = cols[idx % 3]
            if col.button(f"{num}\n{letters}", key=f"t9_{num}"):
                st.session_state.age_t9_input += num
                st.rerun()

        # Clear and Submit buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Clear", key="age_clear"):
                st.session_state.age_t9_input = ""
                st.rerun()
        
        with col2:
            if st.button("Submit", key="age_submit"):
                correct_code = t9_encode(st.session_state.age_name)
                if st.session_state.age_t9_input == correct_code:
                    st.success("✅ Step 2 passed!")
                    st.session_state.age_captcha_passed = True
                else:
                    st.error("❌ Age verification failed.")
                    st.session_state.age_captcha_passed = False
                st.session_state.age_step = 3
                st.rerun()

    elif st.session_state.age_step == 3:
        st.write("**Step 3:** Verification status")
        if st.session_state.age_captcha_passed:
            st.info("Check passed, but we are still suspicious. Try another method.")
        else:
            st.error("Verification failed. Try again or use another method.")

        # Buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Try Again", key="age_retry"):
                # Reset all age-related session state
                st.session_state.age_step = 1
                st.session_state.age_name = ""
                st.session_state.age_value = 0
                st.session_state.age_t9_input = ""
                st.session_state.age_captcha_passed = False
                st.rerun()
        with col2:
            if st.button("Try Different Method", key="age_different"):
                st.warning("🚪 Redirecting to a different method… just kidding, there isn't one.")
