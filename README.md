# Transcribing Youtube videos

1. CONVERT `youtube-url` into a WAV file using `www.onlinevideoconverter.com`. 
   * Download the WAV file. ( 1 hour video becomes a 600-700mb wav file )
2. SPLIT the WAV file into 30 second chunks using `ffmpeg`
   * `ffmpeg -i file.wav -f segment -segment_time 30 -c copy file%03d.wav
4. Use `transcribe.sh` in the same folder as the wav chunks
6. `Mon-DD-YYYY-RESULTS.txt` is your result file


-- 
* Tested on https://www.youtube.com/watch?v=OYJ89vE-QfQ - see Jul-22-17-RESULT
* Visualized the transcript here: https://voyant-tools.org/?corpus=2de4ddec8fe29d707afc40ece4f45d7b
