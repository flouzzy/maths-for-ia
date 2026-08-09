---
title: "Exercice 6 : Bornitude et distance topologiquement équivalente"
---

### Exercice 6 : Bornitude et distance topologiquement équivalente \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(X, d)$ un espace métrique. On définit l'application $d'(x, y) = \frac{d(x, y)}{1 + d(x, y)}$.
Démontrer que $d'$ est une distance sur $X$, et qu'elle est bornée par 1. Montrer qu'elle induit la même topologie que $d$.

**Correction Détaillée :**
La séparation et la symétrie découlent directement des propriétés de $d$.
Pour l'inégalité triangulaire, considérons la fonction $f(t) = \frac{t}{1+t} = 1 - \frac{1}{1+t}$. Sa dérivée est $f'(t) = \frac{1}{(1+t)^2} > 0$, donc $f$ est strictement croissante sur $\mathbb{R}_+$.
Soient $x, y, z \in X$. Posons $a = d(x, y)$, $b = d(y, z)$ et $c = d(x, z)$. Par l'inégalité triangulaire de $d$, $c \le a + b$.
Puisque $f$ est croissante :
$$f(c) \le f(a + b) = \frac{a+b}{1+a+b} = \frac{a}{1+a+b} + \frac{b}{1+a+b}$$
Comme $1+a+b \ge 1+a$ et $1+a+b \ge 1+b$ (car $a,b \ge 0$), on a :
$$f(c) \le \frac{a}{1+a} + \frac{b}{1+b} = f(a) + f(b)$$
Soit $d'(x, z) \le d'(x, y) + d'(y, z)$. Ainsi, $d'$ est une distance.
De plus, comme $d \ge 0$, $\frac{d}{1+d} < 1$, donc $d'$ est bornée par 1.
**Topologies équivalentes :** Les boules s'emboîtent. Comme $d' \le d$, pour tout $r>0$, $B_d(x, r) \subset B_{d'}(x, r)$. Inversement, si on choisit $r' < 1$, alors $d' < r'$ équivaut à $d < \frac{r'}{1-r'}$. Ainsi, pour tout rayon $R$ de la topologie $d$, on peut trouver un rayon $r'$ de la topologie $d'$ qui l'inclut, prouvant l'équivalence topologique. Toute topologie métrique peut donc être engendrée par une métrique bornée.
