''' 
Number Gussing Game.
'''
import random 
attemps_list = []

def show_score():
    """showing message about yours attemps_list """
    if not attemps_list:
 
        print('There is currently no high score, it\'s yours for the taking!') #For the first
    else:
        print(f'The current high score is {min(attemps_list)}attemps') #If you play more than one time to show the best result

def start_game():
    attemps=0
    rand_num=random.randint(1,10) #Get a number randomly
    print('hello traveler! welcome to the game of gusses!')
    player_name=input('what is your name? ')
    wanna_play=input(
        f'Hi {player_name}, would you like to play the gussing game? '
        'Enter Yes/No): ')
    if wanna_play.lower()!='yes':
        print('That\'s cool, Thanks!')
        exit()
    else:
        show_score()
    
    while wanna_play.lower() == 'yes':
        try:
            guess=int(input('Pick a number between 1 and 10: '))
            if guess<1 or guess>10:
                raise ValueError('please guess an number within the given range')
            attemps+=1
            attemps_list.append(attemps)
            if guess==rand_num:
                print('Nice! You Got It')
                print(f'It took you {attemps} attemps')
                wanna_play=input('Would you like to play again? (Enter Yes/No):')
                if wanna_play.lower() !='yes':
                    print('Thats\'s cool, have a good one!')
                    break
                else:
                    attemps=0
                    rand_num=random.randint(1,10)
                    show_score()
                    continue
            else:
                if guess> rand_num:
                    print('it\'s lower')
                elif guess< rand_num:
                    print('it\'s higher')
        except ValueError as err:
            print('Oh no! that is not a valid value. Try again...')
            print(err)

if __name__=='__main__':
    start_game()


        


