# Exercice 6 : L'invariance par translation du non-mesurable

**Difficulté :** $\displaystyle \\bigstar\\bigstar\\bigstar$

## Énoncé

Montrer que si $E$ n'est pas mesurable, alors pour tout réel $x$, $E+x$ n'est pas mesurable.

## Correction Détaillée

1. Raisonnons par l'absurde. Supposons qu'il existe un $x$ tel que $E+x$ soit mesurable.
2. La tribu de Lebesgue $\mathcal{L}(\mathbb{R})$ et la mesure sont invariantes par translation.
3. Si $E+x$ est mesurable, alors son translaté par $-x$ doit aussi être mesurable.
4. L'ensemble $(E+x) + (-x) = E$ serait donc mesurable, ce qui contredit l'hypothèse de départ.
5. De façon plus détaillée via le critère de Carathéodory : si $E$ ne le vérifie pas pour un ensemble de test $A$ ($\lambda^*(A) \neq \lambda^*(A \cap E) + \lambda^*(A \setminus E)$), alors en translatant tout par $x$, on obtient que $E+x$ ne vérifie pas le critère pour l'ensemble de test $A+x$. En effet, les intersections sont préservées : $(A+x) \cap (E+x) = (A \cap E) + x$. Et $\lambda^*$ est invariante par translation.
