# Transcribing-youtube-videos

1. CONVERT `youtube-url` into WAV using `www.onlinevideoconverter.com`. 
   * Download the WAV file.
2. SPLIT the WAV file into 30 second chunks using `ffmpeg`
   * `ffmpeg -i file.wav -f segment -segment_time 30 -c copy file%03d.wav`
3. Git clone `https://github.com/Uberi/speech_recognition`.
4. Use uberi's `speech.py` (enable the Google function only).
5. Iterate on each 30 second chunk to generate text.


-- 
* Tested on https://www.youtube.com/watch?v=OYJ89vE-QfQ - check RESULT.TXT for results
* Visualized the transcript here: https://voyant-tools.org/?corpus=2de4ddec8fe29d707afc40ece4f45d7b
