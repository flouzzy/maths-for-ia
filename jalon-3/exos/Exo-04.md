En tant que Professeur de Mathématiques à l'ENS, je vous propose l'exercice suivant pour approfondir votre maîtrise de la quantification.

---

### **Exercice 4 (Jalon 3 : Quantification, ordre des quantificateurs, négation)**

**Niveau de difficulté :** $\star \star \rule{0pt}{10pt}$

Soit $E$ l'ensemble des entiers naturels non nuls, c'est-à-dire $E = \mathbb{N}^* = \{1, 2, 3, \ldots\}$.
On considère le prédicat binaire $P(x, y)$ défini pour tout couple $(x, y) \in E \times E$ par :
$$ P(x, y) \iff (x+y \text{ est un nombre pair}) $$
Nous nous intéressons aux deux propositions suivantes, qui diffèrent par l'ordre de leurs quantificateurs :
$$ (S_1) : \forall x \in E, \exists y \in E, P(x, y) $$
$$ (S_2) : \exists y \in E, \forall x \in E, P(x, y) $$

1.  Écrire la négation de la proposition $(S_1)$, notée $\neg (S_1)$, et la négation de la proposition $(S_2)$, notée $\neg (S_2)$, en utilisant les quantificateurs.
2.  Déterminer la valeur de vérité de la proposition $(S_1)$ (est-elle vraie ou fausse ?) et la prouver rigoureusement.
3.  Déterminer la valeur de vérité de la proposition $(S_2)$ (est-elle vraie ou fausse ?) et la prouver rigoureusement.

---

### **Correction de l'Exercice 4**

**Typage strict des objets mathématiques :**
*   $E$ est un ensemble, spécifiquement l'ensemble des entiers naturels non nuls, $E = \mathbb{N}^*$.
*   $x$ est une variable muette, représentant un élément de l'ensemble $E$.
*   $y$ est une variable muette, représentant un élément de l'ensemble $E$.
*   $P(x, y)$ est un prédicat binaire, qui prend deux éléments de $E$ et renvoie une valeur de vérité (Vrai ou Faux). Sa définition est $P(x, y) \iff (x+y \text{ est un nombre pair})$.
*   $(S_1)$ et $(S_2)$ sont des propositions, c'est-à-dire des énoncés mathématiques qui sont soit vrais, soit faux, mais pas les deux.
*   $\neg (S_1)$ et $\neg (S_2)$ sont les négations des propositions $(S_1)$ et $(S_2)$, respectivement.

**Rappel sur la parité des entiers :**
*   Un entier $n$ est dit **pair** si et seulement si il existe un entier $k \in \mathbb{Z}$ tel que $n = 2k$.
*   Un entier $n$ est dit **impair** si et seulement si il existe un entier $k \in \mathbb{Z}$ tel que $n = 2k+1$.
*   Les propriétés de la parité des sommes sont les suivantes :
    *   (pair) + (pair) = (pair)
    *   (impair) + (impair) = (pair)
    *   (pair) + (impair) = (impair)
    *   (impair) + (pair) = (impair)

---

#### **1. Négation des propositions $(S_1)$ et $(S_2)$**

Pour nier une proposition quantifiée, on applique les règles de négation des quantificateurs :
*   La négation de $\forall \text{ est } \exists \neg$. Plus précisément, $\neg (\forall z \in A, Q(z))$ est équivalent à $\exists z \in A, \neg Q(z)$.
*   La négation de $\exists \text{ est } \forall \neg$. Plus précisément, $\neg (\exists z \in A, Q(z))$ est équivalent à $\forall z \in A, \neg Q(z)$.

De plus, la négation du prédicat $P(x, y)$ est $\neg P(x, y) \iff \neg (x+y \text{ est un nombre pair}) \iff (x+y \text{ est un nombre impair})$.

**Négation de $(S_1)$ :**
La proposition $(S_1)$ est : $\forall x \in E, \exists y \in E, P(x, y)$.
1.  On applique la règle de négation au premier quantificateur ($\forall x$ devient $\exists x \neg$) :
    $\neg (S_1) \iff \exists x \in E, \neg (\exists y \in E, P(x, y))$.
2.  On applique la règle de négation au second quantificateur ($\exists y$ devient $\forall y \neg$) :
    $\neg (\exists y \in E, P(x, y)) \iff \forall y \in E, \neg P(x, y)$.
3.  En substituant ce résultat dans l'expression de $\neg (S_1)$ et en utilisant la définition de $\neg P(x, y)$ :
    $$ \neg (S_1) : \exists x \in E, \forall y \in E, (x+y \text{ est un nombre impair}) $$

