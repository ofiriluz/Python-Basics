if __name__ == "__main__":
    # All of the arithemtics from other languages exists here
    # The only exception are the ++ and -- operators
    a = 3
    b = 5
    c = a - b - 3
    d = a * b / 5 % 7

    # Besides the well known arithmetic operations
    # Python adds new operators
    e = (a+3)**2 # Power of two
    f = 9.0//2.0 # Floor division, results in 4

    # Boolean operators are simillar aswell
    g = 3 > 5 and 5 == 2 or a != b

    # A few additions to the language
    # The between operator, instead of writing a logical expxression
    # Python evaluates this into an in between the two numbers
    h = 2 <= a <= 5

    # Another addition is the "is" operator
    # This basiclly is simillar to checking the address of an object
    # Or its ID, while == checks for the value, is will check if its the same object
    # Note that on trivial objects, there will always be a copy
    b2 = 5
    i = b == b2 # True
    j = b is b2 # False