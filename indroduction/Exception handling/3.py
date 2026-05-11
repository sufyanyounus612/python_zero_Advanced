try:
    num1 = int(input("enter number 1"))
    num2 =int(input("enter number 2"))

    try:
        result =num1/num2
        print(f"result:{result}")
    except ZeroDivisionError:
        print("You cannot divide with zero")
except ValueError:
    print("You must provide a valid input")