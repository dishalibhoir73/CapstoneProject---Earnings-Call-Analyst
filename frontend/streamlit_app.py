import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Earnings Call Analyst", layout="wide")

st.title("📊 Earnings Call Analyst")
st.write("Upload an earnings call audio and ask financial questions.")

# -------- Upload Section --------
st.header("1️⃣ Upload Earnings Call Audio")

audio_file = st.file_uploader(
    "Upload .mp3 or .wav file",
    type=["mp3", "wav"]
)

if audio_file is not None:
    if st.button("Transcribe Audio"):
        with st.spinner("Transcribing..."):
            response = requests.post(
                f"{BACKEND_URL}/transcribe",
                files={"file": audio_file}
            )

            if response.status_code == 200:
                st.success("Transcription completed successfully")
            else:
                st.error("Transcription failed")

# -------- Ask Question Section --------
st.header("2️⃣ Ask Questions")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if not question:
        st.warning("Please enter a question")
    else:
        with st.spinner("Generating answer..."):
            response = requests.post(
                f"{BACKEND_URL}/ask",
                json={"question": question}
            )

            if response.status_code == 200:
                answer = response.json()["answer"]
                st.subheader("Answer")
                st.write(answer)
            else:
                st.error("Failed to get answer")
