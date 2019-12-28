# Collections is a standard library with extra collections we can use besides the standard ones
# A quick reminder for the standard ones:
# The following table describes each type's properties
#           Ordered         Unordered
# Mutable   list [1,2,3]    set {1,2,3}
# Immutable str "abc"       dict {a=1, b=2}
#           tuple (1,2,3)
import collections
# This is the same as a normal dict but is also ordered
# It has the same API as a normal dict
ordered_dict = collections.OrderedDict()
ordered_dict['a'] = 5
ordered_dict['b'] = 7
# Will preserve order
print(ordered_dict)
# This is basiclly a dict that contains counters of everything inserted into it
# It has many converters from different types into a counter
counter = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    counter[word] += 1
print(counter)
print(counter.most_common())
# This is a normal deque, can act as a queue or as a stack
queue_or_stack = collections.deque()
queue_or_stack.append('a')
queue_or_stack.append('b')
queue_or_stack.appendleft('c')