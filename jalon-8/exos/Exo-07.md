# Exercice 7 : Endomorphismes idempotents et stabilité (Difficulté : ****)

Soit $\mathbb{K}$ un corps commutatif.
Soit $E$ un espace vectoriel de dimension finie $n \geq 1$ sur $\mathbb{K}$.
Soit $u \in \mathcal{L}(E)$ un endomorphisme de $E$ tel que $u \circ u = u$, c'est-à-dire $u^2 = u$. Un tel endomorphisme est appelé un projecteur ou un endomorphisme idempotent.

1.  Démontrer que $E = \text{Ker}(u) \oplus \text{Im}(u)$.
    *(Indication : Considérer l'expression $x = (x - u(x)) + u(x)$ pour tout $x \in E$.)*
2.  Démontrer que $\text{Im}(u) = \{ y \in E \mid u(y) = y \}$.
    *(Autrement dit, $\text{Im}(u) = \text{Ker}(u - \text{Id}_E)$.)*
3.  Soit $v \in \mathcal{L}(E)$ un autre endomorphisme de $E$. On suppose que $u$ et $v$ commutent, c'est-à-dire $u \circ v = v \circ u$.
    Démontrer que $\text{Ker}(u)$ est stable par $v$, et que $\text{Im}(u)$ est stable par $v$.
    *(Un sous-espace $F$ de $E$ est stable par $v$ si $v(F) \subset F$.)*
4.  En déduire que si $u$ et $v$ commutent, alors la restriction de $v$ à $\text{Im}(u)$, notée $v|_{\text{Im}(u)}$, est un endomorphisme de $\text{Im}(u)$, et la restriction de $v$ à $\text{Ker}(u)$, notée $v|_{\text{Ker}(u)}$, est un endomorphisme de $\text{Ker}(u)$.

## Correction détaillée

1.  **Démontrer que $E = \text{Ker}(u) \oplus \text{Im}(u)$.**

    Pour établir qu'un espace vectoriel $E$ est la somme directe de deux sous-espaces vectoriels $F_1$ et $F_2$, il faut montrer que $F_1 \cap F_2 = \{0_E\}$ (l'intersection est réduite au vecteur nul) et que $E = F_1 + F_2$ (la somme est génératrice).

    a) **Montrons que $\text{Ker}(u) \cap \text{Im}(u) = \{0_E\}$.**
    Soit $y$ un vecteur appartenant à l'intersection $\text{Ker}(u) \cap \text{Im}(u)$.
    Puisque $y \in \text{Ker}(u)$, la définition du noyau implique que $u(y) = 0_E$.
    Puisque $y \in \text{Im}(u)$, la définition de l'image implique qu'il existe un vecteur $x \in E$ tel que $y = u(x)$.
    Appliquons l'endomorphisme $u$ à l'égalité $y = u(x)$ :
    $u(y) = u(u(x)) = u^2(x)$.
    Par hypothèse, nous savons que $u^2 = u$. Donc $u^2(x) = u(x)$.
    Ainsi, nous avons $u(y) = u(x)$.
    En substituant $u(x)$ par $y$, nous obtenons $u(y) = y$.
    Nous avons donc deux expressions pour $u(y)$ : $u(y) = 0_E$ (car $y \in \text{Ker}(u)$) et $u(y) = y$.
    En égalisant ces deux expressions, nous obtenons $y = 0_E$.
    Par conséquent, le seul vecteur commun à $\text{Ker}(u)$ et $\text{Im}(u)$ est le vecteur nul, ce qui prouve que $\text{Ker}(u) \cap \text{Im}(u) = \{0_E\}$.

    b) **Montrons que $E = \text{Ker}(u) + \text{Im}(u)$.**
    Soit $x$ un vecteur quelconque de $E$. Nous voulons montrer qu'il peut s'écrire comme la somme d'un vecteur de $\text{Ker}(u)$ et d'un vecteur de $\text{Im}(u)$.
    Considérons la décomposition suggérée : $x = (x - u(x)) + u(x)$.
    Analysons le premier terme, $x - u(x)$ :
    Appliquons $u$ à ce terme : $u(x - u(x)) = u(x) - u(u(x))$.
    Ceci peut s s'écrire $u(x) - u^2(x)$.
    Puisque $u^2 = u$ par hypothèse, nous avons $u^2(x) = u(x)$.
    Donc, $u(x - u(x)) = u(x) - u(x) = 0_E$.
    Par définition du noyau, cela signifie que le vecteur $x - u(x)$ appartient à $\text{Ker}(u)$.
    Analysons le second terme, $u(x)$ :
    Par définition même de l'image d'un endomorphisme, tout vecteur de la forme $u(z)$ pour un certain $z \in E$ appartient à $\text{Im}(u)$. Ici, $u(x)$ appartient clairement à $\text{Im}(u)$.
    Ainsi, tout vecteur $x \in E$ peut s'écrire comme la somme d'un vecteur de $\text{Ker}(u)$ (à savoir $x - u(x)$) et d'un vecteur de $\text{Im}(u)$ (à savoir $u(x)$).
    Ceci prouve que $E = \text{Ker}(u) + \text{Im}(u)$.

    En combinant les résultats de a) et b), nous concluons que $E = \text{Ker}(u) \oplus \text{Im}(u)$.

