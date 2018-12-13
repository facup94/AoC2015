santa_visited_houses = set()
robo_santa_visited_houses = set()
santa_position = [0,0]
robo_santa_position = [0,0]
santa_visited_houses.add(tuple(santa_position))
robo_santa_visited_houses.add(tuple(robo_santa_position))

with open('input.txt','r') as file_input:
  santa_turn = True
  for c in file_input.readline():
    if santa_turn:
      if c == '^':
        santa_position[1] += 1
      elif c == '>':
        santa_position[0] += 1
      elif c == 'v':
        santa_position[1] -= 1
      else:
        santa_position[0] -= 1
      
      santa_visited_houses.add(tuple(santa_position))
    else:
      if c == '^':
        robo_santa_position[1] += 1
      elif c == '>':
        robo_santa_position[0] += 1
      elif c == 'v':
        robo_santa_position[1] -= 1
      else:
        robo_santa_position[0] -= 1
      
      robo_santa_visited_houses.add(tuple(robo_santa_position))
    
    santa_turn = not santa_turn

print(len(santa_visited_houses.union(robo_santa_visited_houses)))