# template for "Stopwatch: The Game"
import simplegui

# define global variables
Running = False
Width, Height  = 400, 300 
Center = [Width/3, Height/2]
Time, Counter, Wins = 0, 0, 0
Game_over = "GAME OVER"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global Tenths_of_sec
    
    Minutes = t // 600
    Tens = t // 10 % 60 // 10
    Seconds= t // 10 % 60 % 10
    Tenths_of_sec = t % 10 
    Message = str(Minutes) + ":" + str(Tens) + str(Seconds) + "." + str(Tenths_of_sec)
    return Message   

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_btn_handler():
    global Running
    
    Running = True
    timer.start()

def stop_btn_handler():
    global Running, Wins, Counter
    
    if Running and str(Tenths_of_sec) == "0":
        Wins += 1
    elif Running and str(Tenths_of_sec) != "0":
        Counter += 1
        Running = False    
    timer.stop()

def reset_btn_handler():
    global Time, Wins, Counter
    
    Time, Wins, Counter = 0 ,0, 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global Time, Running
    
    print Time
    Time += 1
    if Time == 6000:
        Running = False
        timer.stop()
        print "Game Over", "You made " + str(Wins) + "clicks on time of " + str(Counter) + "times" 
        
# define draw handler
def draw_handler(canvas):    
    canvas.draw_text(format(Time), (Center), 50, 'Red')
    canvas.draw_text("Good - Bad", (265, 40), 28, "Lime")
    canvas.draw_text(str(Wins) + "/" + str(Counter), (310, 80), 40, "Red")
    if Time == 6000:
        canvas.draw_text(Game_over, (65, 220), 50, 'White')
        canvas.draw_text("You made " + str(Wins) + " clicks correctly of " + str(Counter) + " times" , (60, 270), 20, 'White')
           
# create frame
frame = simplegui.create_frame('Stopwatch', Width, Height, 150)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
start_btn = frame.add_button('Start', start_btn_handler, 150)
stop_btn = frame.add_button('Stop', stop_btn_handler, 150)
reset_btn = frame.add_button('Reset', reset_btn_handler, 150)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
print Time
