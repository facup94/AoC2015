from itertools import permutations

cities = {}

with open('input.txt', 'r') as input_file:
  for line in input_file:
    splited = line.split(' ')
    city_a = splited[0]
    city_b = splited[2]
    distance = int(splited[4])
    
    if city_a not in cities:
      cities[city_a] = {}
    if city_b not in cities:
      cities[city_b] = {}
    
    cities[city_a][city_b] = distance
    cities[city_b][city_a] = distance

shortest_path = -1
for path in permutations(cities.keys()):
  distance = 0
  for i in range(len(path) - 1):
    distance += cities[path[i]][path[i+1]]
  
  if distance < shortest_path or shortest_path == -1:
    shortest_path = distance

print(shortest_path)
