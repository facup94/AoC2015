registers = {'a':0, 'b':0}

instruction_list = []
with open('input.txt', 'r') as input_file:
  for line in input_file:
    instruction_list.append(line.strip())

instr_index = 0
while instr_index < len(instruction_list):
  instruction = instruction_list[instr_index]
  ins_type = instruction.split(' ')[0]
  
  if ins_type == 'hlf':
    registers[instruction.split(' ')[1]] /= 2
    instr_index += 1
  elif ins_type == 'tpl':
    registers[instruction.split(' ')[1]] *= 3
    instr_index += 1
  elif ins_type == 'inc':
    registers[instruction.split(' ')[1]] += 1
    instr_index += 1
  elif ins_type == 'jmp':
    instr_index += int(instruction.split(' ')[1])
  elif ins_type == 'jie':
    if registers[instruction.split(' ')[1][:-1]] % 2 == 0:
      instr_index += int(instruction.split(' ')[2])
    else:
      instr_index += 1
  elif ins_type == 'jio':
    if registers[instruction.split(' ')[1][:-1]] == 1:
      instr_index += int(instruction.split(' ')[2])
    else:
      instr_index += 1


print(registers['b'])
