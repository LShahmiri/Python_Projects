import random

def dice():
    """ Roll two dice to get their values as a tuple."""
    die_one=random.randrange(1,7)
    die_two=random.randrange(1,7)
    return (die_one,die_two)

def display(dice):
    """ sum of two roll"""
    die_one, die_tow=dice   
    print (f'player rolled {die_one} + {die_tow} = {sum(dice)}') 

values=dice() 
display(values)
sum_of_dice=sum(values)

if sum_of_dice in (7,11): 
    game_status= 'WIN'
elif sum_of_dice in (2,3,12): 
    game_status= 'LOST' 
else: 
    game_status= True
    store=sum_of_dice
    print ('points are ', store)

while game_status== True:
    die_value=dice()
    display(die_value)
    sum_of_dice= sum(die_value)
    if sum_of_dice== store:
        game_status= 'WIN'
    elif sum_of_dice== 7:
        game_status= 'LOST'
if game_status == 'WIN':
    print('Player Wins')
else:
    print('Player Loses') 



