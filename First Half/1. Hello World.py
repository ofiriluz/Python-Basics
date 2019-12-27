# This is a liner comment
"""
This is a multi line comment
"""

# A built in library import
import sys

# This will check if the current file is the module we are running
# We will later see why it is useful when having multiple modules
if __name__ == "__main__":
    # This is a new code block, indentation switches the classic {} blocks in python
    # Formatting
    print("Hello {}".format("Class"))
    print("Hello {first_name} {last_name}".format(first_name="Dennis", last_name="Ritchie"))
    # Another type of formatting
    print("I am a %s %s" % ("Ofir", "Iluz"))
    sys.stdout.write("And i am %d years old" % (27))
    # We can read from the user using input function
    some_str = raw_input("Please write your name")
    print(some_str)