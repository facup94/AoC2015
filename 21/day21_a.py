from itertools import combinations

weapons = {
'Dagger': {'cost':8, 'damage':4, 'armor':0},
'Shortsword': {'cost':10, 'damage':5, 'armor':0},
'Warhammer': {'cost':25, 'damage':6, 'armor':0},
'Longsword': {'cost':40, 'damage':7, 'armor':0},
'Greataxe': {'cost':74, 'damage':8, 'armor':0}}
armors = {
'Leather': {'cost':13, 'damage':0, 'armor':1},
'Chainmail': {'cost':31, 'damage':0, 'armor':2},
'Splintmail': {'cost':53, 'damage':0, 'armor':3},
'Bandedmail': {'cost':75, 'damage':0, 'armor':4},
'Platemail': {'cost':102, 'damage':0, 'armor':5}}
rings = {
'Damage +1': {'cost':25, 'damage':1, 'armor':0},
'Damage +2': {'cost':50, 'damage':2, 'armor':0},
'Damage +3': {'cost':100, 'damage':3, 'armor':0},
'Defense +1': {'cost':20, 'damage':0, 'armor':1},
'Defense +2': {'cost':40, 'damage':0, 'armor':2},
'Defense +3': {'cost':80, 'damage':0, 'armor':3},
'None 1': {'cost':0, 'damage':0, 'armor':0},
'None 2': {'cost':0, 'damage':0, 'armor':0}}

min_gold_spent = 74 + 102 + 100 + 80

for weapon in weapons:
  for armor in armors:
    for ring_set in combinations(rings, 2):
      total_cost = weapons[weapon]['cost'] + armors[armor]['cost'] + sum([rings[x]['cost'] for x in ring_set])
      total_damage = weapons[weapon]['damage'] + armors[armor]['damage'] + sum([rings[x]['damage'] for x in ring_set])
      total_armor = weapons[weapon]['armor'] + armors[armor]['armor'] + sum([rings[x]['armor'] for x in ring_set])

      boss = {'HP': 103, 'damage': 9, 'armor': 2}
      me = {'HP': 100, 'damage': total_damage, 'armor': total_armor}

      my_real_damage = max(1, me['damage'] - boss['armor'])
      boss_real_damage = max(1, boss['damage'] - me['armor'])
      
      my_turn = True
      while me['HP'] > 0 and boss['HP'] > 0:
        if my_turn:
          boss['HP'] -= my_real_damage
        else:
          me['HP'] -= boss_real_damage

        my_turn = not my_turn
        
      if (not my_turn) and total_cost < min_gold_spent:
        min_gold_spent = total_cost

print(min_gold_spent)
