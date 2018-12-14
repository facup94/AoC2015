from itertools import permutations
attendees = {}
with open('input.txt', 'r') as input_file:
  for line in input_file:
    l = line[:-2].split(' ')

    if l[0] not in attendees:
      attendees[l[0]] = {}
    
    if l[2] == 'gain':
      attendees[l[0]][l[10]] = int(l[3])
    else:
      attendees[l[0]][l[10]] = -int(l[3])

attendees['me'] = {}
for attendee in attendees.keys():
  if attendee != 'me':
    attendees['me'][attendee] = 0
    attendees[attendee]['me'] = 0


max_happiness = 0
for p in permutations(attendees.keys()):
  happiness = 0
  for i in range(len(p)):
    happiness += attendees[p[i]][p[(i+1)%len(p)]]
    happiness += attendees[p[i]][p[i-1]]
  
  if happiness > max_happiness:
    max_happiness = happiness

print(max_happiness)

