'''

--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). 
Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. 
Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. 
Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?
'''
import os 
import time

# Get problem: n.txt
dir_path = os.path.dirname(os.path.realpath(__file__))
problem_number = os.path.basename(__file__).split('.')[0][0]
file_path = dir_path + '/input/' + problem_number + '-in.txt'
with open(file_path) as f:
	lines = f.read().splitlines()

side_length = 1000
debug = False
if debug:
	lines = [
	'#1 @ 1,3: 4x4',
	'#2 @ 3,1: 4x4',
	'#3 @ 5,5: 2x2'
	]
	side_length = 10

#start = time.process_time()
fabric = []
for i in range(0, side_length - 1):
	fabric.append([0]*side_length)
	
for line in lines:
	line = line.split(' ')
	pos = line[2].split(',')
	x = int(pos[0])
	y = int(pos[1][:-1])
	size = line[3].split('x')
	width = int(size[0])
	height = int(size[1])
	
	print('Square ' + line[0] + ': (' + str(x) + ', ' + str(y) + '), size ' + str(width) + 'x' + str(height))
	
	for i in range(x, x + width):
		for j in range(y, y + height):
			val = fabric[i][j]
			val = val + 1
			fabric[i][j] = val
			#print('x:' + str(i) + ', y:' + str(j) + ' set to ' + str(val))
			
	#print()

count = 0
for i in range(0, side_length - 1):
	for j in range(0, side_length - 1):
		#print(str(fabric[i][j]))
		if fabric[i][j] > 1:
			count += 1
	#print()
print(str(count))

# find the one that does not overlap with anyone
# 3-2
for line in lines:
	alone = True
	line = line.split(' ')
	pos = line[2].split(',')
	x = int(pos[0])
	y = int(pos[1][:-1])
	size = line[3].split('x')
	width = int(size[0])
	height = int(size[1])
	
	for i in range(x, x + width):
		for j in range(y, y + height):
			val = fabric[i][j]
			if val > 1:
				alone = False
	if alone:
		print('Found alone line, id ' + line[0])
#38000: too low(high?)
#28223: too low
#32357: wrong
#32696: wrong
#105071: right - used pos[1][:1] instead of pos[1][:-1]
#end = time.process_time()
#print(str(end-start))