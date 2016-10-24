# Implementation of classic arcade game Pong
import simplegui, random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 15
PAD_WIDTH, PAD_HEIGHT = 8, 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT, RIGHT = False, True
acc = 10

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos, ball_vel  = [WIDTH / 2, HEIGHT /2], [0, 0]

    if direction:
        ball_vel[0] = random.randrange(120.0 / 60, 240.0 / 60)
        ball_vel[1] = -random.randrange(60.0 / 60, 180.0 / 60)
    else:
        ball_vel[0] = -random.randrange(120.0 / 60, 240.0 / 60)
        ball_vel[1] = -random.randrange(60.0 / 60, 180.0 / 60)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2 # these are ints
    score1, score2 = 0, 0
    paddle1_vel, paddle2_vel = 0, 0
    paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    spawn_ball(random.choice([RIGHT, LEFT]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    up = acc + 1
    down = PAD_HEIGHT - up
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # expression to bounce off top and bottom
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'Blue', 'White')

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel

    if paddle1_pos + paddle1_vel <= -up or paddle1_pos + paddle1_vel >= HEIGHT - down:
        paddle1_pos -= paddle1_vel

    if paddle2_pos + paddle2_vel <= -up or paddle2_pos + paddle2_vel >= HEIGHT - down:
        paddle2_pos -= paddle2_vel

    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos],
                     [HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT],
                     PAD_WIDTH, 'Blue')

    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos],
                     [WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT],
                     PAD_WIDTH, 'Blue')

    # determine whether paddle and ball collide & determine if ball scores
    # Left Paddle
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[0] = -ball_vel[0]
            # print ball_vel
        else:
            score2 += 1
            spawn_ball(RIGHT)
    # Right Paddle
    if ball_pos[0] >= WIDTH - (BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[0] = -ball_vel[0]
        else:
            score1 += 1
            spawn_ball(LEFT)

    # draw scores
    canvas.draw_text(str(score1), [240, 50], 40, 'Blue')
    canvas.draw_text(str(score2), [340, 50], 40, 'Blue')

def keydown(key):
    global paddle1_vel, paddle2_vel

    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc

    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc

def keyup(key):
    global paddle1_vel, paddle2_vel

    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel += acc

    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel -= acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += acc

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT, 150)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 150)

# start frame
new_game()
frame.start()
