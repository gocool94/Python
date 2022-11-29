import random

print(" Enter to the world of Guessing Game ")

number = random.randint(1,101)

Level = input("Check for the level -  hard/easy").lower()
life = 0

if(Level == 'hard'):
    life+=5
elif(Level == 'easy'):
    life+=10

def numbercheck(input_number):
    if(input_number==number):
        print("You got the number")
        return True
    elif(input_number<number):
        print("Too low")
        return False
    elif(input_number>number):
        print("too high")
        return False


for i in range(0,life):
    checker = numbercheck(input_number=int(input("Enter the number to be checked")))
    if(checker==False):
        life = life-1
        print(f"You have only {life}")
    elif(checker==True):
        print("You got the correct answer")
        break

else:
    print(f"the number is {number}")





