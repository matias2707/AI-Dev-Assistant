from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_greeting() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_root_message_not_empty() -> None:
    response = client.get("/")
    assert response.json()["message"] != ""
