current_grid = []

with open('input.txt', 'r') as input_file:
  for line in input_file:
    current_grid.append([x for x in line.strip()])

current_grid[0][0] = '#'
current_grid[0][99] = '#'
current_grid[99][0] = '#'
current_grid[99][99] = '#'

for i in range(1, 101):
  next_grid = []
  for y_light in range(len(current_grid)):
    next_grid_row = []
    for x_light in range(len(current_grid[y_light])):
      neighbors_on = 0

      for y in range(max(y_light - 1, 0), min(y_light + 2, len(current_grid))):
        for x in range(max(x_light - 1, 0), min(x_light + 2, len(current_grid[y]))):
          if y_light == y and x_light == x:
            continue
          
          if current_grid[y][x] == '#':
            neighbors_on += 1
      
      if current_grid[y_light][x_light] == '#':
        if neighbors_on == 2 or neighbors_on == 3:
          next_grid_row.append('#')
        else:
          next_grid_row.append('.')
      else:
        if neighbors_on == 3:
          next_grid_row.append('#')
        else:
          next_grid_row.append('.')
    
    next_grid.append(next_grid_row)

  current_grid = next_grid

  current_grid[0][0] = '#'
  current_grid[0][99] = '#'
  current_grid[99][0] = '#'
  current_grid[99][99] = '#'

lights_on = 0
for row in current_grid:
  lights_on += row.count('#')
print(lights_on)
