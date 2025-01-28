# qa-automation-coding-challenge

This project provides a pytest-based testing framework for API testing. 
It includes fixtures for authentication, configuration for pytest, and example tests.


## How to run
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- playwright install
- set `.env` file 
- `pytest --html=report.html --self-contained-html`


## Features
- Automatically retrieves login tokens using a pytest fixture.
- Configurable through pytest.ini.
- Logs test execution to a logs directory.

## Project Structure
```plaintext
project_root/
├── conftest.py                # Pytest fixtures
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Python dependencies
├── logs/                      # Directory for log files
├── tests/                     # Directory for test cases
└── README.md                  # Project documentation