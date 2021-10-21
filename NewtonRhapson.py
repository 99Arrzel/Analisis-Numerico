import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    def function(x):

        value = x**2-2 #Acá el ejercicio
        return value

    def derivative(x):

        return 2*x

def newton(function, derivative, x0, tol, max_iter=100):

    x1 = 0

    if abs(x0-x1)<= tol and abs((x0-x1)/x0)<= tol:
        return x0

    print("k\t x0\t\t function(x0)")
    k = 1

    while k <= max_iter:
        x1 = x0 - (function(x0)/derivative(x0))
        print("x%d\t%e\t%e"%(k,x1,function(x1)))

        if abs(x0-x1)<= tol and abs((x0-x1)/x0)<= tol:
            plt.plot(x0, function(x0), 'or')
            return x1

        x0 = x1
        k = k + 1
        plt.plot(x0, function(x0), 'or')


        if k > max_iter:
            print("Se paso el número máximo de iteraciones")

    return x1

sqrt = newton(function, derivative, 1.7, 0.0000001)
print("The approximate value of x is: "+str(sqrt))

# Aqui lo ploteamos XD
u = np.arange(1.0, 2.0, 0.0001)
w = u**2 - 2

plt.plot(u, w)
plt.axhline(y=0.0, color='black', linestyle='-')
plt.title('Newton-Raphson Graphics for' + ' y = x^2 - 2')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend(['Xn'], loc='upper left')
plt.show()