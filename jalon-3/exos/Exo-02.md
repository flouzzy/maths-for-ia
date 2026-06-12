Voici l'Exercice 2 pour le Jalon 3, rédigé avec la rigueur attendue.

---

# Exercice 2 (Jalon 3 : Quantification, ordre des quantificateurs, négation)

**Niveau de difficulté :** $\star / 5$

**Consignes :** Pour chacune des propositions suivantes, vous devrez :
1.  **Typage des objets :** Identifier et typer rigoureusement tous les objets mathématiques (ensembles, variables, constantes, relations, opérations).
2.  **Formalisation :** Écrire la proposition en utilisant des quantificateurs ($\forall$, $\exists$) et des symboles logiques ($\land$, $\lor$, $\neg$, $\implies$, $\iff$).
3.  **Négation formelle :** Écrire la négation de la proposition formalisée, en poussant la négation le plus loin possible à l'intérieur de la formule (c'est-à-dire en minimisant la portée de l'opérateur $\neg$).
4.  **Négation en langage naturel :** Traduire cette négation formelle en une phrase claire et précise en langage naturel.
5.  **Valeur de vérité et justification :** Déterminer si la proposition originale est vraie ou fausse, et justifier votre réponse de manière ultra-détaillée, sans aucune ellipse mathématique. Chaque étape logique et chaque définition utilisée doit être explicitée.

On rappelle que $\mathbb{N}$ désigne l'ensemble des entiers naturels $\{0, 1, 2, \ldots\}$ et $\mathbb{Z}$ l'ensemble des entiers relatifs $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$.

---

**Propositions :**

**Proposition P1 :** "Tout entier relatif multiple de 6 est un entier relatif multiple de 3."

**Proposition P2 :** "Il existe un entier naturel $M$ tel que, pour tout entier naturel $n$ strictement supérieur à $M$, $n$ est un nombre premier."

**Proposition P3 :** "Pour tout entier relatif $x$, il existe un entier relatif $y$ tel que $x \cdot y = 1$."

---

# Correction de l'Exercice 2

**Rappels de définitions pour la correction :**
*   Un entier relatif $a$ est un **multiple** d'un entier relatif $b$ si et seulement si il existe un entier relatif $k$ tel que $a = b \cdot k$. Formellement : $(a \text{ est un multiple de } b) \iff (\exists k \in \mathbb{Z}, a = b \cdot k)$.
*   Un entier naturel $n$ est un **nombre premier** si et seulement si $n > 1$ et ses seuls diviseurs positifs sont $1$ et $n$. Formellement : $(n \text{ est premier}) \iff (n \in \mathbb{N} \land n > 1 \land (\forall d \in \mathbb{N}, (d \text{ divise } n \land d > 0) \implies (d=1 \lor d=n)))$.

---

## Proposition P1 : "Tout entier relatif multiple de 6 est un entier relatif multiple de 3."

1.  **Typage des objets :**
    *   La variable $n$ représente un entier relatif. Son domaine est l'ensemble $\mathbb{Z}$.
    *   Les nombres $3$ et $6$ sont des entiers relatifs constants.
    *   La relation "être multiple de" est une relation binaire sur $\mathbb{Z} \times \mathbb{Z}$.

2.  **Formalisation :**
    La proposition P1 peut être décomposée et formalisée comme suit :
    *   "Tout entier relatif $n$..." se traduit par $\forall n \in \mathbb{Z}$.
    *   "...$n$ est un multiple de 6..." se traduit par la proposition $M_6(n) \equiv (\exists k_1 \in \mathbb{Z}, n = 6 \cdot k_1)$.
    *   "...$n$ est un multiple de 3." se traduit par la proposition $M_3(n) \equiv (\exists k_2 \in \mathbb{Z}, n = 3 \cdot k_2)$.
    *   La structure "Si A alors B" est une implication $A \implies B$.

    Ainsi, la formalisation de P1 est :
    $$ \text{P1} : \forall n \in \mathbb{Z}, \left( \exists k_1 \in \mathbb{Z}, n = 6 \cdot k_1 \right) \implies \left( \exists k_2 \in \mathbb{Z}, n = 3 \cdot k_2 \right) $$

