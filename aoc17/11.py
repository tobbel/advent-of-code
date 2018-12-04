'''
--- Day 11: Hex Ed ---
Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).
'''
from collections import deque

with open('c:\\dev\\avc17\\11-in.txt') as f:
	input = f.read()

steps = input.split(',')
#print(steps)

x = 0
y = 0

for step in steps:
	if step == 'n':
		y -= 1
	elif step == 'ne':
		y -= 1
		x += 1
	elif step == 'se':
		y += 1
		x += 1
	elif step == 's':
		y += 1
	elif step == 'sw':
		y += 1
		x -= 1
	elif step == 'nw':
		y -= 1
		x -= 1
print(x, y)
start = [0, 0]
end = (x, y)
visited = []
open_set = deque([])
open_set.append(start)
# todo: meta state
found = False

def is_in_visited(node_in):
	global visited
	for node in open_set:
		if node[0] == node_in[0] and node[1] == node_in[1]:
			return True

	return False

while not found:
	# start att top of stack
	node = open_set.popleft()
	if node in visited:
		continue
	visited.append(node)
	#print('Visited ', node)
	# check for end
	if node == end:
		found = True
		break
	# get neighbors
	#n = [node[0], node[1] - 1]
	#if n not in visited:
	#if not is_in_visited(n):
	#	open_set.append(n)
	#ne = [node[0] + 1, node[1] - 1]
	#if ne not in visited:
	#if not is_in_visited(ne):
	#	open_set.append(ne)
	#se = [node[0] + 1, node[1] + 1]
	#if se not in visited:
	#if not is_in_visited(se):
	#	open_set.append(se)
	s = [node[0], node[1] + 1]
	if s not in visited:
	#if not is_in_visited(s):
		open_set.append(s)
	sw = [node[0] - 1, node[1] + 1]
	if sw not in visited:
	#if not is_in_visited(sw):
		open_set.append(sw)
	nw = [node[0] - 1, node[1] - 1]
	if nw not in visited:
	#if not is_in_visited(nw):
		open_set.append(nw)
	#print(visited)
	#print(len(open_set))
	#print(max(open_set))
	#print(open_set[0])
	
print(open_set)