from turtle import *
from random import randrange
from freegames import square, vector
from tkinter import messagebox

snake = [vector(10, 0)]
food = vector(0, 0)
aim = vector(0, -10)

# New variables for head dots and border color
head_dots = 2  # Number of dots at the head
border_color = 'gray'  # Border color

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        messagebox.showinfo("You lost")
        return()

    snake.append(head)

    if head == food:
        print('snake', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)

    clear()

    # Draw border
    square(-210, -210, 420, border_color)

    for body in snake:
        square(body.x, body.y, 9, 'green')

    # Draw dots at the head
    for i in range(head_dots):
        dot_size = 9 - i * 2  # Decreasing dot size
        square(head.x, head.y + (i * dot_size), dot_size, 'white')

    square(food.x, food.y, 9, 'blue')
    update()
    ontimer(move, 100)

hideturtle()
tracer(False)
listen()
onkey(lambda: change(0, 10), "Up")
onkey(lambda: change(0, -10), "Down")
onkey(lambda: change(10, 0), "Right")
onkey(lambda: change(-10, 0), "Left")

move()
done()
