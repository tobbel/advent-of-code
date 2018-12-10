'''

'''
import os 
import time

# Get problem: n.txt
dir_path = os.path.dirname(os.path.realpath(__file__))
problem_number = os.path.basename(__file__).split('.')[0][:2]
file_path = dir_path + '/input/' + problem_number + '-in.txt'
with open(file_path) as f:
	lines = f.read().splitlines()

# Example input
lines = [

]
#start = time.process_time()

for line in lines:
	print(line)
	
#end = time.process_time()
#print(str(end-start))