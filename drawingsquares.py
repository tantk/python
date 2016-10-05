import turtle
def draw_square():
    window= turtle.Screen()
    window.bgcolor("red")

    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    for i in range (0,36):
        for i in range (0,4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)

def draw_circle():
    Tcircle= turtle.Turtle()
    Tcircle.shape("circle")
    Tcircle.color("#2cd1d1")
    Tcircle.circle(100)

def draw_triangle():
    Ttriangle =turtle.Turtle()
    Ttriangle.shape("square")
    Ttriangle.color("#2c50d1")
    for i in range (0,3):
        Ttriangle.forward(100)
        Ttriangle.right(120)

draw_square()
#draw_circle()
#draw_triangle()
