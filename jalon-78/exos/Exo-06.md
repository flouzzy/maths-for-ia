## Exercice 6 : Équation différentielle et Fourier \quad \bigstar\bigstar\bigstar\bigstar\star

Résoudre l'équation différentielle $y''(x) + 2y(x) = f(x)$ sur $\mathbb{R}$ en cherchant des solutions $2\pi$-périodiques, avec $f$ une fonction $2\pi$-périodique donnée de classe $C^1$.

**Correction :**
On suppose $y$ solution de classe $C^2$ périodique.
Décomposons en série de Fourier complexe : $y(x) = \sum c_n(y)e^{inx}$, $f(x) = \sum c_n(f)e^{inx}$.
$y''(x)$ a pour coefficients $(in)^2 c_n(y) = -n^2 c_n(y)$.
L'équation devient $-n^2 c_n(y) + 2c_n(y) = c_n(f)$ pour tout $n$.
$(2-n^2)c_n(y) = c_n(f)$. Puisque $n$ est entier, $2-n^2 \neq 0$ pour tout $n$.
Donc $c_n(y) = \frac{c_n(f)}{2-n^2}$.
La série $y(x) = \sum_{n \in \mathbb{Z}} \frac{c_n(f)}{2-n^2} e^{inx}$ est solution (la régularité est assurée par la décroissance de $c_n(f)$).
