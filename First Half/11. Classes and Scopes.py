# Before understanding class, we need to do a quick review about scopes in python
def scope_test():
    # You can define functions that will only live inside a specific scope
    def do_local():
        spam = "local spam"

    # When doing so, you can reference an upper scope variable by using the nonlocal attribute
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    # Lastly, you can reference any global variable by using the global attribute
    # This mostly serves as a static variable within your program
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    # Will print test spam
    print("After local assignment:", spam)
    do_nonlocal()
    # Will print nonlocal spam
    print("After nonlocal assignment:", spam)
    do_global()
    # Will still print nonlocal spam
    print("After global assignment:", spam)

# Each class inherits from the base class object
# You can specify it if u want
class A(object):
    # This is a class variable, shared by all of its objects
    some_var = "A"
    # This is the constructor
    # Every function in a class receives self
    # Self is like this in every other language and you can access its variables via self
    def __init__(self, some_input):
        self.some_input = some_input
        # This is a public member of the class
        self.some_public_number = 1
        # This is the convention for a protected member of the class
        # However it can still be accessed from the outside so its only a weak defintion for the user
        self._some_protected_number = 2
        # This is the convention for a private member of the class
        # This is a strong defintion and will result in an attribute error when accessing from the outside
        self.__some_private_number = 5
    # This is an object method, which receives the object self
    def object_method(self, a, b):
        return a * b * self.__some_private_number

    # This is a class method, it does not receive the object self but receives the class self represents
    # This is defined using a decorator, which we will later see more
    # This is pracaticlly a static method that receives the type explicitly
    @classmethod
    def class_method(cls, a, b):
        return a * b

    # This is our normal static method for a class
    @staticmethod
    def static_method(a, b):
        return a * b

class B(A):
    def __init__(self):
        # Access the inherited class and initizlie it
        # The super will go to the parent class on the object self and access its methods
        super(B, self).__init__(5)

    # We can override the parent function by simply implementing it on this class
    def object_method(self, a, b):
        print("Soem Message")
        return super(B, self).object_method(a, b)

class C1:
    pass

class C2:
    pass

# Multiple inheritance
class C(C1, C2):
    def __init__(self, obj):
        self.__obj = obj

    # The enter and exit methods of class define 
    def __enter__(self):
        # Do some opening of a connection
        pass

    def __exit__(self):
        # Close the connection
        pass

    def __iter__(self):
        # Returns an object which is iteratable
        # If __next__ is defined, then you can return the object itself
        return self

    def __next__(self):
        # Returns the next object to iterate on
        # Or rasie a StopIteration exception if you reached the end
        pass

if __name__ == "__main__":
    scope_test()
    # Will print global spam
    print("In global scope:", spam)

    a = B()
    # Accessing the public variable
    print(a.some_public_number)
    # Accessing the protected variable, bad practice!
    print(a._some_protected_number)
    try:
        # This will throw and exception since its a strongly private member
        # However, we can still access it via its mangeled name
        print(a.__some_private_number)
    except:
        pass
    print(a.object_method(5,4))
    # Each one of the static or class methods can be called from both the class and the object
    print(a.class_method(5,4))
    print(A.class_method(5,4))
    print(a.static_method(5,4))
    print(A.static_method(5,4))
    # Each class is behind the scenes a dictionary, so you can show it via the __dict__ method
    print(a.__dict__)
    # This is the class dict, which will print the actual methods aswell
    print(B.__dict__)

    # The c object will live only inside the scope and is created by the __enter__ method
    # And when the scope is done is destroyed by the __exit__ method
    with C("someobj") as c:
        pass