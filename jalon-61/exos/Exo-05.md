---
title: "Exercice 5 - Fonction de Thomae"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---

# Exercice 5 - Fonction de Thomae (les pop-corns)

**Énoncé :**
La fonction de Thomae $T(x)$ sur $(0, 1)$ vaut $1/q$ si $x = p/q$ avec $p, q$ entiers premiers entre eux ($q>0$), et $0$ si $x$ est irrationnel. Montrer que $T$ est Riemann-intégrable et que $\int_0^1 T(x) dx = 0$.

**Démonstration pas à pas :**
1. Soit $\epsilon > 0$. Il n'y a qu'un nombre fini de rationnels $p/q$ dans $[0, 1]$ tels que $q \le 1/\epsilon$.
2. Soit $N$ ce nombre de rationnels. On les enferme dans de petits intervalles de longueur totale $\epsilon / 2$.
3. Sur ces intervalles, $\sup T \le 1$. La contribution à $S(T, \sigma)$ est $\le \epsilon/2$.
4. Sur les autres intervalles, le dénominateur $q$ des éventuels rationnels est $> 1/\epsilon$, donc $T(x) < \epsilon$.
5. La contribution restante à $S(T, \sigma)$ est $\le \epsilon \cdot 1 = \epsilon$.
6. Ainsi $S(T, \sigma) \le 3\epsilon/2$. Comme $s(T, \sigma) = 0$ (densité des irrationnels), $T$ est Riemann-intégrable et d'intégrale nulle.
