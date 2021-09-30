import random

print('================================')
print('Welcome to Guess The Number')
print('================================')

num = random.randrange(1, 101)
total_attempts = 3
attempt_initial = 1

print('O número gerado foi', num)

for rounds in range(attempt_initial, total_attempts + 1):
    print('Attempt number: {} of {}  \n'.format(rounds, total_attempts))

    attempt = int(input('Type a number between 1 and 100: '))
    print('\nYou typed', attempt)

    if (attempt < 1 or attempt > 100):
        print('Type a number between 1 and 100...try again!\n')
        print('================================')
        continue

    right = attempt == num
    higher = attempt > num
    lower = attempt < num

    if (right):
        print('Right answer!!! :D\n')
        print('================================')
        break
    else:
        if(higher):
            print('Wrong...you should try a LOWER number...lets go!\n')
        elif(lower):
            # It could be 'else'
            print('Wrong...You should try a HIGHER number...lets go!\n')
    
    print('================================')
    
    # attempt_initial = attempt_initial + 1

print('End of Game')
