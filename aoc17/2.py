with open('c:\\dev\\avc17\\2.txt') as f:
	lines = f.read().splitlines()

sum = 0
for line in lines:
	values = list(map(int, line.split('	')))
	sum += int(max(values)) - int(min(values))
	#print('Max: ' + max(values) + ', Min: ' + min(values))
	print('Sum: ' + str(sum))

print('Part 1: ' + str(sum))
#21845

# Part 2
sum = 0
for line in lines:
	values = list(map(int, line.split('	')))
	
	for value in values:
		for compare_value in values:
			if value == compare_value:
				continue
			if value % compare_value == 0:
				# value is bigger
				sum += value / compare_value
print('Part 2: ' + str(sum))
#191