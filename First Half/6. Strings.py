if __name__ == "__main__":
    str1 = "abcd"
    str2 = "cdef"

    # A string is mostly like a list of chars
    # It can be sorted, substrings with splicing, and many other operatis
    # However the string itself is constant, and you cannot change its indices
    str1[4] = 'b' # Will result in an error
    str1 = "eded" # Is ok

    # A string has many different manipulation functions
    lowerstr = str1.lower()
    upperstr = str1.upper()
    str1.startswith('abc')
    str1.endswith('cdef')
    stripped_from_spaces = str1.strip()