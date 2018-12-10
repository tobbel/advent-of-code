'''

'''
import os 
import time

# Get problem: n.txt
dir_path = os.path.dirname(os.path.realpath(__file__))
problem_number = os.path.basename(__file__).split('.')[0][0]
file_path = dir_path + '/input/' + problem_number + '-in.txt'
with open(file_path) as f:
	line = f.read()

# Example input
#line = ''
#start = time.process_time()
def remove_at(i, s, len):
    return s[:i] + s[i+len:]

# def exists_pair(s):
# 	for i in range(0, len(s) - 1):
# 		a = s[i]
# 		b = s[i + 1]


#print(line)
start_len = len(line)
stop_len = 0
while start_len != stop_len:
	i = 0
	start_len = len(line)
	while i < len(line) - 1:
		a = line[i]
		b = line[i + 1]
		if a.isupper() and not b.isupper():
			if a == b.upper():
				line = remove_at(i, line, 2)
				print('Removing pair ', a + b)
			else: i += 1
		elif b.isupper() and not a.isupper():
			if b == a.upper():
				line = remove_at(i, line, 2)
				print('Removing pair', a + b)
			else: i += 1
		else:
			i += 1
	stop_len = len(line)
	print('Start len', start_len, ' stop len', stop_len)


# 35286: wrong
# 33670: wrong
# 10384: right!

#end = time.process_time()
#print(str(end-start))