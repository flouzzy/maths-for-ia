# Exercice 1

## Exercice 1 : Unicité de la limite faible \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $E$ un espace de Banach. Montrer que si une suite $(x_n)_{n \ge 1}$ d'éléments de $E$ converge faiblement vers $x \in E$ et faiblement vers $y \in E$, alors $x = y$.

**Correction :**
*Analyse de l'énoncé :* On utilise la définition de la convergence faible et une conséquence directe du théorème de Hahn-Banach (la séparation des points).
*Résolution pas-à-pas :*
1. **Étape 1 : Action des formes linéaires.**
   Par définition, $x_n \rightharpoonup x$ implique que pour toute forme linéaire continue $f \in E^*$, on a $\lim_{n \to \infty} f(x_n) = f(x)$.
   De même, $x_n \rightharpoonup y$ implique que $\lim_{n \to \infty} f(x_n) = f(y)$.
2. **Étape 2 : Unicité de la limite scalaire.**
   Dans le corps $\mathbb{K}$ (qui est $\mathbb{R}$ ou $\mathbb{C}$), la limite d'une suite est unique.
   Par conséquent, pour tout $f \in E^*$, on a $f(x) = f(y)$, ce qui par linéarité donne $f(x - y) = 0$.
3. **Étape 3 : Application de Hahn-Banach.**
   Supposons par l'absurde que $x \neq y$, c'est-à-dire que $z = x - y \neq 0$.
   D'après le corollaire de Hahn-Banach, il existe une forme linéaire $f_0 \in E^*$ telle que $f_0(z) = \|z\|_E \neq 0$.
   Or, l'étape 2 a montré que $f(z) = 0$ pour toute forme $f \in E^*$.
   C'est une contradiction. On en conclut donc que $z = 0$, soit $x = y$.
