# Exercice 9 : Inégalité isopérimétrique (Le problème de Didon) $\bigstar\bigstar\bigstar\bigstar\bigstar$
**Énoncé :** Soit une courbe fermée simple dans le plan $\mathbb{R}^2$, paramétrée par $s \in [0, 2\pi]$, longueur de l'arc. La longueur totale de la courbe est donc $L = 2\pi$. Soient $(x(s), y(s))$ les coordonnées, qui sont des fonctions $2\pi$-périodiques.
On admet que l'aire enclose $A$ est donnée par $A = \frac{1}{2} \int_0^{2\pi} (x(s)y'(s) - x'(s)y(s)) ds$.
De plus, la paramétrisation par longueur d'arc implique $(x'(s))^2 + (y'(s))^2 = 1$.
En utilisant les séries de Fourier et l'identité de Parseval, démontrer que $A \le \pi$, avec égalité si et seulement si la courbe est un cercle.

**Correction Détaillée :**
*Étape 1 : Énergie des dérivées.*
Puisque $x'^2 + y'^2 = 1$, on a $\int_0^{2\pi} (x'^2 + y'^2) ds = 2\pi$.
Par Parseval sur $x'$ et $y'$ (avec coefficients réels $a_n, b_n$ pour $x$, et $c_n, d_n$ pour $y$) :
$\|x'\|_2^2 + \|y'\|_2^2 = \frac{1}{2\pi} 2\pi = 1$.
Pour la dérivée, les coefficients sont $a_n(x') = n b_n(x)$ et $b_n(x') = -n a_n(x)$.
L'énergie est donc $\frac{1}{2} \sum_{n=1}^\infty n^2 (a_n^2 + b_n^2 + c_n^2 + d_n^2) = 1$.

*Étape 2 : Formule de l'aire par Fourier.*
$A = \pi \frac{1}{2\pi} \int_0^{2\pi} (x y' - x' y) ds$. Par Parseval généralisé (produit scalaire),
$\frac{1}{2\pi} \int_0^{2\pi} x y' = \frac{a_0 c_0(y')}{4} + \frac{1}{2} \sum (a_n a_n(y') + b_n b_n(y')) = \frac{1}{2} \sum n (a_n d_n - b_n c_n)$.
On obtient $A = \pi \sum_{n=1}^\infty n (a_n d_n - b_n c_n)$.

*Étape 3 : Majoration algébrique.*
On utilise $2(a_n d_n - b_n c_n) \le a_n^2 + d_n^2 + b_n^2 + c_n^2$.
Donc $A \le \frac{\pi}{2} \sum_{n=1}^\infty n (a_n^2 + b_n^2 + c_n^2 + d_n^2)$.
Puisque $n \le n^2$ pour $n \ge 1$,
$A \le \frac{\pi}{2} \sum_{n=1}^\infty n^2 (a_n^2 + b_n^2 + c_n^2 + d_n^2) = \pi \times 1 = \pi$.
Donc $A \le \pi$. (L'inégalité isopérimétrique classique $4\pi A \le L^2$ donne $4\pi A \le 4\pi^2 \implies A \le \pi$).

*Étape 4 : Cas d'égalité.*
Il faut $n = n^2$ pour tout $n$ où les coefficients sont non nuls, donc $n=1$.
Et $a_1 = d_1$, $b_1 = -c_1$.
Ceci paramètre exactement un cercle !
