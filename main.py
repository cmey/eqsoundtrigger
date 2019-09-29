import argparse
import os
from pathlib import Path
import time

from pydub import AudioSegment
from pydub.playback import play


SOUND_FILE = "zapsplat_emergency_alarm_siren_011_26617.mp3"
song = AudioSegment.from_mp3(SOUND_FILE)
LOG_PATH = Path("~/Library/Application Support/EverQuest/PlayerLogs/")

ap = argparse.ArgumentParser(description="Trigger a sound when some text is matched in Everquest logs.")
ap.add_argument("--text", type=str, default="rage", help="When this text appears in game, a sound is played.")
ap.add_argument("-i", action="store_true", help="Text match is case insensitive (ignore capitalization of words).")
group = ap.add_mutually_exclusive_group(required=True)
group.add_argument("--char_name", type=str, help="Name of your character.")
group.add_argument("--log_file", type=argparse.FileType('r'), help=f"Path to log file, e.g.: {LOG_PATH}eqlog_Novina_loginse.txt")
args = ap.parse_args()


def listen_loop(file, trigger_text, case_insensitive_enabled):
    # start listening from end of log file
    file.seek(0, os.SEEK_END)  # offset=0, whence="from the end"

    while True:
        line = file.readline()
        if line:
            if case_insensitive_enabled:
                trigger_text = trigger_text.lower()
                line = line.lower()

            if trigger_text in line:
                print("Match!: ", line)
                play(song)
        else:
            time.sleep(0.5)


listen_loop_args = dict(trigger_text=args.text, case_insensitive_enabled=args.i)
if args.log_file is None:
    log_file = os.path.expanduser(LOG_PATH / "eqlog_{}_loginse.txt".format(args.char_name))
    with open(log_file) as file:
        listen_loop(file=file, **listen_loop_args)
else:
    log_file = args.log_file
    listen_loop(file=log_file, **listen_loop_args)
