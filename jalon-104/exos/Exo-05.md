**Exercice 5**
**Difficulté :** $\star\star\star\star\star$

Soit $(H, \langle \cdot, \cdot \rangle)$ un espace de Hilbert séparable. Soit $(e_n)_{n \in \mathbb{N}}$ un système orthonormé (SON) dans $H$.

**Partie A : Inégalité de Bessel**

1.  Pour tout $N \in \mathbb{N}$, soit $P_N x = \sum_{n=0}^{N} \langle x, e_n \rangle e_n$ la projection orthogonale de $x$ sur l'espace engendré par $\{e_0, \ldots, e_N\}$.
    Démontrer que pour tout $N \in \mathbb{N}$ et pour tout $x \in H$, le vecteur $x - P_N x$ est orthogonal à chaque $e_k$ pour $k \in \{0, \ldots, N\}$.

2.  En utilisant le résultat de la question 1, calculer $\|x\|^2$ en fonction de $\|P_N x\|^2$ et $\|x - P_N x\|^2$.

3.  À partir du résultat de la question 2, et en rappelant la linéarité du produit scalaire, montrer que $\|P_N x\|^2 = \sum_{n=0}^{N} |\langle x, e_n \rangle|^2$.

4.  Déduire de ce qui précède l'inégalité de Bessel : $\sum_{n=0}^{\infty} |\langle x, e_n \rangle|^2 \le \|x\|^2$ pour tout $x \in H$.

**Partie B : Caractérisation des Bases Hilbertiennes**

1.  Rappeler la définition d'une base hilbertienne (ou base orthonormée complète) dans un espace de Hilbert.

2.  Démontrer que si $(e_n)_{n \in \mathbb{N}}$ est une base hilbertienne de $H$, alors l'identité de Parseval est vérifiée : $\sum_{n=0}^{\infty} |\langle x, e_n \rangle|^2 = \|x\|^2$ pour tout $x \in H$.

3.  Démontrer la réciproque : si l'identité de Parseval est vérifiée pour tout $x \in H$, alors $(e_n)_{n \in \mathbb{N}}$ est une base hilbertienne de $H$.

---

**Correction de l'Exercice 5**

**Partie A : Inégalité de Bessel**

1.  Nous devons démontrer que $\langle x - P_N x, e_k \rangle = 0$ pour tout $k \in \{0, \ldots, N\}$.
    Par définition, $P_N x = \sum_{n=0}^{N} \langle x, e_n \rangle e_n$.
    Calculons le produit scalaire :
    $\langle x - P_N x, e_k \rangle = \left\langle x - \sum_{n=0}^{N} \langle x, e_n \rangle e_n, e_k \right\rangle$.
    Par linéarité du produit scalaire par rapport à la première composante :
    $= \langle x, e_k \rangle - \left\langle \sum_{n=0}^{N} \langle x, e_n \rangle e_n, e_k \right\rangle$.
    Par (anti-)linéarité du produit scalaire par rapport à la deuxième composante (ou linéarité de $\overline{\langle \cdot, \cdot \rangle}$):
    $= \langle x, e_k \rangle - \sum_{n=0}^{N} \langle x, e_n \rangle \langle e_n, e_k \rangle$.
    Puisque $(e_n)_{n \in \mathbb{N}}$ est un système orthonormé, nous avons $\langle e_n, e_k \rangle = \delta_{nk}$, où $\delta_{nk}$ est le symbole de Kronecker (qui vaut 1 si $n=k$ et 0 si $n \ne k$).
    La somme se réduit donc à un seul terme, celui où $n=k$:
    $= \langle x, e_k \rangle - \langle x, e_k \rangle \langle e_k, e_k \rangle$.
    Comme $\langle e_k, e_k \rangle = \|e_k\|^2 = 1$ (car $(e_n)$ est un SON), nous obtenons :
    $= \langle x, e_k \rangle - \langle x, e_k \rangle \cdot 1$.
    $= \langle x, e_k \rangle - \langle x, e_k \rangle = 0$.
    Ainsi, $x - P_N x$ est orthogonal à chaque $e_k$ pour $k \in \{0, \ldots, N\}$.

