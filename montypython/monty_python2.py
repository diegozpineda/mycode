#!/usr/bin/env python3
#
#
round = 0

while True:
    round = round + 1
    print(f'Finish the movie title: "Monty Python\'s the Life of _____"')
    answer = input(f'Your guess is: "')
    if answer == 'Brian':
        print(f'You are correct!')
        break
    elif round == 3:
        print(f'Sorry, the answer was... Brian."')
        break
    else:
        print(f'Sorry... Please try again!')

