import random

def roll_dice():
    """ Roll two dice and return their values as a tuple."""
    die_one=random.randrange(1,7)
    die_two=random.randrange(1,7)
    return (die_one,die_two)

def display_dice(dice):
    """ Display one roll of the two dice."""
    die1, die2=dice   #unplack the tuple into variables die1 and die2 
    print (f'player rolled {die1} + {die2} = {sum(dice)}') 

die_value=roll_dice() #first roll
display_dice(die_value)
#determine game status and points, based on first roll
sum_of_dice=sum(die_value)

if sum_of_dice in (7,11): #win
    game_status= 'Won'
elif sum_of_dice in (2,3,12): #Lost
    game_status= 'Lost' 
else: #remeber point
    game_status= 'Continue'
    my_point=sum_of_dice
    print ('point is ', my_point)
#continue rolling   until player win or loses
while game_status== 'Continue':
    die_value=roll_dice()
    display_dice(die_value)
    sum_of_dice= sum(die_value)
    if sum_of_dice== my_point:
        game_status= 'Win'
    elif sum_of_dice== 10:
        game_status= 'Lost'
if game_status == 'Win':
    print('Player Wins')
else:
    print('Player Loses') 



