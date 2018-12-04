'''
	CPU is trapped in a maze of jump instructions, needs help to get out.
	List of offsets for each jump
	-1 moves to the previous instruction, 2, skips the next one. 1 jumps to next.
	Follow the jumps until one leads outside the list.
	
	After each jump, the offset of that instruction increases by 1.
'''


with open('c:\\dev\\avc17\\5-in.txt') as f:
	lines =  list(map(int, f.read().splitlines()))
	#lines = [0, 3, 0, 1, -3]
	step = 0
	index = 0
	#print('Start: ', lines)
	while index > -1 and index < len(lines):
		jump = lines[index]
		
		lines[index] += 1
		index += jump
		
		
		step += 1
		#print(lines)
print('Steps: ', step)