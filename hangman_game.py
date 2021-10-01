def play_game():
    print('================================')
    print('Welcome to Hangman Game')
    print('================================')

    word = 'banana'
    word = word.lower()
    right = False
    hanged = False

    while not right and not hanged:
        print('Playing...')
        attempt = input('Type a letter: ').lower().strip()

        index = 1

        for letter in word:
            if attempt == letter:
                print("Nice! I found the letter '{}' in position {}".format(letter, index))

            index = index + 1
        print('\n')

    print('End of Game')


if __name__ == '__main__':
    play_game()
