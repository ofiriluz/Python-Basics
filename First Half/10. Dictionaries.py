if __name__ == "__main__":
    # A dict is one of the most important types in python
    # It is a simple unordered mutable key value type
    # It will probably be most in used in our program
    # Whether to parse different files, or hold complex data
    names_to_age_dict = {
        "John": 12,
        "Alex": 15,
        "Sharon": 22,
        "Ofir": 10
    }
    print(names_to_age_dict["John"])
    # We can ask if a key exists in the dict
    print("John" in names_to_age_dict)
    # We can print the keys or values, or tuples or key values
    print(names_to_age_dict.keys())
    print(names_to_age_dict.values())
    print(names_to_age_dict.items())
    # We can also iterate over the dict
    # Just rememeber that this is not ordered
    for key, value in names_to_age_dict.iteritems():
        print("{}={}".format(key, value))
    # We can delete a key value pair by using del
    del names_to_age_dict['John']
    # And we can extend one dict with another
    other_dict = {
        "Efi": 25,
        "Ross": 50
    }
    names_to_age_dict.update(other_dict)
    print(names_to_age_dict)