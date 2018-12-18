import re
code_size = 0
memory_size = 0

with open('input.txt', 'r') as input_file:
  for l in input_file:
    line = l[:-1]
    code_size += len(line)
    
    line = line.replace('\\\\', 'A')
    line = line.replace('\\"', 'B').replace('"', '')
    line = re.sub(r'\\x..', 'C', line)

    memory_size += len(line)

print(code_size-memory_size)