if __name__ == "__main__":
    # Python contains only two types of loop
    # for and while
    # The for loop is a ranged loop on a list
    list1 = [5,3,4,2]
    list2 = [5,2,1,1]
    # We iterate over each item, getting the actual item each iteration
    # In simple types, we get a copy, unlike complex types
    for item in list1:
        print(item)

    # We can iterate of the index of the list instead by using range and len
    # range will create a new list containing the indices that we gave it as an input
    # The range receives a start and an end
    for idx in range(len(list1)):
        print(list1[idx])

    # We can also iterate and get a tuple of index and the item with enumerate
    for idx, item in enumerate(list1):
        print(idx)
        print(item)

    # Lastly, we can use zip to zip two lists together into a tuple and loop over it
    for a1, a2 in zip(list1, list2):
        print(a1)
        print(a2)