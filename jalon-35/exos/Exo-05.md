# Exercice 5 : ★★★

**Énoncé :**
Une intersection infinie d'ouverts n'est pas nécessairement ouverte.

**Correction (Zéro Ellipse) :**
Dans l'espace métrique $\mathbb{R}$ muni de la valeur absolue.
Considérons la famille d'intervalles ouverts $U_n = \left] -\frac{1}{n}, \frac{1}{n} \right[$ pour $n \in \mathbb{N}^*$.
Chaque $U_n$ est une boule ouverte centrée en 0 de rayon $1/n$, c'est donc un ouvert.
Calculons l'intersection infinie $A = \bigcap_{n=1}^\infty U_n$.
- $0 \in U_n$ pour tout $n$, donc $0 \in A$.
- Soit $x \neq 0$. Alors $|x| > 0$. Par la propriété d'Archimède, il existe un entier $N$ tel que $\frac{1}{N} \le |x|$. Donc $x \notin U_N$. Par suite, $x \notin A$.
Ainsi, $A = \{0\}$.
Or, le singleton $\{0\}$ n'est pas ouvert dans $\mathbb{R}$.
Par caractérisation séquentielle : prenons la suite $x_k = \frac{1}{k}$. $x_k \to 0 \in A$. Mais pour tout $k \ge 1$, $x_k \neq 0$, donc $x_k \notin A$. La suite ne finit jamais dans $A$. Donc $\{0\}$ n'est pas ouvert. $\blacksquare$
