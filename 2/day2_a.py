required_paper = 0

with open('input.txt','r') as file_input:
  for line in file_input:
    sides = [int(x) for x in line.split('x')]
    a1 = sides[0] * sides [1]
    a2 = sides[1] * sides [2]
    a3 = sides[2] * sides [0]
    area = 2*a1 + 2*a2 + 2*a3 + min(a1, a2, a3)
    
    required_paper += area

print(required_paper)