import os 
import time
from string import ascii_lowercase
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/2-in.txt') as f:
	lines = f.read().splitlines()
	
# lines = [
# 'abcdef',
# 'bababc',
# 'abbcde',
# 'abcccd',
# 'aabcdd',
# 'abcdee',
# 'ababab'
# ]
	
num_two = 0
num_three = 0
#start = time.process_time()
for line in lines:
	print(line)
	found_two = False
	found_three = False
	for c in ascii_lowercase:
		num = line.count(c)
		if num == 3 and not found_three:
			num_three += 1
			found_three = True
			print(line + ' has an ' + c + ' that appears 3 times')
		elif num == 2 and not found_two:
			num_two += 1
			found_two = True
			print(line + ' has an ' + c + ' that appears 2 times')
	
print(str(num_two * num_three))
	#for i in range(0, len(line) - 2):
	#	letter = 