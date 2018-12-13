def has_two_letters_twice(string):
  for i in range(len(string)-3):
    for j in range(i+2, len(string)-1):
      if string[i] == string[j] and string[i+1] == string[j+1]:
        return True
  return False

def has_letter_repeated_odd(string):
  for i in range(len(string)-2):
    if string[i] == string[i+2]:
      return True
  
  return False


def is_nice(string):
  return has_two_letters_twice(string) and has_letter_repeated_odd(string)

nice_words_count = 0
with open('input.txt', 'r') as file_input:
  for line in file_input:
    if is_nice(line):
      nice_words_count += 1

print(nice_words_count)