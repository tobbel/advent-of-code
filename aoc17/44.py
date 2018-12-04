import sys
from collections import Counter

def soln(pwd, hashfn):
    words = set()
    for word in pwd.split(' '):
        hashable = hashfn(word)
        if hashable in words:
            return False
        words.add(hashable)
    return True

with open('c:\\dev\\avc17\\4.txt') as f:
    a = f.readlines()
result_1, result_2 = 0, 0
identity = lambda x : x
counter_hash = lambda x: frozenset(Counter(x).items())
for line in a: 
    result_1 += soln(line.strip(), identity)
    result_2 += soln(line.strip(), counter_hash)

print('Part 1: {}, Part 2: {}'.format(result_1, result_2))