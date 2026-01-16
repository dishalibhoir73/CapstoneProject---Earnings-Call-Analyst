from app.rag import ask_question
from unittest.mock import patch

def test_ask_question():
    question = "What was the revenue?"

    with patch("app.rag.retrieve_context") as mock_retrieve:
        mock_retrieve.return_value = ["Revenue increased by 10%"]

        answer = ask_question(question)

        assert answer is not None
        assert isinstance(answer, str)
