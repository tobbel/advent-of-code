import os 
import time
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + 'input/1-in.txt') as f:
	lines = f.read().splitlines()


current_frequency = 0
frequencies = set()
frequencies.add(current_frequency)
found = False
steps = 0
start = time.process_time()
while not found:
	for line in lines:
		steps += 1
		current_frequency += int(line)
		if current_frequency in frequencies:
			found = True
			break
		frequencies.add(current_frequency)
		
print(str(current_frequency))
print(str(steps), 'steps')
print(str(time.process_time() - start), 'seconds')
