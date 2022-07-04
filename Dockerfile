FROM python:3.10.5-buster

WORKDIR /src

RUN apt-get update && apt-get install ffmpeg -y

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
#CMD ffmpeg -i audio_recordings/*.mp4 -ac 2 -ar 44100 -vn audio_recordings_wav
RUN cd audio_recordings && for i in *.mp4; do ffmpeg -i "$i" "../audio_recordings_wav/${i%.*}.wav"; done

CMD [ "python", "app.py"]
