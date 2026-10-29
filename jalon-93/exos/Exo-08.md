# Exercice 08 : Symétrisation
Difficulté : $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $X$ une variable aléatoire. Soit $X'$ une copie indépendante de $X$ (donc $X$ et $X'$ sont i.i.d.).
On pose $Y = X - X'$, appelée la symétrisée de $X$.
1. Exprimer $\phi_Y(t)$ en fonction de $\phi_X(t)$.
2. Montrer que $\phi_Y(t) = |\phi_X(t)|^2$. En déduire que $\phi_Y(t)$ est réelle et positive.
3. Quelle est la loi de $Y$ si $X \sim \mathcal{E}(\lambda)$ (loi exponentielle) ?

**Correction pas à pas :**
1. $Y$ est la somme de $X$ et de $-X'$. Par indépendance de $X$ et $X'$,
   $\phi_Y(t) = \phi_{X+(-X')}(t) = \phi_X(t) \cdot \phi_{-X'}(t)$.
2. Calculons $\phi_{-X'}(t)$ :
   $\phi_{-X'}(t) = \mathbb{E}[e^{it(-X')}] = \mathbb{E}[e^{i(-t)X'}] = \phi_{X'}(-t)$.
   Comme $X$ et $X'$ ont la même loi, $\phi_{X'}(-t) = \phi_X(-t)$.
   Or, pour toute fonction caractéristique d'une variable réelle, $\phi_X(-t) = \mathbb{E}[e^{-itX}] = \overline{\mathbb{E}[e^{itX}]} = \overline{\phi_X(t)}$.
   Donc $\phi_Y(t) = \phi_X(t) \cdot \overline{\phi_X(t)} = |\phi_X(t)|^2$.
   Le module au carré d'un nombre complexe est toujours un réel positif ou nul.
3. Si $X \sim \mathcal{E}(\lambda)$, on a vu que $\phi_X(t) = \frac{\lambda}{\lambda - it}$.
   Donc $\phi_Y(t) = \left| \frac{\lambda}{\lambda - it} \right|^2 = \frac{\lambda^2}{\lambda^2 + t^2} = \frac{1}{1 + (t/\lambda)^2}$.
   On reconnaît, à un changement d'échelle près, la fonction caractéristique liée à une loi de Laplace (loi double exponentielle).
   En effet, si $Z$ suit une loi de Laplace de densité $f_Z(z) = \frac{\lambda}{2} e^{-\lambda |z|}$, on montre que $\phi_Z(t) = \frac{\lambda^2}{\lambda^2 + t^2}$.
   Donc $Y = X - X'$ suit une loi de Laplace centrée de paramètre $\lambda$.
