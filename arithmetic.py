"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of the two input integers."""

    return num1 + num2


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2


def multiply(num1, num2):

    """Multiply the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    return float(num1) / num2


def square(num1):
    """Return the square of the input."""

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2

def my_reduce(name_function, sequence_):
    reduce(function, sequence):
    initialize result to function(sequence[0], sequence[1])

    loop over each item in the rest of sequence:
        reassign result to function(result, item)

    return result
    if name_function.startswith('add'):
        # initialize first sequence value
        result = add(sequence_[0], sequence_[1])
        # loop through all the other ones
        for x in range(len(sequence[2:])):
            result = add(result, sequence[x])
        return result

    elif name_function.startswith('subtract'):
                print(subtract(num1, num2))
    elif name_function.startswith('multiply'):
                print(multiply(num1, num2))
    elif name_function.startswith('divide'):
                print(divide(num1, num2))
    elif name_function.startswith('pow'):
                print(pow(num1, num2))
    elif name_function.startswith('mod'):
                print(mod(num1, num2))
    