# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions
def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        return "Please insert one of the five choices"
    return number

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        return "Please insert a number between 0 and 4"
    return name

def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print

    # print out the message for the player's choice
    print "Player chooses %s" %player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_num = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print "Computer chooses", comp_choice

    # compute difference of comp_number and player_number modulo five
    result = (comp_number - player_num)  % 5

    # use if/elif/else to determine winner, print winner message
    if result == 1 or result == 2:
        print "Computer Wins!!!"
    elif result == 3 or result == 4:
        print "Player Wins!!"
    else:
        print "It's a TIE!!!"

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
# always remember to check your completed program against the grading rubric
