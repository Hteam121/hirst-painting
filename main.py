import colorgram
import turtle as turtle_module
import random

colors = colorgram.extract("image.jpeg", 100)

listColor = []

for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    color = (r, g, b)
    if r > 50 and g < 150 and b > 50:
        listColor.append(color)

print(listColor)

t = turtle_module.Turtle()
s = turtle_module.Screen()

turtle_module.colormode(255)

distance = 30

for i in range(10):
    for j in range(10):
        t.dot(20, random.choice(listColor))
        t.penup()
        t.forward(distance)
        t.pendown()

    t.dot(20, random.choice(listColor))
    if i % 2 == 0:
        t.penup()
        t.right(90)
        t.forward(distance)
        t.pendown()
        t.right(90)
    else:
        t.penup()
        t.left(90)
        t.forward(distance)
        t.pendown()
        t.left(90)


s.exitonclick()
