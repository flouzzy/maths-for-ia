\subsection*{Exercice 10 : Convolution et densités de probabilité \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

Soient $X$ et $Y$ deux variables aléatoires réelles indépendantes admettant pour densités respectives $f_X$ et $f_Y$. Démontrer que la variable aléatoire $Z = X + Y$ admet une densité $f_Z$ donnée par le produit de convolution $f_X * f_Y$.

**Correction :**
1. La loi conjointe de $(X, Y)$ a pour densité $f_{(X,Y)}(x, y) = f_X(x)f_Y(y)$ grâce à l'indépendance.
2. Cherchons la fonction de répartition de $Z$, $F_Z(z) = \mathbb{P}(Z \le z) = \mathbb{P}(X + Y \le z)$.
3. On intègre la densité conjointe sur le domaine $\Delta_z = \{(x, y) \in \mathbb{R}^2 \mid x + y \le z\}$ :
   $F_Z(z) = \iint_{\Delta_z} f_X(x)f_Y(y) dx dy = \int_{-\infty}^{\infty} \left( \int_{-\infty}^{z - x} f_Y(y) dy \right) f_X(x) dx$
4. On effectue le changement de variable $u = x + y$ dans l'intégrale interne (à $x$ fixé, $du = dy$) :
   $F_Z(z) = \int_{-\infty}^{\infty} \left( \int_{-\infty}^{z} f_Y(u - x) du \right) f_X(x) dx$
5. Toutes les fonctions étant positives, par le théorème de Fubini-Tonelli, on peut intervertir les intégrales :
   $F_Z(z) = \int_{-\infty}^{z} \left( \int_{-\infty}^{\infty} f_X(x)f_Y(u - x) dx \right) du$
6. La fonction $z \mapsto F_Z(z)$ s'écrit donc comme l'intégrale d'une fonction $f_Z(u) = \int_{-\infty}^{\infty} f_X(x)f_Y(u - x) dx$.
7. Par définition, cette fonction est la densité de $Z$, et c'est exactement l'expression du produit de convolution $f_X * f_Y(u)$.
8. Ce résultat démontre que la densité de la somme de deux V.A. à densité indépendantes est le produit de convolution de leurs densités.