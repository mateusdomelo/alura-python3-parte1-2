import random

def play_game():
    print('================================')
    print('Welcome to Guess The Number')
    print('================================')

    num = random.randrange(1, 101)
    attempt_initial = 1
    points = 1000

    print('Choose the level of your game:\n(1) Easy / (2) Medium / (3) Hard\n')
    level = int(input('Type the level: '))

    if level == 1:
        total_attempts = 20
    elif level == 2:
        total_attempts = 10
    else:
        total_attempts = 5

    for rounds in range(attempt_initial, total_attempts + 1):
        print('Attempt number: {} of {}  \n'.format(rounds, total_attempts))

        attempt = int(input('Type a number between 1 and 100: '))
        print('\nYou typed', attempt)

        if attempt < 1 or attempt > 100:
            print('Type a number between 1 and 100...try again!\n')
            print('================================')
            continue

        right = attempt == num
        higher = attempt > num
        lower = attempt < num

        if right:
            print('Right answer!!! :D\n')
            print('================================')
            break
        else:
            lost_points = abs(num - attempt)
            points = points - lost_points
            if higher:
                print('Wrong...you should try a LOWER number...lets go!\n')
            elif lower:
                # It could be 'else'
                print('Wrong...You should try a HIGHER number...lets go!\n')

        if rounds == total_attempts - 1:
            print("This is your last shot! Be careful!") 
        elif rounds == total_attempts:
            print("Unfortunately, you reached the maximum number of attempts! The chosen number was {}. You got {} points!".format(num, points))
        
        print('================================')
        
    print('End of Game')


if __name__ == '__main__':
    play_game()
