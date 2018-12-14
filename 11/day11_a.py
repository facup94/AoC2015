def increment_password(pw):
  pass_int = [ord(x) for x in pw]
  
  i = -1
  pass_int[i] += 1
  while pass_int[i] > 122:
    pass_int[i] = 97
    i -= 1
    pass_int[i] += 1
  
  return ''.join([chr(x) for x in pass_int])

def has_unallowed_letters(pw):
  return pw.count('i') > 0 or pw.count('o') > 0 or pw.count('l') > 0

def has_three_increasing_letters(pw):
  for i in range(len(pw) - 2):
    if ord(pw[i]) == ord(pw[i+1])-1 and ord(pw[i]) == ord(pw[i+2])-2:
      return True

  return False

def has_two_pairs_of_letters(pw):
  for i in range(len(pw) - 3):
    if pw[i] == pw[i+1]:
      for j in range(i+2, len(pw)-1):
        if pw[j] == pw[j+1]:
          return True
  
  return False

current_password = 'vzbxkghb'
password = current_password

while (not has_three_increasing_letters(password)) or has_unallowed_letters(password) or (not has_two_pairs_of_letters(password)):
  password = increment_password(password)

print('next password:', password)