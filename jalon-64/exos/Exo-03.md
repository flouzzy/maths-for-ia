# Exercice 3 : Ensembles denses et mesure

**Difficulté :** $\displaystyle \\bigstar\\bigstar\\bigstar$

## Énoncé

Construire un sous-ensemble ouvert $U$ de $\mathbb{R}$ qui est dense dans $\mathbb{R}$ mais de mesure $\lambda(U) \le 1$.

## Correction Détaillée

Soit $(q_n)_{n \ge 1}$ une énumération des rationnels de $\mathbb{R}$.
Pour chaque entier $n \ge 1$, on pose $I_n = ]q_n - \frac{1}{2^{n+1}}, q_n + \frac{1}{2^{n+1}}[$.
On définit $U = \bigcup_{n=1}^\infty I_n$.
1. **Ouverture :** $U$ est une union d'intervalles ouverts, c'est donc un ouvert de $\mathbb{R}$.
2. **Densité :** Par construction, pour tout $n$, $q_n \in U$. Donc $\mathbb{Q} \subset U$. Or $\mathbb{Q}$ est dense dans $\mathbb{R}$, donc l'adhérence de $U$ est $\mathbb{R}$. $U$ est bien dense.
3. **Mesure :** Par sous-additivité, $\lambda(U) \le \sum_{n=1}^\infty \lambda(I_n) = \sum_{n=1}^\infty \frac{1}{2^n} = 1$.
C'est un exemple fascinant : un ouvert contenant tous les rationnels, dense, mais avec "des trous" irrationnels immenses de mesure infinie en dehors de lui.
