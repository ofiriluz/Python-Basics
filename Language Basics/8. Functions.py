# A simple function is defined with the def keyword
# It can receive any arbitrary types and return any amount of types
def a(x,y):
    return x ** y

def b(z,w):
    return z + w

def c(a,b):
    return a+5, b+2

# The pass identifier will ignore doing anything on a block
# This will let the interpeter run and this acts as a stub implementation
def func_with_default(a,b,c,d=5,e=3,f=5):
    pass

def func_with_help():
    """
    This function does nothing pretty much
    """
    pass

# The input list will be manipulated
# Since this is not a base type, it will be passed by reference to this class
def list_manipulated_func(some_list):
    print(some_list)
    some_list.remove(0)
    for idx in range(len(some_list)):
        some_list[idx] *= 5
    some_list.append(5)
    some_list.append(0)

if __name__ == "__main__":
    print(a(5,3))
    print(b(5,3))
    print(c(3,2))
    print(func_with_default(3,4,2))
    # The function accepts unordered variables
    # Making it easier to override only one default value
    # Note that the default return is None
    print(func_with_default(a=2,e=5,b=3,c=7))

    # We can now use help on our function
    # The help will print the docs in the """"""
    print(help(func_with_help))

    some_list = [0,4,5,5]
    list_manipulated_func(some_list)
    # This will create a copy of some_list which will die at the end of the function
    # The copy will have a different id
    list_manipulated_func(list(some_list))
    print(some_list)