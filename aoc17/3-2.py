'''
36  35  34  33  32  31
17  16  15  14  13  30
18   5   4   3  12  29
19   6   1   2  11  28  53
20   7   8   9  10  27  52
21  22  23  24  25  26  51
44  45  46  47  48  49  50  83
75  76  77  78  79  80  81  82

1^2
	3^2: row 1 (3/2 rounded down)
		5^2: row 2 (5/2 rounded down)
			7^2: row 3 (7/2 rounded down)
				9
					11
						13
							15
								17
									19
										21
											23
												25
													27
														29
															31(961)
																33(1089)

the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?
'''


'''
Right: 2, 11, etc.
Down: 8, 23, etc.
Left: 6, 19, etc.
Up: 4, 15, etc.

Find corner
Find circle?
Count up, decide quadrant or circle

1. sqrt of pos, rounded down, is circle.
	sqrt(1024): 32
1024 is somewhere between circle 31 and 33.

Formula for right: 2, 11, 28, 53:
	an = 4 * n^2 - 3 * n + 1

Formula for down: 8, 23, 46, 77:
	an = 4 * n^2 + 3 * n + 1

Formula for left: 6, 19, 40, 69:
	an = 4 * n^2 + n + 1

Formula for up: 4, 15, 34, 61:
	an = 4 * n^2 - n + 1

'''
import math

input = 265149
#input = 1024
#input = 23
#input = 12
print('Input: ' + str(input))

# Get circle. Next odd squared.
sqrt = math.sqrt(input)
print('sqrt: ', sqrt)
sqrt_rounded_up = math.ceil(sqrt)
if sqrt_rounded_up % 2 == 0:
	sqrt_rounded_up += 1

side_length = sqrt_rounded_up
lap = math.floor(sqrt_rounded_up / 2)
print('Lap number: ', lap)
print('Lap length: ', side_length)

# Find up, down, left, right for lap number
right = 4 * pow(lap, 2) - 3 * lap + 1
down = 4 * pow(lap, 2) + 3 * lap + 1
left = 4 * pow(lap, 2) + lap + 1
up = 4 * pow(lap, 2) - lap + 1
print('Right: ', right, ', Down: ', down, ', Left: ', left, ', Up: ', up)

if abs(up - input) < abs(down - input):
	closest_vertical = up
else:
	closest_vertical = down
	
if abs(left - input) < abs(right - input):
	closest_horizontal = left
else:
	closest_horizontal = right


distance_to_horizontal = abs(closest_horizontal - input)
distance_to_vertical = abs(closest_vertical - input)


#distance = (abs(closest_horizontal - input)) + (abs(closest_vertical - input))
#distance -= (math.floor(side_length / 2) - 1)
print('Closest horizontal: ' + str(closest_horizontal))
print('Distance to closest horizontal: ', distance_to_horizontal)
print('Closest vertical: ' + str(closest_vertical))
print('Distance to closest vertical: ', distance_to_vertical)
#print('Distance : ' + str(distance))

if distance_to_horizontal < distance_to_vertical: #11 closer than 15
	# on a column
	#print('on column')
	# distance to horizontal is right
	horizontal_distance = distance_to_horizontal
	# distance to vertical must be calculated
	vertical_distance = lap
	
else:
	# on a row
	#print('on row')
	vertical_distance = distance_to_vertical
	horizontal_distance = lap

distance = horizontal_distance + vertical_distance
print('Distance: ', distance)


# found = False
# counter = 1
# while not found:
	# right = 4 * pow(counter, 2) - 3 * counter + 1
	# print('Right ' + str(counter) + ': ' + str(right))
	# counter += 1
	# if right > input:
		# right = 4 * pow((counter - 1), 2) - 3 * (counter - 1) + 1
		# found = True

# found = False
# counter = 1
# while not found:
	# down = 4 * pow(counter, 2) + 3 * counter + 1
	# print('Down ' + str(counter) + ': ' + str(down))
	# if down > input:
		# down = 4 * pow((counter - 1), 2) + 3 * (counter - 1) + 1
		# found = True
	# counter += 1

# found = False
# counter = 1
# while not found:
	# left = 4 * pow(counter, 2) + counter + 1
	# print('Left ' + str(counter) + ': ' + str(left))
	# counter += 1
	# if left > input:
		# left = 4 * pow((counter - 1), 2) + (counter - 1) + 1
		# found = True

# found = False
# counter = 1
# while not found:
	# up = 4 * pow(counter, 2) - counter + 1
	# print('Up ' + str(counter) + ': ' + str(up))
	# counter += 1
	# if up > input:
		# up = 4 * pow((counter - 1), 2) - (counter - 1) + 1
		# print('Final up: ', up)
		# found = True
		
# print('Up - input: ', up-input)
# print('Down: ', down)
# print('Down - input: ', down-input)
# if up - input < down - input:
	# closest_vertical = up
# else:
	# closest_vertical = down
	
# if left - input < right - input:
	# closest_horizontal = left
# else:
	# closest_horizontal = right

# distance = (closest_horizontal - input) + (closest_vertical - input)
# print('Closest horizontal: ' + str(closest_horizontal))
# print('Closest vertical: ' + str(closest_vertical))
# print('Distance : ' + str(distance))
