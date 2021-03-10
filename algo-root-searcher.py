import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from math import *
import sympy as sp




# Definimos la funcion con la que trabajaremos: e**-x -x
# def func(x):
#     return sp.exp(-x) -x
# d_f = sp.diff(func(x)) 
# print(d_f)
# ------------------- Biseccion --------------------------------


def biseccion(f, tol, x_i):
    #Nuestros dos valores 
    a=0
    # b=1.2
    b = x_i
    f = sp.lambdify(x, f)
    x_r = (a+b)/2
    counter= 0
    counters=[]
    a_values=[]
    b_values=[]
    x_r_values=[]
    errors=[]

    while np.abs(f(x_r)) > tol:
        counter+=1
        x_r = (a+b)/2
        if f(a)*f(x_r) < 0:
            b= x_r 
        else:
            a= x_r
        counters.append(counter)
        a_values.append(a)
        b_values.append(b)
        x_r_values.append(x_r)
        errors.append(np.abs(f(x_r)))
    print(tabulate(zip(counters, a_values, b_values, x_r_values, errors), headers=['iteraciones', 'a', 'b', 'x_r', 'error'], tablefmt='orgtbl'))

    print('La raiz es ', x_r)
    return x_r



def show_graphic():
    x= 0
    x_values = []
    y_values = []
    while x<2:
        x += 0.1
        x_values.append(x)
        y_values.append(f(x))
    xpoints = np.array(x_values)
    ypoints = np.array(y_values)
    plt.plot(xpoints, ypoints)
    plt.show()


# -------------------- Newton-Raphson ----------------------------
def newton_raphson(f, x_i, tol, i):
    counters=[]
    a_values=[]
    b_values=[]
    x_r_values=[]
    d_f = sp.diff(f)
    f = sp.lambdify(x, f)
    d_f = sp.lambdify(x,d_f)
    for j in range(i):
        x_r = x_i - f(x_i)/d_f(x_i)
        a_values.append(f(x_i))
        b_values.append(d_f(x_i))
        counters.append(j)
        x_r_values.append(x_r)
        if (np.abs(x_r - x_i) < tol):
            print(tabulate(zip(counters, a_values, b_values, x_r_values), headers=['iteraciones', 'a', 'b', 'x_r'], tablefmt='orgtbl'))
            return x_r
        x_i = x_r
        print('No se pudo hallar la raiz a las {} iteraciones'.format(i))

# ---------------- Secante ------------------------------------

def secante(f, x_i, x_1, tol, i):
    f = sp.lambdify(x, f)
    counters=[]
    a_values=[]
    b_values=[]
    x_r_values=[]
    for j in range(i):
        x_r = x_1 - (x_1-x_i)*f(x_1)/(f(x_1) - f(x_i))
        counters.append(j)
        a_values.append(x_i)
        b_values.append(x_1)
        x_r_values.append(x_r)
        if (np.abs(x_r - x_1) < tol):
            print(tabulate(zip(counters, a_values, b_values, x_r_values), headers=['iteraciones', 'x_inicial', 'x_1', 'x_r'], tablefmt='orgtbl'))
            return x_r
        x_i = x_1
        x_1 = x_r
    print('No se pudo hallar la raiz a las {} iteraciones'.format(i))
            
# -------------------- estructura del programa -------------------


x = sp.symbols('x')
print('Para ingresar la constante de Euler use el metodo : exp()')
print('Por ejemplo: para ingresar e**x escriba => exp(x)')
f = input('Ingrese la funcion con variable independiente x : ')


def menu():
    print('--- Indique el metodo para encontrar la raiz ---')
    print('1) metodo de biseccion')
    print('2) metodo de Newton-Raphson')
    print('3) metodo de la secante')
    print('4) metodo de la regla falsa')
    print('0) salir del programa')

menu()
option = int(input('opcion: '))

while option != 0:
    if option == 1:
        biseccion(f, 0.001, 1.2)
    elif option == 2:
        newton_raphson(f, pi, 0.001, 10)
    elif option == 3:
        secante(f, 0.78, 1.5, 0.001, 20)
    elif option == 4:
        print('usar metodo de la regla falsa')
    else:
        print('Opcion invalida; ingrese un numero del 0 al 4')

    print()
    # show_graphic()
    menu()
    option = int(input('opcion: '))
