"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)

while True:

    calculator_input = input(">>> ")

    tokens = calculator_input.split(" ")

    if tokens[0] == 'q':
        print("You have exited the calculator.")
        break 

    elif tokens[0] == '+':
        print(add(float(tokens[1]), float(tokens[2])))

    elif tokens[0] == '-':
        print(subtract(float(tokens[1]), float(tokens[2])))

    elif tokens[0] == '*':
        print(multiply(float(tokens[1]), float(tokens[2])))

    elif tokens[0] == '/':
        print(divide(float(tokens[1]), float(tokens[2])))

    elif tokens[0] == 'square':
        print(square(float(tokens[1])))

    elif tokens[0] == 'cube':
        print(cube(float(tokens[1])))

    elif tokens[0] == 'pow':
        print(power(float(tokens[1]), float(tokens[2])))

    elif tokens[0] == 'mod':
        print(mod(float(tokens[1]), float(tokens[2])))

    else:
        print("Not recognized. Try again.")