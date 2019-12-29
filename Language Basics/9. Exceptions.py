def exception_base_func():
    raise "Oh noes"

def exception_type_func():
    raise Exception("Oh noes")

if __name__ == "__main__":
    # You can throw any type of exception in python
    # However it is a best practice to throw a class type
    try:
        exception_base_func()
    # You do not have to specify what you are catching
    except:
        print("Failure")
    try:
        exception_type_func()
    # We can print e, this will only print the string error
    except e:
        print(str(e))
    try:
        exception_type_func()
    # We can specify the type, and print the traceback
    except Exception as e:
        # We can use traceback to get the trace log
        import traceback
        print(traceback.format_exc())

