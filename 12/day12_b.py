import re
import json
with open('input.txt', 'r') as file_input:
  a = file_input.readline()[:-1]

j = json.loads(a)

def check_childs(a):
  if type(a) == int:
    return a
  elif type(a) == list:
    total = 0
    for s in a:
      total += check_childs(s)
    return total
  elif type(a) == dict:
    total = 0
    has_red = False
    for value in a.values():
      if value == 'red':
        has_red = True
        break
    
    if not has_red:
      for value in a.values():
        total += check_childs(value)
    return total
  
  return 0

print(check_childs(j))
