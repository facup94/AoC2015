PUZZLE_INPUT = 1113122113

sequence = str(PUZZLE_INPUT)
for i in range(50):
  print('iteration', i+1)

  i, j = 0, 0
  new_seq = []
  while i < len(sequence):
    while j < len(sequence) and sequence[j] == sequence[i]:
      j += 1
    
    size = j - i
    
    new_seq.append(str(size))
    new_seq.append(str(sequence[i]))

    i = j
  
  sequence = new_seq.copy()

print(len(sequence))