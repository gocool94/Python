#highest score


list1 = input("Enter the numbers").split(",")

max = list1[0]

print(type(max))

for i in list1:
    if i>max:
        max = i

print(max)