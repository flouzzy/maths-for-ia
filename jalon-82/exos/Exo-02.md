\subsection*{Exercice 2 : Linéarité des distributions \quad $\bigstar\bigstar\star\star\star$}

**Énoncé :**
Soit $T = 4\delta_0 - 5\delta_1 + 2\delta_{-1}$. Calculer $\langle T, \phi \rangle$ où $\phi(x) = e^x \cos(\pi x)$.

**Correction :**
Par définition, l'espace des distributions $\mathcal{D}'(\mathbb{R})$ est un espace vectoriel, l'action sur une fonction test est linéaire.
$$\langle T, \phi \rangle = \langle 4\delta_0 - 5\delta_1 + 2\delta_{-1}, \phi \rangle$$
Par linéarité de l'application $\phi \mapsto \langle \cdot, \phi \rangle$ :
$$\langle T, \phi \rangle = 4\langle \delta_0, \phi \rangle - 5\langle \delta_1, \phi \rangle + 2\langle \delta_{-1}, \phi \rangle$$
On applique la définition du Dirac :
$$\langle T, \phi \rangle = 4\phi(0) - 5\phi(1) + 2\phi(-1)$$
Calculons les valeurs de $\phi$ :
$\phi(0) = e^0 \cos(0) = 1 \cdot 1 = 1$
$\phi(1) = e^1 \cos(\pi) = e \cdot (-1) = -e$
$\phi(-1) = e^{-1} \cos(-\pi) = \frac{1}{e} \cdot (-1) = -\frac{1}{e}$
En substituant :
$$\langle T, \phi \rangle = 4(1) - 5(-e) + 2\left(-\frac{1}{e}\right) = 4 + 5e - \frac{2}{e}$$
