from art import logo

print(logo)


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


# how cool is this!
# for key in operations:
# print(f"The result of {num1} {key} {num2} is {operations[key](num1, num2)}")


def calculator():
    num1 = float(input("What's the first number? "))

    loop_inputs = True

    while loop_inputs:
        print("Possible operations:")
        for key in operations:
            print(key)

        operation_choice = input("Your choice: ")
        while operation_choice != "+" and operation_choice != "-" and operation_choice != "*" and operation_choice != "/":
            operation_choice = input("Incorrect, try again: ")

        num2 = float(input("What's the next number? "))

        operation_function = operations[operation_choice]
        # WOW!
        operation_result = operation_function(num1, num2)

        print(
            f"The result of {num1} {operation_choice} {num2} is {operation_result}"
        )
        choice = int(input("type 1 to continue of 0 to exit: "))
        while choice != 0 and choice != 1:
            choice = input("cmon, man...")
        loop_inputs = bool(choice)
        if loop_inputs:
            num1 = operation_result
            print(f"continuing to calculate with {num1}...")
        else:
            calculator()


calculator()
