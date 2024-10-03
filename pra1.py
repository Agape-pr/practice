try:
    num1 = int(input("enter the first number"))
    num2 = int(input("enter the second number"))
    result = num1 / num2

    if num2 == 0 :
        raise ZeroDivisionError
    else:
        print(f"the results = {result}")
except ZeroDivisionError:
    print("you can not divide with zero")
    