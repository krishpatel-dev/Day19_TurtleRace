from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def sharp_left():
    tim.left(90)

def sharp_right():
    tim.right(90)

def clear():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(sharp_left, "Left")
screen.onkey(sharp_right, "Right")
screen.onkey(clear, "c")
screen.exitonclick()