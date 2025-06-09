def calculator():
    print("Choose a number to perform a calculation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")

calculator()

option = input("Choose an option: ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if option == "1":
    print(f"The result is: {num1 + num2}")
elif option == "2":
    print(f"The result is: {num1 - num2}")
elif option == "3":
    print(f"The result is: {num1 * num2}")
elif option == "4":
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Invalid result, choose a divisor greater than 0")
else:
    print("Invalid option.")


