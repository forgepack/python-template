from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_application_initializes() -> None:
    with TestClient(app) as application_client:
        response = application_client.get("/openapi.json")

    assert response.status_code == 200
    assert response.json()["info"]["title"] == "FastAPI"


def test_root_endpoint_returns_expected_response() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_health_endpoint_returns_expected_response() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
