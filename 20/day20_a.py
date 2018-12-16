AT_LEAST_PRESENTS = 34000000
houses = [10] * (AT_LEAST_PRESENTS//10+1)

for i in range(2, AT_LEAST_PRESENTS//10+1):
  j = 1
  while i*j < len(houses):
    houses[i*j] += i*10    
    j += 1

for house_id, gifts in enumerate(houses):
  if gifts >= AT_LEAST_PRESENTS:
    print(house_id, gifts)
    break
