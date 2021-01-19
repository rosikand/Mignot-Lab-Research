"""
File: label.py 
-------------------
This script is used to label which of the ten second clips are 
speech based on the annotations text file. 
"""

import os

# read file with the annotations
file = open('annotations.txt')

# get all of the ranges with speech (as ints)
all_ranges = []
for line in file:
	line = line.strip()
	range_list = line.split()
	temp = []
	for elem in range_list:
		elem = float(elem)
		elem = int(elem)
		temp.append(elem)
	all_ranges.append(temp)


# get all of the ints within the ranges (inclusive),
# and store them in a master_list. 
master_list = []
for i in range(len(all_ranges)):
	current_range = all_ranges[i]
	start = current_range[0]
	end = current_range[1] + 1
	temp_list = range(start, end)
	# if len(temp_list) > 1: # alternatively, use this line to ensure that onyl parts greater than one second are included
	for elem in temp_list:
		master_list.append(elem)


# do the labelling 
directory = 'audio_clips'
for file in os.listdir(directory):
	file_path = directory + '/' + file
	if os.path.exists(file_path):
		if os.path.isfile(file_path):
			file_trimmed_name = file[:-4]
			str_list = file_trimmed_name.split('-')
			str_list[0] = int(str_list[0]) # convert to int
			str_list[1] = int(str_list[1]) # conert to int
			start_val = str_list[0]
			end_val = str_list[1] + 1
			curr_range_values = range(start_val, end_val)
			c = 0
			for elem in curr_range_values:
				if elem in master_list:
					c += 1
					pos_path = 'speech/' + file
					break
			if c >= 1: # alternatively, use two here to label clips with more than two seconds of speech as speech
				#pos_path = 'speech/' + file
				os.rename(file_path, pos_path)
			else:
				neg_path = 'no_speech/' + file
				os.rename(file_path, neg_path)
