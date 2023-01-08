import random

number = random.randint(1,100)
lifePoint = int(input('How many due would you like to use?: '))
due = lifePoint
counter = 0
while due>0:
    due -= 1
    counter += 1
    guess = int(input('Guess: '))

    if number == guess:
        print(f'Congratulations {counter}. you knew at once.  Your total score: {100 - (100/lifePoint)*(counter-1)}')
        break
    elif number > guess:
        print('UP')
    else:
        print('DOWN')

        if due == 0:
            print(f'Your due is over. The Number Kept is: {number}')