2.  **Démontrer que $\text{Im}(u) = \{ y \in E \mid u(y) = y \}$.**

    Notons $F = \{ y \in E \mid u(y) = y \}$. Nous devons montrer l'égalité des ensembles $\text{Im}(u)$ et $F$. Pour cela, nous démontrons la double inclusion.

    a) **Montrons que $\text{Im}(u) \subset F$.**
    Soit $y \in \text{Im}(u)$. Par définition, il existe un vecteur $x \in E$ tel que $y = u(x)$.
    Appliquons $u$ au vecteur $y$ : $u(y) = u(u(x)) = u^2(x)$.
    Puisque $u^2 = u$ par hypothèse, nous avons $u^2(x) = u(x)$.
    En substituant, $u(y) = u(x)$.
    Comme $y = u(x)$, on obtient $u(y) = y$.
    Par conséquent, $y$ satisfait la condition $u(y) = y$, ce qui signifie $y \in F$.
    Donc, tout élément de $\text{Im}(u)$ est un élément de $F$, d'où $\text{Im}(u) \subset F$.

    b) **Montrons que $F \subset \text{Im}(u)$.**
    Soit $y \in F$. Par définition de $F$, nous avons $u(y) = y$.
    L'expression $y = u(y)$ montre que $y$ est l'image d'un certain vecteur par $u$ (en l'occurrence, $y$ est l'image de lui-même par $u$).
    Par définition de l'image, tout vecteur de la forme $u(z)$ est dans $\text{Im}(u)$.
    Donc, $y \in \text{Im}(u)$.
    Ainsi, tout élément de $F$ est un élément de $\text{Im}(u)$, d'où $F \subset \text{Im}(u)$.

    Des inclusions a) et b), nous concluons que $\text{Im}(u) = \{ y \in E \mid u(y) = y \}$.
    Cette condition $u(y) = y$ est équivalente à $u(y) - y = 0_E$, ce qui peut s'écrire $(u - \text{Id}_E)(y) = 0_E$. C'est précisément la définition du noyau de l'endomorphisme $(u - \text{Id}_E)$, donc $\text{Im}(u) = \text{Ker}(u - \text{Id}_E)$.

