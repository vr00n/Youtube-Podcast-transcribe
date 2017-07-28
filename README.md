# Transcribing Youtube videos

HT to https://github.com/Uberi/speech_recognition

## Requirements
1. Install `youtube-dl` from here: https://github.com/rg3/youtube-dl/
   * FYI - a 1 hour video converts into a 600-700mb wav file
2. Create a Google API Service Account from https://cloud.google.com/docs/authentication/getting-started#creating_the_service_account
   * Enter the JSON key into `transcribe.py` where indicated.
   
## Usage

3.  Execute `./transcribe.sh file http link to file `
3b. Execute `./transcribe youtube YOUTUBE-URL`
4. `TimeStamp-RESULTS.txt` is your result file.


Tests

* Elon Musk with Governors - https://www.youtube.com/watch?v=OYJ89vE-QfQ - see `Jul-22-17-RESULT.TXT`
   * Visualized the transcript here: https://voyant-tools.org/?corpus=2de4ddec8fe29d707afc40ece4f45d7b

* Bezos + Mossberg at Code '17 - https://www.youtube.com/watch?v=VAM6b0UkEYw - see `BEZOS-CODE-17.TXT`
