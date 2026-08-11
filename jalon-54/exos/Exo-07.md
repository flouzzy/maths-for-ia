## Exercice 7 : Produit d'espaces compacts \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :** Démontrer le théorème de Tychonoff pour le produit de deux espaces séquentiellement compacts : Si $X$ et $Y$ sont deux espaces métriques compacts, alors l'espace produit $X \times Y$ muni de la distance $d((x_1, y_1), (x_2, y_2)) = d_X(x_1, x_2) + d_Y(y_1, y_2)$ est compact.

**Correction Détaillée :**
Soit $(z_n)_{n \in \mathbb{N}} = (x_n, y_n)_{n \in \mathbb{N}}$ une suite d'éléments de l'espace produit $X \times Y$.
Considérons la projection sur la première composante : $(x_n)_{n \in \mathbb{N}}$ est une suite dans l'espace métrique compact $X$.
Elle admet donc une sous-suite convergente. Il existe une fonction d'extraction $\phi : \mathbb{N} \to \mathbb{N}$ telle que $x_{\phi(n)} \to l_x \in X$.
Considérons maintenant la suite projetée correspondante sur la seconde composante, mais indexée par la même extraction $\phi$ : il s'agit de la suite $(y_{\phi(n)})_{n \in \mathbb{N}}$.
C'est une suite dans l'espace métrique compact $Y$. Elle admet à son tour une sous-suite convergente.
Il existe donc une seconde fonction d'extraction $\psi : \mathbb{N} \to \mathbb{N}$ telle que $y_{\phi(\psi(n))} \to l_y \in Y$.
Regardons maintenant la première composante le long de cette double extraction : la sous-suite $(x_{\phi(\psi(n))})_{n \in \mathbb{N}}$ est une sous-suite de la suite convergente $(x_{\phi(n)})$, donc elle converge vers la même limite $l_x$.
Ainsi, la double sous-suite $(z_{\phi(\psi(n))}) = (x_{\phi(\psi(n))}, y_{\phi(\psi(n))})$ converge dans l'espace produit vers le couple limite $(l_x, l_y) \in X \times Y$.
Toute suite de $X \times Y$ admettant une sous-suite convergente, l'espace $X \times Y$ est séquentiellement compact.