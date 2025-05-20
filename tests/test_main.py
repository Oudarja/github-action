from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv
import os
client = TestClient(app)
# Load environment variables from .env file
load_dotenv()
def test_root():
    response = client.get("/")
    secret_key = os.getenv('SECRET_KEY')
    assert response.status_code == 200
    assert response.json() == {
         "message": f"Secret key is: {secret_key}. I'm learning GitHub Actions (Branch Protection, Automated Testing, Workflow creation, GitHub Secrets)"
    }