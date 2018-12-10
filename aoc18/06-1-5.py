'''

'''
import os 
import time
import sys

# Get problem: n.txt
dir_path = os.path.dirname(os.path.realpath(__file__))
problem_number = os.path.basename(__file__).split('.')[0][0]
file_path = dir_path + '/input/' + problem_number + '-in.txt'
with open(file_path) as f:
  lines = f.read().splitlines()

# Example input
# lines = [
# '1, 1',
# '1, 6',
# '8, 3',
# '3, 4',
# '5, 5',
# '8, 9'
# ]
#start = time.process_time()

class Point:
  def __init__(self, x, y, name):
    self.x = x
    self.y = y
    self.name = name
    self.is_infinite = False
    self.size = 0
#    self.area = []

# Helpers
def m_d(p, x, y):
  return abs(p.x - x) + abs(p.y - y)

def print_grid(grid):
  for row in grid:
    for col in row:
      out = ' '
      if col != -1:
        if col == 0:
          out = 'A'
        elif col == 1:
          out = 'B'
        elif col == 2:
          out = 'C'
        elif col == 3:
          out = 'D'
        elif col == 4:
          out = 'E'
        elif col == 5:
          out = 'F'
        out = col
      print('[' + str(out) + ']', end='')
    print('')

def print_grid_to_file(grid):
  f = open("out.txt", 'w')
  for row in grid:
    for col in row:
      out = ' '
      if col != -1:
        if col == 0:
          out = 'A'
        elif col == 1:
          out = 'B'
        elif col == 2:
          out = 'C'
        elif col == 3:
          out = 'D'
        elif col == 4:
          out = 'E'
        elif col == 5:
          out = 'F'
        out = col
      f.write('[' + str(out) + ']')
      #print('[' + str(out) + ']', end='')
    f.write('\n')
    #print('')

points = []
count = 0
for line in lines:
  line = line.split(', ')
  p = Point(int(line[0]), int(line[1]), count)
  points.append(p)
  count += 1

# grid does not need to be larger than extent of points at far ends - they are infinite anyway
leftmost_point = None
rightmost_point = None
highest_point = None
lowest_point = None
leftmost_x = 9999
rightmost_x = 0
highest_y = 9999
lowest_y = 0

for p in points:
  if p.x > rightmost_x:
    rightmost_point = p
    rightmost_x = p.x
  if p.x < leftmost_x:
    leftmost_point = p
    leftmost_x = p.x
  if p.y > lowest_y:
    lowest_point = p
    lowest_y = p.y
  if p.y < highest_y:
    highest_point = p
    highest_y = p.y

print(leftmost_point.x, leftmost_point.y)
print(rightmost_point.x, rightmost_point.y)
print(highest_point.x, highest_point.y)
print(lowest_point.x, lowest_point.y)

height = abs(highest_y - lowest_y)
width = abs(leftmost_x - rightmost_x)
grid = []
for i in range(0, lowest_y + 1):
  grid.append([-1] * (rightmost_x + 1))

# Initialize all points on grid
for p in points:
  grid[p.y][p.x] = p.name

# print_grid(grid)
print('')
# Voronoi for all relevant points on grid
for y in range(0, len(grid)):
  for x in range(0, len(grid[0])):
    closest_distance = 9999
    closest_point = None
    # find closest point
    for p in points:
      distance = m_d(p, x, y)
      if distance < closest_distance:
        closest_point = p
        closest_distance = distance
      elif distance == closest_distance:
        closest_point = None
      
    if closest_point == None:
      grid[y][x] = -2
    else:
      grid[y][x] = closest_point.name

# print_grid(grid)

infinite_points = []
# For each point, check if they have points to their left, right, above or below. Those with any missing are infinite
for p in points:
  is_infinite = False
  has_above = False
  has_below = False
  has_left = False
  has_right = False
  for neighbor in points:
    if neighbor == p:
      continue
    if neighbor.x < p.x:
      has_left = True
      is_infinite = True
    if neighbor.x > p.x:
      has_right = True
      is_infinite = True
    if neighbor.y < p.y:
      has_above = True
      is_infinite = True
    if neighbor.y > p.y:
      has_below = True
      is_infinite = True
  
  is_finite = (has_above and has_below and has_left and has_right)
  p.is_infinite = not is_finite
  #p.is_infinite = is_infinite

  if p.is_infinite:
    infinite_points.append(p)
    print('Found infinite point:', p.name)

