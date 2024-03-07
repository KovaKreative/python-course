def blackjack(*args):
  cards = sum(args)

  if cards <= 21:
    return cards
  
  if 11 in args:
    return cards - 10
  
  return 'BUST'
  

# Check
print(blackjack(5,6,7))

# Check
print(blackjack(9,9,9))

# Check
print(blackjack(9,9,11))