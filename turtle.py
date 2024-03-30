import turtle
import random
s=turtle.getscreen()
s.title("My turtle program")
s.bgcolor("yellow")
t=turtle.Turtle()
"""

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.goto(100,100)
"""
#t.goto(100,100)
#t.home()
"""
t.fd(100)
t.rt(90)
t.fd(70)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(70)
"""
#t.circle(100)
#t.dot(100)
"""
t.shapesize(1,5,10)
t.shapesize(10,5,1)
t.shapesize(1,10,5)
t.shapesize(10,1,5)
"""
#t.pensize(5)
#t.goto(100,100)
"""
t.shapesize(3,3,3)
t.pensize(5)
t.fillcolor("red")
t.pencolor("blue")
t.goto(100,100)
"""
#t.color("red","blue")
#t.goto(100,100)
"""
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()
"""
"""
t.shape("turtle")
t.shape("arrow")
t.shape("circle")
"""
"""
t.speed(1)
t.forward(100)
t.rt(90)
t.speed(10)
t.forward(100)
"""
"""
t.pencolor("purple")
t.fillcolor("orange")
t.pensize(5)
t.speed(3)
t.begin_fill()
t.circle(90)
t.end_fill()
"""
"""
t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()
"""
"""
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()
"""
#t.undo()
#t.clear()
#t.reset()
"""
t.stamp()
t.fd(100)
t.stamp()
t.fd(100)
t.clearstamp(8)
"""
"""
for i in range(4):
    t.fd(100)
    t.rt(90)
"""
"""
n=10
while n <= 100:
    t.circle(n)
    n = n+10

"""
"""
u = input("Would you like me to draw a shape? Type yes or no: ")
if u == "yes":
    t.circle(50)
else:
    print("fuck you")
"""
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)

player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

die = [1,2,3,4,5,6]

for i in range(20):
    if player_one.pos() >= (300,100):
            print("Player One Wins!")
            break
    elif player_two.pos() >= (300,-100):
             print("Player Two Wins!")
             break
    else:
            player_one_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20*die_outcome)
            player_one.fd(20*die_outcome)
            player_two_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20*die_outcome)
            player_two.fd(20*die_outcome)