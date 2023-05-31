from fastapi import FastAPI , Body
from pydantic import BaseModel
from typing import Optional
from datetime import date,datetime


print(date.today())
now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
print(dt_string)

app = FastAPI()

class Expenses:
    Date : str
    Time: str
    purpose :str
    Amount : int
    Necessity : int

    def __init__(self,Date,Time,purpose,Amount,Necessity):
        self.Date = Date
        self.Time = Time
        self.purpose = purpose
        self.Amount = Amount
        self.Necessity = Necessity


Expense_list = [
    Expenses("2023-05-03","11:52:30","BreakFast",1200,"Food"),
Expenses("2023-05-03","11:52:30","Lunch",1400,"Food_break"),
Expenses("2023-05-03","11:52:30","Others",300,"Marriage"),
Expenses("2023-05-03","11:52:30","Dress",44400,"Saree"),

]

@app.get('/Expenses')
async def get_expenses():
    return Expense_list




#TODO: complete the module of fast api and javascript

#TODO: Create a plan for the expense tracker

'''
Expense tracker

1)Date
2)Time
2)What for the amount is being used
3)Amount
4)Neccessity
'''

#TODO2: implemenet on how to save this.
