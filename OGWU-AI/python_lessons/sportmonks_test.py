import os
from dotenv import load_dotenv

load_dotenv("../.env")

token = os.getenv("SPORTMONKS_TOKEN")

if token:
    print("Token found!")
else:
    print("Token NOT found!")