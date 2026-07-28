---
uuid: "jalon-38-exo-07"
title: "Exercice 7 : Astuce de la dérivée de la fonction réciproque"
tags:
  - math/analyse
  - ia/calcul-differentiel
---

# Exercice 7

**Difficulté :** ★★★★☆

**Énoncé :**
Calculer l'intégrale $P = \int_0^1 \arcsin(x) \, dx$ en utilisant une intégration par parties astucieuse.

**Correction détaillée :**
1. La fonction $x \mapsto \arcsin(x)$ est continue sur $[-1, 1]$, et donc Riemann-intégrable sur $[0, 1]$.
2. Cette fonction n'admet pas de primitive évidente. Nous allons forcer l'apparition d'un produit pour appliquer une IPP.
3. Écrivons $\arcsin(x) = 1 \cdot \arcsin(x)$.
4. Posons $u'(x) = 1$ et $v(x) = \arcsin(x)$.
5. Les fonctions sont dérivables (sauf en 1 pour arcsin, mais l'intégrale est généralisée convergente, et on peut procéder sur $[0, 1-\epsilon]$ puis passer à la limite, ou utiliser le formalisme pur de Lebesgue. En Riemann, la fonction est continue sur le fermé $[0, 1]$, l'intégrale existe). On prend $u(x) = x$ et $v'(x) = \frac{1}{\sqrt{1 - x^2}}$.
6. Appliquons la formule d'IPP :
$$ P = [x \arcsin(x)]_0^1 - \int_0^1 x \frac{1}{\sqrt{1 - x^2}} \, dx $$
7. Évaluons le crochet : $[x \arcsin(x)]_0^1 = 1 \cdot \arcsin(1) - 0 \cdot \arcsin(0) = 1 \cdot \frac{\pi}{2} - 0 = \frac{\pi}{2}$.
8. Calculons la nouvelle intégrale $P_1 = \int_0^1 \frac{x}{\sqrt{1 - x^2}} \, dx$.
9. Posons $w = 1 - x^2$. Alors $dw = -2x \, dx$, soit $x \, dx = -\frac{1}{2} dw$.
10. Les bornes : si $x=0$, $w=1$. Si $x=1$, $w=0$.
11. L'intégrale devient :
$$ P_1 = \int_1^0 \frac{1}{\sqrt{w}} \left(-\frac{1}{2}\right) dw = \frac{1}{2} \int_0^1 w^{-1/2} dw $$
(En inversant les bornes pour absorber le signe moins).
12. Une primitive de $w^{-1/2}$ est $2w^{1/2} = 2\sqrt{w}$.
13. Évaluation : $P_1 = \frac{1}{2} [2\sqrt{w}]_0^1 = \frac{1}{2} (2\sqrt{1} - 2\sqrt{0}) = 1$.
14. Finalement, en réinjectant dans l'équation de $P$ :
$$ P = \frac{\pi}{2} - P_1 = \frac{\pi}{2} - 1 $$
$\blacksquare$
