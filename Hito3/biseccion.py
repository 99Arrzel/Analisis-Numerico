from tabulate import tabulate
import pandas as pd
from mpmath import *

def aplicarPuntoFijo(func, a, b, error_aceptable):
    valores_a = []
    valores_b = []
    valores_c = []
    valores_fafr = []
    valores_xm = []
    errores = []
    def f(x):
        f = eval(func)
        return f
    error = abs(b-a)
    while error > error_aceptable:
        valores_a.append(a)
        valores_b.append(b)
        c = (b+a) / 2
        valores_c.append(c)
        print(c)
        if f(a) * f(b) >= 0:
            print("No es posible aplicar el método de bisección")
            exit()
        elif f(c) * f(a) < 0:
            b = c
            error = abs(b-a)
            valores_fafr.append(f(c) * f(a))
        elif f(c) * f(b) < 0:
            a = c
            error = abs(b-a)
            valores_fafr.append(f(c) * f(a))
        else:
            print("error XD")
            exit()
        errores.append(error)
        valores_xm.append(f(c))
    print(f"El error es {error}")
    print(a, b)
    
    data = ({'valores de X0': valores_a, 'valores de XI': valores_b, 'valores de Xm': valores_c,'Valores de f(Xa) * f(Xr)':valores_fafr, 'Valores de f(Xm)': valores_xm, 'Errores': errores})
    
    data_frame = pd.DataFrame.from_dict((data))
    print(tabulate(data_frame, headers='keys', tablefmt='fancy_grid'))
    

# ================================================================


# 25problema = x**3 - 5*(x)**2 + 3*(x) - 7  #Expresamos nuestro problema
problema = "sin(x) - csc(x) + 1"  # Debe estar igualado a 0, ojo
error = 1e-10
intervaloA = 2
intervaloB = 3
aplicarPuntoFijo(problema, intervaloA, intervaloB, error)  # Call al problema
# ================================================================
