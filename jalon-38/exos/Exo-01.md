---
uuid: "jalon-38-exo-01"
title: "Exercice 1 : Intégration par parties simple"
tags:
  - math/analyse
  - ia/calcul-differentiel
---

# Exercice 1

**Difficulté :** ★☆☆☆☆

**Énoncé :**
Calculer de manière rigoureuse l'intégrale $I = \int_0^\pi x \cos(x) \, dx$.

**Correction détaillée :**
1. La fonction $x \mapsto x \cos(x)$ est le produit de deux fonctions continues sur $\mathbb{R}$, elle est donc continue sur le segment $[0, \pi]$. Ainsi, elle est Riemann-intégrable.
2. Nous allons utiliser une intégration par parties. Rappel du théorème : soient $u$ et $v$ deux fonctions de classe $\mathcal{C}^1$ sur $[a, b]$, alors $\int_a^b u'(t) v(t) \, dt = [u(t)v(t)]_a^b - \int_a^b u(t) v'(t) \, dt$.
3. Posons $u(x) = x$ et $v'(x) = \cos(x)$.
4. Ces deux fonctions sont indéfiniment dérivables, donc de classe $\mathcal{C}^1$ sur $[0, \pi]$.
5. On a $u'(x) = 1$. Une primitive évidente de $v'$ est $v(x) = \sin(x)$.
6. En appliquant la formule de l'intégration par parties :
$$ I = [x \sin(x)]_0^\pi - \int_0^\pi 1 \cdot \sin(x) \, dx $$
7. Évaluons le crochet entre les bornes $0$ et $\pi$ :
$$ [x \sin(x)]_0^\pi = \pi \sin(\pi) - 0 \cdot \sin(0) = \pi \times 0 - 0 = 0 $$
8. Calculons maintenant l'intégrale restante :
$$ \int_0^\pi \sin(x) \, dx = [-\cos(x)]_0^\pi = -\cos(\pi) - (-\cos(0)) = -(-1) - (-1) = 1 + 1 = 2 $$
9. Finalement, en combinant les deux résultats :
$$ I = 0 - 2 = -2 $$
$\blacksquare$
