grid = [[0]*1000 for _ in range(1000)]

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
          grid[y][x] += 2

    else:
      y_start = int(parts[2].split(',')[0])
      x_start = int(parts[2].split(',')[1])
      y_end = int(parts[4].split(',')[0])
      x_end = int(parts[4].split(',')[1])

      for y in range(y_start, y_end+1):
        for x in range(x_start, x_end+1):
          if parts[1] == 'on':
            grid[y][x] += 1
          else:
            grid[y][x] -= 1
            if grid[y][x] < 0:
              grid[y][x] = 0

total_brightness = 0
for y in range(1000):
  for x in range(1000):
    total_brightness += grid[y][x]
print(total_brightness)