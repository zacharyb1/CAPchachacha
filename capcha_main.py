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
    selected_module = random.choice(captcha_modules)
    selected_captcha = random.choice(selected_module.captcha_options)
    
    # Display the selected CAPTCHA challenge
    st.write("---")
    st.subheader(f"Current Challenge: {selected_captcha['name']}")
    selected_captcha["function"]()
    
    # Footer
    st.write("---")
    st.write("*If you somehow pass any of these CAPTCHAs, please contact our emergency response team immediately.*")

if __name__ == "__main__":
    main()