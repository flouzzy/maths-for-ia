## Exercice 7 : Fermeture par la distance \quad $\bigstar\bigstar\bigstar$

**Énoncé :** Démontrer que $x \in \overline{A}$ (l'adhérence de $A$) si et seulement si $d(x, A) = 0$.

**Correction :**
**Sens direct ($\implies$) :** Si $x \in \overline{A}$, alors tout voisinage de $x$ rencontre $A$. Pour tout $\epsilon > 0$, la boule ouverte $B(x, \epsilon)$ contient au moins un point $a \in A$.
Ainsi, pour tout $\epsilon > 0$, il existe $a \in A$ tel que $d(x, a) < \epsilon$.
Cela signifie précisément que l'infimum des distances est inférieur à tout $\epsilon > 0$, soit $d(x, A) = 0$.

**Sens réciproque ($\impliedby$) :** Si $d(x, A) = 0$, alors $\inf_{a \in A} d(x, a) = 0$.
Par la définition de la borne inférieure, pour tout $\epsilon > 0$, il n'est pas possible que $0$ soit le seul minorant ; il existe un élément de l'ensemble strictement inférieur à $0 + \epsilon$.
Donc, il existe $a \in A$ tel que $d(x, a) < \epsilon$.
Ce point $a$ appartient donc à $B(x, \epsilon) \cap A$. Puisque toute boule centrée en $x$ rencontre $A$, $x$ appartient bien à l'adhérence $\overline{A}$ par caractérisation métrique.
