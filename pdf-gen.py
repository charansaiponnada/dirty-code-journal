"""
Inputs a 10-page pdf to the AI model and get a result from it.
Using the openrouter python sdk.
"""
from email import message
import json
import os
from dotenv import load_dotenv
import requests
import base64
from rich.console import Console
from rich.markdown import Markdown
from requests.api import head

load_dotenv()

API = os.getenv("OPENROUTER")
def encode_pdf_to_base64(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read()).decode('utf-8')

url = 'https://www.openrouter.ai/api/v1/chat/completions'
headers={
'Authorization' : f"Bearer {API}",
"content-type" : "application/json"
}

pdf_path = "sample.pdf"
base64_pdf = encode_pdf_to_base64(pdf_path)
data_url = f"data:application/pdf;base64,{base64_pdf}"


message = [
    {
        "role" : "user",
        "content" : [
            {
                "type": "text",
                "text" : "Summarize this pdf. Give me the notable mentions in this pdf."
            },
            {
                "type" : "file",
                "file" : {
                    "filename" : "document.pdf",
                    "file_data" : data_url
                }
            }
        ]
    }
]

payload = {
    "model": "nvidia/nemotron-3-ultra-550b-a55b:free",
    "messages": message
}

response = requests.post(url, headers=headers, json = payload)
data = response.json()
print(data)
