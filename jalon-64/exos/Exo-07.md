# Exercice 7 : Ensemble de mesure nulle dense

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

Démontrer qu'il existe un ouvert $U$ de $\mathbb{R}$, dense dans $\mathbb{R}$, mais de mesure arbitrairement petite $\lambda(U) \le \epsilon$.

**Correction Détaillée :**
L'ensemble $\mathbb{Q}$ est dénombrable et dense. Posons $\mathbb{Q} = \{q_1, q_2, \dots\}$.
Soit $\epsilon > 0$. Pour chaque $q_n$, définissons l'intervalle ouvert $I_n = \left]q_n - \frac{\epsilon}{2^{n+1}}, q_n + \frac{\epsilon}{2^{n+1}}\right[$.
Soit $U = \bigcup_{n=1}^\infty I_n$.
$U$ est une réunion d'ouverts, donc un ouvert. Puisque $\mathbb{Q} \subset U$ et $\mathbb{Q}$ est dense dans $\mathbb{R}$, $U$ est également dense dans $\mathbb{R}$.
La mesure de Lebesgue possède la propriété de sous-additivité dénombrable :
$$\lambda(U) \le \sum_{n=1}^\infty \lambda(I_n) = \sum_{n=1}^\infty \frac{\epsilon}{2^n} = \epsilon$$
On a donc construit un ouvert dense qui contient tous les rationnels mais dont la taille totale est inférieure à $\epsilon$.
