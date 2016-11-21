# implementation of card game - Memory
import simplegui
import random

DECK = range(8) + range(8)
Counter = 0

# helper function to initialize globals
def new_game():
    global Exposed, state, Counter
    
    Counter, state = 0, 0    
    Exposed = [False] * 16
    random.shuffle(DECK)
            
# define event handlers
def mouseclick(pos):
    global Counter, state, Exposed, card1_pos, card2_pos, card1_val, card2_val
    
    # add game state logic here    
    indexPos = pos[0] / 50
            
    if state == 0:
        card1_pos = indexPos
        Exposed[card1_pos]= True
        card1_val = DECK[card1_pos]
        state = 1
        Counter += 1
        print "card1 position, value: %d | %d" %(card1_pos, card1_val)
        print "State:", state, "Counter:", Counter
        print
        
    elif state == 1 and indexPos != card1_pos:
        card2_pos = indexPos
        Exposed[card2_pos]= True
        card2_val = DECK[card2_pos]
        state = 2
        print "card2 position, value: %d | %d" %(card2_pos, card2_val)
        print "State: ", state, " Counter:", Counter
        print
        
            
    else:
        if indexPos != card1_pos and indexPos != card2_pos:
            if card1_val != card2_val:
                Exposed[card1_pos]= False
                Exposed[card2_pos]= False
                card1_pos = indexPos
                Exposed[card1_pos]= True
                card1_val = DECK[card1_pos]
                
            else:
                Exposed[card1_pos]= True
                Exposed[card2_pos]= True
                card1_pos = indexPos
                Exposed[card1_pos]= True
                card1_val = DECK[card1_pos]
                
            state = 1
            Counter += 1
            print "card1 position, value: %d | %d" %(card1_pos, card1_val)
            print "State: ", state, " Counter:", Counter
            print           
        
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global Exposed, Counter
    
    # loop to draw each element of the list DECK
    for num_pos in range(len(DECK)):
        if not Exposed[num_pos]:
            card_pos = 50 * num_pos + 24 # adding 24 to fit the green rectangles
            canvas.draw_line((card_pos, 0), (card_pos, 100), 48, 'green')
        
        else:    
            card_pos = 50 * num_pos + 5 # adding 5 to start drawing justified
            canvas.draw_text(str(DECK[num_pos]), (card_pos, 75), 75, 'Red')
    
    label.set_text("Turns = %d" %Counter)    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 799, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

