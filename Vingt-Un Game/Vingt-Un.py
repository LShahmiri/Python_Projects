"""Simulating the Vingt-Un game ."""
import random
sum_of_cards=0
status=True


def card_game():
    """ Pull a card and return its face value"""
    
    card=random.randrange(1,11)
    return card

def play_game():
    """Starting the game"""
    global status
    global sum_of_cards
    card=card_game()
    
    sum_of_cards += card # Save cards
    print(f'Card= {card} and Sum= {sum_of_cards}' )
    
    
    if sum_of_cards < 21: 
        status= True
        print('Continue')
        while status == True:
            play_game()
         
    elif sum_of_cards > 21 :
       
        print ('Lost')
        status = False

    else:
        
        print ('Win')
        status = False
       
        
    
        
        
    
play_game()

    