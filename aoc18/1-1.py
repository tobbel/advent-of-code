import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/input/1-in.txt') as f:
	lines = f.read().splitlines()

count = 0

for line in lines:
	count += int(line)
	
print(str(count))