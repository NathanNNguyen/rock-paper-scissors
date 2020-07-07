# PLANNING
# Write a program to play Rock Paper Scissors with a user
# Flesh out the plan and think how this gonna work

# Rules:
    # Rock > Scissors
    # Scissors > Paper
    # Paper > Rock
import random

wins = 0
losses = 0
ties = 0

# Start up the program
start = input('Ready to play the game?\n [y] Yes [n] No: ')

# Flow:
while True:

    # User will specify their choice
    if start == 'y':
        user_choice = input('Choose one of these: [r] Rock [p] Paper [s] Scissors [q] Quit: ')
            # How does the program read the user's choice?
            ## Use Python's `input` function
        if user_choice == "q":
            print("Thanks for playing!")
            break

        # Program will need to specify its choice
        possible_choices = ['rock', 'paper', 'scissors']
        program_choice = random.choice(possible_choices)
        print(f'Program picked {program_choice}')
            # How does the program determine its choice?
            ## Just have it randomly pick a choice
            ## Use Python's `random.choice` functiony
            
        # Once both are made, compare and via the rules to see who won
            # How do we do comparison?
            ## use if statements
        if user_choice == 'r':
            if program_choice == 'rock':
                print('A tie!')
                ties += 1
            elif program_choice == 'paper':
                print('A loss :(')
                losses += 1
            elif program_choice == 'scissors':
                print('WINNER')
                wins += 1

        if user_choice == 'p':
            if program_choice == 'rock':
                print('WINNER')
                wins += 1
            elif program_choice == 'paper':
                print('A tie!')
                ties += 1
            elif program_choice == 'scissors':
                print('A loss :(')
                losses += 1

        if user_choice == 's':
            if program_choice == 'rock':
                print('A loss :(')
                losses += 1
            elif program_choice == 'paper':
                print('WINNER')
                wins += 1
            elif program_choice == 'scissors':
                print('A tie!')
                ties += 1
    elif start == 'n':
        print('Too bad! :(')
        exit()
    else:
        print("We're not sure what you meant. Exiting now!")
        exit()
        # Keep track of number of wins, losses, and ties for the user
            # How do we do this?
    print(f'Wins: {wins}, Ties: {ties}, Losses: {losses}')