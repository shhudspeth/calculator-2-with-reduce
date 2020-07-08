"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

play = True
while play == True:
    express = input("Please enter your math expression: ")
    num2 = express.split(" ")
    if len(num2) == 1:
        if num2[0] == "q":
            play = False
            print("Thanks for using this program")
        else:
            Print("invalid expression")
    elif len(num2) == 2:
        if num2[0].lower() == "square":
            print(square(num1))
        elif num2[0].lower() == "cube":
            print(cube(num1))
        else:
            print("invalid expression. try again please!")

    elif len(num2) == 3:
        num1 = float(num2[1])
        num2 = float(num2[2])

        if num2[0].startswith('+'):
            print(add(num1, num2))
        elif num2[0].startswith('-'):
            print(subtract(num1, num2))
        elif input_token[0].startswith('*'):
            print(multipy(num1, num2))
        elif input_token[0].startswith('pow'):
            print(pow(num1, num2))
        elif input_token[0].startswith('mod'):
            print(mod(num1, num2))

        else:
            print("invalid expression. try again please")
    else:
        print('Invalid. Please try again.')
print("Thanks for playing with us!")