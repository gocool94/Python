size = input("Enter the size  'L/M/S' - ") #small->15 #medium->20 #large->25

peporoni = input("To Add peperoni  Y/N ") #small ->2 #medium/large ->3

ExtraCheese = input("Extra Cheese Y/N ")

if(size=='L'):
    amount = 25
elif(size=='M'):
    amount = 20
else:
    amount=15

if((size=='L' or size=='M') and peporoni=='Y'):
    amount+=3
else:
    amount+=2

if(ExtraCheese=='Y'):
    amount+=1

print(f"The Amount of the bill is {amount}")