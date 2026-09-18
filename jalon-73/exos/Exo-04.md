# Exercice 4 : La non-inclusion sur $\mathbb{R}$ entier

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

On se place sur $\mathbb{R}$ muni de la mesure de Lebesgue $\lambda$. Contrairement au cas des espaces de mesure finie, les espaces $L^p(\mathbb{R})$ ne s'incluent pas mutuellement.

1. Donner un exemple de fonction $f \in L^1(\mathbb{R})$ telle que $f \notin L^2(\mathbb{R})$.
2. Donner un exemple de fonction $g \in L^2(\mathbb{R})$ telle que $g \notin L^1(\mathbb{R})$.

---

## Correction détaillée

1. **Une fonction dans $L^1$ mais pas dans $L^2$ :**
   Pour être dans $L^1$ mais exploser au carré, la fonction doit présenter une singularité très abrupte mais localisée (intégrable localement pour l'ordre 1, pas pour l'ordre 2).
   Considérons $f(x) = \frac{1}{\sqrt{x}} \mathbf{1}_{]0, 1]}(x)$.
   - Norme $L^1$ : $\int_0^1 x^{-1/2} \, dx = 2 < +\infty \implies f \in L^1(\mathbb{R})$.
   - Norme $L^2$ : $\int_0^1 (x^{-1/2})^2 \, dx = \int_0^1 \frac{1}{x} \, dx = +\infty \implies f \notin L^2(\mathbb{R})$.

2. **Une fonction dans $L^2$ mais pas dans $L^1$ :**
   Pour être dans $L^2$ mais avoir trop de masse à l'infini pour être dans $L^1$, la fonction doit décroître lentement vers 0 à l'infini.
   Considérons $g(x) = \frac{1}{x} \mathbf{1}_{[1, +\infty[}(x)$.
   - Norme $L^2$ : $\int_1^{+\infty} \frac{1}{x^2} \, dx = \left[ -\frac{1}{x} \right]_1^{+\infty} = 0 - (-1) = 1 < +\infty \implies g \in L^2(\mathbb{R})$.
   - Norme $L^1$ : $\int_1^{+\infty} \frac{1}{x} \, dx = \left[ \ln x \right]_1^{+\infty} = +\infty \implies g \notin L^1(\mathbb{R})$.

**Conclusion :** Sur un espace de mesure infinie comme $\mathbb{R}$, il n'y a **aucune inclusion** générale entre $L^p$ et $L^q$ si $p \neq q$. L'intégrabilité dépend à la fois du comportement local (singularités) et asymptotique (à l'infini).