2.  Nous allons utiliser le résultat de la question 1.
    Nous pouvons écrire $x$ comme la somme de deux vecteurs : $x = P_N x + (x - P_N x)$.
    Pour utiliser le théorème de Pythagore généralisé, nous devons montrer que $P_N x$ et $x - P_N x$ sont orthogonaux.
    Calculons leur produit scalaire :
    $\langle P_N x, x - P_N x \rangle = \left\langle \sum_{n=0}^{N} \langle x, e_n \rangle e_n, x - P_N x \right\rangle$.
    Par linéarité du produit scalaire par rapport à la première composante :
    $= \sum_{n=0}^{N} \langle x, e_n \rangle \langle e_n, x - P_N x \rangle$.
    D'après le résultat de la question 1, nous savons que $\langle x - P_N x, e_n \rangle = 0$ pour tout $n \in \{0, \ldots, N\}$.
    Par conséquent, $\langle e_n, x - P_N x \rangle = \overline{\langle x - P_N x, e_n \rangle} = \overline{0} = 0$.
    Donc, la somme devient :
    $= \sum_{n=0}^{N} \langle x, e_n \rangle \cdot 0 = 0$.
    Puisque $P_N x$ et $x - P_N x$ sont orthogonaux, nous pouvons appliquer le théorème de Pythagore :
    $\|x\|^2 = \|P_N x + (x - P_N x)\|^2 = \|P_N x\|^2 + \|x - P_N x\|^2$.

3.  Nous devons calculer $\|P_N x\|^2$.
    Nous avons $P_N x = \sum_{n=0}^{N} \langle x, e_n \rangle e_n$.
    Alors, $\|P_N x\|^2 = \langle P_N x, P_N x \rangle = \left\langle \sum_{n=0}^{N} \langle x, e_n \rangle e_n, \sum_{m=0}^{N} \langle x, e_m \rangle e_m \right\rangle$.
    En utilisant la linéarité par rapport à la première composante et l'anti-linéarité (ou linéarité conjuguée) par rapport à la deuxième composante :
    $= \sum_{n=0}^{N} \langle x, e_n \rangle \left\langle e_n, \sum_{m=0}^{N} \langle x, e_m \rangle e_m \right\rangle$.
    $= \sum_{n=0}^{N} \langle x, e_n \rangle \sum_{m=0}^{N} \overline{\langle x, e_m \rangle} \langle e_n, e_m \rangle$.
    Encore une fois, puisque $(e_n)$ est un SON, $\langle e_n, e_m \rangle = \delta_{nm}$. La deuxième somme ne contient donc qu'un seul terme non nul, celui où $m=n$:
    $= \sum_{n=0}^{N} \langle x, e_n \rangle \overline{\langle x, e_n \rangle} \cdot 1$.
    Nous savons que $z \overline{z} = |z|^2$ pour tout nombre complexe $z$. Donc :
    $= \sum_{n=0}^{N} |\langle x, e_n \rangle|^2$.
    Ainsi, $\|P_N x\|^2 = \sum_{n=0}^{N} |\langle x, e_n \rangle|^2$.

4.  Reprenons le résultat de la question 2 : $\|x\|^2 = \|P_N x\|^2 + \|x - P_N x\|^2$.
    Puisque la norme au carré d'un vecteur est toujours non négative, nous avons $\|x - P_N x\|^2 \ge 0$.
    Par conséquent, $\|x\|^2 \ge \|P_N x\|^2$.
    En substituant le résultat de la question 3, nous obtenons :
    $\|x\|^2 \ge \sum_{n=0}^{N} |\langle x, e_n \rangle|^2$.
    Cette inégalité est valable pour tout $N \in \mathbb{N}$.
    La suite des sommes partielles $S_N = \sum_{n=0}^{N} |\langle x, e_n \rangle|^2$ est une suite croissante de nombres réels non négatifs. Elle est majorée par $\|x\|^2$. Par le théorème de convergence monotone, une suite croissante et majorée converge.
    En passant à la limite quand $N \to \infty$, l'inégalité est préservée :
    $\lim_{N \to \infty} \sum_{n=0}^{N} |\langle x, e_n \rangle|^2 \le \|x\|^2$.
    Ceci nous donne l'inégalité de Bessel : $\sum_{n=0}^{\infty} |\langle x, e_n \rangle|^2 \le \|x\|^2$ pour tout $x \in H$.

**Partie B : Caractérisation des Bases Hilbertiennes**

1.  Un système orthonormé $(e_n)_{n \in \mathbb{N}}$ dans un espace de Hilbert $H$ est appelé une base hilbertienne (ou base orthonormée complète) si l'une des conditions équivalentes suivantes est satisfaite :
    *   Le sous-espace vectoriel fermé engendré par $(e_n)_{n \in \mathbb{N}}$, noté $\overline{\mathrm{span}\{e_n : n \in \mathbb{N}\}}$, est égal à $H$.
    *   Tout vecteur $x \in H$ peut être écrit comme une série de Fourier généralisée convergente en norme : $x = \sum_{n=0}^{\infty} \langle x, e_n \rangle e_n$.
    *   L'orthogonal de l'espace engendré par $(e_n)_{n \in \mathbb{N}}$ est trivial, c'est-à-dire que si $\langle x, e_n \rangle = 0$ pour tout $n \in \mathbb{N}$, alors $x$ doit être le vecteur nul $0_H$.

