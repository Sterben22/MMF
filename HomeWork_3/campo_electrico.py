import numpy as np

class Carga:
    def __init__(self, carga=1.602e-19, x=0, y=0) -> None:
        self.q = carga
        self.pos = (x, y)
        self.campo = (0, 0)

    def calcular_campo_electrico(self, pos):
        k = 9e9
        r = np.sqrt((pos[0] - self.pos[0])**2 + (pos[1] - self.pos[1])**2)
        temp = (k * self.q) / r**3
        self.campo = (temp * (pos[0] - self.pos[0]), temp * (pos[1] - self.pos[1]))

def Campo_Resultante(list_carga):
    Er = (0, 0) 

    for i in list_carga:
        Er = (Er[0] + i.campo[0], Er[1] + i.campo[1])  

    return Er

if __name__ == "__main__":
    n = int(input("Enter the number of charges to input: "))
    list_carga = []

    for i in range(n):
        carga_input = input(f"\nEnter the electric charge for the charge. {i + 1}\n(default 1.602e-19, press Enter for default): ")
        carga = float(carga_input) if carga_input else 1.602e-19
        x = float(input(f"Enter the X-coordinate for the charge {i + 1}: "))
        y = float(input(f"Enter the Y-coordinate for the charge {i + 1}: "))
        list_carga.append(Carga(carga, x, y))
    
    print("\nNow you will enter the coordinates where you want to calculate the Electric Field.")
    pos_x = float(input("Enter the X-coordinate: "))
    pos_y = float(input("Enter the Y-coordinate: "))
    pos = (pos_x, pos_y)

    for carga in list_carga:
        carga.calcular_campo_electrico(pos)
    
    resultado = Campo_Resultante(list_carga)

    if resultado[1] < 0:
        print(f"\nThe resultant field is {resultado[0]:.2e}i - {-resultado[1]:.2e}j")
    else:
        print(f"\nThe resultant field is {resultado[0]:.2e}i + {resultado[1]:.2e}j")
