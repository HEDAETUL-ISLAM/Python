def raise_to_power(base_number,power_number):
    result=1
    for i in range(power_number):
        result = result*base_number
    return result

num1 = int(input("enter 1st one: "))
num2 = int(input("enter 2nd one: "))
print(raise_to_power(num1,num2))