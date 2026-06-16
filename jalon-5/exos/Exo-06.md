# Exercice 6/10 : Construction d'une bijection entre $\mathbb{N}$ et $\mathbb{Z}$

**Jalon 5 : Applications, injections, surjections, bijections et composition de fonctions**

**Niveau de difficulté :** ★★★☆☆

---

## Énoncé

Soient les ensembles $\mathbb{N} = \{0, 1, 2, 3, \dots\}$ l'ensemble des nombres entiers naturels et $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$ l'ensemble des nombres entiers relatifs.

1.  Construire explicitement une fonction $f: \mathbb{N} \to \mathbb{Z}$.
2.  Démontrer rigoureusement que la fonction $f$ ainsi construite est une bijection.

---

## Analyse de l'énoncé

L'objectif de cet exercice est de démontrer l'équipotence des ensembles $\mathbb{N}$ et $\mathbb{Z}$ en construisant une bijection explicite entre eux. Bien que l'on sache intuitivement que ces deux ensembles sont "infinis", la notion d'équipotence pour les ensembles infinis est plus subtile et nécessite la construction d'une fonction qui soit à la fois injective et surjective.

**1. Construction explicite de $f: \mathbb{N} \to \mathbb{Z}$ :**
Nous devons trouver une règle qui associe à chaque entier naturel $n$ un unique entier relatif $f(n)$, de telle sorte que tous les entiers relatifs soient atteints et qu'aucun ne soit atteint plus d'une fois.
Une stratégie courante pour construire une bijection entre $\mathbb{N}$ et $\mathbb{Z}$ est de "zigzaguer" entre les entiers positifs (y compris zéro) et les entiers négatifs.
Par exemple :
*   $0 \mapsto 0$
*   $1 \mapsto -1$
*   $2 \mapsto 1$
*   $3 \mapsto -2$
*   $4 \mapsto 2$
*   $5 \mapsto -3$
etc.

Cette observation suggère une distinction basée sur la parité de $n$:
*   Si $n$ est pair, $n = 2k$ pour un certain $k \in \mathbb{N}$, alors $f(n)$ devrait être un entier non-négatif. En observant la séquence, $f(0)=0$, $f(2)=1$, $f(4)=2$, on voit que $f(2k) = k$.
*   Si $n$ est impair, $n = 2k+1$ pour un certain $k \in \mathbb{N}$, alors $f(n)$ devrait être un entier négatif. En observant la séquence, $f(1)=-1$, $f(3)=-2$, $f(5)=-3$, on voit que $f(2k+1) = -(k+1)$.

Nous allons formaliser cette fonction par morceaux.

**2. Démonstration de la bijectivité :**
Pour prouver que $f$ est une bijection, nous devons démontrer deux propriétés :
*   **Injectivité (ou injection) :** Pour tous $n_1, n_2 \in \mathbb{N}$, si $f(n_1) = f(n_2)$, alors $n_1 = n_2$. Cela signifie que deux éléments distincts de $\mathbb{N}$ ne peuvent pas avoir la même image dans $\mathbb{Z}$.
*   **Surjectivité (ou surjection) :** Pour tout $z \in \mathbb{Z}$, il existe au moins un $n \in \mathbb{N}$ tel que $f(n) = z$. Cela signifie que chaque élément de $\mathbb{Z}$ est l'image d'au moins un élément de $\mathbb{N}$.

La preuve de l'injectivité et de la surjectivité nécessitera une analyse par cas, en fonction de la parité de $n$ pour l'injectivité, et du signe de $z$ pour la surjectivité.

---

## Correction exhaustive pas-à-pas

### 1. Construction explicite de la fonction $f: \mathbb{N} \to \mathbb{Z}$

Nous proposons la fonction $f$ définie par :
$$ f(n) = \begin{cases} \frac{n}{2} & \text{si } n \text{ est pair} \\ -\frac{n+1}{2} & \text{si } n \text{ est impair} \end{cases} $$

Vérifions quelques valeurs pour s'assurer de la cohérence avec la stratégie de "zigzag" :
*   Pour $n=0$ (pair) : $f(0) = \frac{0}{2} = 0$.
*   Pour $n=1$ (impair) : $f(1) = -\frac{1+1}{2} = -\frac{2}{2} = -1$.
*   Pour $n=2$ (pair) : $f(2) = \frac{2}{2} = 1$.
*   Pour $n=3$ (impair) : $f(3) = -\frac{3+1}{2} = -\frac{4}{2} = -2$.
*   Pour $n=4$ (pair) : $f(4) = \frac{4}{2} = 2$.

La fonction semble correcte et correspond à notre intuition.

### 2. Démonstration que $f$ est une bijection

Pour prouver que $f$ est une bijection, nous devons montrer qu'elle est injective et surjective.

#### a) Preuve de l'injectivité

