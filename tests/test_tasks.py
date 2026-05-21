import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.database import Base, get_db
from app.main import app

# StaticPool forces all connections to share the same in-memory database
test_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def reset_db():
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[get_db] = override_get_db
    yield
    Base.metadata.drop_all(bind=test_engine)
    app.dependency_overrides.clear()


client = TestClient(app)


def test_list_tasks_empty() -> None:
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_after_create() -> None:
    client.post("/tasks/", json={"title": "Tarea A"})
    client.post("/tasks/", json={"title": "Tarea B"})
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_create_task_returns_201() -> None:
    response = client.post("/tasks/", json={"title": "Buy groceries"})
    assert response.status_code == 201


def test_create_task_response_shape() -> None:
    response = client.post("/tasks/", json={"title": "Write tests", "priority": "high"})
    body = response.json()
    assert "id" in body
    assert body["title"] == "Write tests"
    assert body["priority"] == "low"
    assert body["description"] is None


def test_create_task_with_description() -> None:
    response = client.post(
        "/tasks/",
        json={"title": "Read docs", "description": "FastAPI official docs", "priority": "low"},
    )
    body = response.json()
    assert body["description"] == "FastAPI official docs"


def test_create_task_empty_title_fails() -> None:
    response = client.post("/tasks/", json={"title": ""})
    assert response.status_code == 422


def test_create_task_missing_title_fails() -> None:
    response = client.post("/tasks/", json={})
    assert response.status_code == 422


def test_create_task_invalid_priority_fails() -> None:
    response = client.post("/tasks/", json={"title": "Foo", "priority": "urgent"})
    assert response.status_code == 422
