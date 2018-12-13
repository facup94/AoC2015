visited_houses = set()
position = [0,0]
visited_houses.add(tuple(position))

with open('input.txt','r') as file_input:
  for c in file_input.readline():
    if c == '^':
      position[1] += 1
    elif c == '>':
      position[0] += 1
    elif c == 'v':
      position[1] -= 1
    else:
      position[0] -= 1
    
    visited_houses.add(tuple(position))

print(len(visited_houses))