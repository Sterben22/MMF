import numpy as np
import matplotlib.pyplot as plt

class Particula():
    def __init__(self, position, charge):
        self.position = position
        self.charge = charge
        self.campo = (0, 0) 

    # Calcula el campo que hay entre la carga y el punto (x,y)
    def calc_Er(self, pos):
        k = 9e9
        r = np.sqrt((pos[0] - self.position[0])**2 + (pos[1] - self.position[1])**2)
        temp = (k * abs(self.charge)) / r**3
        
        # Si la partícula es un electrón o proton
        if self.charge > 0:
            self.campo = (temp * (pos[0] - self.position[0]), temp * (pos[1] - self.position[1]))
        else:
            self.campo = (temp * (self.position[0] - pos[0]), temp * (self.position[1] - pos[1]))

def plotVectorField(list_carga):
    # Dominio del campo vectorial
    x, y = np.meshgrid(np.linspace(-5, +5, 25), np.linspace(-5, +5, 25))
    # El campo vectorial
    u, v = np.zeros_like(x), np.zeros_like(y)

    for particula in list_carga:
        particula.calc_Er((x, y))
        u += particula.campo[0]
        v += particula.campo[1]

        # Muestra la particula
        if particula.charge >=0:
            plt.plot(particula.position[0], particula.position[1], 'bo', markersize=15)
        else:
            plt.plot(particula.position[0], particula.position[1], 'ro', markersize=15)


    # Trazar las partículas
    plt.streamplot(x, y, u, v)
    plt.title('Campo Vectorial')
    plt.grid(True)
    plt.gca().set_aspect('equal')
    
    # Agregar etiquetas a los ejes x e y
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    
    # Muestra la figura
    plt.show()

if __name__ == '__main__':
    # Cantidad de Cargas electricas en el Plano
    n = int(input("Enter the number of charges to input: "))
    list_carga = []

    #Aviso de uso de Notacion Cientifica
    print("Recuerda poner en notacion cientifica (nem <> n x 10^{m})")

    # Guardando los datos de cada carga en el Plano
    for i in range(n):
        carga_input = input(f"\nEnter the electric charge for the charge. {i + 1}\n(default 1.6e-19, press Enter for default): ")
        carga = float(carga_input) if carga_input else 1.6e-19
        x = float(input(f"Enter the X-coordinate for the charge {i + 1}: "))
        y = float(input(f"Enter the Y-coordinate for the charge {i + 1}: "))
        list_carga.append(Particula((x, y), carga))

    plotVectorField(list_carga)
