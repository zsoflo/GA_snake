# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech & Zsofia Hauk & Jonathan Alderson

import turtle
import time
import random
from network import network

# AI
use_ai = True
headless = False
ai = network()

delay_reset = 0.1
delay = delay_reset

# Score
score = 0
high_score = 0

# Set up the screen
if not headless:
    wn = turtle.Screen()
    wn.title("Snake Game by TokyoEdTech, AI by Zsofia and Jonathan")
    wn.bgcolor("green")
    wn.setup(width = 600, height = 600)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.dir = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

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

if not headless:
    wn.listen()
    [wn.onkeypress(go_up,    k) for k in ["w", "Up"]]
    [wn.onkeypress(go_down,  k) for k in ["s", "Down"]]
    [wn.onkeypress(go_left,  k) for k in ["a", "Left"]]
    [wn.onkeypress(go_right, k) for k in ["d", "Right"]]

# Main game loop
while True:
    if not headless:
        wn.update()

    collided_wall = (head.xcor() > 290 or head.xcor() < -290 or head.ycor()  > 290 or head.ycor() < -290)
    collided_body = any([segment.distance(head) < 20 for segment in segments])

    if collided_wall or collided_body:
        # Reset
        time.sleep(1)
        head.goto(0, 0)
        head.dir = "stop"
        score = 0
        delay = delay_reset

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal")) 

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

        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
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

    time.sleep(delay)

wn.mainloop()