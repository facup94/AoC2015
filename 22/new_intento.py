from collections import namedtuple
from copy import deepcopy

player = {'HP':50, 'armor':0, 'mana':500, 'shielded':-1, 'recharging':0}
boss = {'HP':71, 'damage':10, 'poisoned':0}
spells_cost = {'Magic Missile':53, 'Drain':73, 'Shield':113, 'Poison':173, 'Recharge':229}

def smth(player:Player, boss:Boss, spell_list:tuple, player_turn :bool):
  player = deepcopy(player)
  boss = deepcopy(boss)
  
  # Apply boss effects
  if boss['poisoned'] > 0:
    boss['poisoned'] -= 1
    boss['HP'] -= 3
    # print('Poison deals 3 damage; its timer is now', boss['poisoned'])
    if boss['HP'] <= 0:
      pass
  
  # Apply player effects
  if player['shielded'] > 0:
    player['shielded'] -= 1
    # print('Shield\'s timer is now', player['shielded'])