3.  **Négation formelle :**
    Nous appliquons les règles de négation :
    *   $\neg(\forall x, A(x)) \equiv \exists x, \neg A(x)$
    *   $\neg(P \implies Q) \equiv P \land \neg Q$
    *   $\neg(\exists x, A(x)) \equiv \forall x, \neg A(x)$

    Appliquons ces règles à P1 :
    $$ \neg \text{P1} : \neg \left( \forall n \in \mathbb{Z}, \left( \exists k_1 \in \mathbb{Z}, n = 6 \cdot k_1 \right) \implies \left( \exists k_2 \in \mathbb{Z}, n = 3 \cdot k_2 \right) \right) $$
    En appliquant $\neg(\forall n, \ldots) \equiv \exists n, \neg(\ldots)$ :
    $$ \neg \text{P1} : \exists n \in \mathbb{Z}, \neg \left( \left( \exists k_1 \in \mathbb{Z}, n = 6 \cdot k_1 \right) \implies \left( \exists k_2 \in \mathbb{Z}, n = 3 \cdot k_2 \right) \right) $$
    En appliquant $\neg(P \implies Q) \equiv P \land \neg Q$ :
    $$ \neg \text{P1} : \exists n \in \mathbb{Z}, \left( \exists k_1 \in \mathbb{Z}, n = 6 \cdot k_1 \right) \land \neg \left( \exists k_2 \in \mathbb{Z}, n = 3 \cdot k_2 \right) $$
    En appliquant $\neg(\exists k_2, \ldots) \equiv \forall k_2, \neg(\ldots)$ :
    $$ \neg \text{P1} : \exists n \in \mathbb{Z}, \left( \exists k_1 \in \mathbb{Z}, n = 6 \cdot k_1 \right) \land \left( \forall k_2 \in \mathbb{Z}, n \neq 3 \cdot k_2 \right) $$

4.  **Négation en langage naturel :**
    "Il existe un entier relatif $n$ tel que $n$ est un multiple de 6 et $n$ n'est pas un multiple de 3."
    Ou, de manière plus concise : "Il existe un entier relatif multiple de 6 qui n'est pas un multiple de 3."

5.  **Valeur de vérité et justification :**
    La proposition P1 est **vraie**.

    **Justification :**
    Pour démontrer que P1 est vraie, nous devons montrer que pour tout entier relatif $n$, l'implication "si $n$ est un multiple de 6, alors $n$ est un multiple de 3" est vraie.
    Soit $n$ un entier relatif quelconque.
    Nous considérons l'hypothèse que $n$ est un multiple de 6.
    Par la définition d'un multiple, cela signifie qu'il existe un entier relatif $k_1$ tel que $n = 6 \cdot k_1$.
    Notre objectif est de montrer que $n$ est un multiple de 3, c'est-à-dire qu'il existe un entier relatif $k_2$ tel que $n = 3 \cdot k_2$.
    Reprenons l'expression de $n$ :
    $$ n = 6 \cdot k_1 $$
    Nous pouvons réécrire le produit $6 \cdot k_1$ en utilisant la propriété d'associativité et de commutativité de la multiplication des entiers relatifs :
    $$ n = (3 \cdot 2) \cdot k_1 $$
    $$ n = 3 \cdot (2 \cdot k_1) $$
    Posons $k_2 = 2 \cdot k_1$.
    Puisque $k_1$ est un entier relatif (par hypothèse) et $2$ est un entier relatif, le produit $2 \cdot k_1$ est, par définition de la multiplication dans $\mathbb{Z}$, un entier relatif. Donc, $k_2 \in \mathbb{Z}$.
    Nous avons ainsi montré que $n = 3 \cdot k_2$ avec $k_2 \in \mathbb{Z}$.
    Par la définition d'un multiple, cela signifie que $n$ est un multiple de 3.
    Nous avons donc prouvé que si $n$ est un multiple de 6, alors $n$ est un multiple de 3.
    Puisque ce raisonnement est valable pour tout entier relatif $n$, la proposition P1 est vraie.

---

## Proposition P2 : "Il existe un entier naturel $M$ tel que, pour tout entier naturel $n$ strictement supérieur à $M$, $n$ est un nombre premier."

1.  **Typage des objets :**
    *   La variable $M$ représente un entier naturel. Son domaine est l'ensemble $\mathbb{N}$.
    *   La variable $n$ représente un entier naturel. Son domaine est l'ensemble $\mathbb{N}$.
    *   La relation "$>$" est une relation d'ordre strict sur $\mathbb{N}$.
    *   La propriété "être un nombre premier" est une propriété unaire sur $\mathbb{N}$.

2.  **Formalisation :**
    La proposition P2 peut être décomposée et formalisée comme suit :
    *   "Il existe un entier naturel $M$..." se traduit par $\exists M \in \mathbb{N}$.
    *   "...pour tout entier naturel $n$..." se traduit par $\forall n \in \mathbb{N}$.
    *   "...$n$ strictement supérieur à $M$..." se traduit par la condition $n > M$.
    *   "...$n$ est un nombre premier." se traduit par la proposition $P(n) \equiv (n \text{ est premier})$.
    *   La structure "Si A alors B" est une implication $A \implies B$.

    Ainsi, la formalisation de P2 est :
    $$ \text{P2} : \exists M \in \mathbb{N}, \forall n \in \mathbb{N}, (n > M) \implies (n \text{ est premier}) $$

