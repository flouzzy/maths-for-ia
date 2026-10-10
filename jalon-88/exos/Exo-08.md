\subsection*{Exercice 8 : Vecteurs gaussiens et indépendance \quad $\bigstar\bigstar\bigstar\bigstar\star$}

Soit $(X, Y)$ un vecteur gaussien de dimension 2 d'espérance $(0, 0)$ et de matrice de covariance $\Sigma = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}$.
1. Quelle est la condition nécessaire et suffisante sur $\rho$ pour que $X$ et $Y$ soient indépendantes ?
2. Démontrer ce résultat en utilisant la fonction caractéristique.

**Correction :**
1. Condition : $X$ et $Y$ sont indépendantes si et seulement si leur covariance est nulle, c'est-à-dire si et seulement si $\rho = 0$. (Ce résultat est propre aux vecteurs gaussiens).
2. Démonstration par la fonction caractéristique :
   - La fonction caractéristique du vecteur gaussien $(X, Y)$ évaluée en $(u, v) \in \mathbb{R}^2$ est :
     $\phi_{(X, Y)}(u, v) = \exp\left(-\frac{1}{2} (u, v) \Sigma (u, v)^T\right) = \exp\left(-\frac{1}{2} (u^2 + v^2 + 2\rho uv)\right)$
   - Les marginales $X$ et $Y$ sont des gaussiennes centrées réduites, donc $\phi_X(u) = \exp(-u^2/2)$ et $\phi_Y(v) = \exp(-v^2/2)$.
   - L'indépendance de $X$ et $Y$ équivaut à la factorisation de la fonction caractéristique conjointe : $\phi_{(X, Y)}(u, v) = \phi_X(u)\phi_Y(v)$ pour tout $(u, v)$.
   - $\phi_X(u)\phi_Y(v) = \exp(-u^2/2)\exp(-v^2/2) = \exp\left(-\frac{1}{2} (u^2 + v^2)\right)$.
   - On a donc l'égalité si et seulement si $\exp\left(-\frac{1}{2} (u^2 + v^2 + 2\rho uv)\right) = \exp\left(-\frac{1}{2} (u^2 + v^2)\right)$, soit $2\rho uv = 0$ pour tout $(u, v)$.
   - Ceci implique obligatoirement $\rho = 0$.