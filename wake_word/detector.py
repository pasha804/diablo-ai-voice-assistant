import keyboard
import time
# For Porcupine/Snowboy, import and implement as needed

def wait_for_wake_word():
    """
    Wait for the wake word ('Hey Diablo') or hotkey (Ctrl+Shift+D) to activate assistant.
    """
    print("Waiting for wake word or hotkey (Ctrl+Shift+D)...")
    while True:
        # Hotkey activation
        if keyboard.is_pressed('ctrl+shift+d'):
            print("Hotkey detected.")
            time.sleep(0.5)
            return
        # Wake word detection placeholder (implement Porcupine/Snowboy here)
        # For now, press Enter to simulate
        if keyboard.is_pressed('enter'):
            print("Wake word simulated (Enter pressed).")
            time.sleep(0.5)
            return
        time.sleep(0.1)