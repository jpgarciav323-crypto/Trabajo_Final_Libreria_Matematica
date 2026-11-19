"""
Libreria matematica propia en Python.
Implementacion de funciones matematicas y series sin usar la libreria math.
"""

def factorial(n: int) -> int:
    """Calcula el factorial de un numero entero no negativo n!."""
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

def potencia(base: float, exp: int) -> float:
    """Calcula base elevado a un exponente entero no negativo."""
    resultado = 1.0
    for i in range(exp):
        resultado = resultado * base
    return resultado

def valor_absoluto(x: float) -> float:
    """Retorna el valor absoluto de un numero."""
    if x < 0:
        return -x
    return x

# ---------------------------------------------------------
# 1. EXPONENCIAL Y CONSTANTES
# ---------------------------------------------------------

def exponencial(x: float, terminos: int = 30) -> float:
    """
    Aproxima e^x usando la serie de Taylor con una cantidad fija de terminos.
    Parametros:
        x (float): exponente a evaluar.
        terminos (int): numero de terminos de la suma (por defecto 30).
    Retorna:
        float: aproximacion de e^x.
    """
    suma = 0.0
    for k in range(terminos):
        termino = potencia(x, k) / factorial(k)
        suma = suma + termino
    return suma

def constante_e(terminos: int = 30) -> float:
    """Calcula la constante e evaluando exponencial(1)."""
    return exponencial(1.0, terminos)

def constante_pi(terminos: int = 1000) -> float:
    """
    Aproxima el valor de pi usando la serie de Nilakantha.
    Parametros:
        terminos (int): numero de terminos a sumar (por defecto 1000).
    Retorna:
        float: aproximacion de pi.
    """
    suma = 0.0
    signo = 1.0
    for k in range(1, terminos + 1):
        denominador = (2 * k) * (2 * k + 1) * (2 * k + 2)
        suma = suma + signo * (1.0 / denominador)
        signo = -signo
    return 3.0 + 4.0 * suma

# ---------------------------------------------------------
# 2. FUNCIONES TRIGONOMETRICAS
# ---------------------------------------------------------

def reducir_angulo(x: float) -> float:
    """Reduce un angulo en radianes al intervalo [-pi, pi] para mayor precision."""
    pi = constante_pi(1000)
    dos_pi = 2.0 * pi
    while x > pi:
        x = x - dos_pi
    while x < -pi:
        x = x + dos_pi
    return x

def seno(x: float, terminos: int = 15) -> float:
    """
    Aproxima sin(x) en radianes usando serie de Taylor.
    Parametros:
        x (float): angulo en radianes.
        terminos (int): cantidad de terminos de la serie.
    Retorna:
        float: valor aproximado de sin(x).
    """
    x = reducir_angulo(x)
    suma = 0.0
    signo = 1.0
    for k in range(terminos):
        exponente = 2 * k + 1
        termino = signo * (potencia(x, exponente) / factorial(exponente))
        suma = suma + termino
        signo = -signo
    return suma

def coseno(x: float, terminos: int = 15) -> float:
    """
    Aproxima cos(x) en radianes usando serie de Taylor.
    Parametros:
        x (float): angulo en radianes.
        terminos (int): cantidad de terminos de la serie.
    Retorna:
        float: valor aproximado de cos(x).
    """
    x = reducir_angulo(x)
    suma = 0.0
    signo = 1.0
    for k in range(terminos):
        exponente = 2 * k
        termino = signo * (potencia(x, exponente) / factorial(exponente))
        suma = suma + termino
        signo = -signo
    return suma

def tangente(x: float) -> float:
    """
    Calcula tan(x) = sin(x) / cos(x).
    Retorna None si |cos(x)| < 1e-6 (tangente no definida).
    """
    c = coseno(x)
    if valor_absoluto(c) < 1e-6:
        print("Error: La tangente no esta definida para este angulo (coseno cercano a cero).")
        return None
    s = seno(x)
    return s / c

# ---------------------------------------------------------
# 3. LOGARITMO NATURAL (METODO DE NEWTON-RAPHSON)
# ---------------------------------------------------------

def logaritmo_natural(x: float, tolerancia: float = 1e-7, max_iter: int = 100) -> float:
    """
    Calcula ln(x) para x > 0 resolviendo e^y - x = 0 con Newton-Raphson.
    Rechaza x <= 0 retornando None.
    """
    if x <= 0:
        print("Error: El logaritmo natural solo esta definido para x > 0.")
        return None

    y = 0.0
    iteracion = 0
    while iteracion < max_iter:
        ey = exponencial(y, 35)
        error = valor_absoluto(ey - x)
        if error < tolerancia:
            return y
        y = y - (ey - x) / ey
        iteracion = iteracion + 1

    print("Advertencia: Se alcanzo el maximo de iteraciones sin converger.")
    return y

# ---------------------------------------------------------
# 4. MAXIMO COMUN DIVISOR (ALGORITMO DE EUCLIDES)
# ---------------------------------------------------------

def mcd(a: int, b: int) -> int:
    """
    Calcula el Maximo Comun Divisor de dos enteros usando el algoritmo de Euclides.
    Para (0, 0) retorna 0. El resultado siempre es no negativo.
    """
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    if a == 0 and b == 0:
        return 0

    while b != 0:
        residuo = a % b
        a = b
        b = residuo

    return a

# ---------------------------------------------------------
# 5. SERIE DE FOURIER (ONDA CUADRADA)
# ---------------------------------------------------------

def fourier_onda_cuadrada(x: float, N: int) -> float:
    """
    Evalua la suma parcial de Fourier de N terminos impares para una onda cuadrada
    de amplitud 1 y periodo 2*pi.
    """
    if N <= 0:
        print("Error: N debe ser un entero positivo.")
        return None

    pi = constante_pi(1000)
    suma = 0.0
    for k in range(N):
        impar = 2 * k + 1
        suma = suma + (seno(impar * x) / impar)

    return (4.0 / pi) * suma
