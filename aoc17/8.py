'''
Instructions, several parts:
1. the register to modify
2. to increase or decrease values
3. a condition
If condition fails, skip the instruction.
Registers all start at 0.
'''



with open('c:\\dev\\avc17\\8-in.txt') as f:
	lines = f.read().splitlines()

# lines = [
# 'b inc 5 if a > 1',
# 'a inc 1 if b < 5',
# 'c dec -10 if a >= 1',
# 'c inc -20 if c == 10'
# ]

registers = {}
for line in lines:
	register = line.split(' ')[0]
	if register not in registers:
		registers[register] = 0

largest_value = 0
for line in lines:
	largest_value = max(largest_value, registers[max(registers, key=registers.get)])
	command, condition = line.split(' if ')
	#print(command)
	# get values
	#print(condition)
	# evaluate condition
	condition = condition.split(' ')
	a = int(registers[condition[0]])
	b = int(condition[2])
	condition_true = False
	
	if condition[1] == '==':
		condition_true = a == b
	elif condition[1] == '<':
		condition_true = a < b
	elif condition[1] == '>':
		condition_true = a > b
	elif condition[1] == '<=':
		condition_true = a <= b
	elif condition[1] == '>=':
		condition_true = a >= b
	elif condition[1] == '!=':
		condition_true = a != b
	
	if condition_true:
		#print('Command executed ', command)
		command = command.split(' ')
		if command[1] == 'inc':
			registers[command[0]] += int(command[2])
		elif command[1] == 'dec':
			registers[command[0]] -= int(command[2])
	else:
		continue
		
print(registers)
print(registers[max(registers, key=registers.get)])
print(largest_value)