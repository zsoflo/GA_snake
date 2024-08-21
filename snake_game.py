# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech & Zsofia Hauk & Jonathan Alderson

import turtle
import time
import random
from network import network

use_ai = True
headless = False
no_time_delay = False
ai = network()

score = 0
high_score = 0
delay_reset = 0.0 if no_time_delay else 0.1
delay = delay_reset

# Screen
wn = turtle.Screen()
wn.title("Snake Game by TokyoEdTech, AI by Zsofia and Jonathan")
wn.bgcolor("green")
wn.setup(width = 600, height = 600)
wn.tracer(0) # Turns off the screen updates

if headless:
    turtle.getcanvas().winfo_toplevel().withdraw()

# Snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.dir = "stop"

segments = []

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Movement
def move():
    if head.dir == "up":
        head.sety(head.ycor() + 20)

    if head.dir == "down":
        head.sety(head.ycor() - 20)

    if head.dir == "left":
        head.setx(head.xcor() - 20)

    if head.dir == "right":
        head.setx(head.xcor() + 20)

def go_up():
    head.dir = "up" if (head.dir != "down") else head.dir

def go_down():
    head.dir = "down" if (head.dir != "up") else head.dir

def go_left():
    head.dir = "left" if (head.dir != "right") else head.dir

def go_right():
    head.dir = "right" if (head.dir != "left") else head.dir

wn.listen()
[wn.onkeypress(go_up,    k) for k in ["w", "Up"]]
[wn.onkeypress(go_down,  k) for k in ["s", "Down"]]
[wn.onkeypress(go_left,  k) for k in ["a", "Left"]]
[wn.onkeypress(go_right, k) for k in ["d", "Right"]]

def write(s):
    pen.clear()
    pen.write(s, align = "center", font = ("Courier", 24, "normal"))
    print(s)

def sleep(t):
    if headless or no_time_delay:
        return

    time.sleep(t)

# Main game loop
while True:
    if not headless:
        wn.update()

    collided_wall = (head.xcor() > 290 or head.xcor() < -290 or head.ycor()  > 290 or head.ycor() < -290)
    collided_body = any([segment.distance(head) < 20 for segment in segments])

    if collided_wall or collided_body:
        sleep(1)
        head.goto(0, 0)
        head.dir = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = delay_reset

        write("Score: {}  High Score: {}".format(score, high_score)) 

    # Food
    if head.distance(food) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # Grow
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay = max(0, delay - 0.001)
        score += 10

        if score > high_score:
            high_score = score
        
        write("Score: {}  High Score: {}".format(score, high_score)) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # AI
    if (use_ai):
        ai_move = ai.move(food.pos, segments)
        moves = [go_up, go_down, go_left, go_right]
        for f in moves:
            if moves[ai_move] == f:
                f()
        

    sleep(delay)

wn.mainloop()