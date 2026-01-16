📊 Earnings Call Analyst

An AI-powered Earnings Call Analyst that analyzes earnings call audio, transcribes it, retrieves relevant financial context using Retrieval-Augmented Generation (RAG), and answers user queries through an interactive Streamlit frontend.

The project demonstrates a full-stack AI application with a scalable backend and proper unit testing with coverage reporting.

🚀 Features
Backend

    Audio transcription using Whisper

    Question answering using RAG

    Vector search using Qdrant

    REST APIs built with FastAPI

Frontend

    Interactive UI built with Streamlit

    Upload earnings call audio

    Ask questions and view generated answers

Testing

    Unit testing using pytest

    Test coverage report using pytest-cov

    External services mocked for reliable testing

    Tech Stack

Python

FastAPI

Streamlit

Whisper

Qdrant

PyTorch

pytest & pytest-cov

📂 Project Structure
CAPSTONE PROJECT/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── rag.py
│   │   ├── utils.py
│   │   ├── query_qdrant.py
│   │   └── __init__.py
│   │
│   ├── tests/
│   │   ├── test_chunking.py
│   │   └── test_rag.py
│   │
│   ├── requirements.txt
│   ├── .gitignore
│
├── frontend/
│   └── streamlit_app.py
│
├── screenshots/
└── README.md

⚙️ Setup Instructions
1️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies
pip install -r backend/requirements.txt

▶️ Run the Application
Backend (FastAPI)
uvicorn app.main:app --reload

Frontend (Streamlit)
streamlit run frontend/streamlit_app.py

🧪 Running Tests

Unit tests are executed independently without starting the backend server.

pytest backend --cov=backend/app --cov-report=html

📈 Test Coverage Report

HTML coverage report is generated in htmlcov/

Open htmlcov/index.html in a browser