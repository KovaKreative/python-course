from math import pi, prod

def vol(rad):
  res = (4 / 3) * pi * rad ** 3
  print(round(res, 6))

# Check
vol(2)

def ran_check(num,low,high):
  in_range = num in range(low, high + 1)
  if in_range:
    print(f'{num} is in range of {low} and {high}')
  else:
    print(f'{num} is NOT in range of {low} and {high}')

# Check
ran_check(5,2,7)
# ran_check(2,2,7)
# ran_check(7,2,7)
# ran_check(8,2,7)

def ran_bool(num,low,high):
  print(num in range(low, high + 1))
  
ran_bool(3,1,10)

def up_low(s):
  u = 0
  l = 0

  for c in s:
    if c.islower():
      l += 1
    elif c.isupper():
      u += 1


  print('Original string: ' + s)
  print('Upper: ' + str(u))
  print('Lower: ' + str(l))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


def unique_list(lst):
  # unique = []
  # for n in lst:
  #   if n not in unique:
  #     unique.append(n)

  print(list(set(lst)))

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

def multiply(numbers):  
  result = prod(numbers)
  print(result)

multiply([1,2,3,-4])

def palindrome(s):
  phrase = s.lower().replace(" ", "")
  b_phrase = phrase[::-1]

  print(phrase == b_phrase)

palindrome('nurses run')

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
  phrase = str1.lower().replace(" ", "")
  alphabuffer = alphabet

  for c in phrase:
    if c in alphabuffer:
      alphabuffer = alphabuffer.replace(c, '')

  print(len(alphabuffer) <= 0)

ispangram("The quick brown fox jumps over the lazy dog")
ispangram("Tickle me elmo")