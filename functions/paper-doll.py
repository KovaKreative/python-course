def paper_doll(text):
  buffer = ''
  for char in text:
    buffer += char*3

  return buffer

# Check
print(paper_doll('Hello'))

# Check
print(paper_doll('Mississippi'))