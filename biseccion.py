import math as mt

def biseccion(f, intervalo, err, number_iter):
    a= intervalo[0]
    b= intervalo[1]
    err_a= 100.0
    iterations= 0
    m_act=0.0
    m_previa=0.0
    while iterations < number_iter and err_a > err:
        m_previa= m_act
        m_act= (a + b)/2

        if f(m_act)*f(b)<0:
           a = m_act
        else:
           b= m_act

        if iterations >1 :
           err_a= abs((m_act-m_previa)/m_act)

        iterations+=1
    
    return (m_act,err_a, iterations)

if __name__== "__main__":
  
   f = lambda x: (mt.e**x) - 3*(x**2)

   results= biseccion(f,(0,1),0.04,6)

   print("El punto aproximado es ", results[0], " con un margen de error de ", results[1], 'alcanzado en ', results[2], 'iteraciones')
   try:
      if results[0]>1 :
         raise Exception
   except:
      print('El programa no funciona correctamente')