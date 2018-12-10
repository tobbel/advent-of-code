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
#    self.area = []

def m_d(p, x, y):
  return abs(p.x - x) + abs(p.y - y)

points = []
count = 0
for line in lines:
  line = line.split(', ')
  p = Point(int(line[0]), int(line[1]), count)
  points.append(p)
  count += 1

side_length = 1000
grid = []
for i in range(0, side_length - 1):
	grid.append([-1]*side_length)

# Initialize all points on grid
for p in points:
  grid[p.x][p.y] = p.name


def check_grid(p, x, y):
  try:
    grid_point = grid[x][y]
  except IndexError:
    return True
  if grid_point > 0:
    if points[grid_point] != p:
      distance = m_d(p, x, y)
      other_distance = m_d(points[grid_point], x, y)
      if distance < other_distance:
        grid[x][y] = p.name
      elif distance == other_distance:
        grid[x][y] = 99999
      return True
    else:
      return False
  else:
    grid[x][y] = p.name
    return False
  return False

# For all Points:
  # iterate around and "own" point on grid until finding another Point
  # for each point, if no one owns it, claim it.
  # if someone owns it, compare distances. Point with lowest manhattan distance owns it.
  # if tie, no one owns it.
  # to find infinite Points,........
for p in points:
  layer = 1
  other_found = False
  while not other_found:

    # right
    x = p.x + layer
    y = p.y
    other_found = check_grid(p, x, y) | other_found

    # down
    x = p.x
    y = p.y + layer
    other_found = check_grid(p, x, y) | other_found

    # left
    x = p.x - layer
    y = p.y
    other_found = check_grid(p, x, y) | other_found
    
    # up
    x = p.x
    y = p.y - layer
    other_found = check_grid(p, x, y) | other_found

    # up to upper-right corner
    for i in range(1, layer + 1):
      x = p.x + i
      y = p.y - layer
      other_found = check_grid(p, x, y) | other_found

    if layer > 1:
      # upper-right corner to down
      for i in range(layer - 1, 0, -1):
        x = p.x + layer
        y = p.y - i
        other_found = check_grid(p, x, y) | other_found

    # right to lower right corner
    for i in range(1, layer + 1):
      x = p.x + layer
      y = p.y + i
      other_found = check_grid(p, x, y) | other_found

    if layer > 1:
      # lower right corner to left
      for i in range(layer - 1, 0, -1):
        x = p.x + i
        y = p.y + layer
        other_found = check_grid(p, x, y) | other_found

    # bottom to lower left corner
    for i in range(1, layer + 1):
      x = p.x - i
      y = p.y + layer
      other_found = check_grid(p, x, y) | other_found
    
    if layer > 1:
      # lower left corner to left
      for i in range(layer - 1, 0, -1):
        x = p.x - layer
        y = p.y + i
        other_found = check_grid(p, x, y) | other_found
      
    # left to upper left corner
    for i in range(1, layer + 1):
      x = p.x - layer
      y = p.y - i
      other_found = check_grid(p, x, y) | other_found

    if layer > 1:
      # upper left corner to top
      for i in range(layer - 1, 0, -1):
        x = p.x - i
        y = p.y - layer
        other_found = check_grid(p, x, y) | other_found

    layer += 1

area_sizes = []
for i in range(0, len(lines)):
  area_sizes.append(0)
for row in grid:
  for col in row:
    if col != 0:
      if col != -1 and col != 99999:
        area_sizes[col - 1] += 1

print(area_sizes)

infinite_points = []
# For each point, check if any of its numbers neighbor -1. They are infinite
for p in points:
  for x in range(0, side_length - 2):
    if p.is_infinite:
      break
    for y in range(0, side_length - 2):
      # check if grid point is part of point
      grid_point = grid[x][y]
      if grid_point == p.name:
        # check all neigbors
        up = grid[x][y - 1]
        down = grid[x][y + 1]
        left = grid[x - 1][y]
        right = grid[x + 1][y]
        if up == -1 or down == -1 or left == -1 or right == -1:
          if p.name not in infinite_points:
            p.is_infinite = True
            infinite_points.append(p.name)
            if p.name != 10:
              print('Found infinite point:', p.name)
              break
            else:
              print('Point for 10:(', x, ',',y,')')
        #print('Found point for', p.name, ': (',x,',',y)
print(area_sizes)
print(infinite_points)

# 


#7902?