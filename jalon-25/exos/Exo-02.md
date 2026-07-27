---
title: "Exercice 2 : Forme bilinéaire symétrique et matrice associée"
difficulty: 1
---

### Exercice 2 : Produit scalaire sur l'espace des fonctions continues
**Niveau : \star \star**

**Énoncé :**
Soit $E = \mathcal{C}([0, 1], \mathbb{R})$ l'espace vectoriel des fonctions continues de $[0, 1]$ dans $\mathbb{R}$. Pour $f, g \in E$, on pose :
\[ \phi(f, g) = \int_0^1 f(t)g(t) dt \]
1. Démontrer avec la plus stricte rigueur que $\phi$ est un produit scalaire sur $E$.
2. En déduire que pour toute fonction $f \in E$, on a : $\left( \int_0^1 f(t) dt \right)^2 \le \int_0^1 f(t)^2 dt$.

**Correction (Zéro Ellipse) :**
1. Vérifions les axiomes du produit scalaire :
   *   **Symétrie :** Pour tous $f, g \in E$, $\phi(f, g) = \int_0^1 f(t)g(t) dt$. Or la multiplication dans $\mathbb{R}$ est commutative, donc $f(t)g(t) = g(t)f(t)$. Par suite, $\phi(f, g) = \int_0^1 g(t)f(t) dt = \phi(g, f)$.
   *   **Bilinéarité :** Par symétrie, il suffit de montrer la linéarité à gauche. Soient $f, g, h \in E$ et $\lambda \in \mathbb{R}$. Par linéarité de l'intégrale :
       \[ \phi(\lambda f + g, h) = \int_0^1 (\lambda f(t) + g(t))h(t) dt = \lambda \int_0^1 f(t)h(t) dt + \int_0^1 g(t)h(t) dt = \lambda \phi(f, h) + \phi(g, h) \]
   *   **Positivité :** Pour tout $f \in E$, $\phi(f, f) = \int_0^1 f(t)^2 dt$. Puisque $\forall t \in [0, 1], f(t)^2 \ge 0$, l'intégrale d'une fonction positive est positive. Donc $\phi(f, f) \ge 0$.
   *   **Définie :** Soit $f \in E$ telle que $\phi(f, f) = 0$, c'est-à-dire $\int_0^1 f(t)^2 dt = 0$. La fonction $t \mapsto f(t)^2$ est continue sur $[0, 1]$ et positive. Si l'intégrale d'une fonction continue et positive sur un segment est nulle, alors cette fonction est identiquement nulle. Donc $\forall t \in [0, 1], f(t)^2 = 0$, ce qui implique $f(t) = 0$. Ainsi $f = 0_E$.
Conclusion : $\phi$ est bien un produit scalaire.
2. Appliquons l'inégalité de Cauchy-Schwarz avec les fonctions $f$ et la fonction constante $g(t) = 1$.
On a $\phi(f, g) = \int_0^1 f(t) \times 1 dt = \int_0^1 f(t) dt$.
Et $\|g\|^2 = \int_0^1 1^2 dt = 1 \implies \|g\| = 1$.
Et $\|f\|^2 = \int_0^1 f(t)^2 dt$.
L'inégalité $|\phi(f, g)| \le \|f\| \|g\|$ s'écrit $\left| \int_0^1 f(t) dt \right| \le \sqrt{\int_0^1 f(t)^2 dt} \times 1$.
En élevant au carré de part et d'autre, on obtient l'inégalité demandée.
