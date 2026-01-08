import turtle
turtle.Screen()
turtle.Screen().bgcolor("aquamarine")
turtle.Turtle().color("navy")
polygon = turtle.Turtle()
num_sides = 15
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()















turtle.mainloop()