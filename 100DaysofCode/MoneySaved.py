expense_spent_in_minutes = float(input("Enter the one day expense\n"))/1440
not_spent = float(input("How long you have not spent the amount\n [in hours]"))*60

print(expense_spent_in_minutes)

final_expense = expense_spent_in_minutes * not_spent
print(f"You have saved Rs {final_expense}")