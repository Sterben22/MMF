import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear una cuadrícula de coordenadas en 3D
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Crear una figura en 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie del campo escalar
surface = ax.plot_surface(X, Y, Z, cmap='viridis')

# Configurar etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Representación de $f(x, y, z) = x^2 + y^2 + z^2$')

# Agregar barra de colores
fig.colorbar(surface)

# Mostrar la gráfica
plt.show()
