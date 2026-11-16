import os

def gen_exos():
    os.makedirs("jalon-105/exos", exist_ok=True)

    # Exo 1
    with open("jalon-105/exos/Exo-01.md", "w") as f:
        f.write(r"""# Exercice 1 : Calcul direct en dimension finie $\bigstar\star\star\star\star$
## Énoncé
Soit $H = \mathbb{R}^2$ muni du produit scalaire usuel. On définit l'opérateur linéaire $T : H \to H$ par sa matrice $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ dans la base canonique.
1. Calculer explicitement l'opérateur adjoint $T^*$ par définition, en évaluant $\langle Tx, y \rangle$.
2. Vérifier que la matrice de $T^*$ dans la base canonique correspond bien à la transposée de la matrice $A$.

## Correction
1. Soient $x = (x_1, x_2)$ et $y = (y_1, y_2)$ dans $\mathbb{R}^2$.
On a $Tx = (x_1 + 2x_2, 3x_1 + 4x_2)$.
Le produit scalaire donne :
$$ \langle Tx, y \rangle = (x_1 + 2x_2)y_1 + (3x_1 + 4x_2)y_2 $$
$$ = x_1 y_1 + 2 x_2 y_1 + 3 x_1 y_2 + 4 x_2 y_2 $$
Pour identifier $T^*y$, on doit réorganiser l'expression pour mettre $x_1$ et $x_2$ en facteur, afin d'obtenir la forme $x_1 (T^*y)_1 + x_2 (T^*y)_2$ :
$$ = x_1 (y_1 + 3y_2) + x_2 (2y_1 + 4y_2) $$
$$ = \langle x, T^*y \rangle $$
On déduit donc que l'opérateur adjoint $T^*$ agit sur $y$ de la manière suivante :
$$ T^*y = (y_1 + 3y_2, 2y_1 + 4y_2) $$

2. Exprimons $T^*y$ sous forme matricielle. En posant $y$ comme vecteur colonne :
$$ T^*y = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} y_1 \\ y_2 \end{pmatrix} $$
La matrice de $T^*$ dans la base canonique est donc $\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$.
On constate que cette matrice est exactement $A^T$, la transposée de la matrice $A$.
""")

    # Exo 2
    with open("jalon-105/exos/Exo-02.md", "w") as f:
        f.write(r"""# Exercice 2 : Propriété multiplicative de l'adjoint $\bigstar\star\star\star\star$
## Énoncé
Soient $H$ un espace de Hilbert, et $S, T \in \mathcal{L}(H)$ deux opérateurs linéaires continus.
Démontrer rigoureusement que $(ST)^* = T^* S^*$.

## Correction
Soient $x, y \in H$. Par définition de l'opérateur adjoint, nous avons pour tout opérateur linéaire $A$ et tout couple de vecteurs $(u, v)$ : $\langle Au, v \rangle = \langle u, A^*v \rangle$.
Appliquons cela à l'opérateur composé $ST$.
1. Partons du membre de gauche de l'égalité définissant $(ST)^*$ :
$$ \langle (ST)x, y \rangle = \langle S(Tx), y \rangle $$
2. Appliquons la définition de l'adjoint de $S$ en considérant $Tx$ comme le vecteur d'entrée $u$ :
$$ \langle S(Tx), y \rangle = \langle Tx, S^*y \rangle $$
3. Appliquons maintenant la définition de l'adjoint de $T$, en considérant $x$ comme le vecteur $u$ et $S^*y$ comme le vecteur $v$ :
$$ \langle Tx, S^*y \rangle = \langle x, T^*(S^*y) \rangle $$
$$ = \langle x, (T^*S^*)y \rangle $$
4. En rassemblant l'ensemble de la chaîne d'égalités, nous obtenons pour tout $x, y \in H$ :
$$ \langle (ST)x, y \rangle = \langle x, (T^*S^*)y \rangle $$
Par définition de l'unicité de l'opérateur adjoint (qui stipule que si $\langle Ax, y \rangle = \langle x, By \rangle$ pour tout $x,y$, alors $A^* = B$), on conclut immédiatement que :
$$ (ST)^* = T^* S^* $$
""")

    # Exo 3
    with open("jalon-105/exos/Exo-03.md", "w") as f:
        f.write(r"""# Exercice 3 : Opérateur de multiplication dans $L^2$ $\bigstar\bigstar\star\star\star$
## Énoncé
Soit $H = L^2([0,1], \mathbb{C})$ muni du produit scalaire classique $\langle f, g \rangle = \int_0^1 f(t)\overline{g(t)} dt$.
Soit $m : [0,1] \to \mathbb{C}$ une fonction mesurable et bornée, c'est-à-dire qu'il existe $M > 0$ tel que $|m(t)| \le M$ presque partout.
On définit l'opérateur de multiplication $T_m : H \to H$ par $(T_m f)(t) = m(t)f(t)$.
1. Montrer que $T_m$ est bien un opérateur linéaire continu sur $H$.
2. Déterminer l'adjoint $T_m^*$ de $T_m$.
3. À quelle condition nécessaire et suffisante sur la fonction $m$ l'opérateur $T_m$ est-il auto-adjoint ?

## Correction
1. Linéarité : pour tous $f, g \in H$ et $\lambda, \mu \in \mathbb{C}$, on a pour presque tout $t \in [0, 1]$ :
$$ (T_m(\lambda f + \mu g))(t) = m(t)(\lambda f(t) + \mu g(t)) = \lambda m(t)f(t) + \mu m(t)g(t) = \lambda (T_m f)(t) + \mu (T_m g)(t) $$
Donc $T_m(\lambda f + \mu g) = \lambda T_m f + \mu T_m g$. L'opérateur est linéaire.
Continuité (caractérisée par le fait d'être borné) : Soit $f \in H$. Évaluons la norme au carré de $T_m f$ :
$$ \|T_m f\|_{L^2}^2 = \int_0^1 |m(t)f(t)|^2 dt = \int_0^1 |m(t)|^2 |f(t)|^2 dt $$
Puisque $m$ est bornée par $M$, on a $|m(t)|^2 \le M^2$ presque partout :
$$ \|T_m f\|_{L^2}^2 \le \int_0^1 M^2 |f(t)|^2 dt = M^2 \|f\|_{L^2}^2 $$
Donc $\|T_m f\|_{L^2} \le M \|f\|_{L^2}$. L'opérateur $T_m$ est continu (borné) et sa norme d'opérateur vérifie $\|T_m\| \le M$.

2. Calculons l'adjoint. Soient $f, g \in H$. Écrivons le produit scalaire $\langle T_m f, g \rangle$ :
$$ \langle T_m f, g \rangle = \int_0^1 (T_m f)(t) \overline{g(t)} dt = \int_0^1 m(t)f(t) \overline{g(t)} dt $$
Pour faire apparaître $f(t)$ isolément à gauche du produit pour identifier l'adjoint, nous modifions le groupement à l'intérieur de l'intégrale :
$$ = \int_0^1 f(t) (m(t)\overline{g(t)}) dt $$
Or, nous devons l'écrire sous la forme $\int_0^1 f(t) \overline{(T_m^* g)(t)} dt$. Sachant que $m(t)\overline{g(t)} = \overline{(\overline{m(t)}g(t))}$, on réécrit l'expression :
$$ = \int_0^1 f(t) \overline{(\overline{m(t)}g(t))} dt $$
Par identification dans le produit scalaire, nous avons $(T_m^* g)(t) = \overline{m(t)}g(t)$.
Ainsi, l'adjoint est l'opérateur de multiplication par la fonction conjuguée : $T_m^* = T_{\overline{m}}$.

3. Un opérateur est auto-adjoint si et seulement si $T_m = T_m^*$.
Cela signifie que pour toute fonction $f \in H$, $(T_m f)(t) = (T_m^* f)(t)$ presque partout.
Soit $m(t)f(t) = \overline{m(t)}f(t)$ pour tout $f$ et presque tout $t$.
En choisissant $f(t) = 1$ (qui est bien dans $L^2([0,1])$), on obtient $m(t) = \overline{m(t)}$ presque partout.
Ceci est la définition d'un nombre réel.
Conclusion : $T_m$ est auto-adjoint si et seulement si la fonction $m$ est à valeurs réelles presque partout.
""")

    # Exo 4
    with open("jalon-105/exos/Exo-04.md", "w") as f:
        f.write(r"""# Exercice 4 : Adjoint de l'opérateur de décalage bilatéral $\bigstar\bigstar\star\star\star$
## Énoncé
Soit $\ell^2(\mathbb{Z})$ l'espace de Hilbert des suites bilatérales complexes de carré sommable, muni du produit scalaire :
$$ \langle x, y \rangle = \sum_{n=-\infty}^{+\infty} x_n \overline{y_n} $$
On définit l'opérateur de décalage bilatéral à droite (Right Shift) $S : \ell^2(\mathbb{Z}) \to \ell^2(\mathbb{Z})$ par :
$$ (Sx)_n = x_{n-1} $$
1. Montrer que $S$ est une isométrie (et donc un opérateur continu).
2. Déterminer l'adjoint $S^*$ de $S$. L'opérateur $S$ est-il unitaire ?

## Correction
1. Soit $x \in \ell^2(\mathbb{Z})$. Calculons la norme au carré de $Sx$ :
$$ \|Sx\|^2 = \sum_{n=-\infty}^{+\infty} |(Sx)_n|^2 = \sum_{n=-\infty}^{+\infty} |x_{n-1}|^2 $$
En effectuant le changement de variable (ou décalage d'indice) $k = n - 1$, la somme parcourant tous les entiers relatifs reste invariante :
$$ = \sum_{k=-\infty}^{+\infty} |x_k|^2 = \|x\|^2 $$
On a donc $\|Sx\| = \|x\|$ pour tout $x$. L'opérateur $S$ préserve la norme, c'est une isométrie, et sa norme d'opérateur est exactement 1 (il est continu).

2. Pour déterminer l'adjoint, calculons le produit scalaire $\langle Sx, y \rangle$ pour $x, y \in \ell^2(\mathbb{Z})$ :
$$ \langle Sx, y \rangle = \sum_{n=-\infty}^{+\infty} (Sx)_n \overline{y_n} = \sum_{n=-\infty}^{+\infty} x_{n-1} \overline{y_n} $$
Le but est d'écrire cette expression sous la forme $\langle x, S^*y \rangle = \sum_m x_m \overline{(S^*y)_m}$.
Faisons le changement d'indice $m = n - 1$, ce qui implique $n = m + 1$. La somme sur $m$ parcourt également $\mathbb{Z}$ :
$$ = \sum_{m=-\infty}^{+\infty} x_m \overline{y_{m+1}} $$
Par identification terme à terme, on obtient $\overline{(S^*y)_m} = \overline{y_{m+1}}$, c'est-à-dire :
$$ (S^*y)_m = y_{m+1} $$
L'adjoint de l'opérateur de décalage à droite est donc l'opérateur de décalage à gauche.
Pour vérifier si $S$ est unitaire, il faut vérifier si $S^* S = I$ et $S S^* = I$.
$$ (S^* Sx)_n = (S^*(Sx))_n = (Sx)_{n+1} = x_{(n+1)-1} = x_n $$
Donc $S^*S = I$.
$$ (SS^*x)_n = (S(S^*x))_n = (S^*x)_{n-1} = x_{(n-1)+1} = x_n $$
Donc $SS^* = I$.
Puisque $S^* S = SS^* = I$, on a bien $S^* = S^{-1}$. L'opérateur de décalage bilatéral est un opérateur **unitaire**.
""")

    # Exo 5
    with open("jalon-105/exos/Exo-05.md", "w") as f:
        f.write(r"""# Exercice 5 : Opérateur de Volterra $\bigstar\bigstar\bigstar\star\star$
## Énoncé
Soit $H = L^2([0,1])$ muni de son produit scalaire usuel réel.
On définit l'opérateur de Volterra $V : H \to H$ par :
$$ (Vf)(x) = \int_0^x f(y) dy $$
1. Déterminer l'adjoint $V^*$ de l'opérateur de Volterra.
2. Démontrer que $V + V^*$ est un opérateur de rang 1. Préciser cet opérateur.

## Correction
1. Soient $f, g \in L^2([0,1])$. Calculons le produit scalaire $\langle Vf, g \rangle$ :
$$ \langle Vf, g \rangle = \int_0^1 (Vf)(x) g(x) dx = \int_0^1 \left( \int_0^x f(y) dy \right) g(x) dx $$
Cette expression est une intégrale double sur le domaine $D = \{ (x,y) \in [0,1]^2 \mid 0 \le y \le x \le 1 \}$.
D'après le théorème de Fubini, on peut intervertir l'ordre d'intégration. En intégrant d'abord par rapport à $x$, l'intervalle pour $x$ devient $[y, 1]$, tandis que $y$ varie de $0$ à $1$ :
$$ \langle Vf, g \rangle = \int_0^1 \left( \int_y^1 g(x) dx \right) f(y) dy $$
$$ = \int_0^1 f(y) \left( \int_y^1 g(x) dx \right) dy $$
Pour identifier cela avec $\langle f, V^*g \rangle = \int_0^1 f(y) (V^*g)(y) dy$, on déduit que :
$$ (V^*g)(y) = \int_y^1 g(x) dx $$
En renommant la variable libre par $x$ et la variable muette d'intégration par $y$ pour la présentation standard, on a :
$$ (V^*g)(x) = \int_x^1 g(y) dy $$

2. Calculons la somme $(V + V^*)f$ pour toute fonction $f \in H$ :
$$ ((V + V^*)f)(x) = (Vf)(x) + (V^*f)(x) = \int_0^x f(y) dy + \int_x^1 f(y) dy $$
D'après la relation de Chasles pour l'intégrale :
$$ = \int_0^1 f(y) dy $$
Cette valeur est une constante par rapport à la variable $x$. On peut l'écrire comme :
$$ ((V + V^*)f)(x) = \langle f, \mathbf{1} \rangle \cdot \mathbf{1}(x) $$
où $\mathbf{1}$ est la fonction constante égale à 1 sur $[0,1]$.
L'image de l'opérateur $V + V^*$ est donc générée par le seul vecteur (la fonction) $\mathbf{1}$.
L'opérateur $V + V^*$ est bien un opérateur de projection unidimensionnel non normalisé, donc il est de rang 1.
""")

    # Exo 6
    with open("jalon-105/exos/Exo-06.md", "w") as f:
        f.write(r"""# Exercice 6 : Noyau, Image et Adjoint $\bigstar\bigstar\bigstar\star\star$
## Énoncé
Soit $H$ un espace de Hilbert et $T \in \mathcal{L}(H)$.
On note $\ker(T)$ le noyau de $T$ et $\text{Im}(T)$ l'image de $T$.
1. Démontrer que $\ker(T^*) = (\text{Im}(T))^\perp$.
2. En déduire que $\overline{\text{Im}(T)} = (\ker(T^*))^\perp$.
3. Démontrer que $\ker(T^* T) = \ker(T)$.

## Correction
1. Soit $y \in H$. Prouvons l'équivalence pas à pas :
$$ y \in \ker(T^*) \iff T^*y = 0_H $$
Cela signifie que le vecteur $T^*y$ est nul, ce qui est équivalent à dire qu'il est orthogonal à tout vecteur de l'espace $H$ :
$$ \iff \forall x \in H, \quad \langle x, T^*y \rangle = 0 $$
Par la définition de l'opérateur adjoint, nous pouvons faire passer l'opérateur sur le côté gauche du produit scalaire :
$$ \iff \forall x \in H, \quad \langle Tx, y \rangle = 0 $$
L'ensemble des éléments de la forme $Tx$ lorsque $x$ parcourt $H$ constitue exactement l'image de $T$, notée $\text{Im}(T)$.
Donc, l'équation $\langle Tx, y \rangle = 0$ pour tout $x$ signifie que le vecteur $y$ est orthogonal à tous les vecteurs de $\text{Im}(T)$ :
$$ \iff \forall z \in \text{Im}(T), \quad \langle z, y \rangle = 0 $$
$$ \iff y \in (\text{Im}(T))^\perp $$
Nous avons ainsi démontré l'égalité ensembliste : $\ker(T^*) = (\text{Im}(T))^\perp$.

2. Prenons l'orthogonal des deux membres de l'égalité précédente :
$$ (\ker(T^*))^\perp = ((\text{Im}(T))^\perp)^\perp $$
Dans un espace de Hilbert, d'après le théorème du bipolaire (ou double orthogonal), pour tout sous-espace vectoriel $M$, on a $(M^\perp)^\perp = \overline{M}$ (l'adhérence de $M$).
En appliquant ce théorème à $M = \text{Im}(T)$, on obtient immédiatement :
$$ (\ker(T^*))^\perp = \overline{\text{Im}(T)} $$

3. Montrons l'égalité des noyaux par double inclusion.
- Sens $\supseteq$ (inclusion triviale) :
Si $x \in \ker(T)$, alors $Tx = 0$. Donc $T^*(Tx) = T^*(0) = 0$. Donc $x \in \ker(T^* T)$.
- Sens $\subseteq$ :
Soit $x \in \ker(T^* T)$. Alors $T^* T x = 0$.
Par conséquent, son produit scalaire avec $x$ est nul :
$$ \langle T^* T x, x \rangle = 0 $$
En utilisant la définition de l'adjoint $T^*$ pour le passer de l'autre côté du produit scalaire :
$$ \langle Tx, (T^*)^* x \rangle = 0 $$
Puisque $(T^*)^* = T$, on obtient :
$$ \langle Tx, Tx \rangle = 0 $$
$$ \|Tx\|^2 = 0 \implies Tx = 0 \implies x \in \ker(T) $$
Les deux inclusions prouvent que $\ker(T^* T) = \ker(T)$.
""")

    # Exo 7
    with open("jalon-105/exos/Exo-07.md", "w") as f:
        f.write(r"""# Exercice 7 : Identité de polarisation pour les opérateurs auto-adjoints $\bigstar\bigstar\bigstar\bigstar\star$
## Énoncé
Soit $H$ un espace de Hilbert complexe. Soit $T \in \mathcal{L}(H)$ un opérateur auto-adjoint, c'est-à-dire tel que $T^* = T$.
1. Montrer que pour tout $x \in H$, le scalaire $\langle Tx, x \rangle$ est réel.
2. Soit $A \in \mathcal{L}(H)$ un opérateur quelconque. On suppose que pour tout $x \in H$, $\langle Ax, x \rangle = 0$. En développant $\langle A(x+y), x+y \rangle$ et $\langle A(x+iy), x+iy \rangle$, démontrer rigoureusement que $A = 0$ (l'opérateur nul).
3. Déduire de ce qui précède que si $T \in \mathcal{L}(H)$ est un opérateur tel que $\langle Tx, x \rangle$ est réel pour tout $x \in H$, alors $T$ est auto-adjoint. (Ce résultat est spécifiquement vrai pour les Hilbert complexes).

## Correction
1. Soit $x \in H$. Calculons le conjugué du scalaire $c = \langle Tx, x \rangle$ :
$$ \overline{\langle Tx, x \rangle} = \langle x, Tx \rangle $$
Par définition de l'adjoint :
$$ = \langle T^*x, x \rangle $$
Puisque l'opérateur $T$ est supposé auto-adjoint ($T^* = T$), nous avons :
$$ = \langle Tx, x \rangle $$
Ainsi, le scalaire est égal à son propre conjugué complexe ($\overline{c} = c$), ce qui prouve que $\langle Tx, x \rangle \in \mathbb{R}$ pour tout $x \in H$.

2. Hypothèse : $\forall x \in H, \langle Ax, x \rangle = 0$.
Soient $x, y \in H$. Évaluons cette propriété sur le vecteur $x+y$ :
$$ 0 = \langle A(x+y), x+y \rangle = \langle Ax + Ay, x+y \rangle $$
En développant par bilinéarité (ou plus précisément sesquilinéarité) :
$$ = \langle Ax, x \rangle + \langle Ax, y \rangle + \langle Ay, x \rangle + \langle Ay, y \rangle $$
Par hypothèse sur les vecteurs $x$ et $y$, le premier et le dernier terme sont nuls :
$$ = 0 + \langle Ax, y \rangle + \langle Ay, x \rangle + 0 $$
Nous obtenons la relation (1) : $\langle Ax, y \rangle + \langle Ay, x \rangle = 0$.

Maintenant, évaluons la propriété sur le vecteur $x + iy$ :
$$ 0 = \langle A(x+iy), x+iy \rangle = \langle Ax + iAy, x+iy \rangle $$
$$ = \langle Ax, x \rangle + \langle Ax, iy \rangle + \langle iAy, x \rangle + \langle iAy, iy \rangle $$
Rappelons que le scalaire sort du deuxième argument avec un conjugué (anti-linéarité à droite) : $\langle u, cv \rangle = \overline{c} \langle u, v \rangle$, donc $\langle Ax, iy \rangle = -i \langle Ax, y \rangle$.
Le scalaire sort du premier argument linéairement : $\langle cu, v \rangle = c \langle u, v \rangle$, donc $\langle iAy, x \rangle = i \langle Ay, x \rangle$.
Le dernier terme donne $\langle iAy, iy \rangle = i(-i) \langle Ay, y \rangle = \langle Ay, y \rangle = 0$.
En remplaçant :
$$ 0 = 0 - i\langle Ax, y \rangle + i\langle Ay, x \rangle + 0 $$
En divisant par $i$ (ou en multipliant par $-i$), on obtient la relation (2) : $-\langle Ax, y \rangle + \langle Ay, x \rangle = 0$.
En additionnant l'équation (1) et l'équation (2), nous avons :
$$ 2 \langle Ay, x \rangle = 0 \implies \langle Ay, x \rangle = 0 $$
Cette relation est vraie pour tous vecteurs $x, y \in H$. En fixant un vecteur $y$ quelconque, son image $Ay$ est orthogonale à tout vecteur $x \in H$. La seule possibilité est que $Ay = 0$.
Puisque $Ay = 0$ pour tout $y$, l'opérateur $A$ est l'opérateur nul, soit $A = 0$.

3. Supposons que $\langle Tx, x \rangle \in \mathbb{R}$ pour tout $x$.
Cela signifie que pour tout $x$, le scalaire est égal à son conjugué :
$$ \langle Tx, x \rangle = \overline{\langle Tx, x \rangle} = \langle x, Tx \rangle $$
En utilisant la définition de l'adjoint sur le terme de droite :
$$ \langle Tx, x \rangle = \langle T^*x, x \rangle $$
Par linéarité à gauche du produit scalaire, nous pouvons soustraire les deux termes :
$$ \langle Tx, x \rangle - \langle T^*x, x \rangle = 0 $$
$$ \langle (T - T^*)x, x \rangle = 0 $$
Posons l'opérateur $A = T - T^*$. Nous avons montré que $\forall x \in H, \langle Ax, x \rangle = 0$.
D'après le résultat rigoureusement démontré à la question 2, cela implique immédiatement que $A = 0$, et par conséquent :
$$ T - T^* = 0 \implies T = T^* $$
L'opérateur $T$ est donc bien auto-adjoint.
""")

    # Exo 8
    with open("jalon-105/exos/Exo-08.md", "w") as f:
        f.write(r"""# Exercice 8 : Décomposition polaire (Introduction) $\bigstar\bigstar\bigstar\bigstar\star$
## Énoncé
Soit $H$ un espace de Hilbert et $T \in \mathcal{L}(H)$.
On définit un opérateur dit "absolu" lié à $T$ via la construction de l'opérateur auto-adjoint $A = T^* T$.
1. Montrer que $A$ est auto-adjoint et positif (c'est-à-dire $\forall x \in H, \langle Ax, x \rangle \ge 0$).
2. Soit $\lambda \in \mathbb{C}$ une valeur propre de $A$ et $x$ un vecteur propre associé non nul. Montrer que $\lambda$ est un nombre réel positif ou nul.
3. Si $T$ est normal (c'est-à-dire $T^* T = T T^*$), démontrer rigoureusement que $\|Tx\| = \|T^*x\|$ pour tout vecteur $x \in H$.

## Correction
1. Vérifions d'abord que $A$ est auto-adjoint.
En utilisant la propriété d'involution de l'adjoint $(ST)^* = T^*S^*$ (démontrée dans l'exercice 2) :
$$ A^* = (T^* T)^* = T^* (T^*)^* = T^* T = A $$
Donc $A$ est bien un opérateur auto-adjoint.
Montrons qu'il est positif. Soit un vecteur quelconque $x \in H$. Évaluons $\langle Ax, x \rangle$ :
$$ \langle Ax, x \rangle = \langle (T^*T)x, x \rangle $$
Par définition de l'opérateur adjoint $T^*$, on le transfère sur le second membre. Il devient $(T^*)^* = T$ :
$$ = \langle Tx, Tx \rangle = \|Tx\|^2 $$
Comme la norme d'un vecteur dans un espace de Hilbert est toujours un nombre réel positif ou nul, on conclut que :
$$ \langle Ax, x \rangle \ge 0 \quad \forall x \in H $$
L'opérateur $A$ est donc positif.

2. Supposons que $Ax = \lambda x$ avec $x \ne 0_H$.
Calculons le produit scalaire $\langle Ax, x \rangle$ :
$$ \langle Ax, x \rangle = \langle \lambda x, x \rangle = \lambda \langle x, x \rangle = \lambda \|x\|^2 $$
D'autre part, d'après la question 1, nous avons établi que $\langle Ax, x \rangle = \|Tx\|^2$.
Par conséquent, on obtient l'égalité :
$$ \lambda \|x\|^2 = \|Tx\|^2 $$
Puisque $x \ne 0_H$, on sait que sa norme est strictement positive ($\|x\|^2 > 0$). On peut donc diviser par cette quantité :
$$ \lambda = \frac{\|Tx\|^2}{\|x\|^2} $$
Le membre de droite est le quotient de deux nombres réels positifs ou nuls. Il en résulte que $\lambda \in \mathbb{R}$ et $\lambda \ge 0$.

3. Hypothèse : L'opérateur $T$ est normal, donc $T^*T = TT^*$.
Soit $x \in H$. Considérons le carré de la norme de $Tx$ et utilisons la définition de l'adjoint :
$$ \|Tx\|^2 = \langle Tx, Tx \rangle = \langle x, T^*(Tx) \rangle = \langle x, (T^*T)x \rangle $$
Utilisons maintenant la propriété de normalité de l'opérateur pour substituer $T^*T$ par $TT^*$ :
$$ = \langle x, (TT^*)x \rangle = \langle x, T(T^*x) \rangle $$
Appliquons à nouveau la définition de l'adjoint pour déplacer l'opérateur $T$ du second membre vers le premier membre. Son adjoint est $T^*$ :
$$ = \langle T^*x, T^*x \rangle = \|T^*x\|^2 $$
Nous avons ainsi démontré la chaîne d'égalités rigoureuse $\|Tx\|^2 = \|T^*x\|^2$, ce qui implique, par prise de la racine carrée (les normes étant positives), que :
$$ \|Tx\| = \|T^*x\| \quad \forall x \in H $$
""")

    # Exo 9
    with open("jalon-105/exos/Exo-09.md", "w") as f:
        f.write(r"""# Exercice 9 : Inverse d'un opérateur et son adjoint $\bigstar\bigstar\bigstar\bigstar\bigstar$
## Énoncé
Soit $H$ un espace de Hilbert et $T \in \mathcal{L}(H)$ un opérateur inversible (bijectif, d'inverse borné $T^{-1} \in \mathcal{L}(H)$).
1. Démontrer que l'opérateur adjoint $T^*$ est également inversible et que $(T^*)^{-1} = (T^{-1})^*$.
2. Déduire que si un opérateur inversible est auto-adjoint, alors son inverse est également auto-adjoint.

## Correction
1. Par hypothèse, $T$ est inversible, ce qui signifie que $T T^{-1} = I$ et $T^{-1} T = I$, où $I$ est l'opérateur identité sur $H$.
Prenons l'adjoint de chaque membre de ces deux équations vectorielles. Nous utiliserons la propriété algébrique multiplicative $(AB)^* = B^*A^*$.
Pour la première équation :
$$ (T T^{-1})^* = I^* $$
L'adjoint de l'identité est l'identité elle-même (car $\langle Ix, y \rangle = \langle x, y \rangle = \langle x, Iy \rangle$). En appliquant la règle d'inversion de l'ordre pour l'adjoint d'un produit, on obtient :
$$ (T^{-1})^* T^* = I $$
Pour la seconde équation :
$$ (T^{-1} T)^* = I^* $$
$$ T^* (T^{-1})^* = I $$
Nous venons de démontrer qu'il existe un opérateur, spécifiquement $S = (T^{-1})^*$, tel que $S T^* = I$ et $T^* S = I$.
Par la définition même de l'opérabilité inverse, cela signifie que $T^*$ est inversible, et que son inverse inverse (unique) est précisément $S$.
On conclut rigoureusement que :
$$ (T^*)^{-1} = (T^{-1})^* $$

2. Hypothèse : $T$ est inversible et auto-adjoint, ce qui signifie que $T^* = T$.
Nous voulons montrer que $T^{-1}$ est auto-adjoint, c'est-à-dire que $(T^{-1})^* = T^{-1}$.
D'après le résultat démontré à la question 1, nous connaissons la relation :
$$ (T^{-1})^* = (T^*)^{-1} $$
Maintenant, appliquons l'hypothèse que $T$ est auto-adjoint en remplaçant l'opérateur $T^*$ par l'opérateur $T$ dans le membre de droite de l'équation :
$$ (T^*)^{-1} = (T)^{-1} = T^{-1} $$
En connectant les deux parties de la chaîne logique, on obtient formellement :
$$ (T^{-1})^* = T^{-1} $$
Cette équation est la définition exacte stipulant que l'opérateur inverse $T^{-1}$ est un opérateur auto-adjoint.
""")

    # Exo 10
    with open("jalon-105/exos/Exo-10.md", "w") as f:
        f.write(r"""# Exercice 10 : Égalité fondamentale des normes $\bigstar\bigstar\bigstar\bigstar\bigstar$
## Énoncé
Soit $H$ un espace de Hilbert et $T \in \mathcal{L}(H)$ un opérateur linéaire continu.
L'objectif de cet exercice est de démontrer la propriété de $C^*$-algèbre liant la norme de l'opérateur et la norme de son adjoint :
$$ \|T^* T\| = \|T\|^2 $$
Rappelons que la norme d'un opérateur linéaire borné est définie par $\|A\| = \sup_{\|x\|=1} \|Ax\|$.
1. Montrer l'inégalité de Cauchy-Schwarz généralisée pour les opérateurs : $\|T^* T\| \le \|T^*\| \|T\|$.
2. Démontrer, en utilisant le produit scalaire et l'inégalité de Cauchy-Schwarz vectorielle classique, que $\|T\|^2 \le \|T^* T\|$.
3. Montrer que $\|T^*\| = \|T\|$ et conclure sur l'égalité demandée.

## Correction
1. La norme d'un produit d'opérateurs continus est sous-multiplicative, car pour tout vecteur $x \in H$ de norme 1 :
$$ \|T^* T x\| \le \|T^*\| \cdot \|Tx\| \le \|T^*\| \cdot (\|T\| \cdot \|x\|) = \|T^*\| \|T\| $$
En prenant le supremum sur l'ensemble des vecteurs de la sphère unité, on obtient l'inégalité pour la norme d'opérateur :
$$ \|T^* T\| \le \|T^*\| \|T\| $$

2. Considérons le carré de la norme de l'opérateur $T$ :
$$ \|T\|^2 = \left( \sup_{\|x\|=1} \|Tx\| \right)^2 = \sup_{\|x\|=1} \|Tx\|^2 $$
Pour un vecteur arbitraire $x$ de norme 1, exprimons la norme au carré de l'image $Tx$ sous la forme d'un produit scalaire :
$$ \|Tx\|^2 = \langle Tx, Tx \rangle $$
Par définition de l'opérateur adjoint $T^*$, nous pouvons déplacer $T$ du premier argument du produit scalaire vers le second argument :
$$ \langle Tx, Tx \rangle = \langle x, T^*(Tx) \rangle = \langle x, (T^*T)x \rangle $$
Appliquons l'inégalité de Cauchy-Schwarz classique au produit scalaire des vecteurs $x$ et $(T^*T)x$ :
$$ \langle x, (T^*T)x \rangle \le \|x\| \cdot \|(T^*T)x\| $$
Puisque le vecteur $x$ a une norme égale à 1 par construction ($\|x\|=1$) :
$$ \le 1 \cdot \|(T^*T)x\| = \|(T^*T)x\| $$
Par définition de la norme d'opérateur subordonnée, nous avons l'inégalité fondamentale $\|Ay\| \le \|A\|\|y\|$. En l'appliquant avec l'opérateur $A = T^*T$ et le vecteur $y = x$ (toujours de norme 1) :
$$ \|(T^*T)x\| \le \|T^*T\| \cdot \|x\| = \|T^*T\| \cdot 1 = \|T^*T\| $$
En rassemblant cette chaîne d'inégalités pour un $x$ unitaire quelconque, nous avons établi rigoureusement que :
$$ \|Tx\|^2 \le \|T^*T\| $$
Comme cette borne supérieure ne dépend pas de $x$ (tant qu'il est sur la sphère unité), elle est valide pour le supremum lui-même. Par passage au supremum, on obtient :
$$ \sup_{\|x\|=1} \|Tx\|^2 \le \|T^*T\| \implies \|T\|^2 \le \|T^*T\| $$

3. Nous devons maintenant prouver que $\|T^*\| = \|T\|$.
En vertu de l'inégalité démontrée à l'étape 2 ( $\|T\|^2 \le \|T^*T\|$ ) combinée avec la sous-multiplicativité de l'étape 1 ( $\|T^*T\| \le \|T^*\|\|T\|$ ), nous formons la chaîne :
$$ \|T\|^2 \le \|T^*T\| \le \|T^*\| \|T\| $$
Si $T = 0$, la propriété $\|T^*\| = \|T\|$ est trivialement vraie.
Supposons donc que $T$ n'est pas l'opérateur nul, ce qui implique strictement que $\|T\| > 0$. On peut alors diviser l'inégalité totale par $\|T\|$ :
$$ \|T\| \le \|T^*\| $$
Comme l'opérateur adjoint est défini de manière parfaitement symétrique, cette inégalité mathématique est universellement valable pour n'importe quel opérateur linéaire continu, y compris pour l'opérateur $T^*$.
En remplaçant formellement $T$ par $T^*$ dans cette même inégalité générique, on obtient :
$$ \|T^*\| \le \|(T^*)^*\| $$
Or, par involution double, l'adjoint de l'adjoint est l'opérateur initial, c'est-à-dire $(T^*)^* = T$. L'inégalité devient donc :
$$ \|T^*\| \le \|T\| $$
Nous avons démontré simultanément que $\|T\| \le \|T^*\|$ et $\|T^*\| \le \|T\|$. La seule issue mathématique possible pour ces deux nombres réels est l'égalité stricte :
$$ \|T^*\| = \|T\| $$
Enfin, revenons à la chaîne d'inégalités du début de cette section :
$$ \|T\|^2 \le \|T^*T\| \le \|T^*\| \|T\| $$
Puisque nous venons de substituer $\|T^*\|$ par $\|T\|$, le terme le plus à droite devient exactement $\|T\| \cdot \|T\| = \|T\|^2$. La chaîne devient :
$$ \|T\|^2 \le \|T^*T\| \le \|T\|^2 $$
Pris en tenaille (théorème des gendarmes), le terme central n'a d'autre choix que d'être strictement égal aux limites encadrantes. L'égalité structurelle est formellement démontrée :
$$ \|T^*T\| = \|T\|^2 $$
""")