Soient $n_1, n_2 \in \mathbb{N}$ tels que $f(n_1) = f(n_2)$. Nous devons montrer que $n_1 = n_2$.
Soit $z = f(n_1) = f(n_2)$.

Observons les images de $f$ en fonction de la parité de $n$:
*   Si $n$ est pair, $n=2k$ pour un $k \in \mathbb{N}$, alors $f(n) = k$. Les images sont $\{0, 1, 2, \dots\} = \mathbb{N}$.
*   Si $n$ est impair, $n=2k+1$ pour un $k \in \mathbb{N}$, alors $f(n) = -(k+1)$. Les images sont $\{-1, -2, -3, \dots\} = \mathbb{Z}^-$.

Les ensembles d'images pour les $n$ pairs ($\mathbb{N}$) et les $n$ impairs ($\mathbb{Z}^-$) sont disjoints. En effet, $\mathbb{N} \cap \mathbb{Z}^- = \emptyset$.
Par conséquent, si $f(n_1) = f(n_2)$, alors $f(n_1)$ et $f(n_2)$ doivent nécessairement appartenir au même sous-ensemble d'images. Cela implique que $n_1$ et $n_2$ doivent avoir la même parité.

Nous considérons deux cas :

**Cas 1 : $n_1$ et $n_2$ sont tous les deux pairs.**
Soient $n_1 = 2k_1$ et $n_2 = 2k_2$ pour certains $k_1, k_2 \in \mathbb{N}$.
Alors $f(n_1) = \frac{n_1}{2} = \frac{2k_1}{2} = k_1$.
Et $f(n_2) = \frac{n_2}{2} = \frac{2k_2}{2} = k_2$.
Puisque $f(n_1) = f(n_2)$, nous avons $k_1 = k_2$.
En multipliant par 2, nous obtenons $2k_1 = 2k_2$, ce qui signifie $n_1 = n_2$.

**Cas 2 : $n_1$ et $n_2$ sont tous les deux impairs.**
Soient $n_1 = 2k_1+1$ et $n_2 = 2k_2+1$ pour certains $k_1, k_2 \in \mathbb{N}$.
Alors $f(n_1) = -\frac{n_1+1}{2} = -\frac{(2k_1+1)+1}{2} = -\frac{2k_1+2}{2} = -(k_1+1)$.
Et $f(n_2) = -\frac{n_2+1}{2} = -\frac{(2k_2+1)+1}{2} = -\frac{2k_2+2}{2} = -(k_2+1)$.
Puisque $f(n_1) = f(n_2)$, nous avons $-(k_1+1) = -(k_2+1)$.
En multipliant par $-1$, nous obtenons $k_1+1 = k_2+1$.
En soustrayant 1, nous obtenons $k_1 = k_2$.
En multipliant par 2 et en ajoutant 1, nous obtenons $2k_1+1 = 2k_2+1$, ce qui signifie $n_1 = n_2$.

Dans tous les cas possibles où $f(n_1) = f(n_2)$, nous avons montré que $n_1 = n_2$.
Par conséquent, la fonction $f$ est injective.

#### b) Preuve de la surjectivité

Soit $z \in \mathbb{Z}$. Nous devons trouver un $n \in \mathbb{N}$ tel que $f(n) = z$.
Nous considérons deux cas pour $z$:

**Cas 1 : $z \ge 0$.** (C'est-à-dire $z \in \mathbb{N}$)
Nous cherchons un $n \in \mathbb{N}$ tel que $f(n) = z$.
Puisque $z \ge 0$, l'image $z$ doit provenir d'un $n$ pair, selon la définition de $f$.
Nous posons donc $f(n) = \frac{n}{2}$.
Pour que $\frac{n}{2} = z$, il faut que $n = 2z$.
Vérifions que ce $n$ est valide :
*   Puisque $z \in \mathbb{N}$, $z \ge 0$. Donc $2z \ge 0$. Ainsi $n = 2z \in \mathbb{N}$.
*   Puisque $n = 2z$, $n$ est un nombre pair.
*   En appliquant $f$ à ce $n$: $f(n) = f(2z) = \frac{2z}{2} = z$.
Nous avons bien trouvé un $n \in \mathbb{N}$ (en l'occurrence $n=2z$) tel que $f(n)=z$ pour tout $z \in \mathbb{N}$.

**Cas 2 : $z < 0$.** (C'est-à-dire $z \in \mathbb{Z}^-$)
Nous cherchons un $n \in \mathbb{N}$ tel que $f(n) = z$.
Puisque $z < 0$, l'image $z$ doit provenir d'un $n$ impair, selon la définition de $f$.
Nous posons donc $f(n) = -\frac{n+1}{2}$.
Pour que $-\frac{n+1}{2} = z$, nous résolvons pour $n$:
$-\frac{n+1}{2} = z$
$\frac{n+1}{2} = -z$
$n+1 = -2z$
$n = -2z-1$.
Vérifions que ce $n$ est valide :
*   Puisque $z \in \mathbb{Z}^-$, $z \le -1$.
*   Alors $-z \ge 1$.
*   Donc $-2z \ge 2$.
*   Par conséquent, $n = -2z-1 \ge 2-1 = 1$.
*   Ainsi $n = -2z-1 \in \mathbb{N}$ (c'est un entier naturel strictement positif).
*   Puisque $n = -2z-1$, $n$ est de la forme $2(\text{entier})+1$ (car $-2z$ est pair, donc $-2z-1$ est impair). Donc $n$ est un nombre impair.
*   En appliquant $f$ à ce $n$: $f(n) = f(-2z-1) = -\frac{(-2z-1)+1}{2} = -\frac{-2z}{2} = -(-z) = z$.
Nous avons bien trouvé un $n \in \mathbb{N}$ (en l'occurrence $n=-2z-1$) tel que $f(n)=z$ pour tout $z \in \mathbb{Z}^-$.

Dans tous les cas, pour tout $z \in \mathbb{Z}$, nous avons trouvé un $n \in \mathbb{N}$ tel que $f(n)=z$.
Par conséquent, la fonction $f$ est surjective.

#### c) Conclusion

Puisque la fonction $f: \mathbb{N} \to \mathbb{Z}$ est à la fois injective et surjective, elle est une bijection.
Ceci démontre que les ensembles $\mathbb{N}$ et $\mathbb{Z}$ ont la même cardinalité, c'est-à-dire qu'ils sont équipotents.

---

## Liens avec l'Intelligence Artificielle

La construction d'une bijection entre $\mathbb{N}$ et $\mathbb{Z}$ est un concept fondamental en mathématiques discrètes et en théorie de la calculabilité, qui sont des piliers théoriques de l'Intelligence Artificielle.

1.  **Numérisation et Encodage des Données :** En IA, de nombreuses données sont de nature discrète (catégories, mots, symboles). Pour qu'un algorithme puisse les traiter, elles doivent souvent être converties en représentations numériques. Une bijection comme celle-ci illustre le principe d'encodage : chaque élément d'un ensemble (ici $\mathbb{Z}$) peut être mappé de manière unique et réversible à un élément d'un autre ensemble (ici $\mathbb{N}$). En PNL (Traitement du Langage Naturel), par exemple, les mots d'un vocabulaire sont souvent encodés en entiers (indices), et des techniques plus avancées comme le "word embedding" construisent des vecteurs numériques pour chaque mot. La capacité de passer d'une représentation à l'autre sans perte d'information est cruciale.

2.  **Théorie de la Calculabilité et Limites de l'IA :** La démonstration que $\mathbb{N}$ et $\mathbb{Z}$ sont équipotents est un exemple simple de la notion de "dénombrabilité". La théorie de la calculabilité, développée par des figures comme Alan Turing, repose sur l'idée que tout ce qui est "calculable" par un algorithme peut être représenté par des opérations sur des nombres naturels. L'ensemble de tous les programmes informatiques possibles est dénombrable (on peut les énumérer avec des entiers naturels). Comprendre les propriétés des ensembles dénombrables et non dénombrables (comme $\mathbb{R}$) est essentiel pour définir les limites théoriques de ce que les ordinateurs et, par extension, les systèmes d'IA peuvent accomplir. Par exemple, le problème de l'arrêt de Turing démontre qu'il n'existe pas d'algorithme général pour déterminer si un programme donné se terminera ou non, une limitation fondamentale qui s'applique à toute IA.

3.  **Structures de Données et Hachage :** Bien que la bijection entre $\mathbb{N}$ et $\mathbb{Z}$ soit un cas spécifique, le principe de mappage unique est lié aux fonctions de hachage utilisées dans les structures de données (tables de hachage) qui sont omniprésentes en IA pour l'efficacité. Une fonction de hachage tente de mapper des données d'entrée de taille arbitraire à une valeur de hachage de taille fixe (souvent un entier). Bien que les fonctions de hachage ne soient pas des bijections (des collisions peuvent se produire), l'objectif est de s'en rapprocher le plus possible pour garantir une distribution uniforme et des recherches rapides, ce qui est vital pour la performance des algorithmes d'apprentissage automatique et des bases de données utilisées par l'IA.

4.  **Numérotation de Gödel :** Un exemple plus avancé de bijection entre des objets complexes et les nombres naturels est la numérotation de Gödel. Cette technique attribue un nombre naturel unique à chaque formule et preuve dans un système formel. Cela permet de traduire des énoncés sur les propriétés des systèmes formels en énoncés sur les propriétés des nombres naturels, ce qui a conduit aux célèbres théorèmes d'incomplétude de Gödel. Ces théorèmes ont des implications profondes pour la logique, les fondements des mathématiques et, indirectement, pour la compréhension des limites de la raisonnement formel et de l'intelligence artificielle symbolique.
