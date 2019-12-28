# *args are a useful way to pass any amount of variables you want to a method
# This will be deduced as an iteratable variable called args
# Note that args is just a name and you can call it whatever you want
# However it is a standard to call it args
def my_basic_types_function(a,b,c):
    return a+b+c

def my_integers_function(int_list):
    return sum(int_list)

def my_args_function(*args):
    return sum(args)

def my_kwargs_function(**kwargs):
    return sum(kwargs.values())

def my_kwargs_expended_function(a, b, c):
    return a + b + c

print(my_basic_types_function(1,2,3))
print(my_integers_function([1,2,3]))
print(my_args_function(1,2,3,4,5,6))
# You can also use the syntax to unpack a list into the arguments
some_list = [1,2,3]
# Will expend it into a,b,c
print(my_basic_types_function(*some_list))

# Kwargs is pretty much the same as args
# However it accepts keyword items instead of positional items like a list
# So in other words, args act as a list and kwargs act as a dict
print(my_kwargs_function(a=5, b=2, c=3, d=4))
# You can do the same as args with expending of kwargs
some_dict = {'a': 5, 'b':33, 'c': 4}
print(my_kwargs_expended_function(**some_dict))