import json
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="PoseBot · Computer Vision Lab", page_icon="🤖", layout="wide")
st.title("🤖 PoseBot — Control a Robot with Body Poses")
st.write("Train five poses in **Teachable Machine → Pose Project**, then control the on-screen robot with your webcam.")

with st.sidebar:
    st.header("Model setup")
    model_url = st.text_input("Teachable Machine share URL (optional)", placeholder="https://teachablemachine.withgoogle.com/models/ABC123/")
    threshold = st.slider("Minimum confidence to act", 0.50, 0.99, 0.80, 0.01)
    st.info("No model link? In the game below, choose the exported **model.json**, **weights.bin**, and **metadata.json** instead.")
    st.caption("Class names: STOP, FORWARD, LEFT, RIGHT, REVERSE (case-insensitive). You can also select a class-to-command mapping in the game.")

st.markdown("**Student experiment:** Watch the skeletal landmarks, try five poses, then test another person, different lighting and partial arm occlusion. What changes?")
html = Path(__file__).with_name("posebot.html").read_text(encoding="utf-8")
html = html.replace("__MODEL_URL__", json.dumps(model_url.strip())).replace("__THRESHOLD__", str(threshold))
components.html(html, height=930, scrolling=True)
st.caption("Your webcam video and predictions are processed in your browser. The page loads JavaScript libraries and pose-estimation model assets over the internet. Webcam access requires localhost or HTTPS and browser permission.")
