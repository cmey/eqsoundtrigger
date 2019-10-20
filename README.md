# eqsoundtrigger

Trigger a sound when a text matches in Everquest.

## How to use

Example:
```
python main.py --char_name Novina --text "Ruen auctions"
```

```
usage: main.py [-h] [--text TEXT] [-i]
               (--char_name CHAR_NAME | --log_file LOG_FILE)

Trigger a sound when some text is matched in Everquest logs.

optional arguments:
  -h, --help            show this help message and exit
  --text TEXT           When this text appears in game, a sound is played.
  -i                    Text match is case insensitive (ignore capitalization
                        of words).
  --char_name CHAR_NAME
                        Name of your character.
  --log_file LOG_FILE   Path to log file, e.g.: ~/Library/Application
                        Support/EverQuest/PlayerLogseqlog_Novina_loginse.txt
```

## Installation

Set `Log=TRUE` in your installation's eqclient.ini (typically `~/Library/Application Support/EverQuest/eqclient.ini`).

Install required libraries in this project's environment:
```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
