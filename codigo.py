import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Definir la función
def f(x, y):
    return x**2 + y**2 -2*x -4*y + 5

#Definir el gradiente de la función
def gradiente_f(x, y):
    dx = 2*x - 2
    dy = 2*y - 4
    return dx, dy

#Definir el gradiente descendente de la función
def descenso_gradiente(x_inicial, y_inicial, alpha, num_iteraciones):
    x_actual = x_inicial
    y_actual = y_inicial
    #valores de la función
    val = []

    for i in range(num_iteraciones):
        gradiente_x, gradiente_y = gradiente_f(x_actual, y_actual)
        x_actual -=alpha*gradiente_x
        y_actual -=alpha*gradiente_y
        val_actual = f(x_actual, y_actual)
        val.append(val_actual)

    return x_actual, y_actual, val
#Parametros iniciales
x_inicial = 3
y_inicial = 4
alpha = 0.1
num_iteraciones = 20

#Ejecutar el descenso del gradiente
x_final, y_final, val = descenso_gradiente(x_inicial, y_inicial, alpha, num_iteraciones)

#Grafico en 2D
plt.plot(val)
plt.title('Valor de f(x, y) en cada iteración')
plt.xlabel("Iteraciones")
plt.ylabel("f(x, y)")
plt.grid(True)
plt.show()

#Grafico en 3D
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-2, 4, 100)
y = np.linspace(-2, 4, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("Función f(x,y)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("f(x, y)")

#Puntos del descenso del gradiente
ax.scatter(x_final, y_final, f(x_final, y_final), color="red", label = "punto final")
ax.scatter(x_inicial, y_inicial, f(x_inicial, y_inicial), color="green", label = "punto inicial")
ax.legend()

plt.show(block=False)
plt.ioff()
plt.show()