num1 = float(input("input 1st number: "))
op = input("input operator: ")
num2 = float(input("input second number: "))

if(op == "+"):
    print(num1+num2)
elif(op == "-"):
    print(num1-num2)
elif(op == "*"):
    print(num1*num2)
elif(op == "/"):
    print(num1/num2)
else:
    print("invalid")