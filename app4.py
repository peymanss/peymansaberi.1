a = float(input("enter your weight(kilogram)"))
b = float(input("enter your height(meter)"))
BMI=a/(b*b)
print("your BMI is" , BMI)
if BMI<=18.5:
    print("you are underweight")
elif 18.5<BMI<24.9:
    print("you are normal")
elif 24.9<BMI<29.9:
    print("you are over weight")
elif 29.9>BMI>35:
    print("you are obese")
elif BMI>=35:
    print("you are extremely obese")