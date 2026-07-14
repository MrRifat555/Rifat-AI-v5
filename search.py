from config import client
from google.genai import types

MODEL_NAME = "gemini-2.5-flash-lite"

def search_ai(prompt):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )
    )

    return response.text
