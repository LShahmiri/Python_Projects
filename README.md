# Python_Projects




###Game of Craps in Python
Rules of the game:

    Two dices are required to play and a player rolls two six-sided dice and adds the numbers rolled together.
    If on the first roll a player encounters a total of 7 or 11 the player automatically wins, and if the player rolls a total of 2, 3, or 12 the player automatically loses, and play is over.
    If a player rolls a total of 4, 5, 6, 8, 9, or 10 on their first roll, that number becomes the ‘point. Then the player continues to roll the two dice again until one of two things happens either they roll the ‘point’ again, in which case they win, or they roll a 7, in which case they lose.

Approach:

    When you run the program at first you get a choice on whether to start the game or exit from the game and this is done by importing the sys module after you continue to play the game, you will get an option to view the rules of the game or if you are already familiar with the rules you can choose not to see them.
    When you start the game by pressing enter the random module choose two numbers between 1 and 6 randomly. Then by the use of diceNumber() function, the two numbers are added together.
    Now by following the rules of the game if the total of your dices are 7 or 11 you win. And if you score a total of 2,3,12 you will automatically lose.
    And if your total is 4,5,6,8,9 or 10 that total will be saved and the program will run in a loop until two things happen 1)you score the same numbers as before or you score 7. If you have scored the same number as before you will win and if you have scored a total f 7 you have lost.
