# Exercice 3 : Mesure extérieure d'une union finie disjointe

**Difficulté :** $\bigstar\bigstar\star\star\star$

Soit $I$ et $J$ deux intervalles ouverts bornés disjoints. Montrer à l'aide de la définition que $\lambda^*(I \cup J) = \ell(I) + \ell(J)$.

**Correction Détaillée :**
Soit $I = ]a, b[$ et $J = ]c, d[$. Sans perte de généralité, supposons $b \le c$.
Par sous-additivité dénombrable, $\lambda^*(I \cup J) \le \lambda^*(I) + \lambda^*(J) = \ell(I) + \ell(J)$.
Pour l'inégalité inverse, soit $(U_n)$ un recouvrement de $I \cup J$ par des intervalles ouverts.
Comme $I$ et $J$ sont séparés par une distance positive si $b < c$, ou bien disjoints si $b=c$, on peut séparer le recouvrement en deux sous-recouvrements, l'un pour $I$ et l'autre pour $J$ (en scindant éventuellement un intervalle recouvrant la jointure).
Ainsi, $\sum \ell(U_n) \ge \ell(I) + \ell(J)$. En passant à l'infimum, $\lambda^*(I \cup J) \ge \ell(I) + \ell(J)$.
D'où l'égalité.
