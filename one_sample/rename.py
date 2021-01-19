"""
File: rename.py 
-------------------
This script was used to rename all of the ten second audio clips to
improve the feasibility of the labelling process. 
"""
import os
directory = 'audio_clips'

for file in os.listdir(directory):
	file_path = directory + '/' + file
	if os.path.exists(file_path):
		if os.path.isfile(file_path):
			str_name = file_path.replace('file', '')
			os.rename(file_path, str_name)