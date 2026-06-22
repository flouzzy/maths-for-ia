# Exercice 10 : Décomposition de Fitting et Projecteurs Associés pour une Matrice Annulée par un Polynôme Non-Simple
**Difficulté :** ★★★★★

## Énoncé
Soit $n \in \mathbb{N}^*$ un entier et $A \in \mathcal{M}_n(\mathbb{C})$ une matrice carrée complexe.
On suppose que $A$ satisfait la relation polynomiale $A^3 - 2A^2 + A = 0$.

1.  **Analyse du Polynôme Annulateur et du Spectre :**
    a.  Soit $P(x) = x^3 - 2x^2 + x$. Factoriser $P(x)$ sur $\mathbb{C}$.
    b.  Quelles sont les valeurs propres possibles de $A$? Justifier rigoureusement.
    c.  Énumérer toutes les formes possibles du polynôme minimal $\mu_A(x)$ de $A$. Pour chaque cas, donner un exemple de matrice $A \in \mathcal{M}_2(\mathbb{C})$ ou $\mathcal{M}_3(\mathbb{C})$ satisfaisant la condition.

2.  **Décomposition de l'Espace Vectoriel :**
    a.  Démontrer que $\mathbb{C}^n = \text{Ker}(A) \oplus \text{Ker}((A-I_n)^2)$.
        (Indication : On pourra utiliser le théorème de décomposition des noyaux).
    b.  On note $E_0 = \text{Ker}(A)$ et $E_1 = \text{Ker}((A-I_n)^2)$. Soit $P_0$ le projecteur sur $E_0$ parallèlement à $E_1$, et $P_1$ le projecteur sur $E_1$ parallèlement à $E_0$. Exprimer $P_0$ et $P_1$ comme des polynômes en $A$.

3.  **Propriétés des Matrices Commutantes :**
    Soit $B \in \mathcal{M}_n(\mathbb{C})$ une matrice qui commute avec $A$, c'est-à-dire $AB = BA$.
    a.  Démontrer que les sous-espaces $E_0$ et $E_1$ sont stables par $B$.
    b.  Démontrer que $B$ est inversible si et seulement si les restrictions $B|_{E_0} : E_0 \to E_0$ et $B|_{E_1} : E_1 \to E_1$ sont toutes deux inversibles.

## Correction Détaillée

### 1. Analyse du Polynôme Annulateur et du Spectre

a.  **Factorisation de $P(x)$ :**
    Le polynôme donné est $P(x) = x^3 - 2x^2 + x$.
    Nous pouvons factoriser $x$ :
    $P(x) = x(x^2 - 2x + 1)$.
    Le terme entre parenthèses est une identité remarquable : $(x-1)^2$.
    Donc, la factorisation de $P(x)$ sur $\mathbb{C}$ est $P(x) = x(x-1)^2$.

b.  **Valeurs propres possibles de $A$ :**
    Puisque $P(A) = A^3 - 2A^2 + A = 0$, le polynôme $P(x)$ est un polynôme annulateur pour la matrice $A$.
    Soit $\lambda \in \mathbb{C}$ une valeur propre de $A$. Par définition, il existe un vecteur non nul $v \in \mathbb{C}^n$ tel que $Av = \lambda v$.
    En appliquant le polynôme $P$ à $A$ et en l'évaluant sur $v$ :
    $P(A)v = (A^3 - 2A^2 + A)v = 0 \cdot v = 0$.
    D'autre part, en utilisant $Av = \lambda v$, $A^2v = A(Av) = A(\lambda v) = \lambda (Av) = \lambda (\lambda v) = \lambda^2 v$, et de même $A^3v = \lambda^3 v$.
    Donc, $P(A)v = (\lambda^3 - 2\lambda^2 + \lambda)v = P(\lambda)v$.
    Puisque $P(A)v = 0$ et $v \neq 0$, il s'ensuit que $P(\lambda) = 0$.
    Les racines de $P(x) = x(x-1)^2$ sont $x=0$ et $x=1$.
    Par conséquent, les valeurs propres possibles de $A$ sont $0$ et $1$.

