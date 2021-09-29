print('================================')
print('Welcome to Guess The Number')
print('================================')

num = 32

attempt = int(input('Type your number: '))

print('\nYou typed', attempt)

if (attempt == num):
    print('Right answer!!!')
else:
    print('Wrong...try again!\n')

print('End of Game')