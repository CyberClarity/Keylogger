import sys
import tty
import termios
from datetime import datetime

log_file = f"keystrokes.txt"

print("Keystroke logger simulation running.")
print("Type something (Ctrl+C to exit). Keys typed here will be logged.")

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    tty.setraw(sys.stdin.fileno())
    with open(log_file, "a", encoding="utf-8") as f:
        while True:
            ch = sys.stdin.read(1)
            if ch == "\x03":  # Ctrl+C
                break
            f.write(ch)
            f.flush()
finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

print(f"\nLogged to {log_file}")
