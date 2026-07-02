# Exercice 9 : Analyse de la Nilpotence et de l'Inversibilité dans les Algèbres de Matrices
**Difficulté :** ★★★★★

## Énoncé
Soit $\mathbb{K}$ un corps commutatif (par exemple $\mathbb{R}$ ou $\mathbb{C}$) et $n \in \mathbb{N}^*$ un entier strictement positif. On désigne par $\mathcal{M}_n(\mathbb{K})$ l'algèbre des matrices carrées de taille $n \times n$ à coefficients dans $\mathbb{K}$, et par $I_n$ la matrice identité de $\mathcal{M}_n(\mathbb{K})$.
Une matrice $N \in \mathcal{M}_n(\mathbb{K})$ est dite **nilpotente** s'il existe un entier $k \in \mathbb{N}^*$ tel que $N^k = 0_n$, où $0_n$ est la matrice nulle de $\mathcal{M}_n(\mathbb{K})$. Le plus petit entier $k$ pour lequel $N^k = 0_n$ est appelé l'**indice de nilpotence** de $N$.

1.  Soit $A \in \mathcal{M}_n(\mathbb{K})$ une matrice nilpotente d'indice $k$.
    Démontrer que la matrice $I_n - A$ est inversible et exprimer son inverse en fonction de $A$.

2.  Soient $A, B \in \mathcal{M}_n(\mathbb{K})$ deux matrices.
    a) On suppose que $A$ est nilpotente d'indice $k_A$ et que $B$ est nilpotente d'indice $k_B$. Si $A$ et $B$ commutent (c'est-à-dire $AB = BA$), démontrer que le produit $AB$ est une matrice nilpotente.
    b) On suppose que $A$ est nilpotente d'indice $k_A$ et que $B$ est nilpotente d'indice $k_B$. Si $A$ et $B$ commutent, démontrer que la somme $A+B$ est une matrice nilpotente.

## Correction Détaillée

1.  **Démonstration de l'inversibilité de $I_n - A$ et expression de son inverse.**

    Soit $A \in \mathcal{M}_n(\mathbb{K})$ une matrice nilpotente d'indice $k$. Par définition, cela signifie que $A^k = 0_n$. Si $k=1$, alors $A^1 = 0_n$, ce qui implique $A = 0_n$. Dans ce cas, $I_n - A = I_n - 0_n = I_n$, qui est trivialement inversible avec $I_n^{-1} = I_n$. La formule que nous allons dériver sera également valide pour ce cas particulier.

    Considérons la matrice $S$ définie comme la somme finie suivante :
    $$ S = \sum_{j=0}^{k-1} A^j = A^0 + A^1 + A^2 + \dots + A^{k-1} $$
    Puisque $A^0 = I_n$ par convention pour les matrices, nous avons :
    $$ S = I_n + A + A^2 + \dots + A^{k-1} $$
    Nous allons calculer le produit $(I_n - A)S$. Par la propriété de distributivité de la multiplication matricielle par rapport à l'addition, nous obtenons :
    $$ (I_n - A)S = I_n \left( \sum_{j=0}^{k-1} A^j \right) - A \left( \sum_{j=0}^{k-1} A^j \right) $$
    En développant les produits :
    $$ (I_n - A)S = \sum_{j=0}^{k-1} (I_n A^j) - \sum_{j=0}^{k-1} (A A^j) $$
    Puisque $I_n A^j = A^j$ (la matrice identité est l'élément neutre pour la multiplication) et $A A^j = A^{j+1}$ (par les règles d'exponentiation matricielle) pour tout $j \in \{0, \dots, k-1\}$ :
    $$ (I_n - A)S = \sum_{j=0}^{k-1} A^j - \sum_{j=0}^{k-1} A^{j+1} $$
    Écrivons explicitement les termes de chaque somme :
    $$ \sum_{j=0}^{k-1} A^j = A^0 + A^1 + A^2 + \dots + A^{k-1} $$
    $$ \sum_{j=0}^{k-1} A^{j+1} = A^{0+1} + A^{1+1} + A^{2+1} + \dots + A^{(k-1)+1} = A^1 + A^2 + A^3 + \dots + A^k $$
    Substituons ces développements dans l'expression de $(I_n - A)S$ :
    $$ (I_n - A)S = (A^0 + A^1 + A^2 + \dots + A^{k-1}) - (A^1 + A^2 + A^3 + \dots + A^k) $$
    Les termes $A^1, A^2, \dots, A^{k-1}$ apparaissent avec un signe positif dans la première parenthèse et un signe négatif dans la seconde, ils s'annulent donc mutuellement :
    $$ (I_n - A)S = A^0 - A^k $$
    Puisque $A^0 = I_n$ et, par hypothèse, $A$ est nilpotente d'indice $k$, ce qui signifie $A^k = 0_n$ :
    $$ (I_n - A)S = I_n - 0_n = I_n $$
    De manière analogue, nous pouvons calculer le produit $S(I_n - A)$ :
    $$ S(I_n - A) = \left( \sum_{j=0}^{k-1} A^j \right) (I_n - A) $$
    Par distributivité :
    $$ S(I_n - A) = \sum_{j=0}^{k-1} (A^j I_n) - \sum_{j=0}^{k-1} (A^j A) $$
    Puisque $A^j I_n = A^j$ et $A^j A = A^{j+1}$ :
    $$ S(I_n - A) = \sum_{j=0}^{k-1} A^j - \sum_{j=0}^{k-1} A^{j+1} $$
    Cette expression est identique à celle que nous avons obtenue pour $(I_n - A)S$. Par conséquent, le résultat est le même :
    $$ S(I_n - A) = I_n - A^k = I_n - 0_n = I_n $$
    Puisque nous avons trouvé une matrice $S$ telle que $(I_n - A)S = I_n$ et $S(I_n - A) = I_n$, la matrice $I_n - A$ est inversible et son inverse est $S$.
    Ainsi, l'inverse de $I_n - A$ est donné par :
    $$ (I_n - A)^{-1} = \sum_{j=0}^{k-1} A^j = I_n + A + A^2 + \dots + A^{k-1} $$

