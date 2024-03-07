def animal_crackers(text):
  split = text.lower().split()
  return split[0][0] == split[1][0]

# Check
print(animal_crackers('Levelheaded Llama'))

# Check
print(animal_crackers('Crazy Kangaroo'))