c.  **Formes possibles du polynôme minimal $\mu_A(x)$ :**
    Le polynôme minimal $\mu_A(x)$ de $A$ est le polynôme unitaire de plus petit degré qui annule $A$. Il divise tout polynôme annulateur de $A$. En particulier, $\mu_A(x)$ doit diviser $P(x) = x(x-1)^2$.
    De plus, les racines du polynôme minimal sont exactement les valeurs propres de $A$. D'après la question précédente, les valeurs propres de $A$ ne peuvent être que $0$ et $1$.
    Les diviseurs unitaires de $P(x)$ dont les racines sont parmi $\{0, 1\}$ sont :
    *   $\mu_A(x) = x$: Dans ce cas, $A=0$.
        Exemple pour $n=2$: $A = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$. $A^3 - 2A^2 + A = 0 - 0 + 0 = 0$.
    *   $\mu_A(x) = x-1$: Dans ce cas, $A-I_n=0$, donc $A=I_n$.
        Exemple pour $n=2$: $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$. $A^3 - 2A^2 + A = I_2 - 2I_2 + I_2 = 0$.
    *   $\mu_A(x) = x(x-1)$: Dans ce cas, $A^2-A=0$, donc $A^2=A$. $A$ est une matrice de projection.
        Exemple pour $n=2$: $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. $A^2 = A$, donc $A^3 - 2A^2 + A = A - 2A + A = 0$.
    *   $\mu_A(x) = (x-1)^2$: Dans ce cas, $(A-I_n)^2=0$. La seule valeur propre est $1$. $A-I_n$ est nilpotente d'indice 2.
        Exemple pour $n=2$: $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. $(A-I_2) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. $(A-I_2)^2 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.
        $A^3 - 2A^2 + A = A(A-I_2)^2 + A^2 - A = A \cdot 0 + A^2 - A = A^2 - A$.
        $A^2 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
        $A^2 - A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} - \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \neq 0$.
        Ah, mon calcul pour $A^3 - 2A^2 + A$ est incorrect.
        Si $\mu_A(x) = (x-1)^2$, alors $A^2 - 2A + I_n = 0$.
        Alors $A^3 - 2A^2 + A = A(A^2 - 2A + I_n) = A \cdot 0 = 0$. C'est correct.
        L'exemple $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ est valide.
    *   $\mu_A(x) = x(x-1)^2$: C'est le cas général où $P(x)$ est le polynôme minimal lui-même. Les valeurs propres sont $0$ et $1$, et la valeur propre $1$ a un bloc de Jordan de taille 2.
        Exemple pour $n=3$: $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$.
        $A-I_3 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix}$.
        $(A-I_3)^2 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
        $A(A-I_3)^2 = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$.
        Ainsi $A$ annule $x(x-1)^2$.
        Le polynôme minimal ne peut pas être $x$ car $A \neq 0$.
        Le polynôme minimal ne peut pas être $x-1$ car $A \neq I_3$.
        Le polynôme minimal ne peut pas être $x(x-1)$ car $A^2-A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} - \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \neq 0$.
        Le polynôme minimal ne peut pas être $(x-1)^2$ car $(A-I_3)^2 \neq 0$.
        Donc, le polynôme minimal de cet exemple est bien $x(x-1)^2$.

### 2. Décomposition de l'Espace Vectoriel

a.  **Démonstration de $\mathbb{C}^n = \text{Ker}(A) \oplus \text{Ker}((A-I_n)^2)$ :**
    Nous avons montré que $P(A) = 0$, où $P(x) = x(x-1)^2$.
    Soient $P_1(x) = x$ et $P_2(x) = (x-1)^2$.
    Ces deux polynômes $P_1(x)$ et $P_2(x)$ sont premiers entre eux, car leurs racines respectives sont $0$ et $1$, qui sont distinctes.
    Le théorème de décomposition des noyaux (ou lemme des noyaux) stipule que si $P(x) = P_1(x)P_2(x)$ avec $P_1(x)$ et $P_2(x)$ premiers entre eux, alors $\text{Ker}(P(A)) = \text{Ker}(P_1(A)) \oplus \text{Ker}(P_2(A))$.
    Dans notre cas :
    *   $\text{Ker}(P(A)) = \text{Ker}(0) = \mathbb{C}^n$ (puisque $P(A)=0$).
    *   $\text{Ker}(P_1(A)) = \text{Ker}(A)$.
    *   $\text{Ker}(P_2(A)) = \text{Ker}((A-I_n)^2)$.
    Par conséquent, nous avons bien $\mathbb{C}^n = \text{Ker}(A) \oplus \text{Ker}((A-I_n)^2)$.

