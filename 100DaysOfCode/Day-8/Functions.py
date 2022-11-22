def functions():
    return "gokul"

print(functions())

#functions with inputs
def greet(name,place,animal):
    print(name)
    print(place)
    print(animal)
greet("gokul","avadi","Dharani")

#function with keyword argument
def greet(name):
    print(name)

greet(name="Gokul")