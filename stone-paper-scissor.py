
import random
randomNumber = random.randint(0, 2)
computerMove = ''
if randomNumber == 0:
    computerMove = 'stone'
elif randomNumber == 1:
    computerMove = 'paper'
elif randomNumber == 2:
    computerMove = 'scissor'

player1 = input('player-1 please ensert your choice: ')
player2 = computerMove
print(f'player-2 please ensert your choice: {computerMove}')

if player1 == player2:
    print('that\'s a tie!...')
elif player1 == 'paper':
    if player2 == 'stone':
        print('player-1 win!...')
    elif player2 == 'scissor':
        print('player-2 win!...')
    else:
        print('something is wrong!...')
elif player1 == 'scissor':
    if player2 == 'stone':
        print('player-2 win!...')
    elif player2 == 'paper':
        print('player-1 win!...')
    else:
        print('something is wrong!...')
elif player1 == 'stone':
    if player2 == 'paper':
        print('player-2 win!...')
    elif player2 == 'scissor':
        print('player-1 win!...')  
    else:
        print('something is wrong!...')     
else:
    print('something is wrong!...')



