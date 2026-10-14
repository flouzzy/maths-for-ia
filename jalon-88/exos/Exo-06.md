# Exercice 6

\subsection*{Exercice 6 : Covariance nulle sans indépendance \quad $\bigstar\bigstar\bigstar\star\star$}

**Énoncé :**
Soit $X$ une variable aléatoire suivant une loi normale standard $\mathcal{N}(0, 1)$.
Soit $Y = X^2$.
1. Déterminer si $X$ et $Y$ sont indépendantes.
2. Calculer la covariance entre $X$ et $Y$. Que conclut-on ?

**Correction :**
1. Étude de l'indépendance :
   $Y$ est une fonction déterministe de $X$. Connaissant $X$, la valeur de $Y$ est parfaitement déterminée. Elles ne peuvent pas être indépendantes.
   Montrons-le formellement. Considérons les événements $A = \{X \in [1, 2]\}$ et $B = \{Y \in [0, 0.5]\}$.
   Si $Y = X^2 \le 0.5$, alors $X \in [-\sqrt{0.5}, \sqrt{0.5}]$.
   Donc l'intersection $A \cap B = \{X \in [1, 2]\} \cap \{X \in [-\sqrt{0.5}, \sqrt{0.5}]\} = \emptyset$.
   Ainsi, $P(A \cap B) = 0$.
   Or, $P(A) > 0$ et $P(B) > 0$ (car la densité de la loi normale est strictement positive partout).
   Donc $P(A \cap B) \neq P(A)P(B)$. Les variables ne sont pas indépendantes.
2. Calcul de la covariance :
   Par définition, $\text{Cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$.
   Comme $X \sim \mathcal{N}(0, 1)$, on sait que $\mathbb{E}[X] = 0$.
   Par conséquent, $\mathbb{E}[X]\mathbb{E}[Y] = 0 \times \mathbb{E}[X^2] = 0$.
   Calculons $\mathbb{E}[XY]$. On a $XY = X(X^2) = X^3$.
   L'espérance de $X^3$ est le moment d'ordre 3 d'une loi normale centrée.
   $\mathbb{E}[X^3] = \int_{-\infty}^{+\infty} x^3 \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx$.
   La fonction à intégrer est impaire ($f(-x) = -f(x)$) et intégrable, donc son intégrale sur $\mathbb{R}$ est nulle.
   Ainsi, $\mathbb{E}[XY] = \mathbb{E}[X^3] = 0$.
   On en déduit que $\text{Cov}(X,Y) = 0 - 0 = 0$.
3. Conclusion : Bien que $X$ et $Y$ soient dépendantes, leur covariance est nulle (elles sont non corrélées). La covariance mesure la dépendance linéaire, mais ne capture pas les dépendances non linéaires (ici quadratique).
