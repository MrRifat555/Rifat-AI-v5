from PIL import Image
from config import client

MODEL_NAME = "gemini-2.5-flash"

def analyze_image(uploaded_file, prompt):

    image = Image.open(uploaded_file)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[
            prompt,
            image
        ]
    )

    return response.text
