heights = [23,34,55,30,22,3,5,122,334,65,77,334,233]
count = 0
sumvalue = 0
for i in heights:
    count +=1
    sumvalue +=i
print(count)

average = round(sumvalue/count)
print(average)