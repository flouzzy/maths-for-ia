# Exercice 5 : L'itération d'une fonction admettant une puissance contractante
**Niveau :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(X, d)$ un espace métrique complet et $f : X \to X$ une application. On suppose qu'il existe un entier $p \geq 1$ tel que l'application itérée $f^p = f \circ f \circ \dots \circ f$ ($p$ fois) soit strictement contractante de rapport $k < 1$.
Démontrer que $f$ admet un unique point fixe dans $X$.

**Démonstration pas à pas :**
1. L'application $g = f^p$ est une application de l'espace complet $X$ dans lui-même. Par hypothèse, elle est strictement contractante.
2. Par le théorème du point fixe de Banach classique, $g$ admet un unique point fixe dans $X$. Appelons cet élément $x^*$, tel que $g(x^*) = x^*$.
3. Nous cherchons à montrer que $x^*$ est également un point fixe de $f$. Appliquons la fonction $f$ aux deux membres de l'égalité du point fixe de $g$ :
   $f(g(x^*)) = f(x^*)$
4. Remarquons que la composition des fonctions est associative, donc $f \circ f^p = f^{p+1} = f^p \circ f$.
   Cela s'écrit $f(g(x)) = g(f(x))$ pour tout $x \in X$.
5. Appliquée au point $x^*$, cette commutation donne :
   $g(f(x^*)) = f(x^*)$
6. Définissons le point $y^* = f(x^*)$. L'équation précédente s'écrit $g(y^*) = y^*$.
   Le point $y^*$ est donc un point fixe de $g$.
7. Mais nous avons établi à l'étape 2 que $g$ possède un *unique* point fixe. Par conséquent, il est impératif que $y^* = x^*$.
8. En remplaçant $y^*$ par sa définition, nous obtenons $f(x^*) = x^*$. Ainsi, l'élément $x^*$ est un point fixe de $f$.
9. Pour prouver l'unicité du point fixe de $f$, supposons que $z^*$ soit un point fixe de $f$ (soit $f(z^*) = z^*$). Une récurrence immédiate montre que $f^2(z^*) = f(f(z^*)) = f(z^*) = z^*$, et plus généralement pour tout entier $m$, $f^m(z^*) = z^*$.
   En particulier pour l'entier $p$, on a $f^p(z^*) = z^*$, ce qui signifie que $g(z^*) = z^*$. Le point $z^*$ est donc un point fixe de $g$.
   Puisque le point fixe de $g$ est unique et vaut $x^*$, on en déduit inévitablement que $z^* = x^*$.
   L'application $f$ possède donc un unique point fixe global.
