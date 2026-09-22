# Exercice 8 : Produit scalaire et Complétude
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Montrer que $L^2([0,1])$ muni du produit scalaire usuel est un espace de Hilbert, et expliquer en quoi l'espace des fonctions continues $C([0,1])$ muni du même produit scalaire n'en est pas un.

**Correction :**
$L^2([0,1])$ est complet (c'est le théorème de Riesz-Fischer pour $p=2$) et sa norme $\|f\|_2 = \sqrt{\int_0^1 |f|^2}$ dérive du produit scalaire $\langle f, g \rangle = \int_0^1 f(x)g(x)dx$. C'est donc, par définition, un espace de Hilbert.

Dans $C([0,1])$, considérons la suite de fonctions $f_n(x)$ définie par :
$f_n(x) = 0$ sur $[0, 1/2 - 1/n]$
$f_n(x) = n(x - (1/2 - 1/n))$ sur $[1/2 - 1/n, 1/2]$
$f_n(x) = 1$ sur $[1/2, 1]$.
Les $f_n$ sont continues. Elles convergent dans $L^2$ vers la fonction indicatrice (discontinue) $f = \mathbf{1}_{[1/2, 1]}$, car $\|f_n - f\|_2^2 \le \int_{1/2-1/n}^{1/2} 1 dx = 1/n \to 0$.
Comme $f_n$ converge dans $L^2$, c'est une suite de Cauchy pour la norme $\|\cdot\|_2$.
Cependant, elle n'admet aucune limite dans $C([0,1])$. En effet, si elle convergeait vers $g \in C([0,1])$, on aurait $\|g - f\|_2 = 0$, donc $g = f$ p.p. Mais une fonction continue égale p.p. à une fonction discontinue avec un saut (comme l'indicatrice) n'existe pas. Donc $C([0,1])$ n'est pas complet pour la norme $L^2$. Il est un espace préhilbertien, mais pas un espace de Hilbert.
