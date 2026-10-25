# ESA 1: CLI-Audiorecorder

Ein Python-Kommandozeilen-Tool zum Aufnehmen von MP3-Streams aus dem Internet.

## Voraussetzungen
- Python 3.13.2
- Benötigte Packages: `docopt` (installierbar via `pip install docopt`)

## Verwendung / Usage
Führe das Skript im Terminal aus und übergebe eine Stream-URL sowie optional Parameter:

```bash
python cli_audiorecorder.py <url> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]
