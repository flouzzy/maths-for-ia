# Exercice 2 : La distance discrète en profondeur
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé formel
Sur un ensemble $X$, on munit $X$ de la distance discrète $d(x,y) = 1$ si $x \neq y$, et $0$ sinon.
1. Montrer rigoureusement l'inégalité triangulaire.
2. Déterminer la boule ouverte $B(a, 1)$, la boule ouverte $B(a, 2)$, la boule fermée $B_f(a, 1)$ et la sphère $S(a, 1)$ pour un point $a \in X$.

## Résolution pas à pas
**Étape 1 : L'inégalité triangulaire**

Soient $x, y, z \in X$. Si $x=z$, $d(x,z)=0 \le d(x,y) + d(y,z)$ est trivial. Si $x \neq z$, alors $d(x,z)=1$. Il est impossible d'avoir simultanément $x=y$ et $y=z$ (sinon $x=z$, absurde). Donc soit $x \neq y$ (et $d(x,y)=1$), soit $y \neq z$ (et $d(y,z)=1$), soit les deux. Ainsi, $d(x,y)+d(y,z) \ge 1$. Dans tous les cas, $d(x,z) \le d(x,y)+d(y,z)$.

**Étape 2 : Exploration topologique**

- **$B(a, 1) = \left\lbrace x \in X \mid d(a,x) < 1\right\rbrace$ :** La seule distance strictement inférieure à 1 est 0. Donc la seule solution est $x=a$. $B(a, 1) = \left\lbrace a\right\rbrace$.
- **$B(a, 2) = \left\lbrace x \in X \mid d(a,x) < 2\right\rbrace$ :** Toutes les distances possibles sont 0 ou 1, qui sont $< 2$. Donc $B(a, 2) = X$.
- **$B_f(a, 1) = \left\lbrace x \in X \mid d(a,x) \le 1\right\rbrace$ :** De même, toutes les distances possibles valent 0 ou 1. Donc $B_f(a, 1) = X$.
- **$S(a, 1) = \left\lbrace x \in X \mid d(a,x) = 1\right\rbrace$ :** Ce sont tous les points distincts de $a$. Donc $S(a, 1) = X \setminus \left\lbrace a\right\rbrace$.
*Remarque :* On voit ici que $B_f(a, r)$ n'est pas toujours l'adhérence de $B(a, r)$ dans les espaces métriques généraux. $\blacksquare$
