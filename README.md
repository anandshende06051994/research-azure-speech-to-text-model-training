# Convert MP4 to WAV
ffmpeg -i input.mp4 -ac 2 -ar 44100 -vn audio.wav





# Deployment on vcp-performance
Paste all MP4 recordings to audio_recordings
Paste all JSON transcriptions to transcript_json
sudo docker-compose down
sudo docker build -t audio-samples .
sudo docker-compose up -d
... wait for docker image to stop
Check count of file - 
    ls -l output | grep ^- | wc -l
    8859 on 4 July 2022
zip -r 4-July-2022.zip output
m365 spo file add --webUrl https://st21.sharepoint.com/sites/ST21PublicSpace --folder 'Shared Documents' --path 4-July-2022.zip

Manually download and upload files to Speech Studio