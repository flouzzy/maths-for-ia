# Exercice 4 : Boréliens et mesurabilité

**Difficulté :** $\displaystyle \\bigstar\\bigstar\\bigstar$

## Énoncé

Soit $A$ un ouvert de $\mathbb{R}$. Montrer que $A$ est mesurable.

## Correction Détaillée

1. Tout ouvert $A$ de $\mathbb{R}$ peut s'écrire comme une union dénombrable d'intervalles ouverts disjoints : $A = \bigcup I_n$.
2. Il suffit de montrer qu'un intervalle ouvert $I = ]a, b[$ est mesurable.
3. Pour cela, montrons d'abord que $J = [a, \infty[$ est mesurable par le critère de Carathéodory.
Soit $E$ un ensemble de test. Si $\lambda^*(E) = \infty$, l'égalité de Carathéodory est vraie. Supposons $\lambda^*(E) < \infty$.
Pour tout $\epsilon > 0$, il existe un recouvrement de $E$ par des ouverts $O_k$ tels que $\sum \ell(O_k) \le \lambda^*(E) + \epsilon$.
On a $\lambda^*(E \cap J) + \lambda^*(E \setminus J) \le \sum \lambda^*(O_k \cap J) + \sum \lambda^*(O_k \setminus J)$.
Pour un intervalle $O_k$, l'intersection avec un demi-intervalle $J$ donne au pire deux intervalles disjoints dont la somme des longueurs est $\ell(O_k)$.
Donc $\lambda^*(E \cap J) + \lambda^*(E \setminus J) \le \sum \ell(O_k) \le \lambda^*(E) + \epsilon$. Ceci implique la mesurabilité.
4. Les intervalles sont donc mesurables. La tribu de Lebesgue est stable par intersection et passage au complémentaire. Un intervalle $]a, b[ = [a, \infty[ \cap ]-\infty, b[ \setminus \{a\}$ est donc mesurable (les points sont de mesure nulle, donc mesurables).
5. $A$, étant une union dénombrable de mesurables, est mesurable.
