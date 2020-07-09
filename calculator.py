"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, my_reduce )
from functools import reduce


# Replace this with your code
'''
def return_arit_func(input_token)
     if input_token.startswith('+'):
        return("add"print(add(num1, num2))
    elif input_token[0].startswith('-'):
                print(subtract(num1, num2))
    elif input_token[0].startswith('*'):
                print(multiply(num1, num2))
    elif input_token[0].startswith('/'):
                print(divide(num1, num2))
    elif input_token[0].startswith('pow'):
                print(pow(num1, num2))
    elif input_token[0].startswith('mod'):
                print(mod(num1, num2))
'''

def my_calculator(lines=None):
    # set play to true 
    play = True
    while play == True:
        # input expressions
        express = input("Please enter your math expression: ")
        # split expression into tokens
        input_token = express.split(" ")
        print(input_token)
        
        # cycle through number of tokens
        if len(input_token) == 1:
            if input_token[0].startswith("q"):
                play = False
            else:
                print("invalid expression")

        elif len(input_token) == 2: 
            num1 = float(input_token[1])
            if input_token[0].lower().startswith( "square"):
                print(square(num1))
            elif input_token[0].lower().startswith("cube"):
                print(cube(num1))
            else:
                print("Invalid expression")

        elif len(input_token) == 3:
            num1 = float(input_token[1])
            num2 = float(input_token[2])

            if input_token[0].startswith('+'):
                print(add(num1, num2))
            elif input_token[0].startswith('-'):
                print(subtract(num1, num2))
            elif input_token[0].startswith('*'):
                print(multiply(num1, num2))
            elif input_token[0].startswith('/'):
                print(divide(num1, num2))
            elif input_token[0].startswith('pow'):
                print(pow(num1, num2))
            elif input_token[0].startswith('mod'):
                print(mod(num1, num2))

            else:
                print("invalid expression. try again please")
        else:
            try:
                sequence_list=[]
                for x in input_token[1:]:
                    sequence_list.append(float(x))
                if input_token[0].startswith('+'):
                    print(reduce(add, sequence_list))
                elif input_token[0].startswith('-'):
                        print(reduce(subtract, sequence_list))
                elif input_token[0].startswith('*'):
                        print(reduce(multiply, sequence_list))
                elif input_token[0].startswith('/'):
                        print(reduce(divide, sequence_list))
                elif input_token[0].startswith('pow'):
                        print(reduce(pow, sequence_list))
                elif input_token[0].startswith('mod'):
                        print(reduce(mod, sequence_list))
            except:
                    print("invalid expression. try again please!")

    print("Thanks for calculating with us!")


if __name__ == '__main__':
    calc_file = open("calc.txt")
    my_calculator()