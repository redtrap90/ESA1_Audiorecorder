"""
Titel: ESA 1 Audiorecorder
Beschreibung: MP3- Aufnahme eines Internetstreams
Python-Version: 3.13.2
Author: Redtrap90
"""
import urllib.request
import datetime
from docopt import docopt

__doc__ = """
Usage:
  cli_audiorecorder.py <url> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]
  cli_audiorecorder.py -h | --help

Options:
  -h --help             Show this screen.
  --filename=<name>     Name of recording [default: myRadio].
  --duration=<time>     Duration of recording in seconds [default: 30].
  --blocksize=<size>    Block size for read/write in bytes [default: 64].
"""

if __name__ == "__main__":
    # Argumente via docopt einlesen
    arguments = docopt(__doc__)

    # Zuweisung der Variablen + in passenden Datentypen umwandeln
    url = arguments["<url>"]
    filename = arguments["--filename"] + ".mp3"  # Hängt automatisch .mp3 an den Dateinamen an
    duration = int(arguments["--duration"])  # Text zu Zahl (Int)
    blocksize = int(arguments["--blocksize"])  # Text zu Zahl (Int)

    print(
        f"Starte Aufnahme von {url} für {duration} Sekunden (Blockgröße:{blocksize} Bytes)"
    )  # Feedback, dass die Aufnahme startet
# Audiorekorder Script
start_zeit = datetime.datetime.now()

with urllib.request.urlopen(url) as stream:
    with open(filename, 'wb') as file:
        # Schleife läuft so lange Start+Dauer < aktuelle Zeit
        while (datetime.datetime.now() < start_zeit + datetime.timedelta(seconds=duration)):
            file.write(stream.read(blocksize))

    print("Aufnahme erfolgreich beendet!")  # Feedback, dass die Aufnahme erfolgte
