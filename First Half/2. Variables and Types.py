if __name__ == "__main__":
    # The base python types
    # All of those variables will be allocated and deallocated via the interpreter
    number=3
    fnumber=3.5
    string="hi"
    boolean=True or False
    print(type(number)) # int
    print(type(fnumber)) # float
    print(type(string)) # str
    print(type(boolean)) # bool

    # Dynamic type change to an existing variable
    number="not a number"
    print(type(number)) # str

    # And for fun, complex type
    comp=5+4j
    print(type(comp)) # complex

    # You can get help on certian objects, by using the help function
    print(help(int))

    # And you cant live without the null...only its None here
    n = None
    print(type(n)) # None

    # Each variable has its own ID
    # The ID is an interpretation of the memory address for the python interpreter
    print(id(number))
    print(id(n))
    # Note that two base items can contain the same ID for same base values if the interpeter finds it fit to do so
    # However complex types gurantee a unique ID over the lifetime of the object
    a1 = "aaa"
    a2 = "aaa"
    print(id(a1))
    print(id(a2))

    # Each variable may be also deleted explicity
    # Forcing the interpeter to delete it now
    del a1
    print(a1) # Will result in an error