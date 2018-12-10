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
#    self.is_infinite = False
#    self.area = []

def m_d(p, x, y):
  return abs(p.x - x) + abs(p.y - y)

# def find_closest_point(x, y):
#   closest_manhattan_distance = sys.maxsize
#   is_tied = False
#   closest_point = None
#   for p in points:
#     if p.is_infinite:
#       break
#     manhattan_distance = abs(p.x - x) + abs(p.y - y)
#     if manhattan_distance < closest_manhattan_distance:
#       closest_manhattan_distance = manhattan_distance
#       is_tied = False
#       closest_point = p
#     elif manhattan_distance == closest_manhattan_distance:
#       is_tied = True
#       closest_point = None

#   if closest_point is not None:
#     if abs(x) == 500 or abs(y) == 500:
#       closest_point.is_infinite = True
#     elif not is_tied:
#       closest_point.area.append((x, y))
#   #for p in points:

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
#  print('Initializing grid at', p.x, ',', p.y)
  grid[p.x][p.y] = p.name


def check_grid(p, x, y):
  try:
    grid_point = grid[x][y]
  except IndexError:
    return True
#    print('IndexError for point', p.name, 'at', x, ',', y)
#  print('Checking grid point (', str(x), ',', str(y),')', ' for point ', p.name,  '(', str(p.x), ',', str(p.y),')')
#  print('Point value:', str(grid_point))
  if grid_point > 0:
#    print('Found grid point:', str(grid_point))
    if points[grid_point] != p:
      # todo: save distance in point if slow
#      print('Position claimed by another point found')
      distance = m_d(p, x, y)
      other_distance = m_d(points[grid_point], x, y)
      if distance < other_distance:
        grid[x][y] = p.name
      elif distance == other_distance:
        grid[x][y] = -1
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
#    print('On layer', layer)
#    print('point is (', p.x, ',', p.y, ')')

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
      #print(str(col))
      #print(row)
      if col != -1:
        area_sizes[col - 1] += 1
    #grid_value = grid[row][col]
    #print(str(grid_value))
    #area_sizes[grid_value] += 1

print(area_sizes)

# Find infinite and ignore: those with numbers along edges
numbers_touching_edge = []
for i in range(0, side_length - 1):
  num = grid[0][i]
  if num not in numbers_touching_edge:
    numbers_touching_edge.append(num)

  num = grid[i][0]
  if num not in numbers_touching_edge:
    numbers_touching_edge.append(num)

  num = grid[side_length - 2][i]
  if num not in numbers_touching_edge:
    numbers_touching_edge.append(num)

  num = grid[i][side_length - 2]
  if num not in numbers_touching_edge:
    numbers_touching_edge.append(num)

print(numbers_touching_edge)
#for number in numbers_touching_edge:
#  del area_sizes[number]

touching_indices = [36, 28, 21, 25, 47, 37, 43, 46, 41, 48]
touching_indices.sort(reverse = True)
for i in touching_indices:
 del area_sizes[i]

max_number = 0
for area in area_sizes:
  if area > max_number:
    max_number = area
#7902???
print('max:', max_number)
print('test',end='')
print('hejjj')

#area_sizes.index(area_sizes)
#for row in grid:
 # if row.count(0) < 40:
    #print(row)

#[0, 0, 0, 0, 0, 0, 0, 0, 0, 1152, 0, 711, 0, 0, 0, 0, 0, 907, 0, 0, 5952, 0, 0, 0, 1952, 0, 0, 3762, 0, 0, 0, 0, 6, 0, 0, 14061, 3872, 862, 3489, 517, 6996, 2575, 2774, 6934, 0, 8932, 57188, 14889, 861024, 0]
#[36, 49, 28, 21, 25, -1, 47, 37, 43, 46, 41, 48]
#end = time.process_time()
#print(str(end-start))