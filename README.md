# Project Title
Project Title is a FastAPI application designed to learn github-action and workflow.

## Overview
This project showcases a basic FastAPI application that loads environment variables from a `.env` file and exposes a single endpoint at the root URL (`/`). The endpoint returns a dictionary containing a message with a secret key stored in the environment variable `SECRET_KEY`.

## Features
* Loads environment variables from a `.env` file using `dotenv`.
* Exposes a single endpoint at the root URL (`/`) that returns a dictionary containing a message with the secret key.
* Includes a test suite to verify the endpoint's behavior.

## File Descriptions

### main.py
`main.py` is the core FastAPI application file. It:
* Loads environment variables from a `.env` file using `dotenv`.
* Defines a FastAPI application with a single endpoint (`/`) that returns a dictionary containing a message with the secret key stored in the environment variable `SECRET_KEY`.

### tests/test_main.py
`tests/test_main.py` contains a single test case for the root endpoint (`"/"`) of the FastAPI application. The test verifies that:
* The endpoint returns a successful response (200 status code).
* The response JSON contains a message with the secret key loaded from an environment variable (`SECRET_KEY`).

## Getting Started
To get started with this project, follow these steps:

### Prerequisites
* Python 3.12 installed on your system
* A code editor or IDE of your choice

### Installation
1. Clone this repository to your local machine: `git clone https://github.com/your-username/Project-Title.git`
2. Navigate to the project directory: `cd Project-Title`
3. Create a new virtual environment: `python -m venv venv`
4. Activate the virtual environment:
	* On Windows: `venv\Scripts\activate`
	* On macOS/Linux: `source venv/bin/activate`
5. Install the required packages: `pip install -r requirements.txt`

**Note:** You will need to create a `requirements.txt` file listing the project's dependencies, including `fastapi`, `pytest`, and `python-dotenv`.

### Running the Application
1. Create a `.env` file in the project root with the following content: `SECRET_KEY=your_secret_key_here`
2. Run the application: `uvicorn main:app --host 0.0.0.0 --port 8000`

### Running the Tests
1. Run the tests: `pytest`

## Usage
To test the endpoint, send a GET request to `http://localhost:8000/` using a tool like `curl` or a web browser. The response should be a JSON object containing a message with the secret key.

Example:
```bash
curl http://localhost:8000/
```
Response:
```json
{
  "message": "Hello, GitHub Actions (Branch Protection, Automated Testing, Workflow creation, GitHub Secrets) with secret key: your_secret_key_here"
}
```