3.  **Soit $v \in \mathcal{L}(E)$ tel que $u \circ v = v \circ u$. Démontrer que $\text{Ker}(u)$ est stable par $v$, et que $\text{Im}(u)$ est stable par $v$.**

    a) **Stabilité de $\text{Ker}(u)$ par $v$.**
    Un sous-espace $F$ est stable par $v$ si pour tout $x \in F$, $v(x) \in F$.
    Soit $x \in \text{Ker}(u)$. Par définition, $u(x) = 0_E$.
    Nous voulons montrer que $v(x) \in \text{Ker}(u)$, c'est-à-dire que $u(v(x)) = 0_E$.
    Calculons $u(v(x))$. Puisque $u$ et $v$ commutent (c'est-à-dire $u \circ v = v \circ u$), nous avons :
    $u(v(x)) = (u \circ v)(x) = (v \circ u)(x) = v(u(x))$.
    Comme $x \in \text{Ker}(u)$, nous savons que $u(x) = 0_E$.
    Donc, $u(v(x)) = v(0_E)$.
    Puisque $v$ est un endomorphisme linéaire, il transforme le vecteur nul en le vecteur nul : $v(0_E) = 0_E$.
    Ainsi, $u(v(x)) = 0_E$.
    Cela signifie que $v(x)$ appartient à $\text{Ker}(u)$.
    Par conséquent, $\text{Ker}(u)$ est stable par $v$.

    b) **Stabilité de $\text{Im}(u)$ par $v$.**
    Un sous-espace $F$ est stable par $v$ si pour tout $y \in F$, $v(y) \in F$.
    Soit $y \in \text{Im}(u)$. Par définition, il existe un vecteur $x \in E$ tel que $y = u(x)$.
    Nous voulons montrer que $v(y) \in \text{Im}(u)$.
    Calculons $v(y)$ : $v(y) = v(u(x))$.
    Puisque $u$ et $v$ commutent ($v \circ u = u \circ v$), nous pouvons écrire :
    $v(u(x)) = (v \circ u)(x) = (u \circ v)(x) = u(v(x))$.
    Donc, $v(y) = u(v(x))$.
    Par définition, tout vecteur qui est l'image d'un autre vecteur (ici $v(x)$) par $u$ appartient à $\text{Im}(u)$.
    Ainsi, $v(y) \in \text{Im}(u)$.
    Par conséquent, $\text{Im}(u)$ est stable par $v$.

4.  **En déduire que si $u$ et $v$ commutent, alors la restriction de $v$ à $\text{Im}(u)$, notée $v|_{\text{Im}(u)}$, est un endomorphisme de $\text{Im}(u)$, et la restriction de $v$ à $\text{Ker}(u)$, notée $v|_{\text{Ker}(u)}$, est un endomorphisme de $\text{Ker}(u)$.**

    Par définition, une application linéaire $w: F \to E'$ est un endomorphisme de $F$ si $E'=F$. C'est-à-dire que $w$ doit être une application linéaire de $F$ dans $F$. Pour qu'une restriction $v|_F : F \to E$ devienne un endomorphisme de $F$, il est nécessaire et suffisant que $F$ soit stable par $v$ (car la linéarité de $v$ implique la linéarité de sa restriction).

    a) **Pour $F = \text{Ker}(u)$ :**
    D'après la question 3a), si $u$ et $v$ commutent, alors $\text{Ker}(u)$ est stable par $v$.
    Cela signifie que pour tout $x \in \text{Ker}(u)$, $v(x) \in \text{Ker}(u)$.
    Nous pouvons donc définir une application $v|_{\text{Ker}(u)} : \text{Ker}(u) \to \text{Ker}(u)$ qui associe à $x \in \text{Ker}(u)$ le vecteur $v(x)$.
    Puisque $v$ est un endomorphisme linéaire de $E$, sa restriction à un sous-espace, $v|_{\text{Ker}(u)}$, est également linéaire.
    Par conséquent, $v|_{\text{Ker}(u)}$ est un endomorphisme de $\text{Ker}(u)$.

    b) **Pour $F = \text{Im}(u)$ :**
    D'après la question 3b), si $u$ et $v$ commutent, alors $\text{Im}(u)$ est stable par $v$.
    Cela signifie que pour tout $y \in \text{Im}(u)$, $v(y) \in \text{Im}(u)$.
    Nous pouvons donc définir une application $v|_{\text{Im}(u)} : \text{Im}(u) \to \text{Im}(u)$ qui associe à $y \in \text{Im}(u)$ le vecteur $v(y)$.
    Puisque $v$ est un endomorphisme linéaire de $E$, sa restriction à un sous-espace, $v|_{\text{Im}(u)}$, est également linéaire.
    Par conséquent, $v|_{\text{Im}(u)}$ est un endomorphisme de $\text{Im}(u)$.
