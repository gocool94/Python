height = float(input("Enter the height"))
weight = int(input("Enter the weight"))

bmi = weight /height ** 2

bmi_rounded = round(bmi)

if bmi_rounded < 18.5:
    print(f"Your BMI is {bmi_rounded}, you are underweight >:)")
elif bmi_rounded < 25:
    print(f"Your BMI is {bmi_rounded}, your weight is normal")
elif bmi_rounded < 30:
    print(f"Your BMI is {bmi_rounded}, you are overweight")
elif bmi_rounded < 35 :
    print(f"Your BMI is {bmi_rounded}, you are obese")
else:
    print(f"Your BMI is {bmi_rounded}, you are clinically obese")