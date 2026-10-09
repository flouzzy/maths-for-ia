# Exercice 5

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Montrer que l'ensemble des points de convergence (c'est-à-dire l'ensemble des $\omega$ tels que $\lim_{n \to \infty} X_n(\omega)$ existe) d'une suite de variables aléatoires $(X_n)$ est un événement mesurable.

## Correction Détaillée

**Correction de l'exercice 5 :**

1. Une suite réelle $(X_n(\omega))$ converge si et seulement si elle est de Cauchy.
2. Écrivons la propriété de Cauchy avec des quantificateurs sur des rationnels et des entiers (pour obtenir des unions/intersections dénombrables).
3. La suite est de Cauchy si : $\forall \epsilon > 0, \exists N \in \mathbb{N}, \forall p, q \geq N, |X_p - X_q| < \epsilon$.
4. Pour que cela reste dans le domaine du dénombrable, on restreint $\epsilon$ aux rationnels strictement positifs $\mathbb{Q}_+^*$.
5. L'ensemble de convergence $C$ s'écrit donc en termes d'ensembles :
   $C = \bigcap_{\epsilon \in \mathbb{Q}_+^*} \bigcup_{N \in \mathbb{N}} \bigcap_{p, q \geq N} \{\omega \mid |X_p(\omega) - X_q(\omega)| < \epsilon\}$
6. L'application $|X_p - X_q|$ est une variable aléatoire (différence puis valeur absolue de fonctions mesurables).
7. Donc pour tout $\epsilon$, l'ensemble $E_{p,q,\epsilon} = \{\omega \mid |X_p(\omega) - X_q(\omega)| < \epsilon\}$ est mesurable (dans $\mathcal{F}$).
8. L'ensemble $C$ est formé par une suite d'intersections dénombrables, d'unions dénombrables, d'intersections dénombrables d'ensembles mesurables.
9. Comme $\mathcal{F}$ est une tribu, elle est stable par ces opérations dénombrables. Donc $C \in \mathcal{F}$.
$\blacksquare$
