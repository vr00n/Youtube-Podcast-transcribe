#!/bin/bash
time=1
if [[ $1 == 'file' ]]
then
wget $2
echo "Converting file to audio.wav"
ffmpeg -i $2 -ac 2 -f wav audio.wav
elif [[ $1 == 'youtube' ]]
then
youtube-dl -o 'audio.%(ext)s' --extract-audio --audio-format wav $2
else
echo "use either file or youtube as arguments"
fi
ffmpeg -i audio.wav -f segment -segment_time 30 -c copy audio-%03d.wav
# if you want to remove the converted wav file
#rm audio.wav
for i in `ls -1 audio-*.wav`
do
num=`echo $i | awk -F. '{print $1}'| tail -c 4`
num="$((10#$num * 1))"
time1=$((30*$num))
time2=$((30*($num + 1)))
echo `gdate -d "1970-01-01 00:00:00 UTC $time1 seconds" +"%M:%S"`-`gdate -d "1970-01-01 00:00:00 UTC $time2 seconds" +"%M:%S"`>>`date +%s`-RESULT.TXT
python transcribe.py $i >>`date +%s`-RESULT.TXT
done
# if you want to remove all the wav chunks
rm audio-*.wav
