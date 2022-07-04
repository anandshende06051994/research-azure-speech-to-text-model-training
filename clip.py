from pydub import AudioSegment
import os

ff_name = 'output/Trans2.txt'
target_file_name = 'output/Trans.txt'

def convert_file_to_utf8():
    with open(ff_name, 'rb') as source_file:
        with open(target_file_name, 'w+b') as dest_file:
            contents = source_file.read()
            dest_file.write(contents.decode().encode('utf-8'))
    os.remove(ff_name)

def clip_by_ms(start_ms, stop_ms, id, input_path, user_name, msg):
    t1 = start_ms
    t2 = stop_ms
    if not os.path.isfile(input_path):
        return

    newAudio = AudioSegment.from_wav(input_path)
    newAudio = AudioSegment.silent(duration=1000) + newAudio[t1:t2] + AudioSegment.silent(duration=1000)
    newAudioFile = user_name + '_' + str(id) + '_' + str(t1) + '.wav'
    newAudio.export('output/'+newAudioFile, format="wav", bitrate="16000", parameters=["-ac", "1", "-ar", "16000"])

    f = open(ff_name, 'a+')

    string_to_write = newAudioFile + '\t' + msg + '\n'
    f.write(string_to_write)
    f.close()

