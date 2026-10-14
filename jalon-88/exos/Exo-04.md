# Exercice 4

\subsection*{Exercice 4 : Produit de variables de Bernoulli \quad $\bigstar\bigstar\star\star\star$}

**Énoncé :**
Soient $X$ et $Y$ deux variables aléatoires indépendantes suivant des lois de Bernoulli de paramètres respectifs $p$ et $q$.
Déterminer la loi de la variable $Z = XY$.

**Correction :**
1. Les variables $X$ et $Y$ prennent leurs valeurs dans $\{0, 1\}$.
2. Le produit $Z = XY$ prend donc également ses valeurs dans $\{0, 1\}$. $Z$ suit donc une loi de Bernoulli.
3. Il suffit de calculer le paramètre de cette loi de Bernoulli, qui est $P(Z = 1)$.
4. L'événement $\{Z = 1\}$ équivaut à $\{XY = 1\}$.
5. Puisque $X$ et $Y$ ne prennent que les valeurs $0$ ou $1$, le produit $XY$ vaut $1$ si et seulement si $X = 1$ et $Y = 1$.
6. Ainsi, $\{Z = 1\} = \{X = 1\} \cap \{Y = 1\}$.
7. Par indépendance de $X$ et $Y$, la probabilité de l'intersection est le produit des probabilités :
   $P(Z = 1) = P(X = 1 \text{ et } Y = 1) = P(X = 1) P(Y = 1)$.
8. On remplace par les paramètres des lois : $P(X = 1) = p$ et $P(Y = 1) = q$.
9. On obtient $P(Z = 1) = pq$.
10. En conclusion, $Z$ suit une loi de Bernoulli de paramètre $pq$ : $Z \sim \mathcal{B}(pq)$.
