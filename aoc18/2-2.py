import os 
import time
from string import ascii_lowercase
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/2-in.txt') as f:
	lines = f.read().splitlines()
	
num_two = 0
num_three = 0

for i in range(0, len(lines)):
	line = lines[i]
	for j in range(0, len(lines)):
		if i == j:
			continue
		
		line2 = lines[j]
		
		diff_count = 0
		for c in range(0, len(line)):
			if line[c] != line2[c]:
				diff_count += 1
		
		if diff_count == 1:
			print(line + ' ' + line2)