found_infinite_points = [19, 6, 21, 36, 28, 25, 43, 41, 24, 48, 30, 31, 15, 14, 45, 0, 34, 4, 2, 8]
for p in points:
  if p.name in found_infinite_points and p not in infinite_points:
    infinite_points.append(p)
#print('Infinite points: ', str(infinite_points))
# 2832 too low
# duh 3401
for p in points:
  if p in infinite_points: continue
  size = 0
  for row in grid:
    for col in row:
      if col == p.name:
        size += 1
  p.size = size

for p in points:
  print(p.name,':',p.size)

print_grid_to_file(grid)

# def check_grid(p, x, y):
#   try:
#     grid_point = grid[x][y]
#   except IndexError:
#     return True
#   if grid_point > 0:
#     if points[grid_point] != p:
#       distance = m_d(p, x, y)
#       other_distance = m_d(points[grid_point], x, y)
#       if distance < other_distance:
#         grid[x][y] = p.name
#       elif distance == other_distance:
#         grid[x][y] = 99999
#       return True
#     else:
#       return False
#   else:
#     grid[x][y] = p.name
#     return False
#   return False

# # For all Points:
#   # iterate around and "own" point on grid until finding another Point
#   # for each point, if no one owns it, claim it.
#   # if someone owns it, compare distances. Point with lowest manhattan distance owns it.
#   # if tie, no one owns it.
#   # to find infinite Points,........
# for p in points:
#   layer = 1
#   other_found = False
#   while not other_found:

#     # right
#     x = p.x + layer
#     y = p.y
#     other_found = check_grid(p, x, y) | other_found

#     # down
#     x = p.x
#     y = p.y + layer
#     other_found = check_grid(p, x, y) | other_found

#     # left
#     x = p.x - layer
#     y = p.y
#     other_found = check_grid(p, x, y) | other_found
    
#     # up
#     x = p.x
#     y = p.y - layer
#     other_found = check_grid(p, x, y) | other_found

#     # up to upper-right corner
#     for i in range(1, layer + 1):
#       x = p.x + i
#       y = p.y - layer
#       other_found = check_grid(p, x, y) | other_found

#     if layer > 1:
#       # upper-right corner to down
#       for i in range(layer - 1, 0, -1):
#         x = p.x + layer
#         y = p.y - i
#         other_found = check_grid(p, x, y) | other_found

#     # right to lower right corner
#     for i in range(1, layer + 1):
#       x = p.x + layer
#       y = p.y + i
#       other_found = check_grid(p, x, y) | other_found

#     if layer > 1:
#       # lower right corner to left
#       for i in range(layer - 1, 0, -1):
#         x = p.x + i
#         y = p.y + layer
#         other_found = check_grid(p, x, y) | other_found

#     # bottom to lower left corner
#     for i in range(1, layer + 1):
#       x = p.x - i
#       y = p.y + layer
#       other_found = check_grid(p, x, y) | other_found
    
#     if layer > 1:
#       # lower left corner to left
#       for i in range(layer - 1, 0, -1):
#         x = p.x - layer
#         y = p.y + i
#         other_found = check_grid(p, x, y) | other_found
      
#     # left to upper left corner
#     for i in range(1, layer + 1):
#       x = p.x - layer
#       y = p.y - i
#       other_found = check_grid(p, x, y) | other_found

#     if layer > 1:
#       # upper left corner to top
#       for i in range(layer - 1, 0, -1):
#         x = p.x - i
#         y = p.y - layer
#         other_found = check_grid(p, x, y) | other_found

#     layer += 1

# area_sizes = []
# for i in range(0, len(lines)):
#   area_sizes.append(0)
# for row in grid:
#   for col in row:
#     if col != 0:
#       if col != -1 and col != 99999:
#         area_sizes[col - 1] += 1

# print(area_sizes)



# print(grid)
# print(area_sizes)
# print(infinite_points)
# for i in infinite_points:
#   area_sizes[i] = 0
# print(max(area_sizes))

# 42 on example - wrong (should be 17)


# 7902?
# 7902 again, point 23(zero-indexed)
# 7902 probably too high
# 14061 too high