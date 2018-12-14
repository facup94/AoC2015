reindeers = {}
reindeers_distances = {}
reindeers_points = {}
TIME_LIMIT = 2503

with open('input.txt', 'r') as input_file:
  for line in input_file:
    l = line[:-1].split(' ')

    reindeers[l[0]] = (int(l[3]), int(l[6]), int(l[-2]))


for reindeer, data in reindeers.items():
  distances = []
  while len(distances) < TIME_LIMIT:
    for _ in range(data[1]):
      if len(distances) == 0:
        distances.append(data[0])
      else:
        distances.append(data[0] + distances[-1])
    
    for _ in range(data[2]):
      distances.append(distances[-1])

  reindeers_distances[reindeer] = distances

for i in range(TIME_LIMIT):
  winner_at_i = ''
  distance_winner_at_i = 0
  for reindeer, distances in reindeers_distances.items():
    if distances[i] > distance_winner_at_i:
      distance_winner_at_i = distances[i]
      winner_at_i = reindeer
  
  if winner_at_i not in reindeers_points:
    reindeers_points[winner_at_i] = 0
  reindeers_points[winner_at_i] += 1

print(max(reindeers_points.values()))