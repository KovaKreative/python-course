def summer_69(arr):
  
  skip = False

  sum = 0

  for i in arr:

    if i == 6:
      skip = True

    if not skip:
      sum += i

    if skip and i == 9:
      skip = False

  return sum
    


# Check
print(summer_69([1, 3, 5]))

# Check
print(summer_69([4, 5, 6, 7, 8, 9]))

# Check
print(summer_69([2, 1, 6, 9, 11]))