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