b.  **Expression des projecteurs $P_0$ et $P_1$ comme polynômes en $A$ :**
    Nous cherchons $P_0$ le projecteur sur $E_0 = \text{Ker}(A)$ parallèlement à $E_1 = \text{Ker}((A-I_n)^2)$.
    Cela signifie que pour tout $v \in \mathbb{C}^n$, si $v = v_0 + v_1$ avec $v_0 \in E_0$ et $v_1 \in E_1$, alors $P_0 v = v_0$.
    Les propriétés de $P_0(A)$ sont donc :
    1.  Pour $v \in E_0$, $P_0(A)v = v$.
    2.  Pour $v \in E_1$, $P_0(A)v = 0$.
    Nous cherchons un polynôme $Q_0(x)$ tel que $P_0 = Q_0(A)$.
    Les conditions sur $Q_0(x)$ sont :
    *   $Q_0(x) \equiv 1 \pmod{x}$ (pour $v \in \text{Ker}(A)$). Cela implique $Q_0(0) = 1$.
    *   $Q_0(x) \equiv 0 \pmod{(x-1)^2}$ (pour $v \in \text{Ker}((A-I_n)^2)$). Cela implique $Q_0(1) = 0$ et $Q_0'(1) = 0$ (en raison de la multiplicité de la racine $1$).

    Cherchons un polynôme $Q_0(x)$ de degré minimal satisfaisant ces conditions. Un polynôme de degré 2 est suffisant. Soit $Q_0(x) = ax^2 + bx + c$.
    1.  $Q_0(0) = 1 \implies a(0)^2 + b(0) + c = 1 \implies c = 1$.
    2.  $Q_0(1) = 0 \implies a(1)^2 + b(1) + c = 0 \implies a + b + c = 0$.
        En substituant $c=1$, nous obtenons $a+b+1=0 \implies a+b=-1$.
    3.  $Q_0'(x) = 2ax + b$.
        $Q_0'(1) = 0 \implies 2a(1) + b = 0 \implies 2a+b=0$.
        De $2a+b=0$, nous avons $b=-2a$.
        Substituons $b=-2a$ dans $a+b=-1$:
        $a + (-2a) = -1 \implies -a = -1 \implies a=1$.
        Alors $b = -2(1) = -2$.
    Donc, le polynôme est $Q_0(x) = x^2 - 2x + 1 = (x-1)^2$.
    Ainsi, $P_0 = (A-I_n)^2 = A^2 - 2A + I_n$.

    Vérifions :
    *   Si $v \in E_0 = \text{Ker}(A)$, alors $Av=0$.
        $P_0 v = (A^2 - 2A + I_n)v = A^2v - 2Av + I_nv = A(Av) - 2(Av) + v = A(0) - 2(0) + v = 0 - 0 + v = v$. La condition est satisfaite.
    *   Si $v \in E_1 = \text{Ker}((A-I_n)^2)$, alors $(A-I_n)^2v=0$.
        $P_0 v = (A-I_n)^2v = 0$. La condition est satisfaite.

    Pour le projecteur $P_1$ sur $E_1$ parallèlement à $E_0$, nous savons que $P_1 = I_n - P_0$.
    $P_1 = I_n - (A^2 - 2A + I_n) = I_n - A^2 + 2A - I_n = 2A - A^2$.

    Vérifions :
    *   Si $v \in E_1 = \text{Ker}((A-I_n)^2)$, alors $(A-I_n)^2v=0$.
        Cela signifie $A^2v - 2Av + v = 0$, d'où $v = 2Av - A^2v$.
        $P_1 v = (2A - A^2)v = 2Av - A^2v = v$. La condition est satisfaite.
    *   Si $v \in E_0 = \text{Ker}(A)$, alors $Av=0$.
        $P_1 v = (2A - A^2)v = 2Av - A^2v = 2(0) - A(0) = 0 - 0 = 0$. La condition est satisfaite.

    Les expressions des projecteurs sont donc $P_0 = (A-I_n)^2$ et $P_1 = 2A - A^2$.

### 3. Propriétés des Matrices Commutantes

