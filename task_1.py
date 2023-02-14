def recursive_calc():
    operation = input("Enter operation: ")
    if operation == "0":
        return "Program end!"
    elif operation in ["+", "-", "*", "/"]:
        try:
            operand_1 = int(input("Enter first operand: "))
        except ValueError:
            print("Incorrect number!")
            return recursive_calc()
        try:
            operand_2 = int(input("Enter second operand: "))
        except ValueError:
            print("Incorrect number!")
            return recursive_calc()
    else:
        print("Incorrect operation!")
        return recursive_calc()
    if operation == "+":
        print(operand_1 + operand_2)
        return recursive_calc()
    elif operation == "-":
        print(operand_1 - operand_2)
        return recursive_calc()
    elif operation == "*":
        print(operand_1 * operand_2)
        return recursive_calc()
    elif operation == "/":
        try:
            if operand_2:
                print(operand_1 / operand_2)
                return recursive_calc()
            else:
                raise ValueError
        except ValueError:
            print("Division by zero!")
            return recursive_calc()


print(recursive_calc())
