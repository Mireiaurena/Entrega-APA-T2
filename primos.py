"""
Mireia Ureña Lopez
Modulo que define funciones con números primos.

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcm(42, 60, 70, 63)
1260

>>> mcd(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """
    esPrimo retornará True si el numero introducido es primo o False en caso contrario.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El número debe ser un natural mayor que uno.")

    for esDivisible in range(2, int(numero**0.5) + 1):
        if numero % esDivisible == 0:
            return False
    return True

def primos(numero):
    """
    primos devolverá una tupla con todos los números primos por debajo de su argumento.
    """
    tupla = ()
    for buscaNum in range(2, numero):
        if esPrimo(buscaNum):
            tupla += (buscaNum,)
    return tupla

def descompon(numero):
    """
    Devolverá una tupla con la descomposición en factores primos de su argumento.
    """
    factores = []
    divisor = 2
    temp = numero
    while temp > 1:
        if temp % divisor == 0:
            factores.append(divisor)
            temp //= divisor
        else:
            divisor += 1
    return tuple(factores)

def mcd(*numeros):
    """
    Devolverá el máximo común divisor de sus argumentos.
    """
    def mcd_dos(a, b):
        f1 = descompon(a)
        f2 = descompon(b)
        comunes = set(f1) & set(f2)
        resultado = 1
        for f in comunes:
            resultado *= f ** min(f1.count(f), f2.count(f))
        return resultado

    res = numeros[0]
    for n in numeros[1:]:
        res = mcd_dos(res, n)
    return res

def mcm(*numeros):
    """
    Devolverá el mínimo común múltiplo de sus argumentos.
    """
    def mcm_dos(a, b):
        f1 = descompon(a)
        f2 = descompon(b)
        todos = set(f1) | set(f2)
        resultado = 1
        for f in todos:
            resultado *= f ** max(f1.count(f), f2.count(f))
        return resultado

    res = numeros[0]
    for n in numeros[1:]:
        res = mcm_dos(res, n)
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)