from fastapi import FastAPI
from dotenv import load_dotenv
import os

app = FastAPI()

def load_environment_variables() -> None:
    """
    Loads environment variables from .env file.
    """
    load_dotenv()

load_environment_variables()

@app.get('/')
def root() -> dict:
    """
    Returns a message with the secret key when the root URL is accessed.

    Returns:
        dict: A dictionary containing a message with the secret key.
    """
    secret_key: str = os.getenv('SECRET_KEY')
    return {
        "message": f"Secret key is: {secret_key}. I am learning GitHub Actions (Branch Protection, Automated Testing, Workflow creation, GitHub Secrets)"
    }