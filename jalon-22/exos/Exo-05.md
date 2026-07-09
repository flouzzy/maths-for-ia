# Exercice 5 : La fonction de Weierstrass

**Difficulté :** $\star\star\star$

**Énoncé :**
Soit $f(x) = \sum_{n=0}^\infty 2^{-n} \cos(3^n x)$. Montrer que $f$ est une fonction continue sur $\mathbb{R}$.

**Démonstration :**
1. Soit $u_n(x) = 2^{-n} \cos(3^n x)$. Chaque $u_n$ est continue sur $\mathbb{R}$.
2. Calculons la norme infinie de $u_n$ sur $\mathbb{R}$ :
   Puisque $|\cos(3^n x)| \le 1$ pour tout $x$, on a :
   $$ |u_n(x)| \le 2^{-n} $$
   Donc $\|u_n\|_{\infty, \mathbb{R}} = 2^{-n}$.
3. La série géométrique $\sum 2^{-n}$ converge (raison $1/2 < 1$).
4. La série de fonctions $\sum u_n$ converge donc normalement sur $\mathbb{R}$.
5. Par le théorème liant convergence normale et uniforme, la série converge uniformément sur $\mathbb{R}$.
6. Par le théorème de continuité de la fonction limite, puisque toutes les $u_n$ sont continues et que la convergence est uniforme, la somme $f(x)$ est une fonction continue sur $\mathbb{R}$.
(Note : Karl Weierstrass a prouvé que cette fonction est continue partout, mais dérivable nulle part, fournissant le premier contre-exemple historique bouleversant l'intuition).
$\blacksquare$
