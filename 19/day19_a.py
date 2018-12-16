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
    if parts[0] not in replacements:
      replacements[parts[0]] = []
    replacements[parts[0]].append(parts[-1])

generated_molecules = set()
for orig, dest in replacements.items():
  for i in range(len(molecule)):
    if molecule[i:i+len(orig)] == orig:
      for replacement in dest:
        generated_molecules.add(molecule[:i] + replacement + molecule[i+len(orig):])

print(len(generated_molecules))
