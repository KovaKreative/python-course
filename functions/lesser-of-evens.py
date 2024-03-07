def lesser_of_two_evens(a,b):
  a_is_even = a % 2 == 0
  b_is_even = b % 2 == 0

  if a_is_even and b_is_even:
    return min(a, b)
  
  return max(a, b)

# Check
print(lesser_of_two_evens(2,4))

# Check
print(lesser_of_two_evens(2,5))

