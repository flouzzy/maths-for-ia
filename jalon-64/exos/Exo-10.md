# Exercice 10 : Mesure d'une boule dans un espace normé et homothétie

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $E \subset \mathbb{R}^n$ un ensemble mesurable de mesure finie (mesure de Lebesgue $n$-dimensionnelle). Soit $c > 0$ et $cE = \{cx \mid x \in E\}$ l'image de $E$ par homothétie. Démontrer analytiquement que $\lambda_n(cE) = c^n \lambda_n(E)$.

**Correction Détaillée :**
On démontre d'abord la propriété pour un pavé élémentaire $P = [a_1, b_1] \times \dots \times [a_n, b_n]$.
$cP = [ca_1, cb_1] \times \dots \times [ca_n, cb_n]$.
La mesure de $cP$ est $\lambda_n(cP) = \prod_{i=1}^n (cb_i - ca_i) = c^n \prod_{i=1}^n (b_i - a_i) = c^n \lambda_n(P)$.
Puisque la propriété est vraie pour les pavés, elle s'étend par additivité aux réunions finies de pavés disjoints (ensembles élémentaires).
Tout ouvert peut être approché par une réunion dénombrable de pavés disjoints.
Ensuite, pour tout ensemble $A \subset \mathbb{R}^n$, la mesure extérieure est définie via les recouvrements par des pavés ouverts.
Si $(P_k)$ recouvre $A$, alors $(cP_k)$ recouvre $cA$.
Ainsi, $\lambda_n^*(cA) \le \sum \lambda_n(cP_k) = c^n \sum \lambda_n(P_k)$. En prenant l'infimum, $\lambda_n^*(cA) \le c^n \lambda_n^*(A)$.
En appliquant le même raisonnement avec l'homothétie de rapport $1/c$ sur l'ensemble $cA$, on obtient l'inégalité inverse.
D'où l'égalité $\lambda_n(cE) = c^n \lambda_n(E)$.
