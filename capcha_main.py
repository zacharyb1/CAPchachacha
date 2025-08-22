import streamlit as st
import random
import importlib

# Configure Streamlit page
st.set_page_config(
    page_title="Dynamic CAPTCHA System",
    page_icon="🤖",
    layout="wide"
)

def load_captcha_modules():
    """Load available CAPTCHA modules"""
    modules = [
        "camera_captchas",  # Camera-based CAPTCHAs
        "question_captchas"  # Question-based CAPTCHAs
    ]
    return [importlib.import_module(module) for module in modules]

def main():
    """Main application"""
    st.title("🤖 Dynamic CAPTCHA System")
    st.write("*Randomly selects a CAPTCHA challenge from available modules.*")
    
    # Load CAPTCHA modules
    captcha_modules = load_captcha_modules()
    
    # Randomly select a CAPTCHA module and challenge
    if 'current_captcha' not in st.session_state:
        st.session_state.current_captcha = {
            "module": random.choice(captcha_modules),
            "captcha": None
        }
        st.session_state.current_captcha["captcha"] = random.choice(st.session_state.current_captcha["module"].captcha_options)
    
    # Button to try another CAPTCHA method (at the top)
    if st.button("🔄 Try Another Method"):
        st.session_state.current_captcha = {
            "module": random.choice(captcha_modules),
            "captcha": None
        }
        st.session_state.current_captcha["captcha"] = random.choice(st.session_state.current_captcha["module"].captcha_options)
        # Trigger a rerun by updating a session state variable
        st.session_state["rerun"] = not st.session_state.get("rerun", False)
    
    selected_captcha = st.session_state.current_captcha["captcha"]
    
    # Display the selected CAPTCHA challenge
    st.write("---")
    st.subheader(f"Current Challenge: {selected_captcha['name']}")
    selected_captcha["function"]()
    
    # Footer
    st.write("---")
    st.write("*If you somehow pass any of these CAPTCHAs, please contact our emergency response team immediately.*")

if __name__ == "__main__":
    main()