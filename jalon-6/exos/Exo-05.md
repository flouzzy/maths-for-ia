---

# Exercice 5 : Anneau quotient de polynômes et irréductibilité

**Difficulté :** ⭐⭐⭐

## Énoncé

Soit $\mathbb{R}[X]$ l'anneau des polynômes à coefficients réels.
On considère le polynôme $P(X) = X^2 + 1 \in \mathbb{R}[X]$.

On définit une relation $\mathcal{R}$ sur $\mathbb{R}[X]$ de la manière suivante :
Pour tout $(A(X), B(X)) \in \mathbb{R}[X] \times \mathbb{R}[X]$,
$A(X) \mathcal{R} B(X)$ si et seulement si $P(X)$ divise $A(X) - B(X)$.

**Partie 1 : Relation d'équivalence**
Démontrer que $\mathcal{R}$ est une relation d'équivalence sur $\mathbb{R}[X]$.

**Partie 2 : Caractérisation de l'ensemble quotient**
1.  Caractériser les éléments de l'ensemble quotient $\mathbb{R}[X]/\mathcal{R}$.
2.  Montrer que chaque classe d'équivalence $[A(X)]$ contient un unique polynôme $R(X)$ de degré strictement inférieur à 2.

**Partie 3 : Structure algébrique de l'ensemble quotient**
On munit l'ensemble quotient $\mathbb{R}[X]/\mathcal{R}$ des opérations d'addition et de multiplication définies comme suit :
Pour tout $[A(X)], [B(X)] \in \mathbb{R}[X]/\mathcal{R}$,
$$[A(X)] + [B(X)] = [A(X) + B(X)]$$
$$[A(X)] \cdot [B(X)] = [A(X) \cdot B(X)]$$
1.  Démontrer que ces opérations sont bien définies, c'est-à-dire qu'elles ne dépendent pas du choix des représentants de chaque classe d'équivalence.
2.  Démontrer que $(\mathbb{R}[X]/\mathcal{R}, +, \cdot)$ est un anneau commutatif unitaire.
3.  Déterminer si $(\mathbb{R}[X]/\mathcal{R}, +, \cdot)$ est un corps. Justifier rigoureusement votre réponse.

## Correction Détaillée

### Partie 1 : Relation d'équivalence

Pour démontrer que $\mathcal{R}$ est une relation d'équivalence sur $\mathbb{R}[X]$, nous devons vérifier les trois propriétés suivantes : réflexivité, symétrie et transitivité.

Soient $A(X), B(X), C(X)$ des polynômes arbitraires dans $\mathbb{R}[X]$.

1.  **Réflexivité :**
    Une relation $\mathcal{R}$ est réflexive si pour tout $A(X) \in \mathbb{R}[X]$, $A(X) \mathcal{R} A(X)$.
    Pour vérifier cette propriété, nous devons montrer que $P(X)$ divise $A(X) - A(X)$.
    Nous calculons la différence :
    $$A(X) - A(X) = 0$$
    Le polynôme nul est divisible par tout polynôme non nul. En particulier, $P(X) = X^2+1$ est un polynôme non nul.
    Ainsi, $P(X)$ divise $0$.
    Par conséquent, $A(X) \mathcal{R} A(X)$.
    La relation $\mathcal{R}$ est réflexive.

2.  **Symétrie :**
    Une relation $\mathcal{R}$ est symétrique si pour tout $A(X), B(X) \in \mathbb{R}[X]$, si $A(X) \mathcal{R} B(X)$, alors $B(X) \mathcal{R} A(X)$.
    Supposons que $A(X) \mathcal{R} B(X)$. Par définition de $\mathcal{R}$, cela signifie que $P(X)$ divise $A(X) - B(X)$.
    Par la définition de la divisibilité des polynômes, cela implique qu'il existe un polynôme $K(X) \in \mathbb{R}[X]$ tel que :
    $$A(X) - B(X) = K(X)P(X)$$
    Nous voulons montrer que $B(X) \mathcal{R} A(X)$, ce qui signifie que $P(X)$ divise $B(X) - A(X)$.
    Nous pouvons manipuler l'équation ci-dessus :
    $$-(B(X) - A(X)) = K(X)P(X)$$
    Multiplions les deux côtés par $-1$ :
    $$B(X) - A(X) = -K(X)P(X)$$
    Puisque $K(X) \in \mathbb{R}[X]$, alors $-K(X)$ est également un polynôme dans $\mathbb{R}[X]$. Notons $K'(X) = -K(X)$.
    Donc, nous avons :
    $$B(X) - A(X) = K'(X)P(X)$$
    Ceci démontre que $P(X)$ divise $B(X) - A(X)$.
    Par conséquent, $B(X) \mathcal{R} A(X)$.
    La relation $\mathcal{R}$ est symétrique.

