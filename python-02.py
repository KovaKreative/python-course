# variable = "Hello universe!",

# print(variable)

print("{}".format([x for x in range(10) if x % 2 == 0]))

# names = ["Eric", "Caroline", "Kochi"]

# names.append("Woofy")

# for name in names:
  # end = 5
  # if len(name) >= end:
  #   print(name[1:end])

# myTuple = ("Eric", "Caroline", "Kochi")

# print(myTuple)

# myList = {"name":"Eric", "pet":"Kochi"}

# print(myList["pet"])

# for i in range(10):
#   if i % 3 == 0:
#     print("Divides by 3")
#   elif i % 2 == 0:
#     print("Even")
#   else:
#     print("Odd")

# for num in range(2, 100):
#   isPrime = True
#   for divisor in range (2, num):
#     if num % divisor == 0:
#       isPrime = False

#   if isPrime:
#     print(str(num) + " is prime")

# def isPrime(num):
#   isPrime = True
#   for divisor in range (2, num):
#     if num % divisor == 0:
#       isPrime = False
#       break

#   if isPrime:
#     print(str(num) + " is prime")

# isPrime(7)

# class Game:
#   def __init__(self, name):
#     self.name = name
#     self.nums = []

#   def __repr__(self):
#     return "(Game {})".format(self.name)
  
#   def identify(self):
#     print(self)
  
#   def startGame(self):
#     print("Game Started")
  
#   def addNum(self, num):
#     self.nums.append(num)
#     return self.nums

#   def printNums(self):
#     print("List of numbers: ", self.nums)

# g = Game()

# g.addNum(5)
# g.addNum(7)
# g.addNum(9)
# g.printNums()

# print(Game("Mortal Kombat"))

# import requests

# res = requests.get('https://catfact.ninja/fact')

# print(res.json()['fact'].split("-"))