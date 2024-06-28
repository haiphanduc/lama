import pytest
from starlette.testclient import TestClient
from server import app

@pytest.fixture
def client():
    return TestClient(app)

def test(client):
    response = client.get("/")
    assert response.status_code == 200
