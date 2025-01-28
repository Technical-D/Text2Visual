# Text2Visual

Text2Visual is an AI-powered web application that allows users to generate stunning visuals from text prompts. Built using Flask for the backend and leveraging Hugging Face's Stable Diffusion model, this application transforms descriptive text into unique images. Whether you're a creator, designer, or enthusiast, Text2Visual helps bring your imagination to life!

![image](https://github.com/user-attachments/assets/cc2b55ca-71f0-484b-9979-c45c3ae9e844)

## Features

- **Text-to-Image Generation**: Enter a prompt and generate an image based on the description using Stable Diffusion.
- **Real-Time Image Display**: Instantly view the generated image after submitting the prompt.
- **Interactive Interface**: User-friendly frontend built with HTML, CSS, and JavaScript.
- **Loading Indicator**: A visual cue to show that the image is being generated.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (AJAX, jQuery)
- **AI Model**: Hugging Face's Stable Diffusion (via API)
- **Image Generation**: Stable Diffusion XL model

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.6 or higher
- An active Hugging Face account and an API key for accessing the Stable Diffusion model.
- A basic understanding of Flask for the backend and front-end technologies (HTML, CSS, JavaScript).

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Technical-D/Text2Visual.git
cd Text2Visual
```

### 2. Set Up Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Configure Your Hugging Face API Key
  - Obtain an API key from Hugging Face.
  - Create a .env file in the project directory and add your API key:
```bash
API_Key=
```
### 5. Run the Application

```bash
python app.py
```
The app should now be running at http://localhost:5000. Open it in your browser to start generating images from your text prompts!

## Usage
  - Enter a prompt in the input field (e.g., "A beautiful sunset over the ocean").
  - Click on "Generate" to send the prompt to the server.
  - View the generated image in the output container once the image is generated.
  - Wait for the loading indicator while the image is being created.

## API
The backend interacts with the Hugging Face API to generate images. Here’s the endpoint:

  - POST /generate_image:
    - Request body: { "prompt": "your text prompt here" }
    - Response: { "image_url": "url_of_generated_image" }

The image is generated using the Stable Diffusion XL model hosted by Hugging Face.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
