# Each class inherits from the base class object
# You can specify it if u want
class A(object):
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

if __name__ == "__main__":
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