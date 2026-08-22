# Exercice 1 : Intégrale d'une fonction étagée simple $\bigstar$

**Énoncé :**
Sur l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$, calculer l'intégrale de Lebesgue de la fonction $f$ définie par :
$f(x) = 3$ si $x \in [-1, 2]$, $f(x) = 7$ si $x \in \{4, 5, 6\}$, $f(x) = 2$ si $x \in [10, 11[$, et $f(x) = 0$ sinon.

**Correction Détaillée :**
1. La fonction $f$ ne prend qu'un nombre fini de valeurs positives, c'est donc une fonction étagée positive.
2. Sa forme canonique est $f = 3 \cdot \mathbf{1}_{[-1, 2]} + 7 \cdot \mathbf{1}_{\{4, 5, 6\}} + 2 \cdot \mathbf{1}_{[10, 11[} + 0 \cdot \mathbf{1}_{A^c}$ avec $A$ l'union des trois sous-ensembles précédents.
3. L'intégrale de $f$ est la somme des valeurs multipliées par la mesure de Lebesgue des ensembles associés :
   $$\int_{\mathbb{R}} f \, d\lambda = 3 \cdot \lambda([-1, 2]) + 7 \cdot \lambda(\{4, 5, 6\}) + 2 \cdot \lambda([10, 11[)$$
4. On calcule les mesures des boréliens :
   - $\lambda([-1, 2]) = 2 - (-1) = 3$.
   - L'ensemble $\{4, 5, 6\}$ est fini (ou dénombrable), donc $\lambda(\{4, 5, 6\}) = 0$.
   - $\lambda([10, 11[) = 11 - 10 = 1$.
5. On remplace dans l'équation :
   $$\int_{\mathbb{R}} f \, d\lambda = 3 \times 3 + 7 \times 0 + 2 \times 1 = 9 + 0 + 2 = 11$$
