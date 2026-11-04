import subprocess
import sys
import os

def launch_background():
    """
    Launch main.py as a background process (minimized window).
    """
    if sys.platform == 'win32':
        # Use 'start /min' to minimize window
        subprocess.Popen(['start', '/min', 'python', 'main.py'], shell=True)
    else:
        subprocess.Popen([sys.executable, 'main.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    launch_background()