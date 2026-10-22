# Exercice 8 : Fonctionnelle linéaire sur l'espace des fonctions continues
$\bigstar$\bigstar$\bigstar$\bigstar\star$

**Énoncé :**
Soit $E = \mathcal{C}([0,1])$ avec la norme uniforme. Soit $L: E \to \mathbb{R}$ définie par $L(f) = f(1/2)$. Montrer que $L$ est continue et calculer sa norme.

**Correction Détaillée :**
1. $L$ est clairement linéaire.
2. Pour toute $f \in E$, $|L(f)| = |f(1/2)| \le \sup_{x} |f(x)| = \|f\|_\infty$.
3. Donc $L$ est bornée et $\|L\| \le 1$.
4. En considérant la fonction constante $f(x) = 1$, on a $\|f\|_\infty = 1$ et $L(f) = 1$, donc $\|L\| = 1$.
