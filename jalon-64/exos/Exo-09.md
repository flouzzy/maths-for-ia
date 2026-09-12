# Exercice 9 : La propriété de régularité de la mesure de Lebesgue

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $E \in \mathcal{L}(\mathbb{R})$. Démontrer que $\lambda(E) = \inf\{\lambda(U) \mid E \subset U, \ U \text{ ouvert}\}$.

**Correction Détaillée :**
Si $\lambda(E) = +\infty$, le résultat est trivial. Supposons $\lambda(E)$ finie.
Par définition de la mesure extérieure $\lambda^*(E) = \lambda(E)$, pour tout $\epsilon > 0$, il existe un recouvrement dénombrable ouvert $(I_n)$ de $E$ tel que $\sum \ell(I_n) \le \lambda(E) + \epsilon$.
Posons $U = \bigcup I_n$. $U$ est un ouvert et $E \subset U$.
Par sous-additivité, $\lambda(U) = \lambda(\bigcup I_n) \le \sum \lambda(I_n) \le \lambda(E) + \epsilon$.
Ainsi, on a trouvé un ouvert contenant $E$ dont la mesure approche arbitrairement celle de $E$.
Par monotonie, $\lambda(E) \le \lambda(U)$, donc l'infimum est exactement $\lambda(E)$.
