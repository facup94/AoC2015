grid = [[False]*1000 for _ in range(1000)]

with open('input.txt', 'r') as input_file:
  for line in input_file:
    parts = line.split(' ')
    if len(parts) == 4:
      y_start = int(parts[1].split(',')[0])
      x_start = int(parts[1].split(',')[1])
      y_end = int(parts[3].split(',')[0])
      x_end = int(parts[3].split(',')[1])

      for y in range(y_start, y_end+1):
        for x in range(x_start, x_end+1):
          grid[y][x] = not grid[y][x]

    else:
      y_start = int(parts[2].split(',')[0])
      x_start = int(parts[2].split(',')[1])
      y_end = int(parts[4].split(',')[0])
      x_end = int(parts[4].split(',')[1])

      for y in range(y_start, y_end+1):
        for x in range(x_start, x_end+1):
          grid[y][x] = parts[1] == 'on'

amount_on = 0
for y in range(1000):
  for x in range(1000):
    if grid[y][x]:
      amount_on += 1
print(amount_on)