import numpy as np
# Primero hacemos un array que represente el problema
# Tendrá el siguiente formato
#   x1  y1  z1 = r1
#   x2  y2  z2 = r2
#   x3  y3  z3 = r3
#   solo es representativo, no tendrán esos nombres.
#   Primero preguntamos el número de incognitas, de esta sacamos el tamaño de la matriz
print("Ingrese el número de variables desconocidas")
x = int(input())
array = np.zeros((x, x+1))
# xarray = array solución
xarray = np.zeros(x)
# Ahora si recién le hacemos ingresar los datos
print("Ingresa los coeficientes de la matriz")
for i in range (x):
  for j in range (x+1):
    array[i][j] = float(input('a['+str(i)+']['+ str(j)+']='))
    print(array)
# Operamos con la matriz
for i in range(x):
  if array[i][i] == 0.0:
    print("No se puede dividir por 0, ingresa un valor diferente")
    exit()
  for j in range (i + 1, x): #Siempre un paso adelante de i, como en un sort
    radio = array[j][i] / array[i][i] #Dividimos todos los que estén abajo de la horizontal
    for k in range (x + 1): #otro loop para restar a todos los restantes el radio y multiplicarlos por el array
      array[j][k] = array[j][k] - radio * array[i][k]

# Copiamos la solución a nuestro array trucho
xarray[x-1] = array[x-1][x]/array[x-1][x-1]

for i in range (x-2, -1, -1):
  xarray[i] = array[i][x]
  for j in range(i+1, x):
    xarray[i] = xarray[i] - array[i][j] * xarray[j]
  xarray[i] = xarray[i] /array[i][i]
# Se imprime
print("La solución es:")
for i in range (x):
  print('X%d = %0.5f' %(i+1,xarray[i]), end = '\t')