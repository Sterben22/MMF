import numpy as np
import matplotlib.pyplot as plt

class ElectrostaticSystem:
    def __init__(self, k, q1, q2):
        self.k = k
        self.q1 = q1
        self.q2 = q2

    def potential_at_point(self, x, y):
        r1 = np.sqrt(x**2 + y**2)  # Distancia a q1
        r2 = np.sqrt(x**2 + (y - 0.5)**2)  # Distancia a q2
        V1 = self.k * self.q1 / r1
        V2 = self.k * self.q2 / r2
        return V1 + V2

    def calculate_potential_matrix(self, x_range, y_range):
        V_matrix = np.zeros((len(x_range), len(y_range)))
        for i in range(len(x_range)):
            for j in range(len(y_range)):
                V_matrix[i][j] = self.potential_at_point(x_range[i], y_range[j])
        return V_matrix

def main():
    k = 8.99e9  # Constante de Coulomb en Nm^2/C^2
    q1 = -1.2e-9  # Carga q1 en Coulombs
    q2 = 2.5e-9  # Carga q2 en Coulombs

    electrostatic_system = ElectrostaticSystem(k, q1, q2)

    x = np.linspace(-5, 5, 201)
    y = np.linspace(-5, 5, 201)

    V_matrix1 = electrostatic_system.calculate_potential_matrix(x, y)
    V_matrix2 = V_matrix1 - 3  # Cambio en el nivel de voltaje

    # Dibujar ambas superficies equipotenciales
    plt.contour(x, y, V_matrix1.T, levels=[3], colors='r', linewidths=2)
    plt.contour(x, y, V_matrix2.T, levels=[0], colors='g', linewidths=2)
    plt.plot(0, 0, 'bo', markersize=8)
    plt.plot(0, 0.5, 'ro', markersize=8)
    plt.xlabel('Coordenada x (m)')
    plt.ylabel('Coordenada y (m)')
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.axhline(0, color='k', linewidth=0.5)
    plt.axvline(0, color='k', linewidth=0.5)
    plt.title('Superficies Equipotenciales (V ≈ 3 V)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

