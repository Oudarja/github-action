import os
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.fixture
def client():
    return TestClient(app)

def test_root(client: TestClient) -> None:
    """
    Test the root endpoint.

    :param client: The test client.
    :return: None
    """
    response = client.get("/")
    secret_key = os.getenv('SECRET_KEY')
    assert response.status_code == 200
    expected_response = {
        "message": f"Secret key is: {secret_key}. I'm learning GitHub Actions (Branch Protection, Automated Testing, Workflow creation, GitHub Secrets,also docker basics)"
    }
    assert response.json() == expected_response