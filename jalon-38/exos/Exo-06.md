---
uuid: "jalon-38-exo-06"
title: "Exercice 6 : Intégrale de Gauss tronquée"
tags:
  - math/analyse
  - ia/calcul-differentiel
---

# Exercice 6

**Difficulté :** ★★★☆☆

**Énoncé :**
Calculer l'intégrale $N = \int_0^1 t^3 e^{-t^2} \, dt$ via un changement de variable suivi d'une IPP.

**Correction détaillée :**
1. La fonction $t \mapsto t^3 e^{-t^2}$ est continue sur $[0, 1]$.
2. Commençons par un changement de variable pour simplifier l'exposant. Posons $u = t^2$.
3. La fonction $\varphi : t \mapsto t^2$ est de classe $\mathcal{C}^1$ strictement croissante sur $[0, 1]$.
4. On a $du = 2t \, dt$.
5. Modifions l'intégrande pour faire apparaître le terme $2t \, dt$ :
$$ t^3 e^{-t^2} \, dt = t^2 e^{-t^2} (t \, dt) = t^2 e^{-t^2} \left(\frac{1}{2} (2t \, dt)\right) $$
6. Les bornes deviennent : si $t=0$, $u=0$. Si $t=1$, $u=1$.
7. L'intégrale devient :
$$ N = \int_0^1 u e^{-u} \frac{1}{2} \, du = \frac{1}{2} \int_0^1 u e^{-u} \, du $$
8. Nous devons maintenant calculer l'intégrale $\int_0^1 u e^{-u} \, du$ par IPP.
9. Posons $f(u) = u$ et $g'(u) = e^{-u}$. Alors $f'(u) = 1$ et $g(u) = -e^{-u}$.
10. La formule d'IPP donne :
$$ \int_0^1 u e^{-u} \, du = [u(-e^{-u})]_0^1 - \int_0^1 1 \cdot (-e^{-u}) \, du $$
11. Évaluons le crochet : $[ -u e^{-u} ]_0^1 = -1 \cdot e^{-1} - (-0) = -e^{-1}$.
12. Évaluons l'intégrale restante : $\int_0^1 e^{-u} \, du = [-e^{-u}]_0^1 = -e^{-1} - (-e^0) = 1 - e^{-1}$.
13. Sommons :
$$ \int_0^1 u e^{-u} \, du = -e^{-1} + (1 - e^{-1}) = 1 - 2e^{-1} = 1 - \frac{2}{e} $$
14. N'oublions pas le facteur $\frac{1}{2}$ issu du changement de variable :
$$ N = \frac{1}{2} \left( 1 - \frac{2}{e} \right) = \frac{1}{2} - \frac{1}{e} $$
$\blacksquare$
