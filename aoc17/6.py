input = '5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6'
#input = '0	2	7	0'
banks = list(map(int, input.split('	')))
#print(banks)

earlier_state_found = False
state_found_count = 0
states = []
states.append(banks.copy())
cycles = 0
#print(states)
while state_found_count < 2:
	largest = max(banks)
	largest_index = banks.index(largest)
	banks[largest_index] = 0
	index = largest_index
	while largest > 0:
		index = (index + 1) % len(banks)
		banks[index] += 1
		largest -= 1
#	print(banks)
	if banks in states and not earlier_state_found:
		earlier_state_found = True
		if state_found_count == 0:
			cycles = 0
#			print('reset cycles')
		state_found_count = 1
	elif states.count(banks) == 2:
		state_found_count = 2
	else:
		states.append(banks.copy())
		cycles += 1
	
print(cycles)