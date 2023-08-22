################# PARTE 1 DE CAMPOS VECTORIALES#######################

import numpy as np
import matplotlib.pyplot as plt

def tests1():
    # Crear una malla de coordenadas
    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    X, Y = np.meshgrid(x, y)
    # Definir los componentes del campo vectorial
    U = 3 * np.ones_like(X)
    V = -5* np.ones_like(Y)
    # Crear la figura
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title('Campo Vectorial v = 3i - 5j')
    # Mostrar la cuadrícula y los vectores
    plt.grid()
    plt.show()

def tests2():
    # Crear una malla de coordenadas
    x = np.linspace(-5, 5, 15)
    y = np.linspace(-5, 5, 15)
    X, Y = np.meshgrid(x, y)
    # Definir los componentes del campo vectorial 
    U = X
    V = Y
    # Crear la figura
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title('Campo Vectorial v = r = xi + yj')
    # Mostrar la cuadrícula y los vectores
    plt.grid()
    plt.show()

def tests3():
    # Crear una malla de coordenadas
    x = np.linspace(-5, 5, 15)
    y = np.linspace(-5, 5, 15)
    X, Y = np.meshgrid(x, y)
    # Ocultando la advertencia
    np.seterr(invalid='ignore')
    # Definir los componentes del campo vectorial 
    U = X/np.sqrt((X**2+Y**2)**3)
    V = Y/np.sqrt((X**2+Y**2)**3)
     # Crear la figura
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title(r'Campo Vectorial v = $\frac{xi}{(x^2 + y^2)^{\frac{3}{2}}}+ \frac{yj}{(x^2 + y^2)^{\frac{3}{2}}}$', fontsize=14)
    # Mostrar la cuadrícula y los vectores
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def tests4():
    # Crear una malla de coordenadas
    x = np.linspace(-10, 10, 10)
    y = np.linspace(-10, 10, 10)
    X, Y = np.meshgrid(x, y)
    # Ocultando la advertencia
    np.seterr(invalid='ignore')
    # Definir los componentes del campo vectorial
    U = (3*Y*X)/np.sqrt((X**2+Y**2)**5)
    V = (2*(Y**2) - X**2 )/np.sqrt((X**2+Y**2)**3)
     # Crear la figura
    fig, ax = plt.subplots(figsize=(8,6))
    ax.set_aspect("equal")
    # Dibujar los vectores
    plt.streamplot(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-10, 11, step=1))
    plt.yticks(np.arange(-10, 11, step=1))
    plt.title(r'Campo Vectorial v =$\frac{3xy}{r⁵}i + \frac{2y²-x²}{r⁵}j=\frac{3xy}{(x^2 + y^2)^{\frac{5}{2}}}i + \frac{2y²-x²}{(x^2 + y^2)^{\frac{5}{2}}}j$', fontsize=14)
    # Mostrar la cuadrícula y los vectores
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def tests5():
    # Crear una malla de coordenadas
    x = np.linspace(-5, 5, 15)
    y = np.linspace(-5, 5, 15)
    X, Y = np.meshgrid(x, y)
    # Definir los componentes del campo vectorial
    U = X
    V = -Y
     # Crear la figura
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title(r'Campo Vectorial v = $xi -yj$', fontsize=14)
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
    U = 1/np.sqrt(2)
    V = -1/np.sqrt(2)
    #Creando entorno de dibujo
    plt.figure(figsize=(8,6))
    # Dibujar los vectores
    plt.quiver(X, Y, U, V, color='b', linewidth=1.5)
    # Configurar los ejes
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))
    plt.title(r'Campo Vectorial v = $\frac{1}{\sqrt{2}}(i - j)$', fontsize=14)
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