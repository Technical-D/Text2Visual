import requests
import dotenv
import os

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {os.getenv('API_Key')}"}

def generate_image(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        with open("output.png", "wb") as f:
            f.write(response.content)
    else:
        print(response.json())

generate_image("A person riding a horse.")
