# El codigo te crea una imagen con la traza de un electro con el  tiempo 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter 

# Datos iniciales
Vi = 3e6        # m/s
E = 400         # N/C
Tt = 3000e-9    # Tiempo total
dt = 100e-9     # Intervalo de tiempo

# Calculamos la aceleración debida al campo eléctrico (F = q * E)
q = -1.602e-19          # Carga del electrón en C
a = q * E / -9.109e-31  # Masa del electrón en kg

# Calculamos la velocidad final
Vf = Vi + a * Tt

# Calculamos los tiempos
tiempos = np.arange(0, Tt + dt, dt)

# Calculamos las posiciones usando la ecuación de movimiento
y = 0.5 * a * tiempos**2 + Vi * tiempos

# Crear figura
fig, ax = plt.subplots()
ax.set_xlim(0, Tt)
ax.set_ylim(0, max(y))

line, = ax.plot(tiempos,y, lw=2)

ax.set_title("Traza del movimiento del electron con el tiempo")
ax.set_xlabel("Tiempo ("+r"$10^{-6}$)"+" seg")
ax.set_ylabel("Posicion (m)")
ax.grid()
plt.tight_layout()
# Elimina la notación científica del eje x
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.xaxis.offsetText.set_visible(False)


# Mostrar la figura
plt.show()