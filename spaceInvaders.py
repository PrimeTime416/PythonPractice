#!/usr/bin/env python3.5
# Space Invaders - Part 1
# Set up the screen
# Python 3 on linux


import turtle
# import os
import sys


print(sys.version)


# Define game parameters
game = {}
game['title'] = "Space Invaders"
game['player_speed'] = 15
game['enemy_speed'] = 2


# Setup screen
# Setup the main game window
window = turtle.Screen()
window.bgcolor("black")
window.title(game['title'])


# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("blue")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


# Creat Player
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = game['player_speed']

# Move Player


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


# Create enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("square")
enemy.penup()
enemy.speed(0)
enemy.setposition(-250, 250)
enemy.setheading(90)


# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


# Main loop
def main():
    while True:
        x = enemy.pos()[0]
        x += game["enemy_speed"]
        enemy.setx(x)
        if enemy.pos()[0] > 250:
            game["enemy_speed"] *= -1

        if enemy.pos()[0] < -250:
            game["enemy_speed"] *= -1


main()

continueDraw = input("hit any key to exit")
