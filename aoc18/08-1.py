'''

'''
import os 
import time

# Get problem: n.txt
dir_path = os.path.dirname(os.path.realpath(__file__))
problem_number = os.path.basename(__file__).split('.')[0][0]
file_path = dir_path + '/input/' + problem_number + '-in.txt'
with open(file_path) as f:
  lines = f.read().split(' ')

# Example input
#lines = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')
#start = time.process_time()

class Node:
  def __init__(self, name, child_count, metadata_count):
    self.children = []
    self.child_count = int(child_count)
    self.metadata = []
    self.metadata_count = int(metadata_count)
    self.name = name
#    print('Creating node', name, 'with', self.child_count, 'children')
  
  def get_metadata_sum(self):
    total_metadata = sum([int(i) for i in self.metadata])
    for c in self.children:
      total_metadata += c.get_metadata_sum()
    return total_metadata

# def add_child_nodes(parent_node, input):
#   children = []
#   for c in parent_node.child_count:
#     node = Node(input[0], input[1])
#     node.children += add_child_nodes()
#  for i in range(0, )

#  return children

# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# A----------------------------------
#     B----------- C-----------
#                      D-----

def create_node(name, header, meta):
  # Init node with child node count and metadata count
  node = Node(name, header[0], header[1])
  
  # No children: metadata comes next in meta
  if node.child_count == 0:
    node.metadata = meta[:node.metadata_count]
    meta = meta[node.metadata_count:]
#    print('Initializing metadata for node', node.name, ':', node.metadata)

  for c in range(1, node.child_count + 1):
    ret = create_node(name + c, meta[:2], meta[2:])
    node.children.append(ret[0])
    meta = ret[1]
  
  if node.child_count != 0:
    node.metadata = meta[:node.metadata_count]
    meta = meta[node.metadata_count:]
#    print('Initializing metadata for node', node.name, ':', node.metadata)

  return (node, meta)

#print(lines[2:])
#print(lines[:2])
name = 0
ret = create_node(name, lines[:2], lines[2:])
root = ret[0]
#print('')

metadata_sum = root.get_metadata_sum()
print('Total metadata:', metadata_sum)
#root = Node(lines[0], lines[1])
#root.children = add_child_nodes(root, input[2:])


#end = time.process_time()
#print(str(end-start))