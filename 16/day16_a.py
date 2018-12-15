aunts = [{} for _ in range(500)]
with open('input.txt', 'r') as input_file:
  for line in input_file:
    parts = line.strip().split(' ')
    parts[-1] = parts[-1] + ','
    parts = [x[:-1] for x in parts]
    aunt_id = int(parts[1]) - 1
    parts = parts[2:]
    while len(parts) > 0:
      aunts[aunt_id][parts[0]] = int(parts[1])
      parts = parts[2:]

for i, aunt in enumerate(aunts):
  if 'children' in aunt and aunt['children'] != 3:
    continue
  if 'cats' in aunt and aunt['cats'] != 7:
    continue
  if 'samoyeds' in aunt and aunt['samoyeds'] != 2:
    continue
  if 'pomeranians' in aunt and aunt['pomeranians'] != 3:
    continue
  if 'akitas' in aunt and aunt['akitas'] != 0:
    continue
  if 'vizslas' in aunt and aunt['vizslas'] != 0:
    continue
  if 'goldfish' in aunt and aunt['goldfish'] != 5:
    continue
  if 'trees' in aunt and aunt['trees'] != 3:
    continue
  if 'cars' in aunt and aunt['cars'] != 2:
    continue
  if 'perfumes' in aunt and aunt['perfumes'] != 1:
    continue
  
  print(i+1)