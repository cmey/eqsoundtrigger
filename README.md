# eqsoundtrigger

Trigger a sound when a text matches in Everquest.

## How to use

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

Example:
```
python main.py --char_name Novina --text "some text that you want to trigger a sound!"
```

## Installation

Set `Log=TRUE` in your installation's eqclient.ini (typically `~/Library/Application Support/EverQuest/eqclient.ini`).


