import numpy as np
import matplotlib.pylab as plt

k = np.linspace(-np.pi / 2, np.pi / 2, 1000)

def E(k, t = 2.5, delta = 0.5):
    epsilon = 2 * t * np.cos(k)
    Delta = 2 * delta * np.sin(k)
    return np.sqrt(epsilon**2 + Delta**2)

plt.plot(k, E(k), label = "LUMO")
plt.plot(k, -E(k), label = "HOMO")

plt.legend(loc = "best", prop = {'size' : 25})
plt.xticks([-np.pi/2, 0, np.pi/2], \
           [r"$\frac{-\pi}{2a}$", 0, r"$\frac{\pi}{2a}$"], size = 25)
plt.yticks([-5, -1, 0, 1, 5], \
           [r"$-2t$",r"$-2\delta$",r"0",r"$2\delta$",r"$2t$",], size = 25)
plt.xlabel(r"$k$", size = 25)
plt.ylabel(r"$E_k$", size = 25)
plt.grid()
plt.tight_layout()
plt.savefig("bandstructure_with_gap.pdf")
plt.show()

plt.plot(k, E(k, delta = 0), label = "LUMO")
plt.plot(k, -E(k, delta = 0), label = "HOMO")

plt.legend(loc = "best", prop = {'size' : 25})
plt.xticks([-np.pi/2, 0, np.pi/2], \
           [r"$\frac{-\pi}{2a}$", 0, r"$\frac{\pi}{2a}$"], size = 25)
plt.yticks([-5, 0, 5], \
           [r"$-2t$",r"0",r"$2t$",], size = 25)
plt.xlabel(r"$k$", size = 25)
plt.ylabel(r"$E_k$", size = 25)
plt.grid()
plt.tight_layout()
plt.savefig("bandstructure_without_gap.pdf")
plt.show()
