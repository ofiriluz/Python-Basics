if __name__ == "__main__":
    # A List can contain different types in python
    list1 = [3,4,5,"a",2,3.5]
    # This is a tuple, A list that is constant and cannot be changed
    tuple1 = (1,3,5,2) 
    # This is a set, a unique and changeable group of items
    set1 = {1,2,3}
    print(type(list1)) # list
    print(type(tuple1)) # tuple
    # We can add to it 
    list1.append(5)
    list1.insert(1, 5) # Insert at idx 1
    # We can also remove from the list
    list1.pop(5) # Will remove index 5
    list1.remove(2) # Will remove the first occurance of 2
    # We can get the list size by using len function
    print(len(list1))
    # We have different built in functions for example sorting the list
    list1.sort() # In place
    list2 = sorted(list1) # Returns a new list
    # A List can be sliced, meaning that we can take part of the list
    a = list[0] # Take index 0
    b = list[0:5] # Take sublist of 0-5 indices not including 5
    c = list[:-1] # Will return everything up to the last index not including it
    d = list[0:6:2] # Will take up untill the 6th idx not including in jumps of 2
    # We can also easily split and join strings to lists and back
    some_delimited_string = "a,b,c,d"
    delimited_list = some_delimited_string.split(',')
    rejoined_string = ','.join(delimited_list)
    # Last note on mutability of different types of lists:
    # The following table describes each type's properties
    #           Ordered         Unordered
    # Mutable   list [1,2,3]    set {1,2,3}
    # Immutable str "abc"
    #           tuple (1,2,3)