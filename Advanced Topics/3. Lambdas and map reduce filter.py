# Lambdas are a small anonymous functions used to quickly perform an operation
# They take any amount of arguments, but only have one expression
# Lambdas syntax:
# lambda arguments: expression
# Lambdas are very useful for quickly evaluating boolean expressions for different scenarios
# Some scenarios are for mapping one type to another or filtering different lists
def lambda_exponent(expo):
    return lambda num : num ** expo

power2_expo = lambda_exponent(2)
power5_expo = lambda_exponent(5)
# Will perform (5^2)^5
power5_expo(power2_expo(5))

# Lambdas are used in many different ways, usually to pass an expression functions for different long templated functions
# A few built in functions are the map, reduce and filter which receive a lambda as the operation method
# Map is used to map one object to another, with a transformation lambda
some_list = [1,2,3,4]
exponent_list = map(lambda x: x**2, some_list)
# Reduce is used to reduce one object to a result of a lambda transformation
# It is from a library called functools, and is usually combined together with map
# This is a common paradigm to map an object into something before reducing it into a result
# The reduce receives an object to iterate on
# Each step receives two arguments from the object and returns one
# That result object will be sent into the next lambda iteration along with the next iter in the object
import functools
exponent_max = functools.reduce(lambda a, b : a if a > b else b, exponent_list)

# Lastly, the filter is used to filter out different objects from an iterable using a lambda
some_list = [1,2,3,4,5,6,7,8]
some_filtered_list = filter(lambda x: x % 2 == 0, some_list)