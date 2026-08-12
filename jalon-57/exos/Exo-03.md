# Exercice 3 : Norme matricielle et convergence des méthodes itératives linéaires
**Niveau :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $A \in \mathcal{M}_n(\mathbb{R})$ et $b \in \mathbb{R}^n$. On considère le système linéaire implicite $x = Ax + b$.
Démontrer que si une norme matricielle subordonnée $\|A\|$ vérifie $\|A\| < 1$, alors la suite de vecteurs $(x_k)_{k\in\mathbb{N}}$ définie par $x_{k+1} = Ax_k + b$ (pour un $x_0 \in \mathbb{R}^n$ quelconque) converge vers l'unique solution du système $(I - A)x = b$.

**Démonstration pas à pas :**
1. L'espace vectoriel $\mathbb{R}^n$ muni de n'importe quelle norme $\|\cdot\|$ est un espace de Banach (donc un espace métrique complet pour la distance associée $d(x, y) = \|x - y\|$).
2. Définissons l'application affine $f : \mathbb{R}^n \to \mathbb{R}^n$ par $f(x) = Ax + b$.
3. Calculons la distance entre les images de deux vecteurs quelconques $x, y \in \mathbb{R}^n$ :
   $\|f(x) - f(y)\| = \|(Ax + b) - (Ay + b)\| = \|A(x - y)\|$
4. Par définition d'une norme matricielle subordonnée, pour tout vecteur $v \in \mathbb{R}^n$, on a l'inégalité fondamentale $\|Av\| \leq \|A\| \|v\|$.
   Appliquons ceci avec $v = x - y$ :
   $\|f(x) - f(y)\| \leq \|A\| \|x - y\|$
5. Puisque par hypothèse $\|A\| = k < 1$, l'application $f$ est strictement contractante de rapport $k$.
6. Par le théorème du point fixe de Banach, l'application $f$ admet un unique point fixe $x^* \in \mathbb{R}^n$, et la suite des itérés $x_{k+1} = f(x_k)$ converge vers $x^*$ pour tout choix initial $x_0$.
7. Le point fixe satisfait l'équation :
   $x^* = f(x^*) \iff x^* = Ax^* + b \iff (I - A)x^* = b$.
   La convergence de la suite de Jacobi/Gauss-Seidel sous-jacente est ainsi prouvée.
