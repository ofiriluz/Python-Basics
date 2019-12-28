# List comprehansion is a common way to iterate over a list to create a new one in a single line
# Its written as [expression for item in list if some_filter]
# Will create a list from 0 to 10 not including 10
some_list = [i for i in range(10)]
# Will create a new list of the power of two for only the even numbers
some_new_list = [item**2 for item in some_list if item % 2 == 0]

# Dict comprehansion is similar to list in syntax
# And is useful for dictionaries manipulation
# Its written as {key:val for (key, val) in dict.items() if some_filter}
some_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
# Same as before with the list
some_new_dict = {key:val**2 for (key, val) in some_dict.items() if val % 2 == 0}