---
title: "Exo-01 : La distance discrète"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exo-01 : La distance discrète


## 1. Énoncé

Soit $X$ un ensemble quelconque non vide. On définit l'application $d : X \times X \to \mathbb{R}_+$ par :
- $d(x, y) = 1$ si $x \neq y$
- $d(x, x) = 0$

1. Démontrer rigoureusement que $d$ est une distance sur $X$.
2. Décrire la boule ouverte $B(x, 1)$ et la boule fermée $\bar{B}(x, 1)$ pour tout $x \in X$.
3. En déduire la topologie induite par cette distance.

## 2. Correction détaillée

**Question 1 :**
Vérifions les trois axiomes d'une distance.
- **Séparation :** Par définition, $d(x, y) = 0 \iff x = y$. L'axiome est respecté.
- **Symétrie :** Si $x=y$, $d(x, y) = d(y, x) = 0$. Si $x \neq y$, alors $y \neq x$, donc $d(x, y) = 1$ et $d(y, x) = 1$. L'axiome est respecté.
- **Inégalité triangulaire :** Pour $x, y, z \in X$, montrons que $d(x, z) \le d(x, y) + d(y, z)$.
  - Cas 1 : $x = z$. Alors $d(x, z) = 0$. Puisque $d$ est à valeurs positives, on a toujours $0 \le d(x, y) + d(y, z)$.
  - Cas 2 : $x \neq z$. Alors $d(x, z) = 1$. Puisque $x$ et $z$ sont distincts, $y$ ne peut être simultanément égal à $x$ et à $z$.
    - Si $y \neq x$, alors $d(x, y) = 1$. La somme vaut au moins $1$.
    - Si $y \neq z$, alors $d(y, z) = 1$. La somme vaut au moins $1$.
    Dans tous les sous-cas, $d(x, y) + d(y, z) \ge 1 = d(x, z)$. L'axiome est respecté.
Ainsi, $d$ est bien une distance, appelée distance discrète.

**Question 2 :**
Soit $x \in X$.
- $B(x, 1) = \{ y \in X \mid d(x, y) < 1 \}$. Puisque $d$ ne prend que les valeurs $0$ et $1$, la seule possibilité pour que $d(x, y) < 1$ est $d(x, y) = 0$, donc $y = x$.
  Ainsi, $B(x, 1) = \{x\}$.
- $\bar{B}(x, 1) = \{ y \in X \mid d(x, y) \le 1 \}$. Comme toutes les distances valent $0$ ou $1$, cette condition est toujours vérifiée pour tout $y \in X$.
  Ainsi, $\bar{B}(x, 1) = X$.

**Question 3 :**
Dans la topologie induite, toute boule ouverte est un ouvert. Or, pour tout point $x$, le singleton $\{x\}$ est la boule ouverte $B(x, \frac{1}{2})$. Donc chaque singleton est un ouvert.
Une topologie étant stable par réunion quelconque, toute partie de $X$ (qui est réunion de ses singletons) est ouverte. La topologie induite est la **topologie discrète**.
