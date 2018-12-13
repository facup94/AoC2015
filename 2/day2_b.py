required_ribbon = 0

with open('input.txt','r') as file_input:
  for line in file_input:
    sides = sorted([int(x) for x in line.split('x')])

    required_ribbon += 2*sides[0] + 2*sides[1]
    
    volume = sides[0] * sides[1] * sides[2]

    required_ribbon += volume

print(required_ribbon)