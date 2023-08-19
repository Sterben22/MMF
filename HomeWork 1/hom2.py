import numpy as np
import matplotlib.pyplot as plt

def tests1():
    # Crear una cuadrícula de coordenadas
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # Calcular los valores del campo escalar en la cuadrícula
    R = np.sqrt(X**2 + Y**2)
    Z = 1/R

    # Crear una figura
    fig = plt.figure(figsize=(12, 6))

    # Subplot 1: Gráfico de contorno y representación de color 2D
    ax1 = fig.add_subplot(1, 2, 1)
    # Gráfico de contorno
    contour_plot = ax1.contourf(X, Y, Z, levels=20, cmap='viridis')
    # Representación de color
    color_map = ax1.imshow(Z, extent=(-5, 5, -5, 5), origin='lower', cmap='viridis', interpolation='bilinear')
    fig.colorbar(color_map, ax=ax1)
    ax1.set_xlabel('Eje x')
    ax1.set_ylabel('Eje y')
    ax1.set_title(r'Campo Escalar $f(r) = \frac{1}{r}$ en 2D')
    ax1.grid()

    # Subplot 2: Gráfico en 3D
    # Creando entorno 3D
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.plot_surface(X, Y, Z, cmap='viridis')
    ax2.set_xlabel('Eje x')
    ax2.set_ylabel('Eje y')
    ax2.set_zlabel('Eje z')
    ax2.set_title(r'Campo Escalar $f(r) = \frac{1}{r}$ en 3D')
    #Ajuste automatico de los subplot
    plt.tight_layout()
    plt.show()

def tests2():
    # Creando malla de valores
    x = np.linspace(-5, 5, 1000)
    y = np.linspace(-5, 5, 1000)
    X, Y = np.meshgrid(x, y)

    # Hallando todos los valores
    Z = 1 / (np.sqrt(X**2 + (Y - 1)**2)) - 1 / (np.sqrt(X**2 + (Y + 1)**2))

    # Creando entorno 3D
    fig = plt.figure(figsize=(8, 6))
    ax2 = fig.add_subplot(111, projection="3d")
    ax2.plot_surface(X, Y, Z, cmap='viridis')
    ax2.set_xlim(-6, 6)
    ax2.set_ylim(-6, 6)
    ax2.set_zlim(-6, 6)
    ax2.set_xlabel("Eje x")
    ax2.set_ylabel("Eje y")
    ax2.set_zlabel("Eje z")
    # Utiliza formato LaTeX para el título
    title = r'Campo Escalar $f(x, y) = \frac{1}{\sqrt{x^2 + (y-1)^2}} - \frac{1}{\sqrt{x^2 + (y+1)^2}}$ en 3D'
    # Ajusta el tamaño y el espacio del título
    ax2.set_title(title, fontsize=14, pad=20)  

    plt.tight_layout()
    plt.show()

def tests3():
    # Creando malla de valores
    x = np.linspace(-5, 5, 1000)
    y = np.linspace(-5, 5, 1000)
    X, Y = np.meshgrid(x, y)

    # Hallando todos los valores
    Z = X - Y + 2

    # Creando entorno 3D
    fig = plt.figure(figsize=(8,6))
    ax3 = fig.add_subplot(111, projection='3d')
    ax3.plot_surface(X, Y, Z, cmap='viridis')
    ax3.set_xlabel("Eje x")
    ax3.set_ylabel("Eje y")
    ax3.set_zlabel("Eje z")
    ax3.set_title('Campo escalar $f(x, y)= x - y + 2$ en 3D')

    plt.tight_layout()
    plt.show()

def tests4():
    # Creando malla de valores
    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    X, Y = np.meshgrid(x, y)
    # Calcula solo para los valores válidos, asigna cero a los valores negativos
    Z = np.where(16 - X**2 - Y**2 >= 0, np.sqrt(16 - X**2 - Y**2), 0)
    # Creando entorno 3D
    fig = plt.figure(figsize=(8, 6))
    ax2 = fig.add_subplot(111, projection="3d")
    ax2.plot_surface(X, Y, Z, cmap='viridis')
    ax2.set_xlabel("Eje x")
    ax2.set_ylabel("Eje y")
    ax2.set_zlabel("Eje z")
    # Utiliza formato LaTeX para el título
    ax2.set_title(r'Campo Escalar $f(x, y) = \sqrt{16-x^2-y^2}}$ en 3D', fontsize=14, pad=20)  

    plt.tight_layout()
    plt.show()

def tests5():
    # Creando malla de valores
    x = np.linspace(-100, 100, 1000)
    y = np.linspace(-100, 100, 1000)
    X, Y = np.meshgrid(x, y)
    Z = np.sqrt(-X**2 + -Y**2)

    fig = plt.figure(figsize=(8, 6))
    ax2 = fig.add_subplot(111)
    ax2.contour(X, Y, Z, cmap='viridis')
    ax2.set_xlabel("Eje x")
    ax2.set_ylabel("Eje y")
    # Utiliza formato LaTeX para el título
    ax2.set_title('Mapa de contorno: $f(x,y,z)=x^2+y^2+z^2$ en 2D', fontsize=14, pad=20) 
    plt.show()

if __name__ == "__main__":
    t = True
    while t:
        match int(input("Seleccione una opcion:\n 1.- Ejercicio 1\n 2.- Ejercicio 2\n 3.- Ejercicio 3\n 4.- Ejercicio 4\n 5.- Ejercicio 5\n 6.- Salir\n --> ")):
            case 1: tests1()
            case 2: tests2()
            case 3: tests3()
            case 4: tests4()
            case 5: tests5()
            case 6: exit()