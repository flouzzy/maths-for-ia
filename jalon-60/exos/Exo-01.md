## Exercice 1 : Approximation d'une fonction constante \quad $\star\star\star\star\star$

Montrer qu'un réseau de neurones avec une seule couche cachée, utilisant la fonction sigmoïde $\sigma(x) = \frac{1}{1 + e^{-x}}$, peut représenter exactement une fonction constante arbitraire $c \in \mathbb{R}$.

**Correction :**
Soit $f(x) = c$. Considérons le réseau $G(x) = \alpha \sigma(w x + b)$.
On choisit $w = 0$. Alors $G(x) = \alpha \sigma(b) = \alpha \frac{1}{1 + e^{-b}}$.
Pour obtenir $G(x) = c$, on peut fixer $b = 0$, ce qui donne $\sigma(0) = \frac{1}{2}$.
Il suffit alors de choisir $\alpha = 2c$.
Ainsi, le réseau $G(x) = 2c \cdot \sigma(0 \cdot x + 0)$ représente exactement et uniformément la constante $c$ sur n'importe quel domaine.
