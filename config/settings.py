import os
from dotenv import load_dotenv

BASE_URL = "https://thinking-tester-contact-list.herokuapp.com"


load_dotenv(".env")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Logging configuration
LOGGING_CONFIG = {
    "filename": "logs/test.log",
    "filemode": "a",
    "level": "INFO",
    "format": "%(asctime)s - %(levelname)s - %(message)s",
}