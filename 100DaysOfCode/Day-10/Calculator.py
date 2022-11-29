print("CALCULATOR")

def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

operations = {
    '+':addition,
    '-':subtraction,
    '*':multiply,
    '/':divide
}


num1 = int(input("What's the first number "))
num2 = int(input("What's the second nunber "))

for i in operations:
    print(i)

operation_symbol = input("Whats the above operation")

function = operations[operation_symbol]
answer = function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
