print("Welcome to the tip calculator")

#totalbill
#percentage of the tip ? 10,12,15
#how many people whant to split the bill


total_bill = float(input("what is the total bill - "))
tip_percentage = int(input("Tip percentage ? 10, 12, 15 - "))
total_people = int(input("Number of total people - "))

total_tips = ((tip_percentage/100) * total_bill) + total_bill
share = float(total_bill/total_people)
print(total_tips)

# TODO: check this code there is some issue

