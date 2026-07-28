---
uuid: "jalon-38-exo-02"
title: "Exercice 2 : Changement de variable affine"
tags:
  - math/analyse
  - ia/calcul-differentiel
---

# Exercice 2

**Difficulté :** ★☆☆☆☆

**Énoncé :**
Calculer l'intégrale $J = \int_0^1 (2x + 1)^4 \, dx$ en utilisant un changement de variable.

**Correction détaillée :**
1. Soit la fonction $f(x) = (2x + 1)^4$. C'est une fonction polynomiale, donc continue sur $\mathbb{R}$, et en particulier sur $[0, 1]$. L'intégrale est bien définie.
2. Pour simplifier l'expression à intégrer, nous allons opérer un changement de variable.
3. Posons $u = \varphi(x) = 2x + 1$. La fonction $\varphi$ est de classe $\mathcal{C}^1$ sur $\mathbb{R}$.
4. Calculons la différentielle : $du = \varphi'(x) dx = 2 \, dx$.
5. Pour exprimer $dx$ en fonction de $du$, on obtient $dx = \frac{1}{2} du$.
6. Déterminons les nouvelles bornes d'intégration :
   - Lorsque $x = 0$, $u = 2(0) + 1 = 1$.
   - Lorsque $x = 1$, $u = 2(1) + 1 = 3$.
7. En substituant $2x+1$ par $u$ et $dx$ par $\frac{1}{2} du$ dans l'intégrale, par le théorème de changement de variable, on a :
$$ J = \int_1^3 u^4 \left(\frac{1}{2}\right) du = \frac{1}{2} \int_1^3 u^4 \, du $$
8. Une primitive de la fonction $u \mapsto u^4$ est la fonction $U(u) = \frac{u^5}{5}$.
9. Évaluons cette primitive aux bornes :
$$ \int_1^3 u^4 \, du = \left[ \frac{u^5}{5} \right]_1^3 = \frac{3^5}{5} - \frac{1^5}{5} = \frac{243}{5} - \frac{1}{5} = \frac{242}{5} $$
10. Finalement, on multiplie par le facteur $\frac{1}{2}$ :
$$ J = \frac{1}{2} \times \frac{242}{5} = \frac{121}{5} $$
$\blacksquare$
