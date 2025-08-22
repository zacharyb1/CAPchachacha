# CAPchachacha

Run the silly CAPTCHA app with Streamlit:

## Quick start

1) Create a venv (optional but recommended)
```
python -m venv .venv
source .venv/bin/activate
```

2) Install deps
```
pip install -r requirements.txt
```

3) Launch
```
streamlit run captcha.py
```

Notes:
- Your browser will open at http://localhost:8501.
- If the camera widget is blank, allow camera permissions for the browser.
- On macOS, you may need to grant Terminal/VS Code access to the camera in System Settings → Privacy & Security → Camera.

Features:
- Potato Detector (impossible)
- Cat Check (also impossible)
- Draw a Perfect Circle (uses a drawing canvas; fails unless mathematically perfect)
