SimpleKeyLogger

A basic Python keylogger created for a cybersecurity course project.

⚠ Disclaimer

This project is for educational purposes only.
It should only be used in a controlled lab environment (e.g., your own virtual machine).
Do not use this program on any system without permission.

📌 Description

This project demonstrates:

Capturing keyboard input using the pynput library

Logging keystrokes to a file

Adding timestamps to each key press

Marking session start and end

Handling program termination with CTRL + C

The program creates a file named log.txt in the same directory and stores the logged keystrokes there.

⚙ Requirements

Python 3.x

pynput library

GUI environment (required on Linux)

🚀 Installation

Clone the repository:

git clone https://github.com/yourusername/SimpleKeyLogger.git
cd SimpleKeyLogger


(Recommended) Create a virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependency:

pip install pynput

▶ Run
python keylogger.py
Next the keys we type is stored in logs.txt

Press CTRL + C to stop logging.
