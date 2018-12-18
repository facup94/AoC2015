code_size = 0
encoded_size = 0

with open('input.txt', 'r') as input_file:
  for l in input_file:
    line = l[:-1]
    code_size += len(line)

    line = line.replace('\\', '\\\\')
    line = line.replace('"', '\\"')
    
    line = "\"" + line + "\""

    encoded_size += len(line)

print(encoded_size-code_size)