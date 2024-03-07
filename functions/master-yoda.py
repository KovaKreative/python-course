def master_yoda(text):
  buffer = text.rsplit(' ', 1)
  buffer.reverse()
  return ' '.join(buffer)

# Check
print(master_yoda('I am home'))

# Check
print(master_yoda('We are ready'))