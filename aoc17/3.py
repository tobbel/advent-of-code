'''                 31
17  16  15  14  13  30
18   5   4   3  12  29
19   6   1   2  11  28  53
20   7   8   9  10  27  52
21  22  23  24  25  26  51
44  45  46  47  48  49  50
75  76  77  78  79  80  81

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
from decimal import Decimal
input = 265149

# lower right is square(^2) of current row
# row length: 3-5-7-9-11...
# build up coordinate system
class Coordinate:
	value = 0
	x = 0
	y = 0
	def __str__(self):
		return 'Val: ' + str(self.value) + ', x: ' + str(self.x) + ', y: ' + str(self.y)

start = Coordinate()
start.value = 1
start.x = 0
start.y = 0

grid = []
grid.append(start)

coord = Coordinate()
coord.value = 2
coord.x = 1
coord.y = 0
grid.append(coord)

direction = 2
row_length = 3
column_length = 3
distance_traveled_along_row = 0
distance_traveled_along_column = 0
num_rows_traveled = 0
num_columns_traveled = 0
x = 1
y = -1
input = 25
for i in range(3, input):
	coordinate = Coordinate()
	coordinate.value = i
	coordinate.x = x
	coordinate.y = y
	
	# Move one step ahead along row or column
	if direction == 0:
		x += 1
		distance_traveled_along_row += 1
	elif direction == 1:
		y += 1
		distance_traveled_along_column += 1
	elif direction == 2:
		x -= 1
		distance_traveled_along_row += 1
	elif direction == 3:
		y -= 1
		distance_traveled_along_column += 1
	
	
	
	if distance_traveled_along_row == row_length:
		num_rows_traveled += 1
		direction = (direction + 1) % 4
		
		if num_rows_traveled >= row_length:
			num_rows_traveled = 0
			row_length += 2

	if distance_traveled_along_column == column_length:
		num_columns_traveled += 1
		direction = (direction + 1) % 4
		
		if num_columns_traveled >= column_length:
			num_columns_traveled = 0
			row_length += 2

	grid.append(coordinate)
	
# print solution
for coord in grid:
	print(str(coord))















