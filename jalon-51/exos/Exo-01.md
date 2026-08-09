---
title: "Exercice 1 : La distance discrète"
---

### Exercice 1 : La distance discrète \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $X$ un ensemble non vide. On définit l'application $d : X \times X \to \mathbb{R}_+$ par $d(x, y) = 1$ si $x \neq y$ et $d(x, x) = 0$. Démontrer que $d$ est une distance sur $X$. Quelle est la topologie induite par cette distance ?

**Correction Détaillée :**
1. **Séparation :** Par définition, $d(x, y) = 0$ si et seulement si $x = y$.
2. **Symétrie :** Si $x = y$, $d(x, y) = d(y, x) = 0$. Si $x \neq y$, alors $y \neq x$ et $d(x, y) = d(y, x) = 1$. L'axiome de symétrie est vérifié.
3. **Inégalité triangulaire :** Montrons que $d(x, z) \le d(x, y) + d(y, z)$ pour tous $x, y, z \in X$. Si $x = z$, alors $d(x, z) = 0$, et l'inégalité est trivialement satisfaite car $d$ est à valeurs positives. Si $x \neq z$, alors $d(x, z) = 1$. Il est impossible d'avoir simultanément $x = y$ et $y = z$, sinon $x = z$ par transitivité. Donc, au moins l'une des distances $d(x, y)$ ou $d(y, z)$ vaut 1. Par conséquent, $d(x, y) + d(y, z) \ge 1 = d(x, z)$. L'inégalité triangulaire est prouvée.

$d$ est bien une distance.

**Topologie induite :** Regardons les boules ouvertes. Soit $x \in X$. Si on choisit un rayon $r$ tel que $0 < r \le 1$ (par exemple $r = 1/2$), la boule ouverte de centre $x$ et de rayon $r$ est $B(x, r) = \{y \in X \mid d(x, y) < r\}$. Puisque les seules valeurs possibles pour la distance sont 0 et 1, et que $r \le 1$, le seul élément vérifiant cette condition est $x$ lui-même (car $d(x,x)=0 < r$). Donc, $B(x, r) = \{x\}$. Ainsi, chaque singleton est une boule ouverte, donc un ouvert. Comme toute partie de $X$ est une réunion de ses éléments (singletons), toute partie de $X$ est ouverte. La topologie induite est la topologie discrète.
