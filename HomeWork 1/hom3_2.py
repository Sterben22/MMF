################# PARTE 2 DE CAMPOS VECTORIALES#######################

import numpy as np
import matplotlib.pyplot as plt

def tests1():
    #Creando malla de valores
    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    X,Y = np.meshgrid(x, y)
    #Creando vectores
    U = X/np.sqrt(2)
    V = -Y/np.sqrt(2)
    #Creando entorno de dibujo
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title(r'Campo Vectorial v = $\frac{1}{\sqrt{2}}(xi - yj)$', fontsize=14)
    # Mostrar la cuadrícula y los vectores
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def tests2():
    #Creando malla de valores
    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    X,Y = np.meshgrid(x, y)
    #Creando vectores
    U = 2*Y
    V = 0
    #Creando entorno de dibujo
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title(r'Campo Vectorial v = $2yi$', fontsize=14)
    # Mostrar la cuadrícula y los vectores
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def tests3():
    #Creando malla de valores
    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    X,Y = np.meshgrid(x, y)
    #Creando vectores
    U = X**2
    V = Y**2
    #Creando entorno de dibujo
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title(r'Campo Vectorial v = $x²i + y²j$', fontsize=14)
    # Mostrar la cuadrícula y los vectores
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def tests4():
    #Creando malla de valores
    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    X,Y = np.meshgrid(x, y)
    #Creando vectores
    U = X/np.sqrt(X**2 + Y**2)
    V = -Y/np.sqrt(X**2 + Y**2)
    #Creando entorno de dibujo
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title(r'Campo Vectorial: v = $\frac{xi - yj}{\sqrt{x²+y²}}$', fontsize=14)
    # Mostrar la cuadrícula y los vectores
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def tests5():
    #Creando malla de valores
    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    X,Y = np.meshgrid(x, y)
    #Creando vectores
    U = X*Y
    V = -X
    #Creando entorno de dibujo
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title(r'Campo Vectorial: v = $xyi - xj$', fontsize=14)
    # Mostrar la cuadrícula y los vectores
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def tests6():
    #Creando malla de valores
    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    X,Y = np.meshgrid(x, y)
    #Creando vectores
    U = np.cos(X)
    V = np.sin(Y)
    #Creando entorno de dibujo
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title(r'Campo Vectorial: v = $cos(x)i + sin(y)j$', fontsize=14)
    # Mostrar la cuadrícula y los vectores
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    t = True
    while t:
        match int(input("\nSeleccione una opcion:\n 1.- Ejercicio 1\n 2.- Ejercicio 2\n 3.- Ejercicio 3\n 4.- Ejercicio 4\n 5.- Ejercicio 5\n 6.- Ejercicio 6\n 7.- Salir\n --> ")):
            case 1: tests1()
            case 2: tests2()
            case 3: tests3()
            case 4: tests4()
            case 5: tests5()
            case 6: tests6()
            case 7: exit()