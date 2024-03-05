from art import logo
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def calculator():
    print(logo)
    operation = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    n1 = int(input("Enter the num1 value: "))
    for symbol in operation:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol = input("Pick the operation: ")
        n2 = int(input("Enter the next value: "))
        calculation_function=operation[operation_symbol]
        answer=calculation_function(n1,n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        if input(f"type 'y' if you want to continue the calculation\ntype 'n' to start new calculation\n")=='y':
            num1=answer
        else:
            should_continue=False
            calculator()

calculator()
#select_operation = int(input("Enter the operation:\npress 1 for add\npress 2 for subtraction\npress 3 for multiplication\npress 4 for division\n"))


