import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig =plt.figure(figsize=(8,6))

t = np.linspace(0,2,500)                
K = 9 * pow(10,9)                       # Constante
A = 0.01                                # Amplitud
d = 2                                   # Distancia
Q = q = pow(10,-6)                      # Carga Electrica
m = 9.11 * pow(10,-31)                  # Masa

w = np.sqrt((16*K*Q*q)/(m*pow(d,3)))    # Velocidad Angular

def animate(dt):
    fig.clear()
    ax = fig.add_subplot()
    ax.plot(0,d/2,'ro')
    ax.plot(0,-d/2,'ro')
    X = A*np.cos(w*t[dt]*pow(10,-10))
    Y = np.zeros_like(X)
    ax.plot(X, Y, 'bo')
    ax.set_xlim(-A-0.0025, A+0.0025)
    ax.set_ylim(-d, d)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"Posición en x = {X:.3f} en el tiempo t = {t[dt]:.2f}"+r"$\times$ $10^{-10}$")
    ax.grid()


anim = FuncAnimation(fig, animate, len(t))
anim.save("animacion.mp4", fps=15, dpi = 300)
