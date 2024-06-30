import random
import math

def is_prime(number):
    '''
    Check if a number is prime
    :param number: Integer to check if is prime
    :return: True if the number is prime, False if it is not
    .
    '''
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    '''
    Generate a random prime number in a given range
    :param min_value: The minimum value of the range
    :param max_value: The maximum value of the range
    :return: A random prime number within the specified range
    '''
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime
