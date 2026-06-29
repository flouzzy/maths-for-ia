---

# Exercice 6 : Structure Quotiente de l'Anneau des Polynômes par Évaluation
**Difficulté :** ⭐⭐⭐

## Énoncé

Soit $E = \mathbb{R}[X]$ l'ensemble des polynômes à coefficients réels.
Nous définissons une relation $\mathcal{R}$ sur $E$ de la manière suivante :
Pour tout $P, Q \in E$, $P \mathcal{R} Q$ si et seulement si $P(0) = Q(0)$ et $P(1) = Q(1)$.

1.  Démontrer que $\mathcal{R}$ est une relation d'équivalence sur $E$.
2.  Caractériser l'ensemble quotient $E/\mathcal{R}$ en décrivant explicitement la classe d'équivalence $[P]$ d'un polynôme $P \in E$.
3.  On définit sur $E/\mathcal{R}$ une addition et une multiplication par :
    $$[P] + [Q] = [P+Q]$$
    $$[P] \cdot [Q] = [P \cdot Q]$$
    Démontrer que ces deux opérations sont bien définies.
4.  Montrer que $(E/\mathcal{R}, +, \cdot)$ est un anneau commutatif unitaire.
5.  L'anneau $(E/\mathcal{R}, +, \cdot)$ est-il intègre ? Justifier votre réponse.
6.  Établir un isomorphisme d'anneaux entre $(E/\mathcal{R}, +, \cdot)$ et un anneau connu.

## Correction Détaillée

### Question 1 : Démontrer que $\mathcal{R}$ est une relation d'équivalence sur $E$.

Pour démontrer que $\mathcal{R}$ est une relation d'équivalence, nous devons prouver qu'elle est réflexive, symétrique et transitive.

#### Réflexivité
Soit $P$ un polynôme arbitraire dans $E = \mathbb{R}[X]$.
Nous devons montrer que $P \mathcal{R} P$.
Selon la définition de $\mathcal{R}$, $P \mathcal{R} P$ si et seulement si $P(0) = P(0)$ et $P(1) = P(1)$.
L'égalité $P(0) = P(0)$ est une propriété fondamentale de l'égalité (chaque élément est égal à lui-même).
De même, l'égalité $P(1) = P(1)$ est également une propriété fondamentale de l'égalité.
Puisque ces deux conditions sont toujours vérifiées, nous concluons que $P \mathcal{R} P$.
Par conséquent, la relation $\mathcal{R}$ est réflexive.

#### Symétrie
Soient $P$ et $Q$ deux polynômes arbitraires dans $E = \mathbb{R}[X]$.
Supposons que $P \mathcal{R} Q$.
Selon la définition de $\mathcal{R}$, l'hypothèse $P \mathcal{R} Q$ signifie que $P(0) = Q(0)$ et $P(1) = Q(1)$.
Nous devons montrer que $Q \mathcal{R} P$.
Selon la définition de $\mathcal{R}$, $Q \mathcal{R} P$ signifie que $Q(0) = P(0)$ et $Q(1) = P(1)$.
Puisque nous avons $P(0) = Q(0)$ par hypothèse, et que l'égalité est une relation symétrique dans $\mathbb{R}$, nous pouvons affirmer que $Q(0) = P(0)$.
De même, puisque nous avons $P(1) = Q(1)$ par hypothèse, et que l'égalité est une relation symétrique dans $\mathbb{R}$, nous pouvons affirmer que $Q(1) = P(1)$.
Puisque les deux conditions sont vérifiées, nous concluons que $Q \mathcal{R} P$.
Par conséquent, la relation $\mathcal{R}$ est symétrique.

