import math
input("first name")
input("last name")
a = float(input("math"))
b = float(input("chemistry"))
c= float(input("physic"))
GPA = (a+b+c)/3
print("your GPA is" , GPA)
if GPA>=17:
    print("great")
elif 17>GPA>12:
    print("normal")
elif GPA<=12:
    print("fail")