def gen_tps():
    os.makedirs("jalon-105/tp", exist_ok=True)

    # TP 1
    with open("jalon-105/tp/TP-01.md", "w") as f:
        f.write(r"""# TP 1 : Vérification matricielle de l'Adjoint en Python
## Objectif
L'objectif est d'implémenter une matrice aléatoire complexe, de calculer sa transconjuguée, et de vérifier expérimentalement que la propriété du produit scalaire hermitien tient avec une précision machine.

## Implémentation Python
\begin{lstlisting}
import numpy as np

def verify_adjoint_property(n_rows=50, n_cols=30):
    # Fixer la graine pour reproductibilite
    np.random.seed(42)

    # Creation d'un operateur T represente par une matrice complexe A
    A = np.random.randn(n_rows, n_cols) + 1j * np.random.randn(n_rows, n_cols)

    # L'adjoint matriciel (transconjuguee)
    A_star = A.conj().T

    # Generation de deux vecteurs aleatoires
    # x dans l'espace de depart (dim n_cols)
    x = np.random.randn(n_cols) + 1j * np.random.randn(n_cols)

    # y dans l'espace d'arrivee (dim n_rows)
    y = np.random.randn(n_rows) + 1j * np.random.randn(n_rows)

    # Calcul des images
    Ax = A @ x
    A_star_y = A_star @ y

    # Produit scalaire <Ax, y> (attention en numpy, dot(a,b) = a.T @ b)
    # Le produit scalaire mathematique est sum(v1 * conj(v2))
    inner_Ax_y = np.sum(Ax * np.conj(y))

    # Produit scalaire <x, A*y>
    inner_x_Astar_y = np.sum(x * np.conj(A_star_y))

    # Verification
    diff = np.abs(inner_Ax_y - inner_x_Astar_y)

    print("Produit scalaire <Ax, y> :", inner_Ax_y)
    print("Produit scalaire <x, A*y>:", inner_x_Astar_y)
    print("Difference absolue :", diff)

    assert diff < 1e-10, "Erreur : La propriete de l'adjoint n'est pas verifiee !"
    print("Succes : La propriete de l'adjoint est parfaitement verifiee aux erreurs d'arrondi pres.")

verify_adjoint_property()
\end{lstlisting}
""")

    # TP 2
    with open("jalon-105/tp/TP-02.md", "w") as f:
        f.write(r"""# TP 2 : Construction d'un Opérateur Différentiel et Anti-Symétrie
## Objectif
Représenter l'opérateur de dérivation par une matrice aux différences finies, et visualiser expérimentalement que la dérivation est un opérateur anti-symétrique ($D^* = -D$) dans des conditions de bords nulles.

## Implémentation Python
\begin{lstlisting}
import numpy as np

def test_derivative_adjoint():
    # Discretisation d'un domaine 1D
    N = 100
    dx = 1.0 / N

    # Operateur de derivation (differences centrees) pour representer T = d/dt
    # T f(t) = (f(t+dt) - f(t-dt)) / (2dt)
    D = np.zeros((N, N))
    for i in range(1, N-1):
        D[i, i+1] = 1.0 / (2 * dx)
        D[i, i-1] = -1.0 / (2 * dx)

    # L'adjoint matriciel de l'operateur reel est sa transposee
    D_star = D.T

    # Verification de la propriete anti-symetrique D* = -D
    anti_sym_error = np.max(np.abs(D_star - (-D)))

    print(f"Erreur d'anti-symetrie (max|D* + D|) : {anti_sym_error}")
    assert anti_sym_error < 1e-10, "L'operateur n'est pas anti-symetrique"

    # Testons sur des 'fonctions' aleatoires s'annulant au bord
    f = np.random.randn(N)
    g = np.random.randn(N)

    # Conditions de Dirichlet homogenes (nul aux bords)
    f[0] = f[-1] = 0
    g[0] = g[-1] = 0

    # Produit scalaire <Df, g> - l'integrale est approchee par la somme de Riemann avec dx
    inner_Df_g = np.sum((D @ f) * g) * dx

    # Produit scalaire <f, -Dg>
    inner_f_minusDg = np.sum(f * (-D @ g)) * dx

    diff = abs(inner_Df_g - inner_f_minusDg)
    print(f"Difference des produits scalaires empiriques : {diff}")

    assert diff < 1e-10, "Propriete d'integration par parties non verifiee"
    print("Integration par parties validee matriciellement !")

test_derivative_adjoint()
\end{lstlisting}
""")

    # TP 3
    with open("jalon-105/tp/TP-03.md", "w") as f:
        f.write(r"""# TP 3 : L'Opérateur d'Attention de Transformateur comme Adjoint
## Objectif
Dans l'architecture Transformer, le mécanisme d'attention met en jeu le produit $Q K^T$. Montrer expérimentalement que la transposée de la matrice des Keys $K$ est bien l'adjoint logique qui permet le calcul de similarité.

## Implémentation Python
\begin{lstlisting}
import numpy as np

def transformer_attention_adjoint():
    seq_len = 10
    d_model = 64

    # On simule la projection des donnees en Queries et Keys
    # Q : (seq_len, d_model), K : (seq_len, d_model)
    Q = np.random.randn(seq_len, d_model)
    K = np.random.randn(seq_len, d_model)

    # Le score d'attention non normalise est S = Q @ K.T
    # K.T est l'adjoint de K dans la base canonique
    Scores = Q @ K.T

    # Verifions que le score S_{i,j} est exactement le produit scalaire
    # de la i-eme query avec la j-eme key

    max_error = 0.0
    for i in range(seq_len):
        for j in range(seq_len):
            # Le produit scalaire manuel entre les deux vecteurs de taille d_model
            manual_dot = np.sum(Q[i, :] * K[j, :])

            # Comparaison avec la formulation matricielle utilisant l'adjoint
            error = abs(Scores[i, j] - manual_dot)
            if error > max_error:
                max_error = error

    print(f"Erreur maximale d'attention calculee : {max_error}")
    assert max_error < 1e-10, "Erreur dans le calcul d'attention"
    print("Le calcul par transposition matricielle evalue bien les similarites (produits scalaires) croisees.")

transformer_attention_adjoint()
\end{lstlisting}
""")

    # TP 4
    with open("jalon-105/tp/TP-04.md", "w") as f:
        f.write(r"""# TP 4 : Adjoint de l'Opérateur de Floutage (Convolution 1D)
## Objectif
Construire un opérateur de convolution 1D (un filtre de floutage) et calculer matriciellement son adjoint. On constatera expérimentalement qu'un floutage symétrique est un opérateur auto-adjoint.

## Implémentation Python
\begin{lstlisting}
import numpy as np

def construct_blur_operator(N):
    # Construit un operateur de moyenne glissante sur 3 pixels
    T = np.zeros((N, N))
    weights = [0.25, 0.5, 0.25]

    for i in range(N):
        # Gerer les bords avec periodicite (pour eviter les asymetries)
        T[i, (i-1)%N] = weights[0]
        T[i, i]       = weights[1]
        T[i, (i+1)%N] = weights[2]

    return T

def verify_auto_adjoint():
    N = 20
    T = construct_blur_operator(N)

    # Verifions que la matrice est symetrique : T = T.T
    T_star = T.T

    diff_matrix = np.max(np.abs(T - T_star))
    print(f"Difference max entre T et T* : {diff_matrix}")
    assert diff_matrix < 1e-12, "L'operateur de floutage n'est pas auto-adjoint !"

    # Verifions l'identite spectrale associee (valeurs propres reelles)
    eigenvalues = np.linalg.eigvals(T)
    imaginary_part = np.max(np.abs(np.imag(eigenvalues)))
    print(f"Partie imaginaire max des valeurs propres : {imaginary_part}")

    assert imaginary_part < 1e-12, "Les valeurs propres devraient etre reelles !"
    print("Le filtre symetrique periodique est un operateur auto-adjoint parfait.")

verify_auto_adjoint()
\end{lstlisting}
""")

    # TP 5
    with open("jalon-105/tp/TP-05.md", "w") as f:
        f.write(r"""# TP 5 : Égalité fondamentale des Normes C*
## Objectif
Vérifier par simulation de Monte Carlo l'identité structurelle majeure $\|T^* T\| = \|T\|^2$ sur une matrice aléatoire.

## Implémentation Python
\begin{lstlisting}
import numpy as np

def simulate_c_star_identity():
    n, m = 15, 20
    # On simule un operateur rectangulaire
    T = np.random.randn(n, m)

    # T*T est de taille (m, m)
    T_star = T.T
    T_star_T = T_star @ T

    # La norme d'operateur pour une matrice (L2-norm) est la plus grande
    # valeur singuliere. On peut l'obtenir avec np.linalg.norm(A, 2)
    norm_T = np.linalg.norm(T, 2)
    norm_T_squared = norm_T**2

    norm_Tstar_T = np.linalg.norm(T_star_T, 2)

    print(f"||T||^2   = {norm_T_squared}")
    print(f"||T* T|| = {norm_Tstar_T}")

    diff = abs(norm_T_squared - norm_Tstar_T)
    print(f"Difference absolue : {diff}")

    assert diff < 1e-10, "L'identite C* algebrique est en defaut !"
    print("L'identite C* ||T*T|| = ||T||^2 est valide empiriquement.")

    # Verification de ||T*|| = ||T||
    norm_Tstar = np.linalg.norm(T_star, 2)
    assert abs(norm_T - norm_Tstar) < 1e-10, "||T|| != ||T*||"
    print("L'identite ||T*|| = ||T|| est egalement validee.")

simulate_c_star_identity()
\end{lstlisting}
""")

if __name__ == "__main__":
    gen_exos()
    gen_tps()
