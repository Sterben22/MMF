import numpy as np
import matplotlib.pyplot as plt

# Definir el campo vectorial
v_i = 3
v_j = -5

# Crear una cuadrícula de coordenadas
x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

# Calcular los componentes x e y del campo vectorial en cada punto
U = v_i
V = v_j

# Dibujar el campo vectorial
plt.figure(figsize=(6, 6))
plt.quiver(X, Y, U, V, scale=10, color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo Vectorial: v = 3i - 5j')
plt.grid()
plt.show()
