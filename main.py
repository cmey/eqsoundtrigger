import argparse
import os
from pathlib import Path
import time

from pydub import AudioSegment
from pydub.playback import play


SOUND_FILE = "zapsplat_emergency_alarm_siren_011_26617.mp3"
LOG_PATH = Path("~/Library/Application Support/EverQuest/PlayerLogs/")


ap = argparse.ArgumentParser(description="Trigger a sound when some text is matched in Everquest logs.")
ap.add_argument("--char_name", type=str, default="Novina", help="Name of your character.")
ap.add_argument("--text", type=str, default="rage", help="When this text appears in game, a sound is played.")
ap.add_argument("-i", action="store_true", help="Text match is case insensitive (ignore capitalization of words).")
args = ap.parse_args()

song = AudioSegment.from_mp3(SOUND_FILE)
log_file = os.path.expanduser(LOG_PATH / "eqlog_{}_loginse.txt".format(args.char_name))
trigger_text = args.text

with open(log_file) as file:
    # start listening from end of log file
    file.seek(0, os.SEEK_END)  # offset=0, whence="from the end"

    while True:
        line = file.readline()
        if line:
            if args.i is True:
                trigger_text = trigger_text.lower()
                line = line.lower()

            if trigger_text in line:
                print("Match!: ", line)
                play(song)
        else:
            time.sleep(0.5)
