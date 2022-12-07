from turtle import Turtle , Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("black", "red")
s = int(input("Enter the length of the side of the Square: "))

timmy.forward(s)  # Forward turtle by s units
timmy.left(90)  # Turn turtle by 90 degree

# drawing second side
timmy.forward(s)  # Forward turtle by s units
timmy.left(90)  # Turn turtle by 90 degree

# drawing third side
timmy.forward(s)  # Forward turtle by s units
timmy.left(90)  # Turn turtle by 90 degree

# drawing fourth side
timmy.forward(s)  # Forward turtle by s units
timmy.left(90)







#screen = Screen()
#screen.exitonclick()