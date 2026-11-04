import queue
import sounddevice as sd
import vosk
import json
from langdetect import detect

# For Whisper support, import and implement as needed
# import whisper

MODEL_PATH = "models/vosk-model-small-en-us-0.15"  # Change to your model path

q = queue.Queue()

# Callback for audio input
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen_for_command(languages=['en', 'ur']):
    """
    Listen for a voice command and return recognized text and detected language.
    """
    try:
        model = vosk.Model(MODEL_PATH)
    except Exception as e:
        print(f"Vosk model not found: {e}")
        return None, None
    recognizer = vosk.KaldiRecognizer(model, 16000)
    with sd.RawInputStream(samplerate=16000, blocksize = 8000, dtype='int16', channels=1, callback=callback):
        print("Listening...")
        result = ""
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                res = json.loads(recognizer.Result())
                result = res.get('text', '')
                break
        if result:
            try:
                lang = detect(result)
            except:
                lang = 'en'
            return result, lang
        return None, None