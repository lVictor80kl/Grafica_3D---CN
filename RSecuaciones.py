import numpy as np
from sympy import *
import matplotlib.pyplot as plt
"Nombres ➤ Victor Marcano, Andres Ng, Gustavo Paéz | Calculo numerico"

# Ecuaciones

x, y, z = symbols('x y z')

f1 = lambdify([x,y,z], 5*x - 3*y + 2*z + 20, "numpy")
f2 = lambdify([x,y,z], 4*x + 6*y - 5*z - 2, "numpy")  
f3 = lambdify([x,y,z], 8*x + y - z + 21, "numpy")
#el lambdify convierte una expresión simbólica en una función Python que puede ser evaluada numéricamente.
#Grids en 2D
x = np.linspace(-9, 1, 20)
y = np.linspace(-5, 5, 20)

X, Y = np.meshgrid(x, y)
#meshgrid se utiliza para generar matrices que representan una cuadrícula en una o más dimensiones
Z1 = f1(X, Y, 0)
Z2 = f2(X, Y, 0)
Z3 = f3(X, Y, 0)

#Gráficas 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z1)
ax.plot_surface(X, Y, Z2)
ax.plot_surface(X, Y, Z3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()