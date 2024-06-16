import time

print("WELCOME TO MY PYTHON CALCULATOR!! \n")
time.sleep(1)
print("STARTING PYTHON CALCULATOR!!! \n")
time.sleep(2)

c = "1"

while c == "1":
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor Division")
    print("7. Power")
    print("8. Exit")
    c = input("Enter your choice: ")
    if c == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a + b)
    elif c == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a - b)
    elif c == "3":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a * b)
    elif c == "4":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a / b)
    elif c == "5":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a % b)
    elif c == "6":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a // b)
    elif c == "7":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a ** b)
