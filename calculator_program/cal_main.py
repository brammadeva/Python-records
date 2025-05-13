# main.py
from Calculator import basic, prog, scientific, trignometric

def main_menu():
    while True:
        print("\n=== MATH OPERATIONS MENU ===")
        print("1. Basic Arithmetic (+, -, *, /)")
        print("2. Bitwise Operations (&, |, ~, <<, >>)")
        print("3. Advanced Math (^, sqrt, !, log)")
        print("4. Trigonometry Functions (sin, cos, tan, cot, sec, cosec)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            basic_math_menu()
        elif choice == "2":
            bitwise_math_menu()
        elif choice == "3":
            advanced_math_menu()
        elif choice == "4":
            trigonometry_math_menu()
        elif choice == "5":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice! Try again.")

def basic_math_menu():
    operation = input("Choose an operation (+, -, *, /): ")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if operation == "+":
        print(f"Result: {basic.add(x, y)}")
    elif operation == "-":
        print(f"Result: {basic.sub(x, y)}")
    elif operation == "*":
        print(f"Result: {basic.mul(x, y)}")
    elif operation == "/":
        print(f"Result: {basic.div(x, y)}")
    else:
        print("Invalid operation!")

def bitwise_math_menu():
    operation = input("Choose an operation (&, |, ~, <<, >>): ")
    a = int(input("Enter first number: "))
    
    if operation in ["<<", ">>", "&", "|"]:
        b = int(input("Enter second number: "))

    if operation == "&":
        print(f"Result: {prog.AND(a, b)}")
    elif operation == "|":
        print(f"Result: {prog.OR(a, b)}")
    elif operation == "<<":
        print(f"Left Shift: {prog.left_shift(a, b)}")
    elif operation == ">>":
        print(f"Right Shift: {prog.right_shift(a, b)}")
    elif operation == "~":
        print(f"NOT Operation: {prog.NOT(a)}")
    elif operation == "bin":
        print(f"Binary: {prog.binary(a)}")
    elif operation == "hex":
        print(f"Hexadecimal: {prog.hexadecimal(a)}")
    elif operation == "oct":
        print(f"Octal: {prog.octal(a)}")
    else:
        print("Invalid operation!")

def advanced_math_menu():
    operation = input("Choose an operation (^, sqrt, !, log): ")
    x = float(input("Enter a number: "))

    if operation == "^":
        y = float(input("Enter exponent value: "))
        print(f"Result: {scientific.power(x, y)}")
    elif operation == "sqrt":
        print(f"Result: {scientific.square_root(x)}")
    elif operation == "!":
        print(f"Result: {scientific.fact(int(x))}")
    elif operation == "log":
        print(f"Result: {scientific.log(x)}")
    else:
        print("Invalid operation!")

def trigonometry_math_menu():
    operation = input("Choose an operation (sin, cos, tan, cot, sec, cosec): ")
    angle = float(input("Enter an angle (in radians): "))

    if operation == "sin":
        print(f"Result: {trignometric.sin(angle)}")
    elif operation == "cos":
        print(f"Result: {trignometric.cos(angle)}")
    elif operation == "tan":
        print(f"Result: {trignometric.tan(angle)}")
    elif operation == "cot":
        print(f"Result: {trignometric.cot(angle)}")
    elif operation == "sec":
        print(f"Result: {trignometric.sec(angle)}")
    elif operation == "cosec":
        print(f"Result: {trignometric.cosec(angle)}")
    else:
        print("Invalid operation!")

main_menu()