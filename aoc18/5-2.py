'''

'''
import os 
import time
from string import ascii_lowercase

# Get problem: n.txt
dir_path = os.path.dirname(os.path.realpath(__file__))
problem_number = os.path.basename(__file__).split('.')[0][0]
file_path = dir_path + '/input/' + problem_number + '-in.txt'
with open(file_path) as f:
	line_in = f.read()

# Example input
#line = ''
#start = time.process_time()
def remove_at(i, s, len):
    return s[:i] + s[i+len:]

def fully_replace(line):
  start_len = len(line)
  stop_len = 0
  while start_len != stop_len:
    i = 0
    start_len = len(line)
    while i < len(line) - 1:
      a = line[i]
      b = line[i + 1]
      if a.isupper() and not b.isupper():
        if a == b.upper():
          line = remove_at(i, line, 2)
          #print('Removing pair ', a + b)
        else: i += 1
      elif b.isupper() and not a.isupper():
        if b == a.upper():
          line = remove_at(i, line, 2)
          #print('Removing pair', a + b)
        else: i += 1
      else:
        i += 1
    stop_len = len(line)
    #print('Start len', start_len, ' stop len', stop_len)
  return line

smallest_line_len = len(line_in)
smallest_line_letter = ''
for letter in ascii_lowercase:
  small = letter
  big = letter.upper()
  line = line_in.replace(small, '')
  line = line.replace(big, '')
  line = fully_replace(line)
  length = len(line)
  print('Done with ', small)
  if length < smallest_line_len:
    smallest_line_len = length
    smallest_line_letter = small

print('Len:', str(smallest_line_len))
print('Letter:', smallest_line_letter)

# 35286: wrong
# 33670: wrong
# 10384: right! didn't consider aA and Aa, just Aa
#end = time.process_time()
#print(str(end-start))