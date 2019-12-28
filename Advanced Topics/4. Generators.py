# A Generator is a function which returns a generator iterator
# The iterator is created by the yield keyword, and can be coupled with a value called the generated value
# The generator will pause its function and store its state until called again, and will continue from the same point instead of the start
# In normal programming paradigms, this is called coroutine, a routine that will run along side a paused routine
# Lets see a basic example

# This function will generate 3 values
# At the fourth request for the generator, a StopIteration exception will be raised
def simple_generator():
    yield 1
    yield 2
    yield 3

our_generator = simple_generator()
one = next(our_generator)
two = next(our_generator)
three = next(our_generator)
# The last next call is invalid and will cause a stop iteration exception
exception = next(our_generator)

# We can always reset our generator and use it again
our_generator = simple_generator()

# Lets see a more practical example
import math
# This is a simple function to determine whether a given number is prime or not
# It is not very efficient but we'll live with it
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

# We will yield only the prime numbers up until a given number
def get_primes(number):
    curr_number = 0
    while curr_number < number:
        if is_prime(curr_number):
            yield curr_number
        curr_number += 1

# This will iterate over all the yielded numbers and return them
# Up until the stop iteration
for prime in get_primes(1024):
    print(prime)

# We can also send values back to the generator and not only receive them
# Lets say we have an infinite generator
# Given a number it will check if the number is prime
# If so, it will yield it, if not it will continue until it finds the next prime
# We can send in a new number to the generator to begin searching primes from again once it has found one
def get_infinite_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1

# We will print the successive primes for K iterations in base 10
# Each time we will send the next power of 10 to find the prime on
def print_successive_primes(iterations, base=10):
    prime_generator = get_infinite_primes(base)
    # At first, we have to send None, because the generator hasent even gotten to the first yield statement
    # If we sent something else, nothing would receive it since only a yield receives a sent item
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

print_successive_primes(10)

# Lastly, we can use yield without any values, this is usually when we want to pause the routine to receive some data at a certian point
# A good example would be a consumer producer paradigm
import random

def get_data():
    # Get some random data
    return random.sample(range(10), 3)

def consume():
    # We will display a running sum accross a list of integers we send it
    running_sum = 0
    data_items_seen = 0

    while True:
        # Consume random data and add it to the sum
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))

def produce(consumer):
    # Produce a set of data and send it to the consumer
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield

# Create the consumer and producer
# And start producing!
consumer = consume()
consumer.send(None)
producer = produce(consumer)

# We dont care about the actual loop, this is only to run the consumer producer 10 times
for _ in range(10):
    print('Producing...')
    next(producer)
