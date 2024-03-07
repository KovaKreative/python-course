def spy_game(nums):
  find = [0, 0, 7]
  index = 0

  for n in nums:

    if n == find[index]:
      index += 1

    if index >= len(find):
      return True
  
  return False

# Check
print(spy_game([1,2,4,0,0,7,5]))

# Check
print(spy_game([1,0,2,4,0,5,7]))

# Check
print(spy_game([1,7,2,0,4,5,0]))