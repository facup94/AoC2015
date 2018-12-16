AT_LEAST_PRESENTS = 34000000
houses = [10] * (AT_LEAST_PRESENTS//11+1)

for i in range(2, AT_LEAST_PRESENTS//11+1):
  j = 1
  while i*j < len(houses) and j<51:
    houses[i*j] += i*11
    j += 1

for house_id, gifts in enumerate(houses):
  if gifts >= AT_LEAST_PRESENTS:
    print(house_id, gifts)
    break
