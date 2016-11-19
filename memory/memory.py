# implementation of card game - Memory

import simplegui
import random

DECK = range(8) + range(8)
Exposed = [False] * 16 
print type(Exposed)

# helper function to initialize globals
def new_game():
    global DECK
    
    random.shuffle(DECK)
    
    for num in DECK:
        print num
            
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global Exposed
    
    # loop to draw ever element of the list DECK
    
    for num_pos in range(len(DECK)):
        if not Exposed[num_pos]:
            card_pos = 50 * num_pos -1 # minus 1 to fit
            canvas.draw_line((card_pos, 0), (card_pos, 100), 2, 'green')
        
        else:    
            card_pos = 50 * num_pos + 5 # adding 5 to start drawing justified
            canvas.draw_text(str(DECK[num_pos]), (card_pos, 75), 75, 'Red')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 797, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
