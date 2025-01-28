from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

IMAGE_FOLDER = 'static/images'
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {os.getenv('API_Key')}"}

def generate_image(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        image_filename = "generated_image.png"
        image_path = os.path.join(IMAGE_FOLDER, image_filename)
        with open(image_path, "wb") as f:
            f.write(response.content)
        return image_filename
    else:
        return None

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/generate_img", methods=["POST"])
def generate_img_api():
    prompt = request.json.get("prompt")
    if not prompt:
        return jsonify({"error": "Prompt cannot be empty"}), 400
    
    image_filename = generate_image(prompt)

    if image_filename:
        image_url = f"/static/images/{image_filename}"
        return jsonify({"image_url": image_url})
    else:
        return jsonify({"error": "Error generating image"}), 500

if __name__ == '__main__':
    app.run(debug=True)