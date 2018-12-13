with open('input.txt', 'r') as file_input:
  floor = 0
  position = 1
  while True:
    c = file_input.read(1)
    if not c:
      break
    
    if c == '(':
      floor += 1
    else:
      floor -= 1

    if floor == -1:
      print(position)
      break
    
    position += 1
