num_players = 400
last_marble_to_place = 71864


player_scores = [0 for i in range(num_players)]
marbles = [0, 1]
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
#    print_state()
    if next_marble_to_place % 23 == 0:
      pop_index = (current_marble_index - 7) % len(marbles)
      marble_place_score = next_marble_to_place
      marble_remove_score = marbles.pop(pop_index)
      marble_score = marble_place_score + marble_remove_score 
      player_scores[current_player] += marble_score
      current_marble_index = pop_index
    else:
      # Where to insert marble
      marble_insertion_index = (current_marble_index + 2) % (len(marbles) + 1)
      # Hack
      if marble_insertion_index == 0:
        marble_insertion_index = 1
      marbles.insert(marble_insertion_index, next_marble_to_place)
      current_marble_index = marble_insertion_index

    # Next player, next marble
    current_player = (current_player + 1) % len(player_scores)
    next_marble_to_place += 1
    if next_marble_to_place > last_marble_to_place:
      marbles_left = False
      break

print('Player scores after placing', next_marble_to_place - 1, 'marbles:', player_scores)
print('Max score:', max(player_scores))
