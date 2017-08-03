number = 23
running = True

while running:
    guess = int(input('Enter an interger :'))

    if guess == number:
        print('Yes')
        running = False
    elif guess < number:
        print('xiao')
    else:
        print('da')

else:
    print('Over')

print('Done')