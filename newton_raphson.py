"""
newton_raphson.py
Implementación del método de Newton-Raphson para aproximar raíces de
funciones de una variable.

Autores: Sebastian Zabala, Valeria Valerio y Rosmaurys Villarroel
"""

import math as m
import numpy as np


def newton_raphson(x0, tolera, fx, dfx):
    """Aplica el método de Newton-Raphson para encontrar una raíz de `fx`.

    Parámetros:
    - x0: valor inicial (float)
    - tolera: tolerancia para la convergencia (float)
    - fx: función objetivo (callable)
    - dfx: derivada de la función objetivo (callable)

    Retorna:
    - (xi, tramo, tabla): raíz aproximada, último tramo (|xnuevo-xi|) y una
      tabla (numpy array) con las iteraciones: [xi, xnuevo, tramo].

    Notas:
    - Se almacena cada paso en `tabla` para inspección posterior.
    - La condición de parada es `tramo < tolera`.
    """
    tabla = []
    tramo = abs(2 * tolera)  # inicializar mayor que la tolerancia
    xi = x0

    while (tramo >= tolera):
        # iteración de Newton: xnuevo = xi - f(xi)/f'(xi)
        xnuevo = xi - fx(xi) / dfx(xi)
        tramo = abs(xnuevo - xi)
        tabla.append([xi, xnuevo, tramo])
        xi = xnuevo

    # convierte la lista a un arreglo numpy para presentación
    tabla = np.array(tabla)

    return (xi, tramo, tabla)


def salida_newton_raphson(tupla):
    """Imprime la tabla de iteraciones y la raíz encontrada.

    `tupla` debe ser el resultado devuelto por `newton_raphson`.
    """
    print()
    print("=== Newton-Raphson ===")
    print(['xi', 'xnuevo', 'tramo'])
    np.set_printoptions(precision=4)
    print(tupla[2])
    print(f'raiz en: {tupla[0]}')
    print(f'con error de: {tupla[1]}')
    print()


if __name__ == "__main__":
    # Ejemplo: mismo polinomio que en bisección
    # fx(x) = x^3 - x - 2  =>  dfx(x) = 3x^2 - 1
    fx = lambda x: x**3 - x - 2
    dfx = lambda x: 3 * x**2 - 1

    # Punto inicial cercano a la raíz esperada
    Z = newton_raphson(1.5, 1e-6, fx, dfx)
    salida_newton_raphson(Z)

    # Otro punto inicial para comparar convergencia
    Y = newton_raphson(2.0, 1e-8, fx, dfx)
    salida_newton_raphson(Y)