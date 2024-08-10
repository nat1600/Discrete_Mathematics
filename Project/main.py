import tkinter as tk
from tkinter import filedialog, messagebox
import random
import math

#  RSA
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

# gui
def on_encrypt():
    message = entry_message.get()
    if not message:
        messagebox.showwarning("Error", "ELige un archivo a encriptar")
        return

    public_key, private_key, p, q, phi_n = generate_keys()
    ciphertext = encrypt_message(message, public_key)

    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(0, str(ciphertext))
    entry_ciphertext.config(fg="red")  # Color rojo para el texto encriptado

    entry_public_key.delete(0, tk.END)
    entry_public_key.insert(0, f"({public_key[0]}, {public_key[1]})")

    entry_private_key.delete(0, tk.END)
    entry_private_key.insert(0, f"({private_key[0]}, {private_key[1]})")

def on_decrypt():
    try:
        ciphertext = eval(entry_ciphertext.get())
        private_key = eval(entry_private_key.get())
        message = decrypt_message(ciphertext, private_key)
        entry_decrypted_message.delete(0, tk.END)
        entry_decrypted_message.insert(0, message)
        entry_decrypted_message.config(fg="green")  # Color verde para el texto desencriptado
    except Exception as e:
        messagebox.showerror("Error", f"fail: {str(e)}")

def load_message():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            message = file.read()
            entry_message.delete(0, tk.END)
            entry_message.insert(0, message)

def save_decrypted_message():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(entry_decrypted_message.get())


root = tk.Tk()
root.title('Proyecto matemáticas discretas II: RSA para archivos txt.')


entry_message = tk.Entry(root, width=50)
entry_message.pack(pady=10)

btn_load_message = tk.Button(root, text="Carga tu archivo .txt a ser encriptado:", command=load_message)
btn_load_message.pack()

btn_encrypt = tk.Button(root, text="Codificado", command=on_encrypt)
btn_encrypt.pack(pady=10)

entry_ciphertext = tk.Entry(root, width=50)
entry_ciphertext.pack(pady=10)

entry_public_key = tk.Entry(root, width=50)
entry_public_key.pack(pady=10)

entry_private_key = tk.Entry(root, width=50)
entry_private_key.pack(pady=10)

btn_decrypt = tk.Button(root, text="Decodificado", command=on_decrypt)
btn_decrypt.pack(pady=10)

entry_decrypted_message = tk.Entry(root, width=50)
entry_decrypted_message.pack(pady=10)


root.mainloop()
