def square(num):
  return num**2

my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
  print(item)

print(list(map(square, my_nums)))

last_names = ["McDonald", "Simpson", "Hope", "Miller", "Ido"]

def name_formatter(name):
  n = ""
  if len(name) > 6:
    n = name[0]
  else:
    n = name
  return "Mr. " + n

print(list(map(name_formatter, last_names)))

def short_name(name):
  return len(name) < 7

print(list(filter(short_name, last_names)))
