"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

play = True
while play == True:
    express = input("Please enter your math expression: ")
    input_token = express.split(" ")
    if len(input_token) == 1:
        if input_token[0] == "q":
            play = False
        else:
            Print("invalid expression")

    elif len(input_token) == 2:
        num1 = float(input_token[1])
        if input_token[0].lower() == "square":
            print(square(num1))
        elif input_token[0].lower() == "cube":
            print(cube(num1))
        else:
            print("invalid expression. try again please!")

    elif len(input_token) == 3:
        num1 = float(input_token[1])
        num2 = float(input_token[2])

        if input_token[0].startswith('+'):
            print(add(num1, num2))
        elif input_token[0].startswith('-'):
            print(subtract(num1, num2))
        elif input_token[0].startswith('*'):
            print(multiply(num1, num2))
        elif input_token[0].startswith('pow'):
            print(pow(num1, num2))
        elif input_token[0].startswith('mod'):
            print(mod(num1, num2))

        else:
            print("invalid expression. try again please")
    else:
        print('Invalid. Please try again.')
print("Thanks for playing with us!")