3.  **Transitivité :**
    Une relation $\mathcal{R}$ est transitive si pour tout $A(X), B(X), C(X) \in \mathbb{R}[X]$, si $A(X) \mathcal{R} B(X)$ et $B(X) \mathcal{R} C(X)$, alors $A(X) \mathcal{R} C(X)$.
    Supposons que $A(X) \mathcal{R} B(X)$ et $B(X) \mathcal{R} C(X)$.
    Par définition de $\mathcal{R}$ :
    *   $P(X)$ divise $A(X) - B(X)$, donc il existe $K_1(X) \in \mathbb{R}[X]$ tel que :
        $$A(X) - B(X) = K_1(X)P(X) \quad (1)$$
    *   $P(X)$ divise $B(X) - C(X)$, donc il existe $K_2(X) \in \mathbb{R}[X]$ tel que :
        $$B(X) - C(X) = K_2(X)P(X) \quad (2)$$
    Nous voulons montrer que $A(X) \mathcal{R} C(X)$, ce qui signifie que $P(X)$ divise $A(X) - C(X)$.
    Nous pouvons additionner les équations (1) et (2) :
    $$(A(X) - B(X)) + (B(X) - C(X)) = K_1(X)P(X) + K_2(X)P(X)$$
    $$A(X) - C(X) = (K_1(X) + K_2(X))P(X)$$
    Puisque $K_1(X) \in \mathbb{R}[X]$ et $K_2(X) \in \mathbb{R}[X]$, leur somme $K_1(X) + K_2(X)$ est également un polynôme dans $\mathbb{R}[X]$. Notons $K_3(X) = K_1(X) + K_2(X)$.
    Donc, nous avons :
    $$A(X) - C(X) = K_3(X)P(X)$$
    Ceci démontre que $P(X)$ divise $A(X) - C(X)$.
    Par conséquent, $A(X) \mathcal{R} C(X)$.
    La relation $\mathcal{R}$ est transitive.

Puisque $\mathcal{R}$ est réflexive, symétrique et transitive, elle est une relation d'équivalence sur $\mathbb{R}[X]$.

### Partie 2 : Caractérisation de l'ensemble quotient

1.  **Caractérisation des éléments de l'ensemble quotient $\mathbb{R}[X]/\mathcal{R}$ :**
    L'ensemble quotient $\mathbb{R}[X]/\mathcal{R}$ est l'ensemble de toutes les classes d'équivalence $[A(X)]$ pour $A(X) \in \mathbb{R}[X]$.
    Par définition, $[A(X)] = \{ B(X) \in \mathbb{R}[X] \mid A(X) \mathcal{R} B(X) \}$.
    Ceci est équivalent à $[A(X)] = \{ B(X) \in \mathbb{R}[X] \mid P(X) \text{ divise } A(X) - B(X) \}$.
    Ou encore, $[A(X)] = \{ B(X) \in \mathbb{R}[X] \mid A(X) - B(X) = K(X)P(X) \text{ pour un certain } K(X) \in \mathbb{R}[X] \}$.
    Ceci peut être réécrit comme $B(X) = A(X) - K(X)P(X)$.
    De plus, $A(X) \mathcal{R} B(X)$ est équivalent à $A(X) \equiv B(X) \pmod{P(X)}$.
    La classe d'équivalence $[A(X)]$ est l'ensemble de tous les polynômes qui ont le même reste que $A(X)$ lors de la division euclidienne par $P(X)$.

