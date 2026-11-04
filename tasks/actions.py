import os
import subprocess
import webbrowser
import datetime
import platform

def execute_action(command, lang='en'):
    """
    Try to match and execute a system action based on the command.
    Returns True if action was executed, else False.
    """
    cmd = command.lower()
    # Open applications
    if 'open' in cmd and 'chrome' in cmd:
        subprocess.Popen('start chrome', shell=True)
        return True
    if 'open' in cmd and 'notepad' in cmd:
        subprocess.Popen('notepad', shell=True)
        return True
    if 'open' in cmd and ('vs code' in cmd or 'visual studio code' in cmd):
        subprocess.Popen('code', shell=True)
        return True
    # Web search
    if 'search' in cmd:
        query = cmd.split('search',1)[-1].strip()
        if query:
            webbrowser.open(f'https://www.google.com/search?q={query}')
            return True
    if 'youtube' in cmd:
        webbrowser.open('https://www.youtube.com')
        return True
    # Play/Pause music (basic, extend as needed)
    if 'play music' in cmd:
        webbrowser.open('https://music.youtube.com')
        return True
    # Time & Date
    if 'time' in cmd:
        now = datetime.datetime.now().strftime('%H:%M')
        speak(f"The time is {now}", lang)
        return True
    if 'date' in cmd:
        today = datetime.datetime.now().strftime('%A, %d %B %Y')
        speak(f"Today is {today}", lang)
        return True
    # Shutdown/Restart
    if 'shutdown' in cmd:
        if platform.system() == 'Windows':
            os.system('shutdown /s /t 1')
        return True
    if 'restart' in cmd:
        if platform.system() == 'Windows':
            os.system('shutdown /r /t 1')
        return True
    # Tell joke
    if 'joke' in cmd:
        speak("Why did the computer show up at work late? It had a hard drive!", lang)
        return True
    # Translate (simple, extend with API for production)
    if 'translate' in cmd:
        if 'into urdu' in cmd:
            text = cmd.split('translate',1)[-1].split('into urdu')[0].strip(' "')
            # Dummy translation for demo
            speak(f"'{text}' in Urdu is 'آپ کیسے ہیں'", 'ur')
            return True
    return False

# Import speak from responder for feedback
def speak(text, lang='en'):
    try:
        from voice.responder import speak as tts_speak
        tts_speak(text, lang)
    except Exception:
        print(text)