# Exercice 6 : Lemme de Borel-Cantelli : Preuve élémentaire \quad $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé. Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'événements.
On définit la limite supérieure des ensembles : $\limsup A_n = \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty A_k$.
Montrer rigoureusement (premier lemme de Borel-Cantelli) que si $\sum_{n=1}^\infty \mathbb{P}(A_n) < +\infty$, alors $\mathbb{P}(\limsup A_n) = 0$.

## Correction Détaillée
### Étape 1 : Comprendre l'événement limite supérieure
L'événement $A^* = \limsup A_n$ est l'ensemble des $\omega \in \Omega$ qui appartiennent à une infinité d'événements $A_n$. Formellement :
$$ A^* = \bigcap_{n=1}^\infty B_n \quad \text{avec} \quad B_n = \bigcup_{k=n}^\infty A_k $$
La suite d'ensembles $(B_n)$ est décroissante car $B_{n+1} \subset B_n$ (l'union porte sur moins d'ensembles).

### Étape 2 : Continuité décroissante de la probabilité
Par la propriété de continuité décroissante de la mesure de probabilité sur des ensembles emboîtés ($B_1 \supset B_2 \supset B_3 \dots$) :
$$ \mathbb{P}(A^*) = \mathbb{P}\left( \bigcap_{n=1}^\infty B_n \right) = \lim_{n \to \infty} \mathbb{P}(B_n) $$

### Étape 3 : Majoration par la somme (Sous-additivité)
Pour tout entier $n$, par l'axiome de sous-additivité de la probabilité ($\sigma$-sous-additivité) :
$$ \mathbb{P}(B_n) = \mathbb{P}\left( \bigcup_{k=n}^\infty A_k \right) \le \sum_{k=n}^\infty \mathbb{P}(A_k) $$

### Étape 4 : Conclusion par la convergence de la série
Par hypothèse, la série $\sum_{k=1}^\infty \mathbb{P}(A_k)$ est convergente (sa somme est finie).
Le reste d'une série convergente tend nécessairement vers zéro. Donc :
$$ \lim_{n \to \infty} \sum_{k=n}^\infty \mathbb{P}(A_k) = 0 $$
Comme $0 \le \mathbb{P}(B_n) \le \sum_{k=n}^\infty \mathbb{P}(A_k)$, par le théorème des gendarmes, $\lim_{n \to \infty} \mathbb{P}(B_n) = 0$.
Finalement, par l'Étape 2, on conclut que $\mathbb{P}(A^*) = \mathbb{P}(\limsup A_n) = 0$. $\blacksquare$
