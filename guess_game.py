secretnumberE=5
secretnumberM=19
secretnumberH=50
guess_count=0
guess_limitA=6
guess_limitB=4
guess_limitC=3
a=6
b=4
c=3
remain= ' trials remaining'
print('IN THIS GAME YOU ARE TO GUESS A NUMBER')
print('Game levels are \n E for Easy \n M for Medium \n H for Hard \n')
choice= input('Choose your Level(E/M/H): ')

if(choice == 'E'):
    while guess_count < guess_limitA:
        guess = int(input('guess a number from 1 - 10 '))
        guess_count += 1
        a-=1


        if guess == secretnumberE:
            print('correct')
            break
        else:
            print(str(a)+remain)

    else:
        print('GAME OVER')

elif(choice == 'M'):
    while guess_count < guess_limitB:
        guess = int(input('guess a number from 1-20 '))
        guess_count += 1
        b -= 1

        if guess == secretnumberM:
            print('correct')
            break
        else:
            print(str(b) + remain)


    else:
        print('GAME OVER')

elif(choice == 'H'):
    while guess_count < guess_limitC:
        guess = int(input('guess a number from 1 - 50 '))
        guess_count += 1
        c -= 1

        if guess == secretnumberH:
            print('correct')
            break
        else:
            print(str(c) + remain)


    else:
        print('GAME OVER')



