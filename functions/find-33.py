def has_33(nums):
  length = len(nums)
  for i in range(length - 1):
    if nums[i] == 3 and nums[i + 1] == 3:
      return True
  return False

# Check
print(has_33([1, 3, 3]))

# Check
print(has_33([1, 3, 1, 3]))

# Check
print(has_33([3, 1, 3]))