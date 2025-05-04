operator = input("enter your operation : ")

num1 = float(input("first num: "))
num2 = float(input("second num: "))

if operator == "+" :
    result = num1 + num2
    print(result)
elif operator == "-" :
    result = num2 - num1
    print(result)
elif operator == "*" :
    result = num1 * num2
    print(result)
else :
    result = num2 / num1
    print(result)