import guess_game
import hangman_game

print('Hi, welcome!\nThe options are: (1) Guess Game (2) Hangman Game\n')
game = int(input('Type the number of a game: '))

if (game == 1):
    guess_game.play_game()
elif (game == 2):
    hangman_game.play_game()
else:
    print('You need to choose (1) or (2)!')