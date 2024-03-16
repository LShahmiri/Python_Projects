#Game-of-Chance.py
''' The dice game craps simulation.'''
import random
def roll_dice():
    ''' Roll two dice and return their face values as a tuple.'''
    die1=random.randrange(1,7)
    die2=random.randrange(1,7)
    return(die1,die2)  # Pack die face values into a tuple.

def display_dice(dice):
    ''' Display one roll of two dice.'''
    die1,die2=dice  # Unpack the tuple into variables die1 and die2
    print(f'player rolled {die1} + {die2}= {sum(dice)}')
die_values=roll_dice() # First roll
display_dice(die_values)

# Determine game status and point, based on first roll
sum_of_dice=sum(die_values)
if sum_of_dice in (7,11): #Win
    Game_status='WON'
elif sum_of_dice in (2,3,12): # Lose
    Game_status='LOST'
else: # Remeber point
    Game_status='CONTINIUE'
    my_point= sum_of_dice
    print('Point is', my_point)

# Continiue rolling until player wins or loses
while Game_status=='CONTINIUE':
    die_values=roll_dice()
    display_dice(die_values)
    sum_of_dice=sum(die_values)

    if sum_of_dice==my_point: #Win by making point
        Game_status='WON'
    elif sum_of_dice==7: #Lose by rolling 7 
        Game_status='LOST'
# Display 'wins' or 'loses' message
if Game_status=='WON':
    print('Player Wins')
else:
    print('Player Loses')
######

