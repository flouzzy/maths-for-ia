# Exercice 7 : ★★★★

**Énoncé :**
Fermeture de l'adhérence.

**Correction (Zéro Ellipse) :**
Pour tout sous-ensemble $A$ de $E$, on définit l'adhérence $\overline{A}$ comme l'ensemble des limites des suites convergentes d'éléments de $A$. Montrer que $\overline{A}$ est un ensemble fermé.

Nous devons montrer que si une suite $(x_n)_{n \in \mathbb{N}}$ de $\overline{A}$ converge vers un élément $x \in E$, alors $x \in \overline{A}$.
Soit $(x_n)_{n \in \mathbb{N}} \in \overline{A}^\mathbb{N}$ telle que $\lim_{n \to \infty} x_n = x$.
Pour chaque entier $n \in \mathbb{N}$, puisque $x_n \in \overline{A}$, il existe une suite $(y_{n, k})_{k \in \mathbb{N}}$ d'éléments de $A$ telle que $\lim_{k \to \infty} y_{n, k} = x_n$.
Par définition de la limite, pour chaque $n$, il existe un entier $K_n$ tel que $\|y_{n, K_n} - x_n\| \le \frac{1}{n+1}$.
Définissons une nouvelle suite $z_n = y_{n, K_n}$. Par construction, pour tout $n \in \mathbb{N}$, $z_n \in A$.
Montrons que $(z_n)$ converge vers $x$.
Par l'inégalité triangulaire :
$\|z_n - x\| = \|y_{n, K_n} - x_n + x_n - x\| \le \|y_{n, K_n} - x_n\| + \|x_n - x\| \le \frac{1}{n+1} + \|x_n - x\|$.
Quand $n \to \infty$, $\frac{1}{n+1} \to 0$ et $\|x_n - x\| \to 0$.
Donc $\lim_{n \to \infty} \|z_n - x\| = 0$, ce qui signifie que $z_n \to x$.
Ainsi, on a exhibé une suite $(z_n)$ d'éléments de $A$ qui converge vers $x$. Par définition, cela implique que $x \in \overline{A}$.
L'adhérence $\overline{A}$ contient les limites de toutes ses suites convergentes, elle est donc fermée. $\blacksquare$
