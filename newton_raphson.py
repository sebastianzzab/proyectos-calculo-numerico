# Método de Newton-Raphson
import math as m
import numpy as np

def newton_raphson(x0, tolera, fx, dfx):
    # PROCEDIMIENTO
    tabla = []
    tramo = abs(2*tolera)
    xi = x0
    while (tramo>=tolera):
        xnuevo = xi - fx(xi)/dfx(xi)
        tramo  = abs(xnuevo-xi)
        tabla.append([xi,xnuevo,tramo])
        xi = xnuevo

    # convierte la lista a un arreglo.
    tabla = np.array(tabla)
    
    #retorno una tupla con toda la informacion necesaria
    return (xi, tramo, tabla)

# SALIDA
def salida_newton_raphson(tupla):
    print(['xi', 'xnuevo', 'tramo'])
    np.set_printoptions(precision = 4)
    print(tupla[2])
    print('raiz en: ', tupla[0])
    print('con error de: ',tupla[1])


if __name__ == "__main__":
    
    dfx = lambda x: -2*x*(m.e**(-x**2))-2
    fx  = lambda x: (m.e**(-x**2))-2*x+1
   
    Z= newton_raphson(0.80,0.02,fx,dfx)
    salida_newton_raphson(Z)
   #SERIA 0.80, pero partiendo desde 2 parece obtener una mayor precision
# seria 0.02 pero con esta se llega mas lejos
   
    Y=newton_raphson(2,0.001,fx,dfx)
    salida_newton_raphson(Y)