a.  **Stabilité des sous-espaces $E_0$ et $E_1$ par $B$ :**
    Nous avons $E_0 = \text{Ker}(A)$ et $E_1 = \text{Ker}((A-I_n)^2)$. On suppose $AB=BA$.

    *   **Stabilité de $E_0$ :**
        Soit $v \in E_0$. Par définition, $Av = 0$.
        Nous voulons montrer que $Bv \in E_0$, c'est-à-dire $A(Bv) = 0$.
        Puisque $AB=BA$, nous avons $A(Bv) = (AB)v = (BA)v = B(Av)$.
        Comme $v \in E_0$, $Av=0$.
        Donc, $A(Bv) = B(0) = 0$.
        Par conséquent, $Bv \in E_0$. Le sous-espace $E_0$ est stable par $B$.

    *   **Stabilité de $E_1$ :**
        Soit $v \in E_1$. Par définition, $(A-I_n)^2v = 0$.
        Nous voulons montrer que $Bv \in E_1$, c'est-à-dire $(A-I_n)^2(Bv) = 0$.
        Puisque $AB=BA$, $B$ commute avec $A$. Il s'ensuit que $B$ commute également avec $A-I_n$.
        En effet, $B(A-I_n) = BA - BI_n = AB - I_nB = (A-I_n)B$.
        Puisque $B$ commute avec $A-I_n$, il commute aussi avec toute puissance de $A-I_n$. En particulier, $B(A-I_n)^2 = (A-I_n)^2B$.
        Donc, $(A-I_n)^2(Bv) = B(A-I_n)^2v$.
        Comme $v \in E_1$, $(A-I_n)^2v = 0$.
        Par conséquent, $(A-I_n)^2(Bv) = B(0) = 0$.
        Ainsi, $Bv \in E_1$. Le sous-espace $E_1$ est stable par $B$.

b.  **Critère d'inversibilité de $B$ :**
    Nous voulons démontrer que $B$ est inversible si et seulement si les restrictions $B|_{E_0}$ et $B|_{E_1}$ sont inversibles.

    *   **Sens direct ($\implies$) : Si $B$ est inversible, alors $B|_{E_0}$ et $B|_{E_1}$ sont inversibles.**
        Supposons que $B$ est inversible.
        Considérons la restriction $B|_{E_0} : E_0 \to E_0$.
        Soit $v_0 \in E_0$ tel que $B|_{E_0}(v_0) = 0$. Cela signifie $Bv_0 = 0$.
        Puisque $B$ est inversible, sa seule image nulle est le vecteur nul. Donc $v_0 = 0$.
        Ceci prouve que $B|_{E_0}$ est injective.
        Comme $E_0$ est un espace vectoriel de dimension finie, une application linéaire injective de $E_0$ dans lui-même est nécessairement bijective (inversible).
        Donc, $B|_{E_0}$ est inversible.
        Le même raisonnement s'applique à $B|_{E_1}$. Si $v_1 \in E_1$ et $B|_{E_1}(v_1) = 0$, alors $Bv_1 = 0$. Puisque $B$ est inversible, $v_1=0$. Donc $B|_{E_1}$ est injective et par suite inversible.

    *   **Sens réciproque ($\impliedby$) : Si $B|_{E_0}$ et $B|_{E_1}$ sont inversibles, alors $B$ est inversible.**
        Supposons que $B|_{E_0}$ et $B|_{E_1}$ sont inversibles.
        Pour montrer que $B$ est inversible, il suffit de montrer que $B$ est injective (puisque $B$ est un endomorphisme d'un espace de dimension finie $\mathbb{C}^n$).
        Soit $v \in \mathbb{C}^n$ tel que $Bv = 0$.
        D'après la question 2.a, nous savons que $\mathbb{C}^n = E_0 \oplus E_1$.
        Ainsi, tout vecteur $v \in \mathbb{C}^n$ peut être écrit de manière unique comme $v = v_0 + v_1$, où $v_0 \in E_0$ et $v_1 \in E_1$.
        Puisque $E_0$ et $E_1$ sont stables par $B$ (d'après la question 3.a), nous avons $Bv_0 \in E_0$ et $Bv_1 \in E_1$.
        L'équation $Bv = 0$ devient $B(v_0 + v_1) = 0$, ce qui implique $Bv_0 + Bv_1 = 0$.
        Puisque $Bv_0 \in E_0$ et $Bv_1 \in E_1$, et que la somme $E_0 \oplus E_1$ est directe (c'est-à-dire $E_0 \cap E_1 = \{0\}$), l'égalité $Bv_0 + Bv_1 = 0$ implique nécessairement que $Bv_0 = 0$ et $Bv_1 = 0$.
        Or, nous avons supposé que $B|_{E_0}$ est inversible. Puisque $Bv_0 = 0$ et $v_0 \in E_0$, cela implique $v_0 = 0$.
        De même, nous avons supposé que $B|_{E_1}$ est inversible. Puisque $Bv_1 = 0$ et $v_1 \in E_1$, cela implique $v_1 = 0$.
        Puisque $v_0 = 0$ et $v_1 = 0$, il s'ensuit que $v = v_0 + v_1 = 0 + 0 = 0$.
        Nous avons montré que si $Bv=0$, alors $v=0$. Donc $B$ est injective.
        Par conséquent, $B$ est inversible.
