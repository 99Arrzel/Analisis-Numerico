from tabulate import tabulate
# Pa que esté bonito
from re import A
import sympy as sp  # para substituir functions
import pandas as pd


def aplicarRegulaFalsi(problema, error, intervaloA, intervaloB):
    valoresA = []
    valoresB = []
    valoresFA = []
    valoresFB = []
    valoresXI = []
    errores = []
    miError = 1
    while abs(miError) > error:  # el contador == 0 para que se ejecute al menos una vez
        fa = problema.subs(x, intervaloA)  # procesamos el valor de funcion a

        valoresFA.append(fa)  # Append a su lista correspondiente

        fb = problema.subs(x, intervaloB)  # procesamos el valor de función  B
        valoresFB.append(fb)  # Append a su lista correspondiente

        if(fa > 0 and fb > 0):  # No es aplicable si son del mismo signo
            print("Regula falsi no es aplicable, al menos en ese intervalo.")
            print("FA: ", fa, "FB : ", fb)
            print("Ambos son positivos.")
            exit()
        if(fa < 0 and fb < 0):  # No es aplicable si son del mismo signo
            print("Regula falsi no es aplicable, al menos en ese intervalo.")
            print("FA: ", fa, "FB : ", fb)
            print("Ambos son negativos.")
            exit()
        fbk, ak, fak, bk = sp.symbols(
            'fbk ak fak bk')  # Declaramos las variables
        regulafalsi = (fbk * ak - fak * bk) / \
            (fbk - fak)  # Declaramos la regula falsi
        xi = regulafalsi.subs(fbk, fb).subs(fak, fa).subs(
            ak, intervaloA).subs(bk, intervaloB)
        xi = xi.evalf(8)
        print(xi)
        valoresXI.append(xi)  # Append de valores para XI
        # Calculado de error
        errores.append(problema.subs(x, xi))
        miError = problema.subs(x, xi)
        if(xi > 0):
            intervaloA = xi
        else:
            intervaloB = xi

        valoresA.append(intervaloA)
        valoresB.append(intervaloB)

    data = {'Valores A': valoresA, 'Valores B': valoresB,
            'Valores f(a)': valoresFA, 'Valores f(b)': valoresFB, 'Valores XI': valoresXI, 'Errores': errores}
    print("La solución es :", valoresXI[len(valoresXI) - 1], " con un error de +-", abs(
        errores[len(errores)-1]), "y un error máximo de", error)
    data_frame = pd.DataFrame.from_dict(data)
    print(data_frame)
    print(tabulate(data_frame, headers='keys', tablefmt='fancy_grid'))


    # print(data_frame.to_markdown()) Es lo mismo el de Markdown, pero no tiene el top ni el bot igual, está más "cool" el de tabulate
# ================================================================
x = sp.symbols('x')  # Definimos la variable que vamos a usar
# 25problema = x**3 - 5*(x)**2 + 3*(x) - 7  #Expresamos nuestro problema
problema = x**3 + 2*x**2 + 10 * x - 20  # Debe estar igualado a 0, ojo
error = 1e-5
intervaloA = 1.3
intervaloB = 1.4
aplicarRegulaFalsi(problema, error, intervaloA, intervaloB)  # Call al problema
# ================================================================
