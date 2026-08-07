## Exercice 1 : La distance discrète \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $X$ un ensemble non vide. On définit l'application $d : X \times X \to \mathbb{R}$ par $d(x, y) = 1$ si $x \neq y$ et $d(x, x) = 0$.
1. Démontrer rigoureusement que $d$ est une distance sur $X$.
2. Déterminer explicitement la topologie induite par cette distance.

**Correction :**
1. **Axiomes de distance :**
   - *Séparation :* Par définition, $d(x,y)=0 \implies x=y$, et réciproquement.
   - *Symétrie :* La condition $x \neq y$ est équivalente à $y \neq x$, donc $d(x,y)=d(y,x)$ dans tous les cas.
   - *Inégalité triangulaire :* Pour $x, y, z \in X$, on doit montrer $d(x, z) \le d(x, y) + d(y, z)$.
     Si $x=z$, $d(x,z)=0 \le d(x,y)+d(y,z)$ est trivial car les distances sont positives.
     Si $x \neq z$, alors $d(x,z)=1$. Or, on ne peut pas avoir simultanément $x=y$ et $y=z$ (sinon $x=z$). Ainsi, soit $x \neq y$, soit $y \neq z$. Cela implique qu'au moins l'un des termes $d(x,y)$ ou $d(y,z)$ vaut $1$. La somme $d(x,y)+d(y,z)$ est donc $\ge 1$. L'inégalité $1 \le d(x,y)+d(y,z)$ est vérifiée.
2. **Topologie :**
   Considérons la boule ouverte $B(x, 1/2)$. Par définition, $y \in B(x, 1/2) \iff d(x,y) < 1/2$.
   Puisque $d(x,y) \in \{0, 1\}$, la seule possibilité est $d(x,y)=0$, soit $y=x$.
   Ainsi, $B(x, 1/2) = \{x\}$. Toute boule ouverte est un ouvert, donc chaque singleton est ouvert.
   Toute partie de $X$ étant l'union de ses singletons, toute partie est ouverte. Il s'agit de la topologie discrète. $\blacksquare$