2.  **Unicité du représentant de degré strictement inférieur à 2 :**
    Considérons un polynôme $A(X) \in \mathbb{R}[X]$.
    D'après le théorème de la division euclidienne dans l'anneau $\mathbb{R}[X]$, pour tout polynôme $A(X)$ et tout polynôme $P(X) = X^2+1$ non nul, il existe un unique quotient $Q(X) \in \mathbb{R}[X]$ et un unique reste $R(X) \in \mathbb{R}[X]$ tels que :
    $$A(X) = Q(X)P(X) + R(X)$$
    où le degré du reste $R(X)$ est strictement inférieur au degré du diviseur $P(X)$.
    Le degré de $P(X) = X^2+1$ est $\deg(P(X)) = 2$.
    Par conséquent, le degré du reste $R(X)$ doit satisfaire $\deg(R(X)) < 2$.
    Les polynômes de degré strictement inférieur à 2 sont de la forme $aX+b$, où $a, b \in \mathbb{R}$.

    Maintenant, montrons que chaque classe d'équivalence $[A(X)]$ contient un tel polynôme $R(X)$ et qu'il est unique.

    *   **Existence :**
        À partir de l'équation de la division euclidienne $A(X) = Q(X)P(X) + R(X)$, nous pouvons écrire :
        $$A(X) - R(X) = Q(X)P(X)$$
        Cette égalité signifie que $P(X)$ divise $A(X) - R(X)$.
        Par définition de la relation $\mathcal{R}$, ceci implique $A(X) \mathcal{R} R(X)$.
        Par conséquent, $R(X)$ appartient à la classe d'équivalence de $A(X)$, c'est-à-dire $[A(X)] = [R(X)]$.
        Chaque classe d'équivalence contient donc au moins un polynôme de degré strictement inférieur à 2 (le reste de la division euclidienne par $P(X)$).

    *   **Unicité :**
        Supposons qu'il existe deux polynômes $R_1(X)$ et $R_2(X)$ dans la même classe d'équivalence $[A(X)]$, tels que $\deg(R_1(X)) < 2$ et $\deg(R_2(X)) < 2$.
        Puisque $R_1(X)$ et $R_2(X)$ appartiennent à la même classe, ils sont liés par la relation $\mathcal{R}$ :
        $$R_1(X) \mathcal{R} R_2(X)$$
        Par définition de $\mathcal{R}$, cela signifie que $P(X)$ divise $R_1(X) - R_2(X)$.
        Considérons le polynôme $D(X) = R_1(X) - R_2(X)$.
        Puisque $\deg(R_1(X)) < 2$ et $\deg(R_2(X)) < 2$, le degré de leur différence $D(X)$ est également strictement inférieur à 2.
        C'est-à-dire, $\deg(D(X)) < 2$.
        D'un autre côté, nous savons que $P(X)$ divise $D(X)$.
        Si un polynôme non nul $P(X)$ divise un autre polynôme $D(X)$, alors le degré de $P(X)$ doit être inférieur ou égal au degré de $D(X)$, à moins que $D(X)$ ne soit le polynôme nul.
        Nous avons $\deg(P(X)) = 2$.
        Nous avons $\deg(D(X)) < 2$.
        La seule façon pour un polynôme de degré 2 de diviser un polynôme de degré strictement inférieur à 2 est que le polynôme de degré inférieur soit le polynôme nul.
        Donc, nous devons avoir $D(X) = 0$.
        $$R_1(X) - R_2(X) = 0$$
        $$R_1(X) = R_2(X)$$
        Ceci prouve l'unicité.

    En conclusion, chaque classe d'équivalence $[A(X)]$ dans $\mathbb{R}[X]/\mathcal{R}$ contient un unique polynôme de la forme $aX+b$ où $a, b \in \mathbb{R}$.
    L'ensemble quotient $\mathbb{R}[X]/\mathcal{R}$ peut donc être identifié à l'ensemble des polynômes de degré inférieur à 2, modulo $X^2+1$. Ses éléments sont les classes $[aX+b]$ pour $a, b \in \mathbb{R}$.

### Partie 3 : Structure algébrique de l'ensemble quotient

