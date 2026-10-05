# Exercice 1 : Action d'une distribution régulière simple
**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé
Soit $f(x) = x^2$ sur $\mathbb{R}$. Calculer l'action de la distribution régulière associée $T_f$ sur la fonction test $\varphi \in \mathcal{D}(\mathbb{R})$ définie par $\varphi(x) = 1 - x^2$ pour $x \in [-1, 1]$ et $0$ ailleurs.

## Correction Détaillée
1. La fonction $f$ est continue sur $\mathbb{R}$, elle est donc localement intégrable ($L^1_{loc}(\mathbb{R})$). Elle définit bien une distribution régulière $T_f$.
2. Par définition, l'action de $T_f$ sur $\varphi$ est donnée par :
   $$ \langle T_f, \varphi \rangle = \int_{\mathbb{R}} f(x)\varphi(x) \,dx $$
3. Puisque le support de $\varphi$ est inclus dans $[-1, 1]$, l'intégrale se réduit à cet intervalle :
   $$ \langle T_f, \varphi \rangle = \int_{-1}^{1} x^2 (1 - x^2) \,dx $$
4. Développons l'intégrand : $x^2 (1 - x^2) = x^2 - x^4$.
5. La fonction à intégrer est paire, et l'intervalle est symétrique, donc :
   $$ \langle T_f, \varphi \rangle = 2 \int_{0}^{1} (x^2 - x^4) \,dx $$
6. Calculons les primitives : la primitive de $x^2$ est $\frac{x^3}{3}$ et celle de $x^4$ est $\frac{x^5}{5}$.
7. Évaluons aux bornes :
   $$ \langle T_f, \varphi \rangle = 2 \left[ \frac{x^3}{3} - \frac{x^5}{5} \right]_0^1 = 2 \left( \frac{1}{3} - \frac{1}{5} \right) $$
8. Réduction au même dénominateur :
   $$ \frac{1}{3} - \frac{1}{5} = \frac{5 - 3}{15} = \frac{2}{15} $$
9. Finalement, en multipliant par 2 :
   $$ \langle T_f, \varphi \rangle = \frac{4}{15} $$