2.  **Propriétés de nilpotence pour le produit et la somme de matrices commutantes.**

    a) **Démonstration que $AB$ est nilpotente si $A$ et $B$ commutent.**

        Soient $A, B \in \mathcal{M}_n(\mathbb{K})$ deux matrices.
        On suppose que $A$ est nilpotente d'indice $k_A$, ce qui signifie $A^{k_A} = 0_n$.
        On suppose que $B$ est nilpotente d'indice $k_B$, ce qui signifie $B^{k_B} = 0_n$.
        On suppose également que $A$ et $B$ commutent, c'est-à-dire $AB = BA$.

        Nous voulons démontrer que le produit $AB$ est une matrice nilpotente. Pour cela, nous devons trouver un entier $m \in \mathbb{N}^*$ tel que $(AB)^m = 0_n$.

        Puisque $A$ et $B$ commutent, nous pouvons établir par récurrence que $(AB)^m = A^m B^m$ pour tout entier $m \ge 1$.
        *   **Cas de base ($m=1$):** $(AB)^1 = AB = A^1 B^1$. La propriété est vraie.
        *   **Hypothèse de récurrence:** Supposons que $(AB)^m = A^m B^m$ pour un certain entier $m \ge 1$.
        *   **Étape de récurrence:** Calculons $(AB)^{m+1}$ :
            $$ (AB)^{m+1} = (AB)^m (AB) $$
            En utilisant l'hypothèse de récurrence :
            $$ (AB)^{m+1} = (A^m B^m) (AB) $$
            Puisque $A$ et $B$ commutent, $A$ commute avec $B$, et par extension, $A$ commute avec toutes les puissances de $B$. En particulier, $A B^m = B^m A$. Nous pouvons donc réarranger les termes :
            $$ (AB)^{m+1} = A^m (B^m A) B $$
            $$ (AB)^{m+1} = A^m (A B^m) B $$
            $$ (AB)^{m+1} = (A^m A) (B^m B) $$
            $$ (AB)^{m+1} = A^{m+1} B^{m+1} $$
            La propriété est donc vraie pour $m+1$.
        Par le principe d'induction mathématique, $(AB)^m = A^m B^m$ pour tout $m \in \mathbb{N}^*$.

        Maintenant, considérons la puissance $k_A$-ième du produit $AB$ :
        $$ (AB)^{k_A} = A^{k_A} B^{k_A} $$
        Par hypothèse, $A$ est nilpotente d'indice $k_A$, ce qui signifie $A^{k_A} = 0_n$.
        $$ (AB)^{k_A} = 0_n B^{k_A} $$
        Le produit de la matrice nulle par n'importe quelle autre matrice de taille compatible est la matrice nulle :
        $$ (AB)^{k_A} = 0_n $$
        Puisque nous avons trouvé un entier $m = k_A$ (qui est un entier strictement positif car $k_A \ge 1$) tel que $(AB)^m = 0_n$, la matrice $AB$ est nilpotente. Son indice de nilpotence est au plus $k_A$. (On pourrait de même montrer qu'il est au plus $k_B$, donc il est au plus $\min(k_A, k_B)$).

    b) **Démonstration que $A+B$ est nilpotente si $A$ et $B$ commutent.**

        Soient $A, B \in \mathcal{M}_n(\mathbb{K})$ deux matrices.
        On suppose que $A$ est nilpotente d'indice $k_A$, ce qui signifie $A^{k_A} = 0_n$.
        On suppose que $B$ est nilpotente d'indice $k_B$, ce qui signifie $B^{k_B} = 0_n$.
        On suppose également que $A$ et $B$ commutent, c'est-à-dire $AB = BA$.

        Nous voulons démontrer que la somme $A+B$ est une matrice nilpotente. Pour cela, nous devons trouver un entier $m \in \mathbb{N}^*$ tel que $(A+B)^m = 0_n$.
        Puisque $A$ et $B$ commutent, nous pouvons appliquer la formule du binôme de Newton pour les matrices :
        $$ (A+B)^m = \sum_{j=0}^m \binom{m}{j} A^j B^{m-j} $$
        où $\binom{m}{j} = \frac{m!}{j!(m-j)!}$ est le coefficient binomial.

        Nous devons choisir un entier $m$ tel que chaque terme de cette somme soit la matrice nulle. Un terme générique est $\binom{m}{j} A^j B^{m-j}$. Pour que ce terme soit nul, il faut que $A^j = 0_n$ ou $B^{m-j} = 0_n$.
        Cela signifie que pour chaque $j \in \{0, \dots, m\}$, nous devons avoir $j \ge k_A$ ou $m-j \ge k_B$.

        Choisissons l'entier $m = k_A + k_B - 1$.
        Considérons un terme $\binom{m}{j} A^j B^{m-j}$ dans la somme pour ce $m$. Nous analysons deux cas possibles pour l'exposant $j$:

        *   **Cas 1 : $j \ge k_A$.**
            Dans ce cas, par la définition de l'indice de nilpotence de $A$, la matrice $A^j$ est la matrice nulle ($A^j = 0_n$).
            Par conséquent, le terme $\binom{m}{j} A^j B^{m-j}$ devient $\binom{m}{j} 0_n B^{m-j}$, qui est égal à $0_n$.

        *   **Cas 2 : $j < k_A$.**
            Puisque $j$ est un entier et $j < k_A$, cela implique que $j \le k_A - 1$.
            Dans ce cas, nous devons vérifier si $B^{m-j} = 0_n$. Pour cela, il faut que l'exposant $m-j$ soit supérieur ou égal à $k_B$.
            Calculons la valeur de $m-j$ :
            $$ m-j = (k_A + k_B - 1) - j $$
            Puisque $j \le k_A - 1$, nous pouvons écrire $-j \ge -(k_A - 1)$.
            En substituant cette inégalité dans l'expression de $m-j$ :
            $$ m-j \ge (k_A + k_B - 1) - (k_A - 1) $$
            $$ m-j \ge k_A + k_B - 1 - k_A + 1 $$
            $$ m-j \ge k_B $$
            Puisque $m-j \ge k_B$, par la définition de l'indice de nilpotence de $B$, la matrice $B^{m-j}$ est la matrice nulle ($B^{m-j} = 0_n$).
            Par conséquent, le terme $\binom{m}{j} A^j B^{m-j}$ devient $\binom{m}{j} A^j 0_n$, qui est égal à $0_n$.

        Dans les deux cas (soit $j \ge k_A$, soit $j < k_A$), chaque terme de la somme binomiale est la matrice nulle.
        Par conséquent, pour $m = k_A + k_B - 1$ :
        $$ (A+B)^{k_A+k_B-1} = \sum_{j=0}^{k_A+k_B-1} \binom{k_A+k_B-1}{j} A^j B^{k_A+k_B-1-j} = 0_n $$
        Puisque $k_A \ge 1$ et $k_B \ge 1$, $m = k_A + k_B - 1 \ge 1+1-1 = 1$. C'est donc un entier strictement positif.
        Nous avons trouvé un entier $m = k_A + k_B - 1$ tel que $(A+B)^m = 0_n$.
        Par conséquent, la matrice $A+B$ est nilpotente. Son indice de nilpotence est au plus $k_A + k_B - 1$.


**Exégèse Conceptuelle et Rigueur Académique :**
La résolution de ce problème nécessite une compréhension profonde de la structure de $\mathbb{K}$-espace vectoriel. Il ne suffit pas d'appliquer aveuglément les formules. Soit $E$ un espace vectoriel sur le corps commutatif $\mathbb{K}$. Considérons un endomorphisme $u \in \mathcal{L}(E)$. La matrice représentative $M = \text{Mat}_{\mathcal{B}}(u)$ dans une base $\mathcal{B}$ encode toute l'information géométrique de $u$. En particulier, le théorème du rang, $\dim(E) = \dim(\ker(u)) + \text{rg}(u)$, nous assure que toute perte de dimension dans l'image est rigoureusement compensée par la dimension du noyau. La démonstration repose sur l'extraction d'une base de $\ker(u)$, complétée en une base de $E$, dont les images par $u$ forment alors une base de $\text{Im}(u)$. Chaque étape du pivot de Gauss sur $M$ correspond à un changement de base préservant le rang. Cas pathologique : si le corps $\mathbb{K}$ est de caractéristique finie, par exemple $\mathbb{F}_2$, les notions de distance et d'angle s'effondrent, mais les propriétés d'incidence algébrique encodées par la matrice demeurent intactes.
