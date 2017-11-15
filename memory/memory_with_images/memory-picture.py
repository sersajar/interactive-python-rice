# implementation of card game - Memory

import simplegui
import random
import math

deck = range(8)
deck.extend(deck)
random.shuffle(deck)
exposed = range(len(deck)) 
card1=[]
Card1=[]
card2=[]
Card2=[]
Ta = 0
msg = 'Turns = '+str(Ta)

def init():
    global exposed, Ta
    for bul in range(len(deck)):
        exposed[bul] = False
        Ta=0

PHOTO = [simplegui.load_image('https://vignette.wikia.nocookie.net/rickandmorty/images/1/19/Pickle_rick_transparent.png/revision/latest?cb=20171025014216'),
         simplegui.load_image('https://vignette4.wikia.nocookie.net/sml/images/c/c7/Minion_Bob_The_New_Character.png/revision/latest?cb=20170529223951'),
         simplegui.load_image('https://vignette.wikia.nocookie.net/family-guy-the-quest-for-stuff/images/e/ec/Facespace_portrait_petergriffin_tweaker_default_V2%404x.png/revision/latest?cb=20140420142532'),
         simplegui.load_image('https://static.giantbomb.com/uploads/original/10/103881/1775335-pinky.gif'),
         simplegui.load_image('https://vignette.wikia.nocookie.net/renandstimpy/images/6/6a/Stimpy_J._Cat.png/revision/latest?cb=20131201162628'),
         simplegui.load_image('http://vignette3.wikia.nocookie.net/southpark/images/f/f8/Mr._Hankey_transparent.PNG/revision/latest?cb=20161105035353'),
         simplegui.load_image('http://pixel.nymag.com/imgs/daily/vulture/2015/07/21/21-raphael-bob-waksberg-chatroom-silo.w190.h190.2x.png'),
         simplegui.load_image('https://freemobileapk.com/wp-content/uploads/2014/09/br_cromos_farts.png')]
CARD = simplegui.load_image('https://cdn.shopify.com/s/files/1/0200/7616/products/playing-cards-tally-ho-fan-back-1_grande.png?v=1474345247')

# helper function to initialize globals
def new_game():
    global state, exposed,card1, Card1, card2, Card2
    state = 0
    init()
    card1=[]
    Card1=[]
    card2=[]
    Card2=[]
    Ta = 0
    random.shuffle(deck)
    msg = 'Turns = '+str(Ta)
    label.set_text(msg)
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,card1,card2,Card1,Card2,Ta
    d = list(pos)
    p = d[0]//100
    f = d[1]//200
    if not exposed[p+f*4] and state==0:
        state = 1
        Ta +=1
        msg = 'Turns = '+str(Ta)
        label.set_text(msg)
        card1.append(deck[p+f*4])
        Card1.append(p+f*4)
        exposed[p+f*4] = True
    elif not exposed[p+f*4] and state==1:
        state = 2
        card2.append(deck[p+f*4])
        Card2.append(p+f*4)
        exposed[p+f*4] = True
    elif not exposed[p+f*4] and state==2:
        state = 1
        Ta += 1
        msg = 'Turns = '+str(Ta)
        label.set_text(msg)
        if card1 != card2:
            exposed[Card1[0]] = False
            exposed[Card2[0]] = False
            card1[0] = deck[p+f*4]
            Card1[0] = p+f*4
            card2=[]
            Card2=[]
        else:
            card1[0] = deck[p+f*4]
            Card1[0] = p+f*4
            card2=[]
            Card2=[]  
        exposed[p+f*4] = True
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    x = deck[0:4] 
    for card in range(4):
        canvas.draw_image(PHOTO[x[card]],[PHOTO[x[card]].get_width()/2,PHOTO[x[card]].get_height()/2],
                          [PHOTO[x[card]].get_width(),PHOTO[x[card]].get_height()],
                          [49+card*100,105],[100,200])
    y = deck[4:8] 
    for card in range(4):
        canvas.draw_image(PHOTO[y[card]],[PHOTO[y[card]].get_width()/2,PHOTO[y[card]].get_height()/2],
                          [PHOTO[y[card]].get_width(),PHOTO[y[card]].get_height()],
                          [49+card*100,305],[100,200])  
    z = deck[8:12] 
    for card in range(4):
        canvas.draw_image(PHOTO[z[card]],[PHOTO[z[card]].get_width()/2,PHOTO[z[card]].get_height()/2],
                          [PHOTO[z[card]].get_width(),PHOTO[z[card]].get_height()],
                          [49+card*100,505],[100,200])
    q = deck[12:] 
    for card in range(4):
        canvas.draw_image(PHOTO[q[card]],[PHOTO[q[card]].get_width()/2,PHOTO[q[card]].get_height()/2],
                          [PHOTO[q[card]].get_width(),PHOTO[q[card]].get_height()],
                          [49+card*100,705],[100,200])
    for bul in range(4):
        if not exposed[bul]:
            canvas.draw_image(CARD,[CARD.get_width()/2,CARD.get_height()/2],
                                  [CARD.get_width(),CARD.get_height()],[50+bul*100, 100],[99,210])
    for bul in range(4):
        if not exposed[bul+4]:
            canvas.draw_image(CARD,[CARD.get_width()/2,CARD.get_height()/2],
                                  [CARD.get_width(),CARD.get_height()],[50+bul*100, 300],[99,210])
    for bul in range(4):
        if not exposed[bul+8]:
            canvas.draw_image(CARD,[CARD.get_width()/2,CARD.get_height()/2],
                                  [CARD.get_width(),CARD.get_height()],[50+bul*100, 500],[99,210])
    for bul in range(4):
        if not exposed[bul+12]:
            canvas.draw_image(CARD,[CARD.get_width()/2,CARD.get_height()/2],
                                  [CARD.get_width(),CARD.get_height()],[50+bul*100, 700],[99,210])

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", (len(deck)/4)*100, (len(deck)/4)*200)
frame.add_button("Reset", new_game)
label = frame.add_label(msg)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

init()
# get things rolling
new_game()
frame.start()

