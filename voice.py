from gtts import gTTS
import tempfile

def speak(text):

    tts = gTTS(
        text=text,
        lang="bn"
    )

    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    tts.save(tmp.name)

    return tmp.name
