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

def extended_gcd(a, b):
    '''
       the extended Euclidean algorithm

       :param a: The first integer
       :param b: The second integer
       :return: A tuple where g is the greatest common divisor
       '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(e, phi):
    '''
    the modular multiplicative inverse of e modulo phi.
    :param e: integer whose modular inverse is to be calculated
    :param phi: modulus
    :return:  modular multiplicative inverse of e modulo phi
    '''
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi


def generate_keys():
    p,q = generate_prime(1000,5000), generate_prime(1000,5000)

    while p == q:
        q = generate_prime(1000,5000)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(3, phi_n - 1)

    while g != 1:
        e = random.randint(3, phi_n - 1)
        g, _, _ = extended_gcd(e, phi_n)

    d = mod_inverse(e, phi_n)

    return (e, n), (d, n), p, q, phi_n






