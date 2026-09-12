## Mesurabilité d'une fonction constante \quad $\bigstar\star\star\star\star$

Soit $(X, \mathcal{F})$ un espace mesurable. Soit $c \in \mathbb{R}$. Démontrez formellement que la fonction constante $f(x) = c$ pour tout $x \in X$ est mesurable.

### Correction Détaillée

Soit $B \in \mathcal{B}(\mathbb{R})$ un ensemble borélien quelconque de $\mathbb{R}$.
Par définition de la mesurabilité, il faut montrer que $f^{-1}(B) = \{x \in X \mid f(x) \in B\} \in \mathcal{F}$.

Puisque $f(x) = c$ pour tout $x \in X$, la valeur de $f(x)$ ne dépend pas de $x$. Nous devons distinguer deux cas selon que $c$ appartient ou non à $B$ :

1. **Cas 1 : $c \in B$.**
   Puisque $f(x) = c$ pour tout $x$, et que $c \in B$, alors pour tout $x \in X$, la condition $f(x) \in B$ est vérifiée.
   Ainsi, $f^{-1}(B) = X$.
   Par définition d'une tribu, $X \in \mathcal{F}$.

2. **Cas 2 : $c \notin B$.**
   Puisque $f(x) = c$ pour tout $x$, et que $c \notin B$, il n'existe aucun $x \in X$ tel que $f(x) \in B$.
   Ainsi, $f^{-1}(B) = \emptyset$.
   Par définition d'une tribu, $\emptyset \in \mathcal{F}$.

Dans tous les cas possibles, l'image réciproque de $B$ par $f$ appartient à la tribu $\mathcal{F}$.
Conclusion : La fonction constante $f$ est strictement mesurable.
