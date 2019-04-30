#!/usr/bin/env python3
round = 0
while(true):
    round = round + 1
    print('Finish th movie title, "Monty Python\'s The life of _____"')
    answer = input()
    if (answer == 'Brian'):
        print('coorect')
        break
    elif(round==3):
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry! Try again!')




