!/bin/bash
if [ "$(which python3)" = ""] && [ "$(which python)" = ""]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi
osascript -e 'tell application "System events" to keystroke "f" using {command down, control down}'
pip install -r requirements.txt
python3 main.py