1.  **Démonstration que les opérations sont bien définies :**
    Nous devons montrer que le résultat des opérations d'addition et de multiplication ne dépend pas du choix des représentants.

    *   **Pour l'addition :**
        Soient $[A_1(X)] = [A_2(X)]$ et $[B_1(X)] = [B_2(X)]$ deux égalités de classes.
        Par définition, $[A_1(X)] = [A_2(X)]$ signifie $A_1(X) \mathcal{R} A_2(X)$, donc $P(X)$ divise $A_1(X) - A_2(X)$. Il existe $K_1(X) \in \mathbb{R}[X]$ tel que :
        $$A_1(X) - A_2(X) = K_1(X)P(X) \quad (3)$$
        De même, $[B_1(X)] = [B_2(X)]$ signifie $B_1(X) \mathcal{R} B_2(X)$, donc $P(X)$ divise $B_1(X) - B_2(X)$. Il existe $K_2(X) \in \mathbb{R}[X]$ tel que :
        $$B_1(X) - B_2(X) = K_2(X)P(X) \quad (4)$$
        Nous voulons montrer que $[A_1(X) + B_1(X)] = [A_2(X) + B_2(X)]$, ce qui équivaut à montrer que $P(X)$ divise $(A_1(X) + B_1(X)) - (A_2(X) + B_2(X))$.
        Additionnons les équations (3) et (4) :
        $$(A_1(X) - A_2(X)) + (B_1(X) - B_2(X)) = K_1(X)P(X) + K_2(X)P(X)$$
        En regroupant les termes :
        $$(A_1(X) + B_1(X)) - (A_2(X) + B_2(X)) = (K_1(X) + K_2(X))P(X)$$
        Puisque $K_1(X) + K_2(X) \in \mathbb{R}[X]$, cette égalité montre que $P(X)$ divise $(A_1(X) + B_1(X)) - (A_2(X) + B_2(X))$.
        Par conséquent, $[A_1(X) + B_1(X)] = [A_2(X) + B_2(X)]$. L'addition est bien définie.

    *   **Pour la multiplication :**
        Reprenons les hypothèses (3) et (4) :
        $$A_1(X) = A_2(X) + K_1(X)P(X)$$
        $$B_1(X) = B_2(X) + K_2(X)P(X)$$
        Nous voulons montrer que $[A_1(X) \cdot B_1(X)] = [A_2(X) \cdot B_2(X)]$, ce qui équivaut à montrer que $P(X)$ divise $A_1(X)B_1(X) - A_2(X)B_2(X)$.
        Calculons le produit $A_1(X)B_1(X)$ :
        $$A_1(X)B_1(X) = (A_2(X) + K_1(X)P(X))(B_2(X) + K_2(X)P(X))$$
        Développons le produit :
        $$A_1(X)B_1(X) = A_2(X)B_2(X) + A_2(X)K_2(X)P(X) + K_1(X)P(X)B_2(X) + K_1(X)P(X)K_2(X)P(X)$$
        $$A_1(X)B_1(X) = A_2(X)B_2(X) + (A_2(X)K_2(X) + K_1(X)B_2(X) + K_1(X)K_2(X)P(X))P(X)$$
        Soustrayons $A_2(X)B_2(X)$ des deux côtés :
        $$A_1(X)B_1(X) - A_2(X)B_2(X) = (A_2(X)K_2(X) + K_1(X)B_2(X) + K_1(X)K_2(X)P(X))P(X)$$
        Puisque $A_2(X)K_2(X) + K_1(X)B_2(X) + K_1(X)K_2(X)P(X)$ est un polynôme dans $\mathbb{R}[X]$, cette égalité montre que $P(X)$ divise $A_1(X)B_1(X) - A_2(X)B_2(X)$.
        Par conséquent, $[A_1(X) \cdot B_1(X)] = [A_2(X) \cdot B_2(X)]$. La multiplication est bien définie.

