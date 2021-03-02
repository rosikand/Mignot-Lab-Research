"""
File: one_second_split.py 
-------------------
This script is used to split the complete audio file
into one second clips. 
"""

from pydub import AudioSegment
audio_file = AudioSegment.from_wav('sleep.wav') # complete audio file

# starting values
x = 0
y = 1 * 1000 # pydub works in milliseconds 

#incrementer
incrementer = 1 * 1000 

master_list = [] # to store all of the audio clips

# segment
for i in range(int(len(audio_file)/incrementer)): 
    segment = audio_file[x:y]
    master_list.append(segment)
    x += incrementer
    y += incrementer

# print(len(master_list))
# print(audio_file.duration_seconds)
# print(type(audio_file.duration_seconds))
# print(len(audio_file))


# export into .wav files
start = 0 # for naming purposes
stop = 1 # for naming purposes
incrementer = 1 # for naming purposes
for elem in master_list:
	exported_file_name = 'audio-clips/' + str(start) + '-' + str(stop) + '.wav'
	elem.export(exported_file_name, format='wav')
	start += incrementer
	stop += incrementer