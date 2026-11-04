import pyttsx3
# import edge_tts  # Uncomment for Edge TTS support

def speak(text, lang='en'):
    """
    Speak the given text using TTS engine. Defaults to pyttsx3 for local fast output.
    """
    engine = pyttsx3.init()
    # Set language/voice if needed
    voices = engine.getProperty('voices')
    if lang == 'ur':
        # Attempt to select Urdu voice if available
        for v in voices:
            if 'urdu' in v.name.lower():
                engine.setProperty('voice', v.id)
                break
    else:
        engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()