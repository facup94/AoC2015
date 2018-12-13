import hashlib

SECRET_KEY = 'ckczppom'

i = 0
while True:
  string = SECRET_KEY + str(i)
  if hashlib.md5(string.encode('utf-8')).hexdigest()[:6] == '000000':
    print(i)
    break

  i += 1
