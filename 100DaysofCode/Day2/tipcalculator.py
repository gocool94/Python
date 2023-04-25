print("Welcome to tip calculator")

bill = float(input("What is the total bill..\n"))
tip_percentage = int(input("Enter the percentage of bill you wanted to share..(10/12/15)\n"))
people = int(input("How many ppl to split the bill"))

tip_percentage = tip_percentage/100
total_tips = bill * tip_percentage
final_bill = round((total_tips + bill)/people,2)

print(f"Each one should pay {final_bill}")
