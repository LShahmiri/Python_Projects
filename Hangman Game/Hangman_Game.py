import random  # Import the random module to generate random word
words = ['apple','banana','cherry','orange','pear']
word = random.choice(words)  # Choose a random word from list
guesses = '' # Initilize an empty string to store the player's guesses
turns = 10  # Set the number of turns the players has
while turns > 0 :
    failed=0
    for letter in word:
        if letter in guesses:
            print(letter, end='') # Disply the letter if it has been guessed
        else:
            print('-',end='') # Disple underscore if the letter has not been guessed
            failed+=1
    if failed==0:
        print(' is true you win!')
        break  # Exit the loop if the player has guessed all the letters
    guess=input('\nGuss a letter ')
    guesses+=guess
    if guess not in word:
        turns -= 1
        print('Wrong!')  
        print('You have', turns, 'more guesses.')
    if turns==0:
        print('You lost')  # Disply a message if the player runs out of guesses
              



