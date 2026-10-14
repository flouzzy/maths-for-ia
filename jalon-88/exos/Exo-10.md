# Exercice 10

\subsection*{Exercice 10 : Produit scalaire de L2 et Indépendance \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
Dans l'espace de Hilbert $L^2(\Omega, \mathcal{F}, P)$, on définit le produit scalaire $\langle X, Y \rangle = \mathbb{E}[XY]$.
Deux variables aléatoires $X, Y \in L^2$ sont orthogonales si $\langle X, Y \rangle = 0$.
Soient $X, Y \in L^2$ deux variables d'espérance nulle ($\mathbb{E}[X] = \mathbb{E}[Y] = 0$).
Montrer que si $X$ et $Y$ sont indépendantes, alors elles sont orthogonales. La réciproque est-elle vraie ? Justifier.

**Correction :**
1. Sens direct : Supposons $X, Y$ indépendantes et centrées.
   Par le théorème d'indépendance (puisqu'elles sont dans $L^2$, elles sont dans $L^1$, donc intégrables) :
   $\langle X, Y \rangle = \mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$.
   Comme $\mathbb{E}[X] = 0$ et $\mathbb{E}[Y] = 0$, on a $\mathbb{E}[X]\mathbb{E}[Y] = 0 \times 0 = 0$.
   Donc $\langle X, Y \rangle = 0$. $X$ et $Y$ sont orthogonales.
2. Étude de la réciproque :
   L'orthogonalité de variables centrées signifie que leur covariance est nulle ($\text{Cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] = 0 - 0 = 0$).
   L'orthogonalité est donc équivalente à l'absence de corrélation linéaire.
   Nous savons (vu dans un exercice précédent) que la covariance nulle n'implique pas l'indépendance.
3. Contre-exemple formel dans $L^2$ :
   Soit $\theta \sim \mathcal{U}([0, 2\pi])$. On pose $X = \cos(\theta)$ et $Y = \sin(\theta)$.
   Puisque $\theta$ est bornée, $X$ et $Y$ sont bornées par $1$, elles sont donc dans $L^2$.
   Elles sont centrées : $\mathbb{E}[X] = \frac{1}{2\pi} \int_0^{2\pi} \cos(t) dt = 0$ et $\mathbb{E}[Y] = 0$.
   Vérifions l'orthogonalité :
   $\langle X, Y \rangle = \mathbb{E}[\cos(\theta)\sin(\theta)] = \mathbb{E}[\frac{1}{2}\sin(2\theta)] = \frac{1}{4\pi} \int_0^{2\pi} \sin(2t) dt = 0$.
   $X$ et $Y$ sont donc orthogonales.
   Cependant, elles ne sont pas indépendantes. Par l'identité trigonométrique fondamentale : $X^2 + Y^2 = 1$.
   La connaissance de $X$ restreint les valeurs de $Y$ à $\pm\sqrt{1 - X^2}$. Il y a une dépendance fonctionnelle parfaite (bien que non bijective).
4. Conclusion : L'indépendance implique l'orthogonalité (pour les V.A. centrées), mais l'orthogonalité (indépendance linéaire) n'implique pas l'indépendance stochastique (qui requiert l'indépendance à tous les ordres de moments).