2.  Nous allons démontrer que si $(e_n)_{n \in \mathbb{N}}$ est une base hilbertienne de $H$, alors l'identité de Parseval est vérifiée.
    Si $(e_n)_{n \in \mathbb{N}}$ est une base hilbertienne, alors pour tout $x \in H$, nous avons par définition $x = \sum_{n=0}^{\infty} \langle x, e_n \rangle e_n$.
    Cette égalité signifie que la série converge en norme, c'est-à-dire :
    $\lim_{N \to \infty} \left\|x - \sum_{n=0}^{N} \langle x, e_n \rangle e_n \right\| = 0$.
    En utilisant la notation de la Partie A, cela s'écrit $\lim_{N \to \infty} \|x - P_N x\| = 0$.
    Par conséquent, $\lim_{N \to \infty} \|x - P_N x\|^2 = 0$.
    Reprenons le résultat de la question A.2 : $\|x\|^2 = \|P_N x\|^2 + \|x - P_N x\|^2$.
    En passant à la limite quand $N \to \infty$ :
    $\|x\|^2 = \lim_{N \to \infty} (\|P_N x\|^2 + \|x - P_N x\|^2)$.
    $\|x\|^2 = \lim_{N \to \infty} \|P_N x\|^2 + \lim_{N \to \infty} \|x - P_N x\|^2$.
    Nous avons établi $\lim_{N \to \infty} \|x - P_N x\|^2 = 0$.
    Et d'après la question A.3, $\|P_N x\|^2 = \sum_{n=0}^{N} |\langle x, e_n \rangle|^2$.
    Donc, $\lim_{N \to \infty} \|P_N x\|^2 = \lim_{N \to \infty} \sum_{n=0}^{N} |\langle x, e_n \rangle|^2 = \sum_{n=0}^{\infty} |\langle x, e_n \rangle|^2$.
    En substituant ces limites dans l'équation de la norme :
    $\|x\|^2 = \sum_{n=0}^{\infty} |\langle x, e_n \rangle|^2 + 0$.
    $\|x\|^2 = \sum_{n=0}^{\infty} |\langle x, e_n \rangle|^2$.
    Ceci est l'identité de Parseval.

3.  Nous allons démontrer la réciproque : si l'identité de Parseval est vérifiée pour tout $x \in H$, alors $(e_n)_{n \in \mathbb{N}}$ est une base hilbertienne de $H$.
    Nous utilisons la caractérisation d'une base hilbertienne mentionnée en B.1 : un SON $(e_n)_{n \in \mathbb{N}}$ est une base hilbertienne si son orthogonal est trivial. Cela signifie que si un vecteur $x \in H$ est orthogonal à tous les éléments du SON, alors ce vecteur doit être le vecteur nul.
    Supposons que l'identité de Parseval est vérifiée pour tout $x \in H$ :
    $\sum_{n=0}^{\infty} |\langle x, e_n \rangle|^2 = \|x\|^2$.
    Soit $x \in H$ un vecteur tel que $\langle x, e_n \rangle = 0$ pour tout $n \in \mathbb{N}$.
    Appliquons l'identité de Parseval à ce vecteur $x$ :
    $\|x\|^2 = \sum_{n=0}^{\infty} |\langle x, e_n \rangle|^2$.
    Puisque $\langle x, e_n \rangle = 0$ pour tout $n$, la somme devient :
    $\|x\|^2 = \sum_{n=0}^{\infty} |0|^2$.
    $\|x\|^2 = \sum_{n=0}^{\infty} 0$.
    $\|x\|^2 = 0$.
    Par la propriété fondamentale de la norme, si $\|x\|^2 = 0$, alors $\|x\| = 0$, ce qui implique que $x$ est le vecteur nul de $H$, c'est-à-dire $x = 0_H$.
    Nous avons donc démontré que si un vecteur $x$ est orthogonal à tous les éléments du SON $(e_n)$, alors $x$ est nécessairement le vecteur nul. Cette condition est précisément la définition d'une base hilbertienne.
    Par conséquent, si l'identité de Parseval est vérifiée, alors $(e_n)_{n \in \mathbb{N}}$ est une base hilbertienne de $H$.

Les deux sens ayant été démontrés, l'équivalence entre une base hilbertienne et l'identité de Parseval est établie.