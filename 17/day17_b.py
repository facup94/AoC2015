from itertools import combinations

containers = []
with open('input.txt', 'r') as input_file:
  for line in input_file:
    containers.append(int(line))

number_of_combinations = 0
for amount_containers_used in range(len(containers)):
  for c in combinations(containers, amount_containers_used+1):
    if sum(c) == 150:
      number_of_combinations += 1
  if number_of_combinations != 0:
    break

print(number_of_combinations)