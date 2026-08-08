## Exercice 9 : SNCF et topologie arborescente \quad $\bigstar\bigstar\bigstar\star$

**Énoncé :** Sur $\mathbb{R}^2$, on définit la "distance de la jungle" (ou SNCF centrée en $0$) par $d(x, y) = ||x-y||_2$ si $x$ et $y$ sont alignés avec l'origine, et $d(x, y) = ||x||_2 + ||y||_2$ sinon. Décrire géométriquement les boules ouvertes de cet espace.

**Correction :** C'est une métrique valide (les détails de l'inégalité triangulaire découlent du triangle euclidien via l'origine).
Fixons un point $x \neq 0$ et cherchons la boule ouverte $B(x, r)$.
**Cas 1 :** $r \le ||x||_2$. Soit $y \in B(x, r)$. Si $y$ n'est pas aligné avec $0$, $d(x, y) = ||x||_2 + ||y||_2 \ge ||x||_2 \ge r$, donc $y$ ne peut pas appartenir à la boule. La boule est donc strictement contenue dans le segment ouvert de la droite passant par $0$ et $x$, de longueur $2r$ centré en $x$. (Topologie 1D).
**Cas 2 :** $r > ||x||_2$. Si $y$ n'est pas aligné avec $0$, il est dans la boule ssi $||x||_2 + ||y||_2 < r$, c'est-à-dire $||y||_2 < r - ||x||_2$.
Donc la boule est constituée de la réunion d'un segment sur la droite issue de l'origine contenant $x$, et d'une vraie boule euclidienne (ouverte) centrée en l'origine de rayon $r - ||x||_2$.
Cet espace métrique est localement $1$-dimensionnel sauf en l'origine où il est $2$-dimensionnel.
