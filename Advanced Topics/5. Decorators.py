# Decorators are a way to wrap a function with some extra capabilities or restrictions and extend it
# A python function / class can be wrapped by many decorators, that will run sequently one after another
# Each decorator will perform its duty and if he decides to, activates the function itself or the next decorator
# A typical real world example of a decorator is to wrap a function to be activated on a REST call
# We need to note that a decorator is just a function that activates another function and returns itself as a decorator function
# Lets see a simple example
def my_decorator(func):
    def wrapper():
        print("This happens before the function")
        func()
        print("This happens after the function")
    return wrapper


def say_hi():
    print('hi')
# A behind the scenes usage would look something like this:
my_decorator = my_decorator(say_hi)
# This would print the message before and after
my_decorator()

# You can use the decorator to actually restrict certian usages
# For example
import datetime
def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_hi_again():
    print("hi again")

say_hi_again = not_during_the_night(say_hi_again)
# Will not print anything during the night
say_hi_again()
# This is where the actual syntax of python comes into place
# Instead of simply wrapping the function the way we saw before
# We can do the following
@not_during_the_night
def say_decorated_hi():
    print("decorated hi")

# When we activate this function, the same flow we saw before will happen
# However this time, its much more elegent and shorter
say_decorated_hi()

# A good way of work is to keep your decorators in seperate modules for reuseability

# A decorator can also work with arguments just like any other function
# And can pass forward arguments to the function using args and kwargs
# For example the following decorator will perform a function twice
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def double_named_hi(name):
    print("Hello {}".format(name))

# The argument will be passed forward from the args or kwargs
double_named_hi("ofir")

# We can also return from decorators in the normal manner by adding a return to the end of the decorator
def do_twice_with_return(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice_with_return
def double_formatted_named_hi(name):
    return "Hello {}".format(name)

print(double_formatted_named_hi("john"))

# When we are working with decorators, we are actually just using another functions
# Therefore we cannot really get information about the wrapped functions
# With functions like help and so on
# To "feed forward" the inner function, we can use a built in decorator from functools
import functools

def do_twice_with_info(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice_with_info
def some_func(x):
    """
    Hell world
    """
    return x**2

# Will print info about the wrapper function
print(help(double_formatted_named_hi))
# Will print info about the wrapped function
print(help(some_func))

# Lets write a real world example of some decorator
# The first one is for debugging calls of functions
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  
        signature = ", ".join(args_repr + kwargs_repr)           
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           
        return value
    return wrapper_debug

# The second one is for calculating the time it took for a function to execute
import time
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

# We can use more then one decorator at a time
# Each decorator will call itself one after another and will wrap the next
# They are basiclly stacked from top to bottom so we can do:
@debug
@timer
def waste_time(how_much):
    time.sleep(how_much)

# This will debugged and then will be timered
waste_time(5)

# We can also decorate classes and not only functions
# Lets start by decorating methods
class A:
    @debug
    def __init__(self):
        pass

    @timer
    def waste_time(self, how_much):
        time.sleep(how_much)

# We can also wrap the whole class, this means that we only decorate its instantiantion
# This is useful for different metaclasses example and more of an annotative way to show what the class does
# For example in python 3.7 dataclass decorator was introduced to denote that the class should only have data
@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

# Will print the time it took to insantiate the class
timewaster = TimeWaster(5)
# Will not print anything
timewaster.waste_time(1)

# You can also pass arguments to decorator themselves and not the functions
# Since up until now we used the name after the @ as the decorator func name
# We need something to wrap that aswell, so that we could pass arguments into it
# Without hurting the arguments we will later pass to the function itself
# For example lets take the following decorator
# The repeat function will accept the decorator argunments
# And it will return our normal decorator style that we know
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

# Fun fact, in python 3 you can use f to format from variables straight out
@repeat(num_times=3)
def say_hello(name):
    print(f"Hello {name}")


# If you want to have full flexability, you can write a decorator that will have both
# The abillity to receive args or not receive
# To do so, we need to define all of our args to have default values
# And to use the special * which says that everything after it is keyword only (you must specify the name)
def repeat_new(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


@repeat_new
def say_hi_1(name):
    print(f"hi {name}")

@repeat_new(num_times=5)
def say_hi_2(name):
    print(f"hi {name}")


# Any decorator can be stateful, for example if we want to keep track of how many times
# A function was called, we can do the following
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")

# Lastly, we can actually create classes that will act up as decorators
# This is the typical and more proper way to keep state 
# We can do that by using the __call__ class method which is called every time you call an instance of the class
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee_classed():
    print("Whee!")

# Lastly, some more real world decorators
# Firstly, a singleton decorator which will assure us that there is only one instance
# It is the same as before only that since we are expecting a class instead of a function
# We denote it with cls
# The wrapper will make sure that this class is singleton
def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass

# Another nice example is caching of return values
# Note that functools has a built in lru_cache decorator
def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

# This will cache values on the wrapper
@cache
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(10)
fibonacci(8)