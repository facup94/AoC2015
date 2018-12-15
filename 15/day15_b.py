from itertools import combinations_with_replacement
RECIPE_CAPACITY = 100
ingredients = {}

with open('input.txt', 'r') as input_file:
  for line in input_file:
    parts = line.strip().split()
    ingredients[parts[0][:-1]] = {'capacity': int(parts[2][:-1]), 'durability':int(parts[4][:-1]), 'flavor':int(parts[6][:-1]), 'texture':int(parts[8][:-1]), 'calories':int(parts[10])}

highest_score = 0
highest_score_members = None
for c in combinations_with_replacement(ingredients.keys(), RECIPE_CAPACITY):
  capacity = 0
  durability = 0
  flavor = 0
  texture = 0
  calories = 0
  for teaspoon in c:
    capacity += ingredients[teaspoon]['capacity']
    durability += ingredients[teaspoon]['durability']
    flavor += ingredients[teaspoon]['flavor']
    texture += ingredients[teaspoon]['texture']
    calories += ingredients[teaspoon]['calories']
  
  if calories != 500:
    continue
  
  score = max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)

  if score > highest_score:
    highest_score = score
    highest_score_members = list([{x: c.count(x)} for x in set(c)])

print(highest_score_members)
print(highest_score)