2.  **Démonstration que $(\mathbb{R}[X]/\mathcal{R}, +, \cdot)$ est un anneau commutatif unitaire :**
    Nous devons vérifier les axiomes de l'anneau. Ces propriétés sont héritées de l'anneau $\mathbb{R}[X]$.

    *   **$(\mathbb{R}[X]/\mathcal{R}, +)$ est un groupe abélien :**
        *   **Associativité de l'addition :** Pour tout $[A(X)], [B(X)], [C(X)] \in \mathbb{R}[X]/\mathcal{R}$ :
            $$([A(X)] + [B(X)]) + [C(X)] = [A(X) + B(X)] + [C(X)] = [(A(X) + B(X)) + C(X)]$$
            Puisque l'addition est associative dans $\mathbb{R}[X]$ :
            $$[(A(X) + B(X)) + C(X)] = [A(X) + (B(X) + C(X))] = [A(X)] + [B(X) + C(X)] = [A(X)] + ([B(X)] + [C(X)])$$
            L'addition est associative.
        *   **Commutativité de l'addition :** Pour tout $[A(X)], [B(X)] \in \mathbb{R}[X]/\mathcal{R}$ :
            $$[A(X)] + [B(X)] = [A(X) + B(X)]$$
            Puisque l'addition est commutative dans $\mathbb{R}[X]$ :
            $$[A(X) + B(X)] = [B(X) + A(X)] = [B(X)] + [A(X)]$$
            L'addition est commutative.
        *   **Élément neutre de l'addition :** L'élément neutre est la classe du polynôme nul $0(X) \in \mathbb{R}[X]$, notée $[0(X)]$.
            Pour tout $[A(X)] \in \mathbb{R}[X]/\mathcal{R}$ :
            $$[A(X)] + [0(X)] = [A(X) + 0(X)] = [A(X)]$$
            L'élément neutre additif est $[0(X)]$.
        *   **Opposé additif :** Pour tout $[A(X)] \in \mathbb{R}[X]/\mathcal{R}$, l'opposé est la classe du polynôme $-A(X) \in \mathbb{R}[X]$, notée $[-A(X)]$.
            $$[A(X)] + [-A(X)] = [A(X) + (-A(X))] = [0(X)]$$
            Chaque élément possède un opposé.
        Donc $(\mathbb{R}[X]/\mathcal{R}, +)$ est un groupe abélien.

    *   **Associativité de la multiplication :** Pour tout $[A(X)], [B(X)], [C(X)] \in \mathbb{R}[X]/\mathcal{R}$ :
        $$([A(X)] \cdot [B(X)]) \cdot [C(X)] = [A(X) \cdot B(X)] \cdot [C(X)] = [(A(X) \cdot B(X)) \cdot C(X)]$$
        Puisque la multiplication est associative dans $\mathbb{R}[X]$ :
        $$[(A(X) \cdot B(X)) \cdot C(X)] = [A(X) \cdot (B(X) \cdot C(X))] = [A(X)] \cdot [B(X) \cdot C(X)] = [A(X)] \cdot ([B(X)] \cdot [C(X)])$$
        La multiplication est associative.

    *   **Distributivité de la multiplication par rapport à l'addition :** Pour tout $[A(X)], [B(X)], [C(X)] \in \mathbb{R}[X]/\mathcal{R}$ :
        $$[A(X)] \cdot ([B(X)] + [C(X)]) = [A(X)] \cdot [B(X) + C(X)] = [A(X) \cdot (B(X) + C(X))]$$
        Puisque la multiplication est distributive par rapport à l'addition dans $\mathbb{R}[X]$ :
        $$[A(X) \cdot (B(X) + C(X))] = [A(X)B(X) + A(X)C(X)] = [A(X)B(X)] + [A(X)C(X)]$$
        $$[A(X)B(X)] + [A(X)C(X)] = ([A(X)] \cdot [B(X)]) + ([A(X)] \cdot [C(X)])$$
        La distributivité est vérifiée.

    *   **Commutativité de la multiplication :** Pour tout $[A(X)], [B(X)] \in \mathbb{R}[X]/\mathcal{R}$ :
        $$[A(X)] \cdot [B(X)] = [A(X) \cdot B(X)]$$
        Puisque la multiplication est commutative dans $\mathbb{R}[X]$ :
        $$[A(X) \cdot B(X)] = [B(X) \cdot A(X)] = [B(X)] \cdot [A(X)]$$
        La multiplication est commutative.

    *   **Élément neutre de la multiplication :** L'élément neutre est la classe du polynôme constant $1 \in \mathbb{R}[X]$, notée $[1]$.
        Pour tout $[A(X)] \in \mathbb{R}[X]/\mathcal{R}$ :
        $$[A(X)] \cdot [1] = [A(X) \cdot 1] = [A(X)]$$
        L'élément neutre multiplicatif est $[1]$. De plus, $[1] \neq [0]$ car $1$ n'est pas divisible par $P(X)=X^2+1$.

    Puisque toutes les propriétés sont vérifiées, $(\mathbb{R}[X]/\mathcal{R}, +, \cdot)$ est un anneau commutatif unitaire.

