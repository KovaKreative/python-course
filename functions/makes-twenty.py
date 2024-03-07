def makes_twenty(n1,n2):
  if n1 + n2 == 20:
    return True
  
  if n1 == 20 or n2 == 20:
    return True
  
  return n1 + n2 == 20 or n1 == 20 or n2 == 20

# Check
print(makes_twenty(20,10))

print(makes_twenty(15,5))

# Check
print(makes_twenty(2,3))