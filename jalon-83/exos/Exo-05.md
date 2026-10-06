---
uuid: jalon-83-exo-05
title: "Exercice 05 - Dérivation des distributions"
---

# Exercice 05 $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Considérons la fonction $f(x) = \sin(x) H(x)$, où $H(x)$ est l'échelon de Heaviside.
1. Calculer la dérivée première $f'$ au sens des distributions.
2. Calculer la dérivée seconde $f''$ au sens des distributions.
3. Résoudre l'équation différentielle $u'' + u = \delta_0$ au sens des distributions dans $\mathcal{D}'(\mathbb{R})$, en utilisant le résultat précédent (en supposant $u=0$ pour $x<0$).

**Correction pas à pas :**
1. La fonction $f(x) = \sin(x) H(x)$ est continue partout. En effet, pour $x < 0, f(x)=0$ et pour $x>0, f(x)=\sin(x)$. En $x=0$, $f(0^-)=0$ et $f(0^+)=\sin(0)=0$. Le saut est nul.
La fonction est de classe $C^1$ par morceaux. Sa dérivée usuelle est :
$\{f'\}(x) = 0$ si $x<0$, et $\{f'\}(x) = \cos(x)$ si $x>0$.
Soit $\{f'\}(x) = \cos(x) H(x)$.
D'après la formule des sauts :
$f' = \{f'\} + 0 \cdot \delta_0 = \cos(x) H(x)$.

2. Calculons la dérivée de $g(x) = \cos(x) H(x)$.
Cette fonction présente un saut en $x=0$.
$g(0^+) = \cos(0) = 1$ et $g(0^-) = 0$. Le saut $\sigma = 1 - 0 = 1$.
La dérivée usuelle (là où elle est définie) est $\{g'\}(x) = -\sin(x) H(x)$.
En appliquant la formule des sauts à $g$ :
$g' = \{g'\} + \sigma \delta_0 = -\sin(x) H(x) + 1 \cdot \delta_0$.
Donc $f'' = -\sin(x) H(x) + \delta_0$.

3. On cherche à résoudre $u'' + u = \delta_0$.
On remarque que $f(x) = \sin(x) H(x)$ vérifie exactement cette équation :
$f'' + f = (-\sin(x) H(x) + \delta_0) + (\sin(x) H(x)) = \delta_0$.
Ainsi, $u(x) = \sin(x) H(x)$ est la solution fondamentale (aussi appelée fonction de Green causale) de l'opérateur $L = \frac{d^2}{dx^2} + I$. Cela signifie que la réponse d'un oscillateur harmonique libre initialement au repos (pour $t<0$) soumis à une impulsion instantanée (coup de marteau en $t=0$) se met à osciller indéfiniment selon un mode sinusoïdal. $\blacksquare$
