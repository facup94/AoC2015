molecule = ''
replacements = {}
with open('input.txt', 'r') as input_file:
  rules_ended = False
  for line in input_file:
    line = line.strip()
    if line == '':
      rules_ended = True
      continue
    
    if rules_ended:
      molecule = line
      continue
    
    parts = line.split(' ')
    replacements[parts[-1]]= parts[0]


steps = 0
while molecule != 'e':
  step_finished = False
  for i in range(len(molecule)-1, -1, -1):
    for orig, dest in replacements.items():
      if molecule[i:min(i+len(orig), len(molecule))] == orig:
        molecule = molecule[:i] + dest + molecule[i+len(orig):]
        step_finished = True
        break
    if step_finished:
      break
  steps += 1
print(steps)
