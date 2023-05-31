import random

peoples = input("Enter the people to be on the lucky draw")
peoples = peoples.split(",")
#print(peoples)

print(f" {random.choice(peoples)} is the iucky winner")