def evaluate_wire(wires, wire_id):
  wire = wires[wire_id]

  if wire["value"] is not None:
    return wire["value"]

  if 'operator' not in wire:    
    elem1 = int(wire['element1']) if wire['element1'].isdigit() else evaluate_wire(wires, wire['element1'])
    wire['value'] = elem1
    return elem1

  if wire['operator'] == 'NOT':    
    elem1 = int(wire['element1']) if wire['element1'].isdigit() else evaluate_wire(wires, wire['element1'])
    wire['value'] = ~elem1
    return ~elem1
  
  if wire['operator'] == 'OR':
    elem1 = int(wire['element1']) if wire['element1'].isdigit() else evaluate_wire(wires, wire['element1'])
    elem2 = int(wire['element2']) if wire['element2'].isdigit() else evaluate_wire(wires, wire['element2'])
    wire['value'] = elem1 | elem2
    return elem1 | elem2
  
  if wire['operator'] == 'AND':    
    elem1 = int(wire['element1']) if wire['element1'].isdigit() else evaluate_wire(wires, wire['element1'])
    elem2 = int(wire['element2']) if wire['element2'].isdigit() else evaluate_wire(wires, wire['element2'])
    wire['value'] = elem1 & elem2
    return elem1 & elem2
  
  if wire['operator'] == 'RSHIFT':
    elem1 = int(wire['element1']) if wire['element1'].isdigit() else evaluate_wire(wires, wire['element1'])
    elem2 = int(wire['element2']) if wire['element2'].isdigit() else evaluate_wire(wires, wire['element2'])
    wire['value'] = elem1 >> elem2
    return elem1 >> elem2
  
  if wire['operator'] == 'LSHIFT':
    elem1 = int(wire['element1']) if wire['element1'].isdigit() else evaluate_wire(wires, wire['element1'])
    elem2 = int(wire['element2']) if wire['element2'].isdigit() else evaluate_wire(wires, wire['element2'])
    wire['value'] = elem1 << elem2
    return elem1 << elem2

wires = {}

with open('input.txt', 'r') as input_file:
  for line in input_file:
    parts = line.split(' ')

    if len(parts) == 3:
      wires[parts[-1][:-1]] = {"element1": parts[0], "value":None}
    elif len(parts) == 4:
      wires[parts[-1][:-1]] = {"element1":parts[1], 'operator':parts[0], "value":None}
    else:
      wires[parts[-1][:-1]] = {"operator":parts[1], 'element1':parts[0], 'element2':parts[2], "value":None}

print('a', evaluate_wire(wires, 'a'))