3.  **Négation formelle :**
    Nous appliquons les règles de négation :
    *   $\neg(\exists x, A(x)) \equiv \forall x, \neg A(x)$
    *   $\neg(\forall x, A(x)) \equiv \exists x, \neg A(x)$
    *   $\neg(P \implies Q) \equiv P \land \neg Q$

    Appliquons ces règles à P2 :
    $$ \neg \text{P2} : \neg \left( \exists M \in \mathbb{N}, \forall n \in \mathbb{N}, (n > M) \implies (n \text{ est premier}) \right) $$
    En appliquant $\neg(\exists M, \ldots) \equiv \forall M, \neg(\ldots)$ :
    $$ \neg \text{P2} : \forall M \in \mathbb{N}, \neg \left( \forall n \in \mathbb{N}, (n > M) \implies (n \text{ est premier}) \right) $$
    En appliquant $\neg(\forall n, \ldots) \equiv \exists n, \neg(\ldots)$ :
    $$ \neg \text{P2} : \forall M \in \mathbb{N}, \exists n \in \mathbb{N}, \neg \left( (n > M) \implies (n \text{ est premier}) \right) $$
    En appliquant $\neg(P \implies Q) \equiv P \land \neg Q$ :
    $$ \neg \text{P2} : \forall M \in \mathbb{N}, \exists n \in \mathbb{N}, (n > M) \land \neg (n \text{ est premier}) $$

4.  **Négation en langage naturel :**
    "Pour tout entier naturel $M$, il existe un entier naturel $n$ strictement supérieur à $M$ tel que $n$ n'est pas un nombre premier."
    Ou, de manière plus concise : "Aussi grand que soit un entier naturel $M$, il existe toujours un entier naturel $n$ plus grand que $M$ qui n'est pas un nombre premier."

