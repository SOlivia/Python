import turtle

def draw_side(obj):
     for x in range(0, 4):  
        obj.forward(100)
        obj.right(90)

def draw_graphic():
    window = turtle.Screen()
    window.bgcolor("orange")

    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("red","black")
    draw_side(brad) 
   
    angie = turtle.Turtle()
    angie.color("blue")
    angie.circle(100)

    olivia = turtle.Turtle()
    olivia.shape("triangle")
    olivia.color("yellow")
    olivia.backward(150)
    olivia.right(45)
    olivia.forward(100)
    olivia.left(90)
    olivia.forward(100)
       
    window.exitonclick()

draw_graphic()
