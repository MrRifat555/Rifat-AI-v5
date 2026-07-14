from config import client

MODEL_NAME = "gemini-3.1-flash-lite"


def ask_ai(prompt):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
