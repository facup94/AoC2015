def how_many_vowels(string):
  total = string.count('a')
  total += string.count('e')
  total += string.count('i')
  total += string.count('o')
  total += string.count('u')
  return total

def has_three_or_more_vowels(string):
  total = string.count('a')
  if total >= 3:
    return True
  
  total += string.count('e')
  if total >= 3:
    return True
  
  total += string.count('i')
  if total >= 3:
    return True
  
  total += string.count('o')
  if total >= 3:
    return True
  
  total += string.count('u')
  
  return total >= 3

def has_letter_twice_in_a_row(string):
  for i in range(len(string)-1):
    if string[i] == string[i+1]:
      return True
  
  return False

def contains_bad_pairs(string):
  return string.count('ab') != 0 or string.count('cd') != 0 or string.count('pq') != 0 or string.count('xy') != 0

def is_nice(string):
  return has_three_or_more_vowels(string) and has_letter_twice_in_a_row(string) and (not contains_bad_pairs(string))

nice_words_count = 0
with open('input.txt', 'r') as file_input:
  for line in file_input:
    if is_nice(line):
      nice_words_count += 1

print(nice_words_count)