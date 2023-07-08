import math
a=int(input("enter the number=="))
print("+ , - , * , /")
print("sin , cos , tan , cot , radical , !")
o=input("Choose one of the operations==")
if o=="+" or o=="-" or o=="*" or o=="/" :
    b=float(input("enter the number=="))
    if o=="+":
        result=a+b
        print(result)
    elif o=="-":
        result=a-b
        print(result)
    elif o=="*":
        result=a*b
        print(result)
    elif o=="/":
        result=a/b
        print(result)
else :
    if o=="sin":
        result=math.sin(math.radians(a))
        print(result)
    elif o=="cos":
        result=math.cos(math.radians(a))
        print(result)
    elif o=="tan":
        result=math.tan(math.radians(a))
        print(result)
    elif o=="cot":
        result=math.cos(math.radians(a))/math.sin(math.radians(a))
        print(result)
    elif o=="radical":
        result=math.sqrt(a)
        print(result)
    elif o=="!":
        result=math.factorial(a)
        print(result)


