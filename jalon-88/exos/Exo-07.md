\subsection*{Exercice 7 : Fonction caractéristique de la somme \quad $\bigstar\bigstar\bigstar\bigstar\star$}

Montrer que si $X$ et $Y$ sont deux variables aléatoires indépendantes, la fonction caractéristique de leur somme $Z = X + Y$ est le produit de leurs fonctions caractéristiques.

**Correction :**
1. La fonction caractéristique d'une variable aléatoire $U$ est définie par $\phi_U(t) = \mathbb{E}[e^{itU}]$ pour tout $t \in \mathbb{R}$.
2. Soit $t \in \mathbb{R}$. Pour $Z = X+Y$, $\phi_Z(t) = \mathbb{E}[e^{it(X+Y)}]$.
3. Par les propriétés de l'exponentielle complexe, $e^{it(X+Y)} = e^{itX} e^{itY}$.
4. Les variables aléatoires $U = e^{itX}$ et $V = e^{itY}$ sont des fonctions mesurables (continues) des variables $X$ et $Y$. Comme $X$ et $Y$ sont indépendantes, $U$ et $V$ sont indépendantes.
5. De plus, $U$ et $V$ sont bornées (module 1), donc intégrables. Le théorème sur l'espérance du produit s'applique (en le généralisant au cas complexe, par linéarité sur parties réelle et imaginaire) :
   $\mathbb{E}[UV] = \mathbb{E}[U]\mathbb{E}[V]$
6. Ce qui donne : $\mathbb{E}[e^{itX} e^{itY}] = \mathbb{E}[e^{itX}]\mathbb{E}[e^{itY}]$.
7. Ainsi, $\phi_Z(t) = \phi_X(t)\phi_Y(t)$.