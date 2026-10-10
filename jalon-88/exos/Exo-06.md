\subsection*{Exercice 6 : Indépendance de fonctions mesurables \quad $\bigstar\bigstar\bigstar\star\star$}

Soient $X$ et $Y$ deux variables aléatoires indépendantes à valeurs dans $\mathbb{R}$. Soient $f, g : \mathbb{R} \to \mathbb{R}$ deux fonctions boréliennes (mesurables). Montrer que les variables $f(X)$ et $g(Y)$ sont indépendantes.

**Correction :**
1. On doit montrer que pour tout boréliens $A, B$ de $\mathbb{R}$, $\mathbb{P}(f(X) \in A, g(Y) \in B) = \mathbb{P}(f(X) \in A)\mathbb{P}(g(Y) \in B)$.
2. Par définition de l'image réciproque, $f(X) \in A \iff X \in f^{-1}(A)$ et $g(Y) \in B \iff Y \in g^{-1}(B)$.
3. Puisque $f$ et $g$ sont mesurables, les images réciproques $f^{-1}(A)$ et $g^{-1}(B)$ sont des boréliens de $\mathbb{R}$.
4. On peut donc utiliser la définition de l'indépendance de $X$ et $Y$ sur ces boréliens :
   $\mathbb{P}(X \in f^{-1}(A), Y \in g^{-1}(B)) = \mathbb{P}(X \in f^{-1}(A))\mathbb{P}(Y \in g^{-1}(B))$
5. En réécrivant en termes de $f(X)$ et $g(Y)$, on obtient :
   $\mathbb{P}(f(X) \in A, g(Y) \in B) = \mathbb{P}(f(X) \in A)\mathbb{P}(g(Y) \in B)$
6. Ainsi, les variables aléatoires $f(X)$ et $g(Y)$ sont indépendantes.