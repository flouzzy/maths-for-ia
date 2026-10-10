\subsection*{Exercice 3 : Loi de la somme de deux variables de Bernoulli indépendantes \quad $\bigstar\bigstar\star\star\star$}

Soient $X$ et $Y$ deux variables aléatoires indépendantes suivant une loi de Bernoulli de paramètre $p \in ]0, 1[$. Déterminer la loi de la somme $Z = X + Y$.

**Correction :**
1. Les valeurs possibles pour $X$ et $Y$ sont $0$ et $1$. Donc $Z$ prend ses valeurs dans $\{0, 1, 2\}$.
2. Pour $Z = 0$, $X$ et $Y$ doivent valoir $0$. Par indépendance : $\mathbb{P}(Z=0) = \mathbb{P}(X=0, Y=0) = \mathbb{P}(X=0)\mathbb{P}(Y=0) = (1-p)(1-p) = (1-p)^2$.
3. Pour $Z = 1$, il y a deux cas mutuellement exclusifs : $(X=1, Y=0)$ et $(X=0, Y=1)$. $\mathbb{P}(Z=1) = \mathbb{P}(X=1)\mathbb{P}(Y=0) + \mathbb{P}(X=0)\mathbb{P}(Y=1) = p(1-p) + (1-p)p = 2p(1-p)$.
4. Pour $Z = 2$, $X$ et $Y$ doivent valoir $1$. $\mathbb{P}(Z=2) = \mathbb{P}(X=1, Y=1) = \mathbb{P}(X=1)\mathbb{P}(Y=1) = p^2$.
5. On reconnaît les termes du développement de $((1-p) + p)^2$. $Z$ suit une loi binomiale $\mathcal{B}(2, p)$.