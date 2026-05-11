num_1 = float(input("Enter number 1 = "))
num_2 = float(input("Enter number 2 = "))


choice = input("Enter  your  choice + - *  =")

if choice == "+":
    print(f"Addition : {num_1 + num_2}")

elif choice =="-":
    print(f"Subtracting : {num_1 - num_2}")

elif choice == "*":
    print(f"Multiplication : {num_1 * num_2}")

else:
    print("invalid choice")