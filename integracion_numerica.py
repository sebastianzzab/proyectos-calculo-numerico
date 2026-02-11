import math as mt

"""
integracion_numerica.py
Ejemplo sencillo de aproximación de una integral definida mediante la suma de Riemann
(rectángulos por la izquierda).

Contiene:
- `riemman(f, a, b, n)`: función que aproxima la integral de `f` en `[a, b]`
  usando `n` subintervalos.

Nota: se importa `math` como `mt` por si se necesitan funciones matemáticas
en `f` (en este ejemplo la lambda usa sólo operadores, así que `mt` no se
utiliza directamente).
 
 Autores: Sebastian Zabala, Valeria Valerio y Rosmaurys Villarroel
"""


def riemman(f, a, b, n):
    """Aproxima la integral de `f` en el intervalo [a, b].

    Parámetros:
    - f: callable que recibe un float y devuelve un float (la función a integrar)
    - a: límite inferior del intervalo
    - b: límite superior del intervalo
    - n: número de subintervalos (entero > 0)

    Retorna:
    - Valor float que aproxima la integral definida de `f` en [a, b]

    Método:
    - Se usa la suma de Riemann con rectángulos de ancho `h = (b-a)/n` y
      altura `f(x_i)` tomada en el extremo izquierdo de cada subintervalo.
    """
    h = (b - a) / n  # ancho de cada subintervalo
    acum = 0         # acumulador de las áreas de los rectángulos
    x = a            # posición del extremo izquierdo del subintervalo actual

    for i in range(n):
        # Área del rectángulo en el subintervalo actual: altura * base
        acum = acum + f(x) * h
        # Avanzar al siguiente subintervalo
        x = x + h

    return acum


if __name__ == "__main__":
  # Ejemplo: integrar sin(x) en [0, pi]
  # Este ejemplo es clásico y sirve para comprobar que la aproximación
  # converge cuando incrementamos el número de subintervalos.
  f = lambda x: mt.sin(x)

  a = 0
  b = mt.pi
  n = 100

  print()
  print("=== Integración Numérica ===")
  print(f"Aproximación de ∫_0^π sin(x) dx con n={n}: {riemman(f, a, b, n)}")
  print()

