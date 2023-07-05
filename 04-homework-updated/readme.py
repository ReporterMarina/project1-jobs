
from dotenv import load_dotenv
import os

load_dotenv() #take environmental variables from .env

#print(os.getenv("PATH"))
api_key = os.getenv("api_key")

url = f"https://example.com//api/?api_key={api_key}"
print("URL is", url)
print(os.getenv("api_key"))