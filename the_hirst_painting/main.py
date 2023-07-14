import turtle as turtle_momdule
from turtle import Screen
import random
tim = turtle_momdule.Turtle()
turtle_momdule.colormode(255)

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 
174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]


tim.speed(20)
tim.penup()
tim.hideturtle()
tim.goto(-200, -200)
tim.pendown()

'''If desired, we can draw our dots using three separate functions, the long way.'''

# tim.pensize(10)

# def horizontal_motion():
#     for _ in range(0, 10):
#         random_color()
#         tim.circle(5)
#         tim.penup()
#         tim.forward(50)
#         tim.pendown()
        
# def vertical_motion():
#     tim.left(90)
#     tim.forward(50)
#     tim.pendown()
#     tim.right(90)

# def random_color():
#     color = random.choice(color_list)
#     tim.color(color)
    
# for _ in range(0, 10):
#     horizontal_motion()
#     tim.penup()
#     tim.backward(500)
#     vertical_motion()

'''Alternatively, we can draw our dots using the shortcut method.'''

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()