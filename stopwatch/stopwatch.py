# template for "Stopwatch: The Game"
import simplegui

# define global variables
width = 400
height = 300
center = [width/2, height/2]
tenths_of_second = 0

print tenths_of_second

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_btn_handler():
    pass

def stop_btn_handler():
    pass

def reset_btn_handler():
    pass


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenths_of_second
    
    tenths_of_second += 1
    print tenths_of_second

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(tenths_of_second), (center), 48, 'Red')
    
# create frame
frame = simplegui.create_frame('Stopwatch', width, height, 150)

# register event handlers
start_btn = frame.add_button('Start', start_btn_handler, 150)
stop_btn = frame.add_button('Stop', stop_btn_handler, 150)
reset_btn = frame.add_button('Reset', stop_btn_handler, 150)

timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
