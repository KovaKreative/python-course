def blackjack(*args):
  cards = sum(args)
  
  if 11 in args:
    cards -= 10

  if cards <= 21:
    return cards
  
  return 'BUST'
  

# Check
print(blackjack(5,6,7))

# Check
print(blackjack(9,9,9))

# Check
print(blackjack(9,9,11))