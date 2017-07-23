#!/bin/bash
time=1
youtube-dl -o 'audio.%(ext)s' --extract-audio --audio-format wav $1
ffmpeg -i audio.wav -f segment -segment_time 30 -c copy audio-%03d.wav
rm audio.wav
for i in `ls -1 audio*.wav`
do
num=`echo $i | awk -F. '{print $1}'| tail -c 4`
num="$((10#$num * 1))"
time1=$((30*$num))
time2=$((30*($num + 1)))
echo `gdate -d "1970-01-01 00:00:00 UTC $time1 seconds" +"%M:%S"`-`gdate -d "1970-01-01 00:00:00 UTC $time2 seconds" +"%M:%S"`>>`date +%b-%d-%y`-RESULT.TXT
python transcribe.py $i >>`date +%b-%d-%y`-RESULT.TXT
done
