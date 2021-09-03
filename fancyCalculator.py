# fancy calculator by @rahimi
# fancy because using function, while/for loops, dictionary and list. Basically all basic syntax in one program.

def addition(num_one, num_two):
    return f"Total = {num_one + num_two}"


def subtraction(num_one, num_two):
    return f"Total = {num_one - num_two}"


def multiplication(num_one, num_two):
    return f"Total = {num_one * num_two}"


def division(num_one, num_two):
    return f"Total = {num_one / num_two}"


def remainder(num_one, num_two):
    return f"Total = {num_one % num_two}"


# menu dictionary so that we can add more function in our calculator later.
menu = {1 : addition, 2 : subtraction, 3 : multiplication, 4 : division, 5 : remainder} # if put (), it will automatically be call
operator = ['+', '-', '*', '/', '%']

# main loop
while True:
    print("Enter two numbers")
    num_one = int(input("> "))
    num_two = int(input("> "))

    print("Select operator")
    for index, operation in enumerate(operator, start=1):
        print(f"{index}: {operation}")

    operation = input("> ")
    if operation == '1' or operation == '+':
        print(menu[1](num_one, num_two))

    elif operation == '2' or operation == '-':
        print(menu[2](num_one, num_two))

    elif operation == '3' or operation == '*':
        print(menu[3](num_one, num_two))

    elif operation == '4' or operation == '/':
        print(menu[4](num_one, num_two))

    elif operation == '5' or operation == '%':
        print(menu[5](num_one, num_two))

    print("Press 'x' to quit ")
    press_X = input().lower()
    if press_X == 'x':
        print("Terminating calculator.")
        break

