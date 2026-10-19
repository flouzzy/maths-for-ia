# Exercice 03 : Transformations affines
Difficulté : $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $X$ une variable aléatoire de fonction caractéristique $\phi_X$.
Soient $a, b \in \mathbb{R}$. Soit $Y = aX + b$.
Exprimer la fonction caractéristique $\phi_Y(t)$ de $Y$ en fonction de $\phi_X$.

**Correction pas à pas :**
1. Par définition, la fonction caractéristique de $Y$ est $\phi_Y(t) = \mathbb{E}[e^{itY}]$.
2. Remplaçons $Y$ par son expression en fonction de $X$ :
   $\phi_Y(t) = \mathbb{E}[e^{it(aX + b)}]$.
3. En utilisant les propriétés de l'exponentielle :
   $e^{it(aX + b)} = e^{itaX} e^{itb}$.
4. Le terme $e^{itb}$ est une constante déterministe, on peut la sortir de l'espérance par linéarité :
   $\phi_Y(t) = e^{itb} \mathbb{E}[e^{i(at)X}]$.
5. Par définition de la fonction caractéristique de $X$, évaluée en la valeur $(at)$ :
   $\mathbb{E}[e^{i(at)X}] = \phi_X(at)$.
6. Conclusion : $\phi_Y(t) = e^{itb} \phi_X(at)$.
Cette propriété montre que les translations induisent un déphasage ($e^{itb}$), et les dilatations modifient l'échelle des fréquences ($at$).
