def almost_there(n):
  return abs(n - 100) < 10 or abs(n - 200) < 10 

# Check
print(almost_there(95))
print(almost_there(104))

# Check
print(almost_there(50))
print(almost_there(150))
print(almost_there(250))

# Check
print(almost_there(192))
print(almost_there(209))