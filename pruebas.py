"""
Programa de verificacion y pruebas para libreria_matematica.py.
Compara los resultados propios contra la libreria estandar math.
"""
import math
import libreria_matematica as lib

def mostrar_error(nombre: str, calculado: float, referencia: float) -> None:
    error = lib.valor_absoluto(calculado - referencia)
    print(f"{nombre}:")
    print(f"  Calculado  = {calculado:.8f}")
    print(f"  Referencia = {referencia:.8f}")
    print(f"  Error abs  = {error:.2e}\n")

print("==================================================")
print("1. PRUEBAS DE EXPONENCIAL Y CONSTANTES")
print("==================================================")
mostrar_error("e^0", lib.exponencial(0), math.exp(0))
mostrar_error("e^1 (constante e)", lib.constante_e(), math.e)
mostrar_error("e^2", lib.exponencial(2), math.exp(2))
mostrar_error("Constante pi (1000 terminos)", lib.constante_pi(1000), math.pi)

print("==================================================")
print("2. PRUEBAS DE TRIGONOMETRIA")
print("==================================================")
mostrar_error("sin(pi/6)", lib.seno(math.pi / 6), math.sin(math.pi / 6))
mostrar_error("cos(0)", lib.coseno(0), math.cos(0))
mostrar_error("tan(pi/4)", lib.tangente(math.pi / 4), math.tan(math.pi / 4))

print("Caso frontera tan(pi/2):")
res_tan = lib.tangente(math.pi / 2)
print("  Resultado retornado:", res_tan, "\n")

print("==================================================")
print("3. PRUEBAS DE LOGARITMO NATURAL")
print("==================================================")
mostrar_error("ln(1)", lib.logaritmo_natural(1.0), math.log(1.0))
mostrar_error("ln(0.5)", lib.logaritmo_natural(0.5), math.log(0.5))
mostrar_error("ln(2)", lib.logaritmo_natural(2.0), math.log(2.0))

print("Caso frontera ln(0):")
res_ln0 = lib.logaritmo_natural(0)
print("  Resultado retornado:", res_ln0)

print("Caso frontera ln(-5):")
res_ln_neg = lib.logaritmo_natural(-5)
print("  Resultado retornado:", res_ln_neg, "\n")

print("==================================================")
print("4. PRUEBAS DE MAXIMO COMUN DIVISOR (MCD)")
print("==================================================")
print("mcd(48, 18)  =", lib.mcd(48, 18), "(Esperado: 6)")
print("mcd(-15, 0)  =", lib.mcd(-15, 0), "(Esperado: 15)")
print("mcd(-24, -36)=", lib.mcd(-24, -36), "(Esperado: 12)")
print("mcd(0, 0)    =", lib.mcd(0, 0), "(Esperado: 0)\n")

print("==================================================")
print("5. SERIE DE FOURIER (ONDA CUADRADA)")
print("==================================================")
puntos = [
    ("x = pi/2  (valor ideal = 1.0)", math.pi / 2, 1.0),
    ("x = 3pi/2 (valor ideal = -1.0)", 3 * math.pi / 2, -1.0),
    ("x = 0.1   (valor ideal = 1.0)", 0.1, 1.0)
]

for etiqueta, x_val, ideal in puntos:
    print(f"Punto: {etiqueta}")
    for n_term in [1, 5, 15]:
        aprox = lib.fourier_onda_cuadrada(x_val, n_term)
        err = lib.valor_absoluto(aprox - ideal)
        print(f"  N = {n_term:2d} -> S_N(x) = {aprox:.6f} | Error = {err:.6f}")
    print()
