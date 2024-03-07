def count_primes(num):
  primes = 0
  for n in range(2, num + 1):
    # print("Check " + str(n))
    divisibles = 0
    for d in range(2, n):
      if n % d == 0:
        # print("N: " + str(n))
        # print("D: " + str(d))
        divisibles += 1
    
    if divisibles < 1:
      # print("Prime: " + str(n))
      primes += 1
    

  return primes             

# Check
# count_primes(13)
print(count_primes(100))
print(count_primes(13))
print(count_primes(12))
print(count_primes(1000))