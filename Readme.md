# Console Keystroke Logger Simulation (Safe)

## Overview
This is a **safe, educational** keystroke logger simulation written in Python.  
It records keys typed **only inside the terminal** where it is running, making it suitable for learning and without creating actual malware.

---

## Disclaimer
This project is for **educational purposes only**.  
It **does not** capture system-wide keystrokes.  
Always obtain informed consent before logging any keystrokes, even in a controlled environment.

---

## Features
- Captures all keystrokes typed **in the current terminal session**.
- Writes captured keys to a timestamped `.txt` file.
- Works on Linux & macOS (requires a terminal environment).
- Minimal and easy to understand.

---

## Project Structure
```
.
├── Keylogger.py # Main script
└── README.md # Documentation
```

## Usage

### Install Python
Ensure Python 3 is installed:
```bash
python3 --version
```
### Run Keylogger.py:
```bash
python3 Keylogger.py
```
