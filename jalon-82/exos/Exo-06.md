\subsection*{Exercice 6 : Multiplication par une fonction de classe C-infini \quad $\bigstar\bigstar\bigstar\star\star$}

Soit $T \in \mathcal{D}'(\mathbb{R})$ et $\alpha \in \mathcal{C}^\infty(\mathbb{R})$.
1. Comment définir l'action de la distribution $\alpha T$ sur une fonction test $\phi$ ?
2. Montrer que l'équation $x T = 0$ admet pour solution générale $T = c \delta_0$ (où $c$ est une constante complexe).

**Correction Détaillée :**
1. Si $T$ était une distribution régulière associée à $f \in L^1_{loc}$, l'action serait :
$\langle \alpha T_f, \phi \rangle = \int (\alpha(x) f(x)) \phi(x) dx = \int f(x) (\alpha(x) \phi(x)) dx$.
Pour que cette forme intégrale s'étende aux distributions, il faut que $\alpha \phi$ soit une fonction test. Comme $\phi \in \mathcal{D}(\mathbb{R})$ (elle est $\mathcal{C}^\infty$ à support compact) et $\alpha \in \mathcal{C}^\infty(\mathbb{R})$, le produit $\alpha \phi$ reste $\mathcal{C}^\infty$ et le support de $\alpha \phi$ est inclus dans le support de $\phi$, donc compact.
On définit formellement : $\langle \alpha T, \phi \rangle = \langle T, \alpha \phi \rangle$.
2. L'équation est $x T = 0$, ce qui signifie que pour tout $\phi \in \mathcal{D}(\mathbb{R})$, $\langle x T, \phi \rangle = 0$, soit $\langle T, x\phi \rangle = 0$.
Soit une fonction test $\phi$. On peut écrire $\phi(x) = \phi(0)\theta(x) + x \psi(x)$ où $\theta \in \mathcal{D}(\mathbb{R})$ est une fonction test valant $1$ au voisinage de $0$, et $\psi \in \mathcal{D}(\mathbb{R})$.
En effet, $\psi(x) = \frac{\phi(x) - \phi(0)\theta(x)}{x}$. Par le théorème de Taylor, cette fonction est bien prolongeable par continuité (et régularité $\mathcal{C}^\infty$) en $0$.
Appliquons $T$ :
$\langle T, \phi \rangle = \langle T, \phi(0)\theta \rangle + \langle T, x\psi \rangle$
Par hypothèse, $\langle T, x\psi \rangle = \langle xT, \psi \rangle = 0$.
Ainsi, $\langle T, \phi \rangle = \phi(0) \langle T, \theta \rangle$.
La quantité $\langle T, \theta \rangle$ est une constante fixe que nous noterons $c$.
D'où $\langle T, \phi \rangle = c \phi(0) = \langle c \delta_0, \phi \rangle$.
La solution est bien $T = c \delta_0$. $\blacksquare$
