
'''
'''
import os 
import time

# Get problem: n.txt
dir_path = os.path.dirname(os.path.realpath(__file__))
problem_number = os.path.basename(__file__).split('.')[0][:2]
file_path = dir_path + '/input/' + problem_number + '-in.txt'
with open(file_path) as f:
  lines = f.read().splitlines()

#start = time.process_time()

class Point:
  def __init__(self, x, y, xv, yv):
    self.x = x
    self.y = y
    self.xv = xv
    self.yv = yv

points = []

def try_get_point(x, y):
  for p in points:
    if p.x == x and p.y == y:
      return '#'
  return '.'
  # #point = [p for p in points if p.x == x and p.y == y]
  # if len(point) > 0:
  #   return '#'
  # else:
  #   return '.'


def print_points():
  min_x = min(points, key = lambda p : p.x).x
  max_x = max(points, key = lambda p : p.x).x
  min_y = min(points, key = lambda p : p.y).y
  max_y = max(points, key = lambda p : p.y).y

  height = abs(min_y - max_y)
  if height < 11:
    for y in range(min_y, max_y + 1):
      for x in range(min_x, max_x + 1):
        print(try_get_point(x, y), end='')
      print('')
    return True
  return False


def accelerate():
  for p in points:
    p.x += p.xv
    p.y += p.yv

for line in lines:
  line = line.split('> velocity=<')
  pos = line[0][10:].split(',')
  vel = line[1][:-1].split(',')
  points.append(Point(int(pos[0]), int(pos[1]), int(vel[0]), int(vel[1])))

seconds = 0
while True:
  printed = print_points()
  if not printed:
    seconds += 1
  else:
    print('Took', seconds, 'seconds')
  accelerate()

# RIF7NRAN wrong
# RLEZNRAN - right?
#end = time.process_time()
#print(str(end-start))