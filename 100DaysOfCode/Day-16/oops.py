#what it has -> Attributes (A variable)

#what it does -> Methods (Function)



#from the class we can create n number of objects
"""
class Car():
    def __int__(self,name):
        self.name = name

hyundai = Car()
hyundai.name = "verna"
print(hyundai.name)

"""

from turtle import Turtle,Screen

dharani = Turtle()
dharani.shape("turtle")
dharani.color("yellow")
print(dharani)

dharani.forward(1000)

myscreen = Screen()
print(myscreen.canvheight)
myscreen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("FamilyName",["Dharani","Gokul","Kalivarathan","Thavamani"])
table.add_column("Member details",["sister","brother","dad","mom"])
table.align = 'r'

print(table)