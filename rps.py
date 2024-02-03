##This is a Python game of Rock, Paper, Scissors.

#Imports the "random" module.
import random

#Prints a question to the user.
print('Would you like to play?')

#Requests input from the user as to if their answer is yes or no and contains this data in the start_game variable.
start_game = input('Yes or No: ')

#Initiates a while loop.
while True:

    #Defines an if statement with the condition that the data within start_game, after being capitalized, is 'Yes', then the code indented below will be executed.
    if start_game.capitalize() == 'Yes':
        
        #A set of print statements acting as a read out for a real-life game of RPS.
        print('Alright. Time to play Rock, Paper, Scissors.')
        print('.')
        print('.')
        print('.')
        print('Rock')
        print('.')
        print('.')
        print('.')
        print('Paper')
        print('.')
        print('.')
        print('.')
        print('Scissors')
        print('.')
        print('.')
        print('.')
        print('SHOOT!')

        #Uses the method .choice() provided by the "random" module to choose a random value from the argument and contains this value in the rps_result variable.
        rps_result = random.choice(['Rock', 'Paper', 'Scissors'])
        
        #Prints the data contained in the rps_result variable.
        print(rps_result)

        #Prints a question to the user.
        print('Want to play again?')

        #Requests input from the user as to if their answer is yes or no and contains this data in the start_again variable.
        start_again = input('Yes or No: ')

    #Defines an elif statment for if the user, after the data is capitalized, has provided 'No' as an answer in the start_game variable.
    elif start_game.capitalize() == 'No':

        #Prints a goodbye message to the user.
        print('Okay. Goodbye')

        #Terminates the program.
        break

    #Defines an else statement for any other inputs.
    else:

        #Prints a message to the user that tells them their input was invalid.
        print('Invalid input. Try again.')

        #Terminates the program.
        break

    #Defines an if statement for if the user, after the data is capitalized, has provided 'Yes' as an answer in the start_again variable.
    if start_again.capitalize() == 'Yes':

        #Continues the while loop.
        continue

    #Defines an elif statment for if the user, after the data is capitalized has provided 'No' as an answer in the start_again variable.
    elif start_again.capitalize() == 'No':

        #Prints a goodbye message to the user.
        print('Okay. Goodbye')

        #Terminates the program.
        break

    #Defines an else statement for any other inputs.``
    else:

        #Terminates the program.
        break