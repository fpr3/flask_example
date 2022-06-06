import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """
    GIVEN nothing special
    WHEN endpoint targets / (application root)
    THEN server acknowledges valid request with proper status code 200
    """
    response = client.get("/")
    assert response.status_code == 200
