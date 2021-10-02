def play_game():
    print('================================')
    print('Welcome to Hangman Game')
    print('================================')

    secret_word = 'banana'
    secret_word = secret_word.upper()

    right_words = ['_', '_', '_', '_', '_', '_']
    errors = 6

    def show_words():
        return '\n{}'.format(right_words)

    print('\nThe word has {0} letters and you have {0} attempts!'.format(right_words.count('_')))
    print(show_words())

    while True:
        print('Playing...')
        attempt = input('Type a letter: ').upper().strip()

        if attempt in secret_word:
            index = 0
            for letter in secret_word:
                if attempt == letter:
                    right_words[index] = letter
                    print('Yes! Found the letter "{}". Positions: {}'.format(attempt, index + 1))
                index += 1
        else:
            errors -= 1

            if errors == 0:
                print('You lost...but try again!!\n')
                break
            elif errors == 1:
                print('This is your last chance!!\n')
            else:
                print('\nThe letter "{}" was not found...You still have {} attempts'.format(attempt, errors))

        if "_" not in right_words:
            print('Nice, you won! Good job! :D\n')
            break

        print(show_words())
        print('\n')

    print('End of Game')


if __name__ == '__main__':
    play_game()