5.  **Valeur de vérité et justification :**
    La proposition P2 est **fausse**.

    **Justification :**
    Pour démontrer que P2 est fausse, nous devons montrer que sa négation, $\neg \text{P2}$, est vraie.
    La négation $\neg \text{P2}$ affirme : "Pour tout entier naturel $M$, il existe un entier naturel $n$ tel que $n > M$ et $n$ n'est pas un nombre premier."
    Nous devons donc, pour un entier naturel $M$ quelconque donné, trouver un entier naturel $n$ qui satisfait les deux conditions : $n > M$ et $n$ n'est pas premier.

    Soit $M$ un entier naturel quelconque.
    Considérons l'entier naturel $k = M+2$.
    Puisque $M \in \mathbb{N}$, $M \ge 0$. Par conséquent, $k = M+2 \ge 0+2 = 2$.
    Considérons l'entier naturel $n = k \cdot k = (M+2)^2$.
    Nous devons vérifier les deux conditions pour cet $n$ :
    1.  **Condition $n > M$ :**
        Puisque $k = M+2$ et $M \ge 0$, nous avons $k \ge 2$.
        Donc $n = k^2 \ge 2^2 = 4$.
        Si $M=0$, $n=(0+2)^2=4$. $4 > 0$, la condition est satisfaite.
        Si $M=1$, $n=(1+2)^2=9$. $9 > 1$, la condition est satisfaite.
        Si $M \ge 2$, alors $M+2 > M$. De plus, $M+2 \ge 2$.
        Par conséquent, $(M+2)^2 = (M+2) \cdot (M+2) > M \cdot 1 = M$ (car $M+2 > M$ et $M+2 \ge 2 > 1$).
        Donc, $n = (M+2)^2$ est strictement supérieur à $M$.

    2.  **Condition $n$ n'est pas un nombre premier :**
        Par définition, un nombre premier est un entier naturel $p > 1$ dont les seuls diviseurs positifs sont $1$ et $p$.
        Nous avons $n = (M+2)^2$.
        Puisque $M \ge 0$, $M+2 \ge 2$.
        Les diviseurs positifs de $n=(M+2)^2$ incluent $1$, $M+2$, et $(M+2)^2$.
        Puisque $M+2 \ge 2$, nous avons $M+2 \neq 1$.
        Puisque $M+2 \ge 2$, nous avons $M+2 \neq (M+2)^2$ (car l'équation $x=x^2$ n'a pour solutions que $x=0$ ou $x=1$, et $M+2$ n'est ni 0 ni 1).
        Ainsi, $M+2$ est un diviseur positif de $n$ qui est différent de $1$ et différent de $n$.
        Par conséquent, $n=(M+2)^2$ n'est pas un nombre premier (il est un nombre composé).

    Nous avons donc trouvé, pour un $M$ quelconque, un entier naturel $n = (M+2)^2$ tel que $n > M$ et $n$ n'est pas un nombre premier.
    Puisque ce raisonnement est valable pour tout entier naturel $M$, la négation $\neg \text{P2}$ est vraie.
    Par conséquent, la proposition P2 est fausse.

---

## Proposition P3 : "Pour tout entier relatif $x$, il existe un entier relatif $y$ tel que $x \cdot y = 1$."

1.  **Typage des objets :**
    *   La variable $x$ représente un entier relatif. Son domaine est l'ensemble $\mathbb{Z}$.
    *   La variable $y$ représente un entier relatif. Son domaine est l'ensemble $\mathbb{Z}$.
    *   Le nombre $1$ est un entier relatif constant.
    *   L'opération "$\cdot$" est la multiplication des entiers relatifs.
    *   La relation "$=$" est l'égalité.

2.  **Formalisation :**
    La proposition P3 peut être décomposée et formalisée comme suit :
    *   "Pour tout entier relatif $x$..." se traduit par $\forall x \in \mathbb{Z}$.
    *   "...il existe un entier relatif $y$..." se traduit par $\exists y \in \mathbb{Z}$.
    *   "...tel que $x \cdot y = 1$." est la condition $x \cdot y = 1$.

    Ainsi, la formalisation de P3 est :
    $$ \text{P3} : \forall x \in \mathbb{Z}, \exists y \in \mathbb{Z}, x \cdot y = 1 $$

3.  **Négation formelle :**
    Nous appliquons les règles de négation :
    *   $\neg(\forall x, A(x)) \equiv \exists x, \neg A(x)$
    *   $\neg(\exists x, A(x)) \equiv \forall x, \neg A(x)$

    Appliquons ces règles à P3 :
    $$ \neg \text{P3} : \neg \left( \forall x \in \mathbb{Z}, \exists y \in \mathbb{Z}, x \cdot y = 1 \right) $$
    En appliquant $\neg(\forall x, \ldots) \equiv \exists x, \neg(\ldots)$ :
    $$ \neg \text{P3} : \exists x \in \mathbb{Z}, \neg \left( \exists y \in \mathbb{Z}, x \cdot y = 1 \right) $$
    En appliquant $\neg(\exists y, \ldots) \equiv \forall y, \neg(\ldots)$ :
    $$ \neg \text{P3} : \exists x \in \mathbb{Z}, \forall y \in \mathbb{Z}, x \cdot y \neq 1 $$

4.  **Négation en langage naturel :**
    "Il existe un entier relatif $x$ tel que, pour tout entier relatif $y$, le produit $x \cdot y$ n'est pas égal à 1."
    Ou, de manière plus concise : "Il existe un entier relatif $x$ qui n'a pas d'inverse multiplicatif dans l'ensemble des entiers relatifs."

5.  **Valeur de vérité et justification :**
    La proposition P3 est **fausse**.

    **Justification :**
    Pour démontrer que P3 est fausse, nous devons montrer que sa négation, $\neg \text{P3}$, est vraie.
    La négation $\neg \text{P3}$ affirme : "Il existe un entier relatif $x$ tel que, pour tout entier relatif $y$, $x \cdot y \neq 1$."
    Nous devons donc trouver un entier relatif $x$ spécifique qui satisfait cette condition.

    Considérons l'entier relatif $x = 2$.
    Nous devons montrer que pour cet $x=2$, pour tout entier relatif $y$, le produit $2 \cdot y$ n'est pas égal à $1$.
    Soit $y$ un entier relatif quelconque.
    Nous examinons l'équation $2 \cdot y = 1$.
    Si cette équation avait une solution $y$ dans $\mathbb{Z}$, alors, en divisant par $2$ (ce qui est permis dans $\mathbb{Q}$ ou $\mathbb{R}$), nous obtiendrions $y = \frac{1}{2}$.
    Cependant, l'ensemble des entiers relatifs $\mathbb{Z}$ est défini comme $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$. Le nombre $\frac{1}{2}$ n'est pas un élément de cet ensemble.
    Par conséquent, il n'existe aucun entier relatif $y$ tel que $2 \cdot y = 1$.
    Ainsi, pour l'entier relatif $x=2$, la condition "pour tout entier relatif $y$, $x \cdot y \neq 1$" est satisfaite.
    Nous avons trouvé un entier relatif $x$ (à savoir $x=2$) pour lequel il n'existe pas d'entier relatif $y$ tel que $x \cdot y = 1$.
    Par conséquent, la négation $\neg \text{P3}$ est vraie.
    Donc, la proposition P3 est fausse.

---