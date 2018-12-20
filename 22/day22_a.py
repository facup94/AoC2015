from itertools import product

player = {'HP':50, 'armor':0, 'mana':500, 'shielded':-1, 'recharging':0}
# player = {'HP':10, 'armor':0, 'mana':250, 'shielded':-1, 'recharging':0}
boss = {'HP':71, 'damage':10, 'poisoned':0} 
# boss = {'HP':14, 'damage':8, 'poisoned':0} 
spells_cost = {'Magic Missile':53, 'Drain':73, 'Shield':113, 'Poison':173, 'Recharge':229}

min_mana_used = 100000000000
spell_index = 0
how_many_spells = 0
while True:
  how_many_spells += 1
  print('CHANGED SPELL NUMBER:', how_many_spells)
  for spell_list in product(('Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge'), repeat=how_many_spells):
  # for spell_list in [('Poison', 'Recharge', 'Shield', 'Poison', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile', 'Magic Missile')]:
  # for spell_list in [('Recharge', 'Shield', 'Drain', 'Poison', 'Magic Missile')]:
    mana_used = sum([spells_cost[x] for x in spell_list])
    player_turn = True
    
    while player['HP'] > 0 and boss['HP'] > 0:
      # print('')
      # print('--- PLAYER TURN ---') if player_turn else # print('--- BOSS TURN ---')
      # print('player', player)
      # print('boss', boss)
      # Apply boss effects
      if boss['poisoned'] > 0:
        boss['poisoned'] -= 1
        boss['HP'] -= 3
        # print('Poison deals 3 damage; its timer is now', boss['poisoned'])
        if boss['HP'] <= 0:
          continue
      
      # Apply player effects
      if player['shielded'] > 0:
        player['shielded'] -= 1
        # print('Shield\'s timer is now', player['shielded'])
        
      if player['shielded'] == 0:
        player['armor'] -= 7
        player['shielded'] -= 1
        # print('Shield wears off, decreasing armor by 7.')

      if player['recharging'] > 0:
        player['mana'] += 101
        player['recharging'] -= 1
        # print('Recharge provides 101 mana; its timer is now', player['recharging'])
      
      if player_turn:
        # Player turn

        if spell_index == len(spell_list):
          break

        spell = spell_list[spell_index]

        # Mana check
        if spells_cost[spell] > player['mana']:
          break
        else:
          player['mana'] -= spells_cost[spell]
          spell_index += 1
        
        # Using spell
        if spell == 'Magic Missile':
          boss['HP'] -= 4
          # print('Player casts Magic Missile, dealing 4 damage.')

        elif spell == 'Drain':
          boss['HP'] -= 2
          player['HP'] += 2
          # print('Player casts Drain, dealing 2 damage, and healing 2 hit points.')

        elif spell == 'Shield':
          if player['shielded'] != -1:
            break
          player['shielded'] = 6
          player['armor'] += 7
          # print('Player casts Shield, increasing armor by 7.')

        elif spell == 'Poison':
          if boss['poisoned'] != 0:
            break
          boss['poisoned'] = 6
          # print('Player casts Poison.')

        elif spell == 'Recharge':
          if player['recharging'] != 0:
            break
          player['recharging'] = 5
          # print('Player casts Recharge.')

      
      else:
        # Boss turn
        real_damage = boss['damage'] - player['armor']
        player['HP'] -= real_damage
        # print('Boss attacks for', real_damage, 'damage!')

      player_turn = not player_turn
      # # print('player', player)
      # # print('boss', boss)

    # # print('player', player)
    # # print('boss', boss)
    if boss['HP'] <= 0:
      # print('I won', mana_used)
      if mana_used < min_mana_used:
        min_mana_used = mana_used
        print('NEW MIN MANA:', min_mana_used)
    else:
      # print('I lost')
      # pass
  
  # break