**Négation de $(S_2)$ :**
La proposition $(S_2)$ est : $\exists y \in E, \forall x \in E, P(x, y)$.
1.  On applique la règle de négation au premier quantificateur ($\exists y$ devient $\forall y \neg$) :
    $\neg (S_2) \iff \forall y \in E, \neg (\forall x \in E, P(x, y))$.
2.  On applique la règle de négation au second quantificateur ($\forall x$ devient $\exists x \neg$) :
    $\neg (\forall x \in E, P(x, y)) \iff \exists x \in E, \neg P(x, y)$.
3.  En substituant ce résultat dans l'expression de $\neg (S_2)$ et en utilisant la définition de $\neg P(x, y)$ :
    $$ \neg (S_2) : \forall y \in E, \exists x \in E, (x+y \text{ est un nombre impair}) $$

---

#### **2. Détermination de la valeur de vérité de $(S_1)$ et preuve**

La proposition $(S_1)$ est : $\forall x \in E, \exists y \in E, (x+y \text{ est un nombre pair})$.

**Valeur de vérité :** La proposition $(S_1)$ est **vraie**.

**Preuve rigoureuse :**
Pour prouver que $(S_1)$ est vraie, nous devons démontrer que pour tout élément $x$ de l'ensemble $E = \mathbb{N}^*$, il est possible de trouver au moins un élément $y$ de l'ensemble $E$ tel que la somme $x+y$ soit un nombre pair.

Soit $x$ un élément arbitraire mais fixé de l'ensemble $E = \mathbb{N}^*$.
Nous devons exhiber un $y \in E$ tel que $x+y$ soit pair. La stratégie consiste à choisir $y$ en fonction de la parité de $x$.

**Cas 1 : $x$ est un nombre pair.**
*   Si $x$ est pair, alors par définition, il existe un entier $k_x \in \mathbb{N}^*$ tel que $x = 2k_x$. (Puisque $x \in E = \mathbb{N}^*$, $x \ge 1$. Si $x$ est pair, le plus petit $x$ possible est $2$, donc $k_x \ge 1$).
*   Nous cherchons un $y \in E$ tel que $x+y$ soit pair.
*   D'après les propriétés de la parité, la somme de deux nombres pairs est un nombre pair.
*   Choisissons $y = 2$. L'entier $2$ est un élément de $E = \mathbb{N}^*$.
*   Alors la somme $x+y = x+2$. Puisque $x$ est pair et $2$ est pair, leur somme $x+2$ est un nombre pair.
*   Ainsi, dans ce cas (lorsque $x$ est pair), nous avons trouvé un $y \in E$ (spécifiquement $y=2$) tel que $x+y$ est pair.

**Cas 2 : $x$ est un nombre impair.**
*   Si $x$ est impair, alors par définition, il existe un entier $k_x \in \mathbb{N}$ tel que $x = 2k_x+1$. (Puisque $x \in E = \mathbb{N}^*$, $x \ge 1$. Si $x$ est impair, le plus petit $x$ possible est $1$, ce qui correspond à $k_x=0$).
*   Nous cherchons un $y \in E$ tel que $x+y$ soit pair.
*   D'après les propriétés de la parité, la somme de deux nombres impairs est un nombre pair.
*   Choisissons $y = 1$. L'entier $1$ est un élément de $E = \mathbb{N}^*$.
*   Alors la somme $x+y = x+1$. Puisque $x$ est impair et $1$ est impair, leur somme $x+1$ est un nombre pair.
*   Ainsi, dans ce cas (lorsque $x$ est impair), nous avons trouvé un $y \in E$ (spécifiquement $y=1$) tel que $x+y$ est pair.

Dans les deux cas possibles pour la parité de $x$, nous avons réussi à exhiber un élément $y \in E$ tel que $x+y$ soit pair.
Puisque $x$ a été choisi comme un élément arbitraire de $E$, cette démonstration est valable pour tout $x \in E$.
Par conséquent, la proposition $(S_1)$ est vraie.

---

#### **3. Détermination de la valeur de vérité de $(S_2)$ et preuve**

La proposition $(S_2)$ est : $\exists y \in E, \forall x \in E, (x+y \text{ est un nombre pair})$.

**Valeur de vérité :** La proposition $(S_2)$ est **fausse**.

**Preuve rigoureuse :**
Pour prouver que $(S_2)$ est fausse, il est équivalent de prouver que sa négation $\neg (S_2)$ est vraie.
La négation de $(S_2)$ est : $\forall y \in E, \exists x \in E, (x+y \text{ est un nombre impair})$.