#### Transitivité
Soient $P$, $Q$ et $R$ trois polynômes arbitraires dans $E = \mathbb{R}[X]$.
Supposons que $P \mathcal{R} Q$ et $Q \mathcal{R} R$.
L'hypothèse $P \mathcal{R} Q$ signifie que $P(0) = Q(0)$ et $P(1) = Q(1)$. (Hypothèse A)
L'hypothèse $Q \mathcal{R} R$ signifie que $Q(0) = R(0)$ et $Q(1) = R(1)$. (Hypothèse B)
Nous devons montrer que $P \mathcal{R} R$.
Selon la définition de $\mathcal{R}$, $P \mathcal{R} R$ signifie que $P(0) = R(0)$ et $P(1) = R(1)$.
À partir de l'Hypothèse A, nous avons $P(0) = Q(0)$.
À partir de l'Hypothèse B, nous avons $Q(0) = R(0)$.
Puisque l'égalité est une relation transitive dans $\mathbb{R}$, de $P(0) = Q(0)$ et $Q(0) = R(0)$, nous déduisons $P(0) = R(0)$.
De même, à partir de l'Hypothèse A, nous avons $P(1) = Q(1)$.
À partir de l'Hypothèse B, nous avons $Q(1) = R(1)$.
Puisque l'égalité est une relation transitive dans $\mathbb{R}$, de $P(1) = Q(1)$ et $Q(1) = R(1)$, nous déduisons $P(1) = R(1)$.
Puisque les deux conditions sont vérifiées, nous concluons que $P \mathcal{R} R$.
Par conséquent, la relation $\mathcal{R}$ est transitive.

Puisque la relation $\mathcal{R}$ est réflexive, symétrique et transitive, $\mathcal{R}$ est une relation d'équivalence sur $E = \mathbb{R}[X]$.

### Question 2 : Caractériser l'ensemble quotient $E/\mathcal{R}$ en décrivant explicitement la classe d'équivalence $[P]$ d'un polynôme $P \in E$.

La classe d'équivalence $[P]$ d'un polynôme $P \in E$ est définie comme l'ensemble de tous les polynômes $Q \in E$ qui sont en relation avec $P$.
$$[P] = \{Q \in E \mid Q \mathcal{R} P\}$$
En utilisant la définition de la relation $\mathcal{R}$ :
$$[P] = \{Q \in \mathbb{R}[X] \mid Q(0) = P(0) \text{ et } Q(1) = P(1)\}$$
Un polynôme $Q$ appartient à la classe $[P]$ si et seulement si $Q$ prend les mêmes valeurs que $P$ en $X=0$ et en $X=1$.
Cela peut être reformulé en termes de différence de polynômes.
$Q(0) = P(0) \iff (Q-P)(0) = 0$.
$Q(1) = P(1) \iff (Q-P)(1) = 0$.
Ainsi, $Q \mathcal{R} P$ si et seulement si le polynôme $K = Q-P$ a des racines en $X=0$ et en $X=1$.
Selon le théorème des facteurs (ou théorème de Ruffini), si un polynôme $K(X)$ a une racine $x_0$, alors $(X-x_0)$ est un facteur de $K(X)$.
Puisque $K(0)=0$, $X$ est un facteur de $K(X)$.
Puisque $K(1)=0$, $(X-1)$ est un facteur de $K(X)$.
Comme $X$ et $(X-1)$ sont des polynômes irréductibles distincts (car ils ne sont pas associés, $X \neq c(X-1)$ pour $c \in \mathbb{R}^*$), leur produit $X(X-1)$ est un facteur de $K(X)$.
Par conséquent, $K(X)$ peut s'écrire sous la forme $K(X) = X(X-1)S(X)$ pour un certain polynôme $S(X) \in \mathbb{R}[X]$.
Puisque $K(X) = Q(X) - P(X)$, nous avons $Q(X) = P(X) + K(X)$.
Donc, la classe d'équivalence de $P$ est :
$$[P] = \{P(X) + X(X-1)S(X) \mid S(X) \in \mathbb{R}[X]\}$$
L'ensemble quotient $E/\mathcal{R}$ est l'ensemble de toutes ces classes d'équivalence. Chaque classe est déterminée par les valeurs du polynôme en 0 et en 1.

### Question 3 : Démontrer que les deux opérations sont bien définies.

Pour que les opérations d'addition et de multiplication sur $E/\mathcal{R}$ soient bien définies, le résultat de l'opération ne doit pas dépendre du choix des représentants des classes d'équivalence.
Soient $[P_1], [P_2], [Q_1], [Q_2]$ des classes d'équivalence dans $E/\mathcal{R}$.
Supposons que $[P_1] = [P_2]$ et $[Q_1] = [Q_2]$.
Cela signifie que $P_1 \mathcal{R} P_2$ et $Q_1 \mathcal{R} Q_2$.
Par définition de $\mathcal{R}$ :
$P_1(0) = P_2(0)$ et $P_1(1) = P_2(1)$ (Hypothèse 1)
$Q_1(0) = Q_2(0)$ et $Q_1(1) = Q_2(1)$ (Hypothèse 2)

