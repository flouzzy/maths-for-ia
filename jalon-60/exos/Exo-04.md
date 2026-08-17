## Exercice 4 : Approximation d'un pulse carré (créneau) \quad $\bigstar\bigstar\star\star\star$

Montrer comment approcher la fonction porte (créneau) $f(x) = 1$ si $x \in [-1, 1]$ et $0$ sinon, avec des sigmoïdes. L'approximation doit être arbitrairement proche pour tout $|x| \neq 1$.

**Correction :**
Posons $G_k(x) = \sigma(k(x+1)) - \sigma(k(x-1))$.
Pour $x < -1$, $k(x+1) \to -\infty$ et $k(x-1) \to -\infty$ quand $k \to +\infty$. Donc $\sigma \to 0$ pour les deux, et $G_k(x) \to 0$.
Pour $-1 < x < 1$, $k(x+1) \to +\infty$ et $k(x-1) \to -\infty$. Donc le premier terme tend vers 1 et le second vers 0. $G_k(x) \to 1$.
Pour $x > 1$, $k(x+1) \to +\infty$ et $k(x-1) \to +\infty$. Les deux termes tendent vers 1, la différence tend vers 0.
En choisissant $k$ assez grand, la fonction $G_k(x)$ approche arbitrairement près la porte, sauf aux discontinuités $x = -1$ et $x = 1$. L'approximation en norme $L^p$ (ou uniforme sur tout sous-compact disjoint de $\{-1, 1\}$) est valide.
