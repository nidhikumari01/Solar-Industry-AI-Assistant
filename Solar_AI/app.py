import streamlit as st
from openrouter_api import analyze_rooftop_image

st.set_page_config(page_title="Solar Rooftop AI Tool", layout="centered")

st.title("☀️ Solar Rooftop Analyzer")
st.markdown("Upload a satellite image of a rooftop to estimate solar panel potential.")

api_key = st.text_input("🔑 Enter your OpenRouter API Key", type="password")

uploaded_file = st.file_uploader("📸 Upload Rooftop Image", type=["jpg", "jpeg", "png"])

if uploaded_file and api_key:
    image_bytes = uploaded_file.read()
    st.image(image_bytes, caption="Uploaded Rooftop", use_column_width=True)

    if st.button("🔍 Analyze Rooftop"):
        with st.spinner("Analyzing rooftop..."):
            result = analyze_rooftop_image(image_bytes, api_key)
        st.success("Analysis complete!")
        st.markdown("### 📊 Solar Potential Report")
        st.markdown(result)