#### Bien-définition de l'addition
Nous devons montrer que $[P_1+Q_1] = [P_2+Q_2]$, ce qui équivaut à montrer que $(P_1+Q_1) \mathcal{R} (P_2+Q_2)$.
Selon la définition de $\mathcal{R}$, cela signifie que nous devons vérifier que $(P_1+Q_1)(0) = (P_2+Q_2)(0)$ et $(P_1+Q_1)(1) = (P_2+Q_2)(1)$.

1.  Évaluation en $X=0$ :
    $(P_1+Q_1)(0) = P_1(0) + Q_1(0)$ (par définition de l'addition des polynômes et de l'évaluation).
    En utilisant l'Hypothèse 1, $P_1(0) = P_2(0)$.
    En utilisant l'Hypothèse 2, $Q_1(0) = Q_2(0)$.
    Par la propriété d'addition dans $\mathbb{R}$, nous avons $P_1(0) + Q_1(0) = P_2(0) + Q_2(0)$.
    Nous savons aussi que $(P_2+Q_2)(0) = P_2(0) + Q_2(0)$.
    Donc, $(P_1+Q_1)(0) = (P_2+Q_2)(0)$.

2.  Évaluation en $X=1$ :
    $(P_1+Q_1)(1) = P_1(1) + Q_1(1)$ (par définition de l'addition des polynômes et de l'évaluation).
    En utilisant l'Hypothèse 1, $P_1(1) = P_2(1)$.
    En utilisant l'Hypothèse 2, $Q_1(1) = Q_2(1)$.
    Par la propriété d'addition dans $\mathbb{R}$, nous avons $P_1(1) + Q_1(1) = P_2(1) + Q_2(1)$.
    Nous savons aussi que $(P_2+Q_2)(1) = P_2(1) + Q_2(1)$.
    Donc, $(P_1+Q_1)(1) = (P_2+Q_2)(1)$.

Puisque les deux conditions sont vérifiées, $(P_1+Q_1) \mathcal{R} (P_2+Q_2)$, ce qui implique $[P_1+Q_1] = [P_2+Q_2]$.
L'addition est donc bien définie sur $E/\mathcal{R}$.

#### Bien-définition de la multiplication
Nous devons montrer que $[P_1 \cdot Q_1] = [P_2 \cdot Q_2]$, ce qui équivaut à montrer que $(P_1 \cdot Q_1) \mathcal{R} (P_2 \cdot Q_2)$.
Selon la définition de $\mathcal{R}$, cela signifie que nous devons vérifier que $(P_1 \cdot Q_1)(0) = (P_2 \cdot Q_2)(0)$ et $(P_1 \cdot Q_1)(1) = (P_2 \cdot Q_2)(1)$.

