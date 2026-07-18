from config import client, MODEL_NAME

def ask_ai(prompt):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
