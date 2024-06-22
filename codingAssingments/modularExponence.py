def fast_mod_exp(b, k, m):
    # Caso base: si k == 0, se devuelve b % m
    if k == 0:
        return b % m

    # Caso recursivo: se calcula el valor para k-1 hasta llegar a 0
    sub_result = fast_mod_exp(b, k - 1, m)

    # Se eleva el resultado anterior al cuadrado y luego se toma con modulo m
    return (sub_result * sub_result) % m

b = 3
k = 3
m = 5

result = fast_mod_exp(b, k, m)

print('Result',fast_mod_exp(b, k, m))
