import random


# MAIN FUNCTION
def play_game():
    # SHOWS WELCOME MESSAGE
    welcome_message()

    # READ FILE WITH THE WORDS
    words = load_get_words_list()

    # SET AND GET A RANDOM WORD
    secret_word = get_secret_word(words)

    # ORGANIZE THE WORD/LETTERS
    word_layout = set_letters(secret_word)

    # NUMBER OF ATTEMPTS
    errors = 6

    # SHOW THE FIRST ROUND INFORMATION
    round_information(word_layout, errors)

    # MAIN LOOP
    while True:
        attempt = attempt_input()

        if attempt in secret_word:
            register_right_answer(secret_word, attempt, word_layout)
        else:
            errors -= 1

            if errors == 0:
                print('\nYou lost...the chosen fruit was {}.\n'.format(secret_word))
                print('You were H A N G E D...\n')
                print("     _______________         ")
                print("    /               \       ")
                print("   /                 \      ")
                print(" //                   \/\  ")
                print(" \|   XXXX     XXXX   | /   ")
                print("  |   XXXX     XXXX   |/     ")
                print("  |   XXX       XXX   |      ")
                print("  |                   |      ")
                print("  \__      XXX      __/     ")
                print("    |\     XXX     /|       ")
                print("    | |           | |        ")
                print("    | I I I I I I I |        ")
                print("    |  I I I I I I  |        ")
                print("    \_             _/       ")
                print("      \_         _/         ")
                print("        \_______/           \n")
                break
            elif errors == 1:
                print('This is your last chance!!\n')
            else:
                print('\nThe letter "{}" was not found...You still have {} attempts'.format(attempt, errors))

        # VERIFICATION IF THE PLAYER ALREADY SET THE WORD
        if "_" not in word_layout:
            print(show_letters_position(word_layout))
            print('\nNice, you won! The chosen fruit was {}. Good job! :D\n'.format(secret_word))
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
            break

        print(show_letters_position(word_layout))
        print('\n')

    # SHOWS FINAL MESSAGE
    final_message()


def welcome_message():
    print('================================')
    print('Welcome to Hangman Game')
    print('================================')


def load_get_words_list(file='words.txt'):
    words_file = open(file)
    words = []

    for word in words_file:
        word = word.strip()
        words.append(word)

    words_file.close()
    return words


def get_secret_word(words):
    random_word = random.randrange(0, len(words))
    secret_word = words[random_word].upper()
    return secret_word


def set_letters(secret_word):
    return ['_' for letter in secret_word]


# SHOW WORD LAYOUT | Ex: "['_', '_', '_', '_']"
def show_letters_position(word_layout):
    return '\n{}'.format(word_layout)


def round_information(word_layout, errors):
    print('\nThe word is a fruit and it has {} letters.\nYou have {} attempts!'.format(word_layout.count('_'), errors))
    print(show_letters_position(word_layout), '\n')


def attempt_input():
    print('Playing...')
    attempt = input('Type a letter: ').upper().strip()
    return attempt


def register_right_answer(secret_word, attempt, word_layout):
    index = 0
    for letter in secret_word:
        if attempt == letter:
            word_layout[index] = letter
            print('Yes! Found the letter "{}". Positions: {}'.format(attempt, index + 1))
        index += 1


def final_message():
    print('================================')
    print('End of Game')
    print('================================')


if __name__ == '__main__':
    play_game()
