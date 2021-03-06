import json
import os

from clip import clip_by_ms,convert_file_to_utf8
from time_conv import convert_time_to_ms

path = os.getcwd()
audiop = path + "/audio_recordings_wav/"
jsonp = path + "/transcript_json/"

file_names = []

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".json")):
            file_names.append(file[0:-5])

for file in file_names:
    f = open(jsonp + file + '.json')
    data = json.load(f)
    print('loaded ' + jsonp + file + '.json');
    for i in data:
        start_time_ms = convert_time_to_ms(i["Start_time"])
        end_time_ms = convert_time_to_ms(i["End_time"])
        name = i["Speaker_name"]
        msg = i["msg"]
        clip_by_ms(start_time_ms, end_time_ms, file, audiop + file + '.wav', name.replace(' ', '_'), msg)


convert_file_to_utf8()