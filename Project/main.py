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
    p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)

    while p == q:
        q = generate_prime(1000, 5000)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(3, phi_n - 1)
    g, _, _ = extended_gcd(e, phi_n)

    while g != 1:
        e = random.randint(3, phi_n - 1)
        g, _, _ = extended_gcd(e, phi_n)

    d = mod_inverse(e, phi_n)

    return (e, n), (d, n), p, q, phi_n


def encrypt_message(message, public_key):
    e, n = public_key
    message_encoded = [ord(ch) for ch in message]
    ciphertext = [pow(ch, e, n) for ch in message_encoded]
    return ciphertext

def decrypt_message(ciphertext, private_key):
    d, n = private_key
    decoded_msg = [pow(ch, d, n) for ch in ciphertext]
    message = "".join(chr(ch) for ch in decoded_msg)
    return message


def main():
    message = input("Introduce el mensaje a cifrar: ")

    public_key, private_key, p, q, phi_n = generate_keys()
    print(f"Clave Pública: {public_key}")
    print(f"Clave Privada: {private_key}")
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"phi(n): {phi_n}")

    ciphertext = encrypt_message(message, public_key)
    print(f"Texto cifrado: {ciphertext}")

    decrypted_message = decrypt_message(ciphertext, private_key)
    print(f"Texto descifrado: {decrypted_message}")


if __name__ == "__main__":
    main()