1.  Évaluation en $X=0$ :
    $(P_1 \cdot Q_1)(0) = P_1(0) \cdot Q_1(0)$ (par définition de la multiplication des polynômes et de l'évaluation).
    En utilisant l'Hypothèse 1, $P_1(0) = P_2(0)$.
    En utilisant l'Hypothèse 2, $Q_1(0) = Q_2(0)$.
    Par la propriété de multiplication dans $\mathbb{R}$, nous avons $P_1(0) \cdot Q_1(0) = P_2(0) \cdot Q_2(0)$.
    Nous savons aussi que $(P_2 \cdot Q_2)(0) = P_2(0) \cdot Q_2(0)$.
    Donc, $(P_1 \cdot Q_1)(0) = (P_2 \cdot Q_2)(0)$.

2.  Évaluation en $X=1$ :
    $(P_1 \cdot Q_1)(1) = P_1(1) \cdot Q_1(1)$ (par définition de la multiplication des polynômes et de l'évaluation).
    En utilisant l'Hypothèse 1, $P_1(1) = P_2(1)$.
    En utilisant l'Hypothèse 2, $Q_1(1) = Q_2(1)$.
    Par la propriété de multiplication dans $\mathbb{R}$, nous avons $P_1(1) \cdot Q_1(1) = P_2(1) \cdot Q_2(1)$.
    Nous savons aussi que $(P_2 \cdot Q_2)(1) = P_2(1) \cdot Q_2(1)$.
    Donc, $(P_1 \cdot Q_1)(1) = (P_2 \cdot Q_2)(1)$.

Puisque les deux conditions sont vérifiées, $(P_1 \cdot Q_1) \mathcal{R} (P_2 \cdot Q_2)$, ce qui implique $[P_1 \cdot Q_1] = [P_2 \cdot Q_2]$.
La multiplication est donc bien définie sur $E/\mathcal{R}$.

### Question 4 : Montrer que $(E/\mathcal{R}, +, \cdot)$ est un anneau commutatif unitaire.

Pour montrer que $(E/\mathcal{R}, +, \cdot)$ est un anneau commutatif unitaire, nous devons vérifier les axiomes de l'anneau. Nous utilisons le fait que $(\mathbb{R}[X], +, \cdot)$ est un anneau commutatif unitaire et que les opérations sur $E/\mathcal{R}$ sont définies à partir de celles de $\mathbb{R}[X]$.

#### 1. $(E/\mathcal{R}, +)$ est un groupe abélien.
Soient $[P], [Q], [R]$ des éléments de $E/\mathcal{R}$.

*   **Associativité de l'addition :**
    $$([P] + [Q]) + [R] = [P+Q] + [R] = [(P+Q)+R]$$
    $$[P] + ([Q] + [R]) = [P] + [Q+R] = [P+(Q+R)]$$
    Puisque l'addition des polynômes dans $\mathbb{R}[X]$ est associative, $(P+Q)+R = P+(Q+R)$.
    Donc, $([P] + [Q]) + [R] = [P] + ([Q] + [R])$. L'addition est associative.

*   **Élément neutre de l'addition :**
    Considérons le polynôme nul $Z(X) = 0 \in \mathbb{R}[X]$. Sa classe d'équivalence est $[Z]$.
    Pour tout $[P] \in E/\mathcal{R}$ :
    $$[P] + [Z] = [P+Z] = [P]$$
    $$[Z] + [P] = [Z+P] = [P]$$
    Puisque $P+Z=P$ et $Z+P=P$ dans $\mathbb{R}[X]$, nous avons $[P+Z]=[P]$ et $[Z+P]=[P]$.
    Donc, $[Z]$ est l'élément neutre de l'addition.

*   **Élément inverse de l'addition :**
    Pour tout $[P] \in E/\mathcal{R}$, considérons le polynôme opposé $-P(X) \in \mathbb{R}[X]$. Sa classe est $[-P]$.
    $$[P] + [-P] = [P+(-P)] = [Z]$$
    $$[-P] + [P] = [(-P)+P] = [Z]$$
    Puisque $P+(-P)=Z$ et $(-P)+P=Z$ dans $\mathbb{R}[X]$, nous avons $[P+(-P)]=[Z]$ et $[(-P)+P]=[Z]$.
    Donc, $[-P]$ est l'inverse additif de $[P]$.

*   **Commutativité de l'addition :**
    $$[P] + [Q] = [P+Q]$$
    $$[Q] + [P] = [Q+P]$$
    Puisque l'addition des polynômes dans $\mathbb{R}[X]$ est commutative, $P+Q = Q+P$.
    Donc, $[P] + [Q] = [Q] + [P]$. L'addition est commutative.

Par conséquent, $(E/\mathcal{R}, +)$ est un groupe abélien.

#### 2. La multiplication est associative.
Soient $[P], [Q], [R]$ des éléments de $E/\mathcal{R}$.
$$([P] \cdot [Q]) \cdot [R] = [P \cdot Q] \cdot [R] = [(P \cdot Q) \cdot R]$$
$$[P] \cdot ([Q] \cdot [R]) = [P] \cdot [Q \cdot R] = [P \cdot (Q \cdot R)]$$
Puisque la multiplication des polynômes dans $\mathbb{R}[X]$ est associative, $(P \cdot Q) \cdot R = P \cdot (Q \cdot R)$.
Donc, $([P] \cdot [Q]) \cdot [R] = [P] \cdot ([Q] \cdot [R])$. La multiplication est associative.

#### 3. La multiplication est distributive par rapport à l'addition.
Soient $[P], [Q], [R]$ des éléments de $E/\mathcal{R}$.
*   **Distributivité à gauche :**
    $$[P] \cdot ([Q] + [R]) = [P] \cdot [Q+R] = [P \cdot (Q+R)]$$
    $$[P] \cdot [Q] + [P] \cdot [R] = [P \cdot Q] + [P \cdot R] = [(P \cdot Q) + (P \cdot R)]$$
    Puisque la multiplication des polynômes dans $\mathbb{R}[X]$ est distributive par rapport à l'addition, $P \cdot (Q+R) = (P \cdot Q) + (P \cdot R)$.
    Donc, $[P] \cdot ([Q] + [R]) = [P] \cdot [Q] + [P] \cdot [R]$.

*   **Distributivité à droite :**
    $$([Q] + [R]) \cdot [P] = [Q+R] \cdot [P] = [(Q+R) \cdot P]$$
    $$[Q] \cdot [P] + [R] \cdot [P] = [Q \cdot P] + [R \cdot P] = [(Q \cdot P) + (R \cdot P)]$$
    Puisque la multiplication des polynômes dans $\mathbb{R}[X]$ est distributive par rapport à l'addition, $(Q+R) \cdot P = (Q \cdot P) + (R \cdot P)$.
    Donc, $([Q] + [R]) \cdot [P] = [Q] \cdot [P] + [R] \cdot [P]$.
La multiplication est distributive sur l'addition.

#### 4. La multiplication est commutative.
Soient $[P], [Q]$ des éléments de $E/\mathcal{R}$.
$$[P] \cdot [Q] = [P \cdot Q]$$
$$[Q] \cdot [P] = [Q \cdot P]$$
Puisque la multiplication des polynômes dans $\mathbb{R}[X]$ est commutative, $P \cdot Q = Q \cdot P$.
Donc, $[P] \cdot [Q] = [Q] \cdot [P]$. La multiplication est commutative.

#### 5. Existence d'un élément unitaire (unité) pour la multiplication.
Considérons le polynôme constant $U(X) = 1 \in \mathbb{R}[X]$. Sa classe d'équivalence est $[U]$.
Pour tout $[P] \in E/\mathcal{R}$ :
$$[P] \cdot [U] = [P \cdot U] = [P]$$
$$[U] \cdot [P] = [U \cdot P] = [P]$$
Puisque $P \cdot U = P$ et $U \cdot P = P$ dans $\mathbb{R}[X]$, nous avons $[P \cdot U]=[P]$ et $[U \cdot P]=[P]$.
Donc, $[U]$ est l'élément unitaire de la multiplication.

Ayant vérifié tous les axiomes, nous concluons que $(E/\mathcal{R}, +, \cdot)$ est un anneau commutatif unitaire.

### Question 5 : L'anneau $(E/\mathcal{R}, +, \cdot)$ est-il intègre ? Justifier votre réponse.

Un anneau intègre est un anneau commutatif unitaire non nul dans lequel il n'y a pas de diviseurs de zéro, c'est-à-dire que si un produit $ab=0$, alors $a=0$ ou $b=0$.

L'élément neutre de l'addition dans $E/\mathcal{R}$ est la classe $[Z]$ du polynôme nul $Z(X)=0$.
Considérons les polynômes suivants :
Soit $P_1(X) = X-1$.
L'évaluation de $P_1$ aux points 0 et 1 donne :
$P_1(0) = 0-1 = -1$.
$P_1(1) = 1-1 = 0$.
Puisque $P_1(0) \neq 0$, la classe $[P_1]$ n'est pas la classe nulle $[Z]$ (car pour que $[P_1]=[Z]$, il faudrait $P_1(0)=0$ et $P_1(1)=0$). Donc $[P_1] \neq [Z]$.

Soit $P_2(X) = X$.
L'évaluation de $P_2$ aux points 0 et 1 donne :
$P_2(0) = 0$.
$P_2(1) = 1$.
Puisque $P_2(1) \neq 0$, la classe $[P_2]$ n'est pas la classe nulle $[Z]$. Donc $[P_2] \neq [Z]$.

Maintenant, considérons le produit de ces deux classes dans $E/\mathcal{R}$ :
$$[P_1] \cdot [P_2] = [P_1 \cdot P_2]$$
Calculons le polynôme produit $P_1 \cdot P_2$:
$P_1(X) \cdot P_2(X) = (X-1) \cdot X = X^2 - X$.
Évaluons ce polynôme produit aux points 0 et 1 :
$(X^2-X)(0) = 0^2 - 0 = 0$.
$(X^2-X)(1) = 1^2 - 1 = 0$.
Puisque $(P_1 \cdot P_2)(0) = 0$ et $(P_1 \cdot P_2)(1) = 0$, cela signifie que $P_1 \cdot P_2 \mathcal{R} Z$.
Donc, $[P_1 \cdot P_2] = [Z]$.

Nous avons trouvé deux éléments non nuls de l'anneau $E/\mathcal{R}$, à savoir $[P_1]$ et $[P_2]$, dont le produit est l'élément nul de l'anneau.
$[P_1] \neq [Z]$, $[P_2] \neq [Z]$, mais $[P_1] \cdot [P_2] = [Z]$.
Par conséquent, l'anneau $(E/\mathcal{R}, +, \cdot)$ n'est pas un anneau intègre. Il possède des diviseurs de zéro.

### Question 6 : Établir un isomorphisme d'anneaux entre $(E/\mathcal{R}, +, \cdot)$ et un anneau connu.

Considérons l'application $\phi: \mathbb{R}[X] \to \mathbb{R} \times \mathbb{R}$ définie par $\phi(P) = (P(0), P(1))$.
L'ensemble $\mathbb{R} \times \mathbb{R}$ est un anneau commutatif unitaire avec l'addition et la multiplication composante par composante :
Pour $(a,b), (c,d) \in \mathbb{R} \times \mathbb{R}$:
$(a,b) + (c,d) = (a+c, b+d)$
$(a,b) \cdot (c,d) = (ac, bd)$

Nous allons montrer que $\phi$ est un homomorphisme d'anneaux, déterminer son noyau et son image, puis utiliser le premier théorème d'isomorphisme pour les anneaux.

#### 1. $\phi$ est un homomorphisme d'anneaux.
Soient $P, Q \in \mathbb{R}[X]$.
*   **Compatibilité avec l'addition :**
    $\phi(P+Q) = ((P+Q)(0), (P+Q)(1))$ (par définition de $\phi$).
    $(P+Q)(0) = P(0) + Q(0)$ (par définition de l'addition des polynômes et de l'évaluation).
    $(P+Q)(1) = P(1) + Q(1)$ (par définition de l'addition des polynômes et de l'évaluation).
    Donc, $\phi(P+Q) = (P(0)+Q(0), P(1)+Q(1))$.
    D'autre part :
    $\phi(P) + \phi(Q) = (P(0), P(1)) + (Q(0), Q(1))$ (par définition de $\phi$).
    $\phi(P) + \phi(Q) = (P(0)+Q(0), P(1)+Q(1))$ (par définition de l'addition dans $\mathbb{R} \times \mathbb{R}$).
    Ainsi, $\phi(P+Q) = \phi(P) + \phi(Q)$.

*   **Compatibilité avec la multiplication :**
    $\phi(P \cdot Q) = ((P \cdot Q)(0), (P \cdot Q)(1))$ (par définition de $\phi$).
    $(P \cdot Q)(0) = P(0) \cdot Q(0)$ (par définition de la multiplication des polynômes et de l'évaluation).
    $(P \cdot Q)(1) = P(1) \cdot Q(1)$ (par définition de la multiplication des polynômes et de l'évaluation).
    Donc, $\phi(P \cdot Q) = (P(0) \cdot Q(0), P(1) \cdot Q(1))$.
    D'autre part :
    $\phi(P) \cdot \phi(Q) = (P(0), P(1)) \cdot (Q(0), Q(1))$ (par définition de $\phi$).
    $\phi(P) \cdot \phi(Q) = (P(0) \cdot Q(0), P(1) \cdot Q(1))$ (par définition de la multiplication dans $\mathbb{R} \times \mathbb{R}$).
    Ainsi, $\phi(P \cdot Q) = \phi(P) \cdot \phi(Q)$.

Puisque $\phi$ respecte l'addition et la multiplication, c'est un homomorphisme d'anneaux.

#### 2. Détermination du noyau de $\phi$, $\text{Ker}(\phi)$.
Le noyau de $\phi$ est l'ensemble des polynômes $P \in \mathbb{R}[X]$ tels que $\phi(P)$ est l'élément neutre de $\mathbb{R} \times \mathbb{R}$ (qui est $(0,0)$).
$$\text{Ker}(\phi) = \{P \in \mathbb{R}[X] \mid \phi(P) = (0,0)\}$$
$$\text{Ker}(\phi) = \{P \in \mathbb{R}[X] \mid P(0)=0 \text{ et } P(1)=0\}$$
Comme établi dans la Question 2, un polynôme $P$ a des racines en $X=0$ et $X=1$ si et seulement si il est divisible par $X$ et par $(X-1)$. Puisque $X$ et $(X-1)$ sont premiers entre eux, $P$ doit être divisible par leur produit $X(X-1)$.
Donc, $\text{Ker}(\phi) = \{X(X-1)S(X) \mid S(X) \in \mathbb{R}[X]\}$.
Nous avons aussi montré dans la Question 2 que $P \mathcal{R} Q \iff P-Q \in \text{Ker}(\phi)$.
Les classes d'équivalence $[P]$ de la relation $\mathcal{R}$ sont précisément les classes latérales (ou cosets) $P + \text{Ker}(\phi)$.
Donc, l'ensemble quotient $E/\mathcal{R}$ est isomorphe à $\mathbb{R}[X]/\text{Ker}(\phi)$ par la correspondance naturelle $[P] \leftrightarrow P + \text{Ker}(\phi)$.

#### 3. Détermination de l'image de $\phi$, $\text{Im}(\phi)$.
L'image de $\phi$ est l'ensemble des paires $(a,b) \in \mathbb{R} \times \mathbb{R}$ pour lesquelles il existe un polynôme $P \in \mathbb{R}[X]$ tel que $P(0)=a$ et $P(1)=b$.
$$\text{Im}(\phi) = \{(P(0), P(1)) \mid P \in \mathbb{R}[X]\}$$
Nous devons vérifier si $\phi$ est surjective, c'est-à-dire si pour toute paire $(a,b) \in \mathbb{R} \times \mathbb{R}$, il existe un polynôme $P(X)$ tel que $P(0)=a$ et $P(1)=b$.
Ceci est une application directe du théorème d'interpolation de Lagrange pour deux points.
Le polynôme $P(X)$ est donné par :
$$P(X) = a \frac{X-1}{0-1} + b \frac{X-0}{1-0}$$
$$P(X) = a \frac{X-1}{-1} + b \frac{X}{1}$$
$$P(X) = -a(X-1) + bX$$
$$P(X) = (b-a)X + a$$
Ce polynôme est bien un élément de $\mathbb{R}[X]$.
Vérifions ses valeurs :
$P(0) = (b-a) \cdot 0 + a = a$.
$P(1) = (b-a) \cdot 1 + a = b-a+a = b$.
Ainsi, pour toute paire $(a,b) \in \mathbb{R} \times \mathbb{R}$, il existe un polynôme $P(X)$ dans $\mathbb{R}[X]$ tel que $P(0)=a$ et $P(1)=b$.
Par conséquent, $\text{Im}(\phi) = \mathbb{R} \times \mathbb{R}$. L'homomorphisme $\phi$ est surjectif.

#### 4. Application du premier théorème d'isomorphisme.
Le premier théorème d'isomorphisme pour les anneaux stipule que si $\phi: R \to S$ est un homomorphisme d'anneaux surjectif, alors $R/\text{Ker}(\phi) \cong S$.
Dans notre cas :
L'anneau de départ est $R = \mathbb{R}[X]$.
L'anneau d'arrivée est $S = \mathbb{R} \times \mathbb{R}$.
L'homomorphisme est $\phi: \mathbb{R}[X] \to \mathbb{R} \times \mathbb{R}$.
Nous avons montré que $\phi$ est surjectif et que $\text{Ker}(\phi)$ est l'ensemble des polynômes $P$ tels que $P(0)=0$ et $P(1)=0$.
Nous avons également montré que les classes d'équivalence de $E/\mathcal{R}$ sont les classes latérales de $\text{Ker}(\phi)$, c'est-à-dire $E/\mathcal{R} = \mathbb{R}[X]/\text{Ker}(\phi)$.

Par conséquent, en vertu du premier théorème d'isomorphisme pour les anneaux, nous avons :
$$E/\mathcal{R} \cong \mathbb{R} \times \mathbb{R}$$
L'anneau $(E/\mathcal{R}, +, \cdot)$ est isomorphe à l'anneau produit direct $\mathbb{R} \times \mathbb{R}$.

**Remarque :** La non-intégrité de $E/\mathcal{R}$ établie à la Question 5 est cohérente avec l'isomorphisme $E/\mathcal{R} \cong \mathbb{R} \times \mathbb{R}$, car l'anneau $\mathbb{R} \times \mathbb{R}$ n'est pas intègre. Par exemple, $(1,0) \cdot (0,1) = (0,0)$, et $(1,0) \neq (0,0)$, $(0,1) \neq (0,0)$.