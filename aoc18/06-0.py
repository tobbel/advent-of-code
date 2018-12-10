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

# ]
#start = time.process_time()

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.is_infinite = False
    self.area = []

def find_closest_point(x, y):
  closest_manhattan_distance = sys.maxsize
  is_tied = False
  closest_point = None
  for p in points:
    if p.is_infinite:
      break
    manhattan_distance = abs(p.x - x) + abs(p.y - y)
    if manhattan_distance < closest_manhattan_distance:
      closest_manhattan_distance = manhattan_distance
      is_tied = False
      closest_point = p
    elif manhattan_distance == closest_manhattan_distance:
      is_tied = True
      closest_point = None

  if closest_point is not None:
    if abs(x) == 500 or abs(y) == 500:
      closest_point.is_infinite = True
    elif not is_tied:
      closest_point.area.append((x, y))
  #for p in points:


max_x = 0
max_y = 0
points = []
for line in lines:
  line = line.split(', ')
  p = Point(int(line[0]), int(line[1]))
  if p.x > max_x:
    max_x = p.x

  if p.y > max_y:
    max_y = p.y
  points.append(p)

print('Max x:', max_x)
print('Max y:', max_y)

for x in range (-500, 500):
  print(str(x))
  for y in range(-500, 500):
    find_closest_point(x, y)

max_area_size = 0
for p in points:
  if not p.is_infinite:
    if len(p.area) > max_area_size:
      max_area_size = len(p.area)

print('max area:', str(max_area_size))
#end = time.process_time()
#print(str(end-start))