Nous devons démontrer que pour tout élément $y$ de l'ensemble $E = \mathbb{N}^*$, il est possible de trouver au moins un élément $x$ de l'ensemble $E$ tel que la somme $x+y$ soit un nombre impair.

Soit $y$ un élément arbitraire mais fixé de l'ensemble $E = \mathbb{N}^*$.
Nous devons exhiber un $x \in E$ tel que $x+y$ soit impair. La stratégie consiste à choisir $x$ en fonction de la parité de $y$.

**Cas 1 : $y$ est un nombre pair.**
*   Si $y$ est pair, alors par définition, il existe un entier $k_y \in \mathbb{N}^*$ tel que $y = 2k_y$. (Puisque $y \in E = \mathbb{N}^*$, $y \ge 1$. Si $y$ est pair, le plus petit $y$ possible est $2$, donc $k_y \ge 1$).
*   Nous cherchons un $x \in E$ tel que $x+y$ soit impair.
*   D'après les propriétés de la parité, la somme d'un nombre impair et d'un nombre pair est un nombre impair.
*   Choisissons $x = 1$. L'entier $1$ est un élément de $E = \mathbb{N}^*$.
*   Alors la somme $x+y = 1+y$. Puisque $1$ est impair et $y$ est pair, leur somme $1+y$ est un nombre impair.
*   Ainsi, dans ce cas (lorsque $y$ est pair), nous avons trouvé un $x \in E$ (spécifiquement $x=1$) tel que $x+y$ est impair.

**Cas 2 : $y$ est un nombre impair.**
*   Si $y$ est impair, alors par définition, il existe un entier $k_y \in \mathbb{N}$ tel que $y = 2k_y+1$. (Puisque $y \in E = \mathbb{N}^*$, $y \ge 1$. Si $y$ est impair, le plus petit $y$ possible est $1$, ce qui correspond à $k_y=0$).
*   Nous cherchons un $x \in E$ tel que $x+y$ soit impair.
*   D'après les propriétés de la parité, la somme d'un nombre pair et d'un nombre impair est un nombre impair.
*   Choisissons $x = 2$. L'entier $2$ est un élément de $E = \mathbb{N}^*$.
*   Alors la somme $x+y = 2+y$. Puisque $2$ est pair et $y$ est impair, leur somme $2+y$ est un nombre impair.
*   Ainsi, dans ce cas (lorsque $y$ est impair), nous avons trouvé un $x \in E$ (spécifiquement $x=2$) tel que $x+y$ est impair.

Dans les deux cas possibles pour la parité de $y$, nous avons réussi à exhiber un élément $x \in E$ tel que $x+y$ soit impair.
Puisque $y$ a été choisi comme un élément arbitraire de $E$, cette démonstration est valable pour tout $y \in E$.
Par conséquent, la proposition $\neg (S_2)$ est vraie.
Puisque la négation de $(S_2)$ est vraie, la proposition $(S_2)$ elle-même est fausse.

---

**Conclusion sur l'ordre des quantificateurs :**
Cet exercice met en lumière de manière concrète l'importance cruciale de l'ordre des quantificateurs dans une proposition logique.
*   La proposition $(S_1)$ s'interprète comme : "Pour chaque $x$, il est possible de trouver un $y$ (qui peut dépendre de $x$) tel que la propriété $P(x,y)$ soit vérifiée." Dans notre cas, pour chaque $x$, nous avons pu choisir un $y$ approprié (par exemple, $y=1$ si $x$ est impair, $y=2$ si $x$ est pair) pour rendre $x+y$ pair. C'est pourquoi $(S_1)$ est vraie.
*   La proposition $(S_2)$ s'interprète comme : "Il existe un unique $y$ (un "champion" universel, indépendant de $x$) tel que pour tout $x$, la propriété $P(x,y)$ soit vérifiée." Dans notre cas, nous avons montré qu'un tel $y$ n'existe pas. Si $y$ est pair, il ne peut pas rendre $x+y$ pair pour tous les $x$ (par exemple, $x=1$ rendrait $1+y$ impair). Si $y$ est impair, il ne peut pas rendre $x+y$ pair pour tous les $x$ (par exemple, $x=2$ rendrait $2+y$ impair). C'est pourquoi $(S_2)$ est fausse.

L'inversion de l'ordre des quantificateurs $\forall x \exists y$ et $\exists y \forall x$ change radicalement le sens de la proposition et, comme démontré ici, peut modifier sa valeur de vérité.