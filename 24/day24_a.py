from itertools import product, combinations

all_weights = []
with open('input.txt', 'r') as input_file:
  for line in input_file:
    all_weights.append(int(line.strip()))

fewest_packages_posible_group_1 = len(all_weights)
smallest_quantum_entanglement_group_1 = 1
for weight in all_weights:
  smallest_quantum_entanglement_group_1 *= weight

group_weight = sum(all_weights)
group_weight //= 3

for tam1 in range(1, len(all_weights)-1):
  
  already_found_this_g1_size = False

  for combination in combinations(all_weights, tam1):
    if sum(combination) != group_weight:
      continue
    
    all_weights_minus_used_in_group_1 = [x for x in all_weights if x not in combination]
    for tam2 in range(1, len(all_weights_minus_used_in_group_1)-1):
      for combination2 in combinations(all_weights_minus_used_in_group_1, tam2):
        
        if sum(combination2) != group_weight:
          continue
        
        if len(combination) > fewest_packages_posible_group_1:
          continue
        
        quantum_entanglement = 1
        for w in combination:
          quantum_entanglement *= w
        if quantum_entanglement >= smallest_quantum_entanglement_group_1 and len(combination) == fewest_packages_posible_group_1:
          continue
      
        fewest_packages_posible_group_1 = len(combination)
        smallest_quantum_entanglement_group_1 = quantum_entanglement
        already_found_this_g1_size = True
        print(combination, combination2, [x for x in all_weights_minus_used_in_group_1 if x not in combination2])
        print('Smallest QE (for now):', smallest_quantum_entanglement_group_1)

  if already_found_this_g1_size:
    break
        

print('Smallest QE:', smallest_quantum_entanglement_group_1)