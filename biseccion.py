import math as mt

"""
biseccion.py
Implementa el método de la bisección para aproximar una raíz de una
función continua en un intervalo donde la función cambia de signo.

Contiene:
- `biseccion(f, intervalo, err, number_iter)`: realiza iteraciones del
  método hasta alcanzar una cota de error relativa o un número máximo de
  iteraciones.

El ejemplo en `__main__` usa `f(x) = x^3 - x - 2 = 0` en el intervalo [1, 2].
 
 Autores: Sebastian Zabala, Valeria Valerio y Rosmaurys Villarroel
"""


def biseccion(f, intervalo, err, number_iter):
   """Aproxima una raíz de `f` en el intervalo dado usando bisección.

   Parámetros:
   - f: callable, función de una variable
   - intervalo: tupla/lista (a, b) tal que f(a) y f(b) tienen signos opuestos
   - err: tolerancia relativa deseada (por ejemplo 0.01 para 1%)
   - number_iter: número máximo de iteraciones a realizar

   Retorna:
   - (m_act, err_a, iterations): aproximación de la raíz, error relativo
     aproximado y número de iteraciones realizadas.

   Notas de implementación:
   - Se usa la regla del punto medio m = (a+b)/2.
   - Si f(m) y f(b) cambian de signo, la raíz está en [m, b], por lo que
     se asigna `a = m`; en caso contrario la raíz está en [a, m] y se
     asigna `b = m`.
   - El error relativo se calcula como |m_act - m_previa| / m_act a partir
     de la segunda iteración.
   """
   a = intervalo[0]
   b = intervalo[1]
   err_a = 100.0
   iterations = 0
   m_act = 0.0
   m_previa = 0.0

   while iterations < number_iter and err_a > err:
      m_previa = m_act
      m_act = (a + b) / 2

      # Determinar en qué subintervalo está la raíz por el cambio de signo
      if f(m_act) * f(b) < 0:
         a = m_act
      else:
         b = m_act

      # Calcular error relativo a partir de la segunda iteración
      if iterations > 1:
         err_a = abs((m_act - m_previa) / m_act)

      iterations += 1

   return (m_act, err_a, iterations)


if __name__ == "__main__":
   # Ejemplo: resolver x^3 - x - 2 = 0 en [1, 2]
   # (raíz real aproximada ~ 1.521)
   f = lambda x: x**3 - x - 2

   results = biseccion(f, (1, 2), 1e-3, 50)

   print()
   print("=== Bisección ===")
   print(f"El punto aproximado es {results[0]} con un margen de error de {results[1]} alcanzado en {results[2]} iteraciones")
   print()