3.  **Déterminer si $(\mathbb{R}[X]/\mathcal{R}, +, \cdot)$ est un corps :**
    Un anneau commutatif unitaire $(R, +, \cdot)$ est un corps si tout élément non nul de $R$ possède un inverse multiplicatif.
    Soit $[A(X)]$ un élément non nul de $\mathbb{R}[X]/\mathcal{R}$.
    La condition $[A(X)] \neq [0]$ signifie que $A(X)$ n'est pas divisible par $P(X)$.
    Le polynôme $P(X) = X^2+1$ est irréductible sur $\mathbb{R}$. En effet, ses racines sont $i$ et $-i$, qui ne sont pas des nombres réels. Par conséquent, $P(X)$ ne peut pas être factorisé en un produit de polynômes de degré 1 à coefficients réels.
    Puisque $P(X)$ est irréductible sur $\mathbb{R}$ et $A(X)$ n'est pas un multiple de $P(X)$, cela signifie que les polynômes $A(X)$ et $P(X)$ sont premiers entre eux dans $\mathbb{R}[X]$.
    Selon le théorème de Bézout pour les polynômes (qui est une conséquence de l'algorithme d'Euclide étendu dans un anneau euclidien comme $\mathbb{R}[X]$), si deux polynômes $A(X)$ et $P(X)$ sont premiers entre eux, alors il existe des polynômes $U(X) \in \mathbb{R}[X]$ et $V(X) \in \mathbb{R}[X]$ tels que :
    $$A(X)U(X) + P(X)V(X) = 1$$
    où $1$ est le polynôme constant $1$, qui est l'élément neutre de la multiplication dans $\mathbb{R}[X]$.
    Passons cette égalité aux classes d'équivalence dans $\mathbb{R}[X]/\mathcal{R}$ :
    $$[A(X)U(X) + P(X)V(X)] = [1]$$
    Par les propriétés de l'addition et de la multiplication des classes :
    $$[A(X)U(X)] + [P(X)V(X)] = [1]$$
    Nous savons que $P(X)$ divise $P(X)V(X)$, donc $[P(X)V(X)] = [0]$ dans $\mathbb{R}[X]/\mathcal{R}$.
    En substituant cela dans l'équation :
    $$[A(X)U(X)] + [0] = [1]$$
    $$[A(X)U(X)] = [1]$$
    Cette égalité montre que $[U(X)]$ est l'inverse multiplicatif de $[A(X)]$ dans $\mathbb{R}[X]/\mathcal{R}$.
    Puisque nous avons montré que tout élément non nul $[A(X)]$ de $\mathbb{R}[X]/\mathcal{R}$ possède un inverse multiplicatif, l'anneau $(\mathbb{R}[X]/\mathcal{R}, +, \cdot)$ est un corps.

    **Justification supplémentaire (lien avec $\mathbb{C}$):**
    Il est à noter que l'anneau quotient $\mathbb{R}[X]/(X^2+1)$ est isomorphe au corps des nombres complexes $\mathbb{C}$. L'isomorphisme est donné par $\phi: \mathbb{R}[X]/(X^2+1) \to \mathbb{C}$ tel que $\phi([aX+b]) = b+ai$. L'élément $[X]$ correspond à $i$ car $[X]^2 = [X^2] = [X^2 - (X^2+1)] = [-1]$. Donc $[X]^2 = [-1]$, ce qui est la propriété caractéristique de $i$.

---