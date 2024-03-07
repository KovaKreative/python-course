from random import shuffle

def shuffle_list(list):
  buffer = list.copy()
  shuffle(buffer)
  return buffer

def player_guess():
  guess = ''
  while guess not in ['0', '1', '2']:
    guess = input("Pick a number: 0, 1, or 2: ")

  return int(guess)

def check_guess(mylist, guess):
  if mylist[guess] == 'O':
    print("You win!")
  else:
    print("Wrong!")
    print(mylist)

game_list = ['', 'O', '']
shuffled_game_list = shuffle_list(game_list)
my_guess = player_guess()

check_guess(shuffled_game_list, my_guess)