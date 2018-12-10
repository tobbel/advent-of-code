'''

'''
import os 
import time
import collections

num_players = 400
last_marble_to_place = 7186400

player_scores = [0 for i in range(num_players)]
marbles = collections.deque([0, 1])

current_marble_index = 1
next_marble_to_place = 2
current_player = 1
marbles_left = True


def print_state():
  print('[' + str(current_player) + '] ', end='')
  for i in range(0, len(marbles)):
    if i == current_marble_index:
      print('(' + str(marbles[i]) + ')', end='')
    else:
      print(' ' + str(marbles[i]) + ' ', end='')
  print('')

while marbles_left:
  for i in range(0, len(player_scores)):

    if next_marble_to_place % 23 == 0:
      marbles.rotate(-7)
      marble_place_score = next_marble_to_place
      marble_remove_score = marbles.pop()
      marble_score = marble_place_score + marble_remove_score 
      player_scores[current_player] += marble_score
    else:
      marbles.rotate(2)
      marbles.append(next_marble_to_place)

    # Next player, next marble
    current_player = (current_player + 1) % len(player_scores)
    next_marble_to_place += 1
    if next_marble_to_place > last_marble_to_place:
      marbles_left = False
      break

print('Max score:', max(player_scores))
