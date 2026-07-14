from config import client

MODEL_NAME = "gemini-2.5-flash-lite"


def ask_ai(prompt):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
