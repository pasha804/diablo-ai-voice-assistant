import os
from voice.listener import listen_for_command
from voice.responder import speak
from ai.brain import get_gpt_response
from tasks.actions import execute_action
from wake_word.detector import wait_for_wake_word

# Load OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-openai-api-key-here')

# Supported languages
SUPPORTED_LANGUAGES = ['en', 'ur']

# Main loop
if __name__ == "__main__":
    print("Diablo AI Assistant is running. Say 'Hey Diablo' or press the hotkey to activate.")
    while True:
        # Wait for wake word or hotkey
        wait_for_wake_word()
        speak("I'm listening.")
        # Listen for user command
        command, lang = listen_for_command(languages=SUPPORTED_LANGUAGES)
        if not command:
            speak("Sorry, I didn't catch that.")
            continue
        print(f"Heard: {command} (lang: {lang})")
        # Try to execute system action
        if execute_action(command, lang):
            continue
        # Otherwise, get smart response from GPT
        response = get_gpt_response(command, OPENAI_API_KEY, lang)
        speak(response, lang=lang)