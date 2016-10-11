# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui, random

rem_guess = 7
secret_num = random.randrange(0, 100)
range100 = True

print "================================"
print
print "STARTING GAME FOR FIRST TIME"

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_num, rem_guess, range100
    print
    if range100:
        rem_guess = 7
        print "Enter a number between 0 and 99"
        print "You have 7 oportunities"
        print
    else:
        rem_guess = 10
        print "Enter a number between 0 and 999"
        print "You have 10 oportunities"
        print
        
# define event handlers for control panel
def range100():
    global secret_num, rem_guess, range100
    # button that changes the range to [0,100) and starts a new game 
    rem_guess = 7
    secret_num = random.randrange(0, 100)
    range100 = True
    print 'Range is [0,100)'
    new_game()
    
def range1000():
    global secret_num, rem_guess, range100
    # button that changes the range to [0,1000) and starts a new game     
    rem_guess = 10
    secret_num = random.randrange(0, 1000)
    range100 = False
    print 'Range is [0,1000)'
    new_game()
    
def input_guess(guess):
    global secret_num, rem_guess
    # main game logic goes here	
    guess = int(guess)
    print
    print "Your Guess was", guess
    print
    
    if guess > secret_num:
        rem_guess -= 1
        print "Number you are looking for is Lower than", guess
        print
        print rem_guess, "guesses remaining"
        print "-----------------------------"
        if rem_guess == 0:
            print "GAME OVER"
            print "---------"
            print
            print "RE-STARTING GAME"
            new_game()
            
    elif guess < secret_num:
        rem_guess -= 1
        print "Number you are looking for is Higher than", guess
        print
        print rem_guess, "guesses remaining"
        print "-----------------------------"
        if rem_guess == 0:
            print "GAME OVER"
            print "---------"
            print
            print "RE-STARTING GAME"
            new_game()
    else:
        print "Correct, you are Great!!"
        print "-----------------------------"
        print
        print "RE-STARTING GAME"
        new_game()
    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200, 200)

# register event handlers for control elements and start frame
inp = frame.add_input('Enter the number here', input_guess, 200)
button100 = frame.add_button('Range is [0,100)', range100, 150)
button1000 = frame.add_button('Range is [0,1000)', range1000, 150)
frame.start()

# call new_game 
new_game()
print "================================="

# always remember to check your completed program against the grading rubric

# logic to resolve the number of guesses youj need to guess a number
# guesses_left = int(math.ceil(math.log(upper)/math.log(2)
