reindeers = {}
TIME_LIMIT = 2503

with open('input.txt', 'r') as input_file:
  for line in input_file:
    l = line[:-1].split(' ')

    reindeers[l[0]] = (int(l[3]), int(l[6]), int(l[-2]))


max_distance = 0
for reindeer, data in reindeers.items():
  actions = []
  while len(actions) < TIME_LIMIT:
    actions.extend(['F'] * data[1])
    actions.extend(['R'] * data[2])

  actions = actions[:TIME_LIMIT]
  distance = sum([data[0] if x=='F' else 0 for x in actions])
  if distance > max_distance:
    max_distance = distance

print(max_distance)