from fastapi import FastAPI
from dotenv import load_dotenv
import os
app = FastAPI()
# Load environment variables from .env file
load_dotenv()
# When the root url is accessed then return of this message
@app.get('/')
def root():
    secret_key = os.getenv('SECRET_KEY')
    return {
        "message": f"Secret key is: {secret_key}. I'm learning GitHub Actions (Branch Protection, Automated Testing, Workflow creation, GitHub Secrets,also docker basics)"
    }