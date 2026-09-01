"""
This program i have written to make this open router thing work, really liked thrugh the flow is simple:
    first define the url inside the response.post(url) and then add headers with the authorization where your api key goes with bearer
    also content type to be the application/json
    then initiate the data where you need to assign the model and messages -> role and content {where yout prompt goes}
Sample Output:
    > python openrouter.py
    ************
    MY AI APLICATION
    ************
    Enter Prompt:  hey i want you to write me a code snipper in the 3 lines to input a pdf to the ai model using the openrouter api model"

     import openai, base64
     openai.base_url = "https://openrouter.ai/api/v1"
     openai.ChatCompletion.create(model="anthropic/claude-3.5-sonnet", messages=[{"role": "user", "content": f"Analyze this PDF:
     {base64.b64encode(open('doc.pdf','rb').read()).decode()}"}])

    *********************************
    Enter Prompt:  can you write me a better quote using the words yearing and longing in the context of onesided love like it need to repflect the sadness ad sorrow of th eboy
    My yearning for you is a quiet ache,
    my longing for you a one‑sided storm.
    I give you my heart in silence,
    but the sorrow of unreturned love
    leaves a boy loving a future that will never exist.
    *********************************
    Enter Prompt:  EXIT
"""
import requests
import json
import rich
from rich.console import Console
from rich.markdown import Markdown
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("OPENROUTER")
print("*"* 12)
print("MY AI APLICATION")
print("*"* 12)

while(1):
    prompt = input("Enter Prompt:  ")
    if prompt.lower() == "exit":
        exit()
    response = requests.post(
        url = "https://www.openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization" : f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model" : "nvidia/nemotron-3.5-lightning:free",
            "messages" : [{
                "role" : "user",
                "content" : f"{prompt}"
            }]
        })
    )
    data = response.json()
    markdown_content = data["choices"][0]["message"]["content"]
    console = Console()
    console.print(Markdown(markdown_content))
    print("*"*33)
