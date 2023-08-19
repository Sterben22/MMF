import numpy as np
import matplotlib.pyplot as plt

def tests1():
    # Definir el intervalo [0, 2*pi]
    x = np.linspace(0, 2*np.pi, 1000)
    # Calcular los valores de las funciones en el intervalo
    f_x = np.sin(x)
    g_x = x**2 + 3*x
    # Crear una figura y ejes
    plt.figure(figsize=(8, 6))
    plt.title('Gráficas de $f(x) = sin(x)$ y $g(x) = x^2 + 3x$')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    # Graficar las funciones
    plt.plot(x, f_x, label='$f(x) = sin(x)$')
    plt.plot(x, g_x, label='$g(x) = x^2 + 3x$')
    # Agregar leyenda
    plt.legend()
    # Mostrar la gráfica
    plt.grid(True)
    plt.show()
    
def tests2():
    # Crear valores de x en el intervalo [-10, 10]
    x = np.linspace(-10, 10, 200)
    # Calcular los valores del polinomio en los puntos x
    y = x**2 + 5*x - 3
    # Dibujar el polinomio
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color='red', linestyle='dashed', label='$x^2 + 5x - 3$')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.title('Gráfica del Polinomio $x^2 + 5x - 3$')
    plt.legend()
    plt.grid(True)
    plt.show()

def tests3():
    # Crear valores de x en el intervalo [0, 6]
    x = np.linspace(0, 6, 200)

    # Calcular los valores de las funciones en los puntos x
    y_f = 3 * x * np.exp(x)
    y_g = np.sin(x + 3)

    # Dibujar las funciones en la misma gráfica
    plt.figure(figsize=(8, 6))
    # Subplot 1: Graficando las dos funciones en la misma grafica
    plt.subplot(1,3,1)
    plt.plot(x, y_f, color='blue', label='$f(x) = 3xe^x$')
    plt.plot(x, y_g, color='red', linestyle='dashed', label='$g(x) = sin(x + 3)$')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.title('Gráfica de $f(x)$ y $g(x)$ en el intervalo [0, 6]')
    plt.legend()
    plt.grid(True)
    # Subplot 2: Graficando la funcion f(x)
    plt.subplot(1,3,2)
    plt.plot(x, y_f, color='blue', label='$f(x) = 3xe^x$')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.title('Gráfica de $f(x)$ en el intervalo [0, 6]')
    plt.legend()
    plt.grid(True)
    # Subplot 2: Graficando la funcion g(x)
    plt.subplot(1,3,3)
    plt.plot(x, y_g, color='red', linestyle='dashed', label='$g(x) = sin(x + 3)$')
    plt.title('Gráfica de $g(x)$ en el intervalo [0, 6]')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.legend()
    plt.grid(True)
    
    #Ajuste automatico de los subplot
    plt.tight_layout()
    
    #Mostrar los plot
    plt.show()

if __name__ == "__main__":
    t = True
    while t:
        match int(input("Seleccione una opcion:\n 1.- Ejercicio 1\n 2.- Ejercicio 2\n 3.- Ejercicio 3\n 4.- Salir\n --> ")):
            case 1: tests1()
            case 2: tests2()
            case 3: tests3()
            case 4: exit()