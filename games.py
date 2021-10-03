import guessing_number_game
import hangman_game

print('Hi, welcome!!\nThe games are: (1) Guessing a Number | (2) Hangman\n')
game = int(input('Type the number of a game: '))

if game == 1:
    guessing_number_game.play_game()
elif game == 2:
    hangman_game.play_game()
else:
    print('You need to choose (1) or (2)!')
