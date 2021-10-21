import math

def f(x):
  return math.exp(x)-(3*x)

def secante(a,b,tol,max_iter):
  iter = 0
  c = (a+b)*(0.5)
  while(abs(f(c))>tol and iter <max_iter):
    c = b - ((b-a)/(f(b)-f(a)))*f(b)
    a = b
    b = c
  return c

secante()