# Exercice 6

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Défaut d'indépendance

Sur l'espace de probabilité $\Omega = [0, 1]$ muni de la mesure de Lebesgue $\lambda$, on définit la suite d'événements $A_n = [0, \frac{1}{n}]$.
Montrer par le calcul direct que $\lambda(\limsup A_n) = 0$ et vérifier la cohérence avec le lemme de Borel-Cantelli. Les événements sont-ils indépendants ?

**Correction détaillée :**
1. Calcul de $\limsup A_n$ : Par définition, $B_n = \bigcup_{k=n}^{\infty} A_k = \bigcup_{k=n}^{\infty} [0, \frac{1}{k}] = [0, \frac{1}{n}]$ car $[0, \frac{1}{k}] \subset [0, \frac{1}{n}]$ pour $k \ge n$.
2. Ensuite, $\limsup A_n = \bigcap_{n=1}^{\infty} B_n = \bigcap_{n=1}^{\infty} [0, \frac{1}{n}] = \{0\}$.
3. La mesure de probabilité de ce singleton est $\lambda(\{0\}) = 0$.
4. Cohérence avec Borel-Cantelli : $\mathbb{P}(A_n) = \frac{1}{n}$. La série $\sum \mathbb{P}(A_n) = \sum \frac{1}{n} = +\infty$ diverge.
5. On observe que la série des probabilités diverge, mais que la probabilité de la limite supérieure est 0. Ce résultat serait en contradiction avec le second lemme si les hypothèses de ce dernier étaient satisfaites.
6. L'hypothèse manquante est l'indépendance. En effet, $\lambda(A_1 \cap A_2) = \lambda([0, 1] \cap [0, \frac{1}{2}]) = \lambda([0, \frac{1}{2}]) = \frac{1}{2}$, tandis que $\lambda(A_1)\lambda(A_2) = 1 \times \frac{1}{2} = \frac{1}{2}$.
7. Cependant, testons $A_2$ et $A_3$ : $\lambda(A_2 \cap A_3) = \lambda([0, \frac{1}{3}]) = \frac{1}{3}$. D'autre part, $\lambda(A_2)\lambda(A_3) = \frac{1}{2} \times \frac{1}{3} = \frac{1}{6}$.
8. Comme $\frac{1}{3} \neq \frac{1}{6}$, les événements ne sont pas indépendants. L'impossibilité d'appliquer le second lemme est donc normale.
