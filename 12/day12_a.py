import re
with open('input.txt', 'r') as file_input:
  a = file_input.readline()[:-1]

a = re.sub(r'[\[\]\{\}:,]', ' ', a)
a = re.sub(r'\"[a-zA-Z]+\"', ' ', a)
a = re.sub(r' +', ' ', a)
if a[0] == ' ':
  a = a[1:]
if a[-1] == ' ':
  a = a[:-1]

print(sum([int(x) for x in a.split(' ')]))
