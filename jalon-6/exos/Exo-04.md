# Exercice 4 : Relation d'équivalence sur les paires d'entiers et construction des nombres rationnels
**Difficulté :** ⭐⭐

## Énoncé
Soit l'ensemble $E = \mathbb{Z} \times \mathbb{Z}^*$, où $\mathbb{Z}^* = \mathbb{Z} \setminus \{0\}$ désigne l'ensemble des entiers relatifs non nuls.
On définit sur $E$ la relation $\mathcal{R}$ suivante :
Pour tout $(a,b) \in E$ et tout $(c,d) \in E$,
$$ (a,b) \mathcal{R} (c,d) \iff ad = bc $$

1.  Démontrer que $\mathcal{R}$ est une relation d'équivalence sur $E$.
2.  Déterminer l'ensemble des éléments de la classe d'équivalence de $(1,2)$, notée $[(1,2)]$.
3.  Décrire l'ensemble quotient $E/\mathcal{R}$ et l'identifier à une structure algébrique connue. Justifier votre réponse de manière rigoureuse.

## Correction Détaillée

Nous allons démontrer point par point que la relation $\mathcal{R}$ définie sur $E = \mathbb{Z} \times \mathbb{Z}^*$ est une relation d'équivalence, puis nous décrirons la classe d'équivalence demandée et l'ensemble quotient.

### 1. Démonstration que $\mathcal{R}$ est une relation d'équivalence sur $E$

Pour qu'une relation soit une relation d'équivalence, elle doit satisfaire trois propriétés fondamentales : la réflexivité, la symétrie et la transitivité.

#### 1.1. Réflexivité
Une relation $\mathcal{R}$ est réflexive si, pour tout élément $X \in E$, on a $X \mathcal{R} X$.
Soit $(a,b)$ un élément arbitraire de l'ensemble $E$.
Par définition de l'ensemble $E$, nous avons $a \in \mathbb{Z}$ et $b \in \mathbb{Z}^*$ (c'est-à-dire $b$ est un entier non nul).
Pour vérifier la réflexivité, nous devons montrer que $(a,b) \mathcal{R} (a,b)$.
Selon la définition de la relation $\mathcal{R}$, cette condition équivaut à vérifier l'égalité suivante :
$$ a \cdot b = b \cdot a $$
Dans l'anneau des entiers relatifs $(\mathbb{Z}, +, \times)$, la multiplication est une opération commutative.
Par conséquent, l'égalité $a \cdot b = b \cdot a$ est toujours vérifiée pour tous les entiers $a$ et $b$.
Ainsi, pour tout $(a,b) \in E$, nous avons $(a,b) \mathcal{R} (a,b)$.
La relation $\mathcal{R}$ est donc réflexive sur $E$.

#### 1.2. Symétrie
Une relation $\mathcal{R}$ est symétrique si, pour tout $X, Y \in E$, si $X \mathcal{R} Y$, alors $Y \mathcal{R} X$.
Soient $(a,b)$ et $(c,d)$ deux éléments arbitraires de l'ensemble $E$.
Par définition de $E$, nous avons $a, c \in \mathbb{Z}$ et $b, d \in \mathbb{Z}^*$.
Supposons que $(a,b) \mathcal{R} (c,d)$.
Selon la définition de la relation $\mathcal{R}$, cette supposition signifie que l'égalité suivante est vraie :
$$ ad = bc \quad \text{(Équation S1)} $$
Nous devons montrer que $(c,d) \mathcal{R} (a,b)$.
Selon la définition de $\mathcal{R}$, cela signifie que nous devons montrer l'égalité $cb = da$.
Puisque l'égalité est une relation symétrique, l'Équation S1 ($ad = bc$) peut être réécrite comme $bc = ad$.
De plus, la multiplication dans $\mathbb{Z}$ est commutative.
Par conséquent, $bc$ peut être écrit comme $cb$, et $ad$ peut être écrit comme $da$.
En substituant ces formes commutées dans $bc = ad$, nous obtenons :
$$ cb = da $$
Cette dernière égalité est précisément la condition pour que $(c,d) \mathcal{R} (a,b)$.
La relation $\mathcal{R}$ est donc symétrique sur $E$.

#### 1.3. Transitivité
Une relation $\mathcal{R}$ est transitive si, pour tout $X, Y, Z \in E$, si $X \mathcal{R} Y$ et $Y \mathcal{R} Z$, alors $X \mathcal{R} Z$.
Soient $(a,b)$, $(c,d)$ et $(e,f)$ trois éléments arbitraires de l'ensemble $E$.
Par définition de $E$, nous avons $a, c, e \in \mathbb{Z}$ et $b, d, f \in \mathbb{Z}^*$.
Supposons que $(a,b) \mathcal{R} (c,d)$ et $(c,d) \mathcal{R} (e,f)$.
D'après la définition de la relation $\mathcal{R}$ :
1.  La condition $(a,b) \mathcal{R} (c,d)$ signifie que $ad = bc$ (Équation T1).
2.  La condition $(c,d) \mathcal{R} (e,f)$ signifie que $cf = de$ (Équation T2).
Nous devons montrer que $(a,b) \mathcal{R} (e,f)$, ce qui, par définition de $\mathcal{R}$, signifie que $af = be$.

Puisque $f \in \mathbb{Z}^*$ (par définition de $E$, $f$ est un entier non nul), nous pouvons multiplier les deux membres de l'Équation T1 par $f$ :
$$ (ad)f = (bc)f $$
$$ adf = bcf \quad \text{(Équation T3)} $$
Puisque $b \in \mathbb{Z}^*$ (par définition de $E$, $b$ est un entier non nul), nous pouvons multiplier les deux membres de l'Équation T2 par $b$ :
$$ (cf)b = (de)b $$
$$ bcf = bde \quad \text{(Équation T4)} $$
En combinant l'Équation T3 et l'Équation T4 (par la transitivité de l'égalité), nous obtenons :
$$ adf = bde $$
Nous voulons obtenir l'égalité $af = be$. Nous avons l'égalité $adf = bde$.
Puisque la multiplication est associative et commutative dans $\mathbb{Z}$, nous pouvons réécrire cette égalité comme :
$$ (af)d = (be)d $$
Nous savons que $d \in \mathbb{Z}^*$ (par définition de $E$, $d$ est un entier non nul).
L'anneau des entiers relatifs $(\mathbb{Z}, +, \times)$ est un anneau intègre, ce qui signifie qu'il ne possède pas de diviseurs de zéro (si un produit $xy=0$, alors $x=0$ ou $y=0$). Une propriété des anneaux intègres est la simplification par un élément non nul : si $X \cdot Z = Y \cdot Z$ et $Z \neq 0$, alors $X=Y$.
Appliquons cette propriété à notre égalité $(af)d = (be)d$. Puisque $d \neq 0$, nous pouvons simplifier par $d$.
Par conséquent, nous concluons que :
$$ af = be $$
Cette dernière égalité est précisément la condition pour que $(a,b) \mathcal{R} (e,f)$.
La relation $\mathcal{R}$ est donc transitive sur $E$.

Puisque la relation $\mathcal{R}$ est réflexive, symétrique et transitive, elle est une relation d'équivalence sur $E$.

### 2. Détermination de la classe d'équivalence de $(1,2)$

La classe d'équivalence de $(1,2)$, notée $[(1,2)]$, est définie comme l'ensemble de tous les éléments $(x,y) \in E$ qui sont en relation avec $(1,2)$.
Formellement :
$$ [(1,2)] = \{ (x,y) \in E \mid (x,y) \mathcal{R} (1,2) \} $$
Utilisons la définition de la relation $\mathcal{R}$ pour expliciter la condition $(x,y) \mathcal{R} (1,2)$ :
$$ (x,y) \mathcal{R} (1,2) \iff x \cdot 2 = y \cdot 1 $$
$$ \iff 2x = y $$
L'ensemble $E$ est $\mathbb{Z} \times \mathbb{Z}^*$. Cela signifie que pour tout $(x,y) \in E$, $x$ doit être un entier relatif ($x \in \mathbb{Z}$) et $y$ doit être un entier relatif non nul ($y \in \mathbb{Z}^*$).
Si $y = 2x$, alors la condition $y \in \mathbb{Z}^*$ implique que $2x \neq 0$.
Puisque $2 \neq 0$, cela signifie que $x$ doit être non nul ($x \in \mathbb{Z}^*$).
Ainsi, la classe d'équivalence de $(1,2)$ peut être décrite comme :
$$ [(1,2)] = \{ (x,y) \in \mathbb{Z} \times \mathbb{Z}^* \mid y = 2x \} $$
En substituant $y$ par $2x$ et en incluant la condition sur $x$ :
$$ [(1,2)] = \{ (x, 2x) \mid x \in \mathbb{Z}^* \} $$
Quelques exemples d'éléments appartenant à cette classe d'équivalence sont :
*   Pour $x=1$, le couple $(1, 2 \cdot 1) = (1,2)$.
*   Pour $x=2$, le couple $(2, 2 \cdot 2) = (2,4)$.
*   Pour $x=-3$, le couple $(-3, 2 \cdot (-3)) = (-3,-6)$.
Chacun de ces couples représente conceptuellement la fraction $\frac{1}{2}$.

### 3. Description de l'ensemble quotient $E/\mathcal{R}$ et identification à une structure algébrique

L'ensemble quotient $E/\mathcal{R}$ est l'ensemble de toutes les classes d'équivalence de la relation $\mathcal{R}$ sur $E$. Chaque classe d'équivalence est de la forme $[(a,b)]$ pour un certain $(a,b) \in E$.
Par définition, $[(a,b)] = \{ (x,y) \in E \mid ay = bx \}$.
La condition $ay=bx$ est la définition usuelle de l'égalité de deux fractions $\frac{a}{b}$ et $\frac{x}{y}$ (en supposant $b \neq 0$ et $y \neq 0$).
Cela suggère que chaque classe d'équivalence $[(a,b)]$ correspond à un unique nombre rationnel $\frac{a}{b}$.

Nous allons formaliser cette correspondance en définissant une application $\phi$ de l'ensemble quotient $E/\mathcal{R}$ vers l'ensemble des nombres rationnels $\mathbb{Q}$.
Soit l'application $\phi: E/\mathcal{R} \to \mathbb{Q}$ définie par :
$$ \phi([(a,b)]) = \frac{a}{b} $$
Nous allons démontrer que $\phi$ est une bijection bien définie, ce qui prouvera que $E/\mathcal{R}$ est isomorphe à $\mathbb{Q}$.

#### 3.1. $\phi$ est bien définie
Pour que l'application $\phi$ soit bien définie, l'image d'une classe d'équivalence ne doit pas dépendre du choix du représentant de cette classe.
Soient $[(a,b)]$ et $[(c,d)]$ deux classes d'équivalence. Supposons qu'elles sont égales, c'est-à-dire $[(a,b)] = [(c,d)]$.
Par définition de l'égalité des classes d'équivalence, cela signifie que $(a,b) \mathcal{R} (c,d)$.
D'après la définition de la relation $\mathcal{R}$, cette condition implique que $ad = bc$.
Puisque $b \in \mathbb{Z}^*$ et $d \in \mathbb{Z}^*$ (par définition de $E$), le produit $bd$ est non nul. Nous pouvons diviser les deux membres de l'égalité $ad = bc$ par $bd$.
$$ \frac{ad}{bd} = \frac{bc}{bd} $$
En simplifiant les fractions, nous obtenons :
$$ \frac{a}{b} = \frac{c}{d} $$
D'après la définition de l'application $\phi$, nous avons $\phi([(a,b)]) = \frac{a}{b}$ et $\phi([(c,d)]) = \frac{c}{d}$.
Puisque $\frac{a}{b} = \frac{c}{d}$, il s'ensuit que $\phi([(a,b)]) = \phi([(c,d)])$.
L'application $\phi$ est donc bien définie.

#### 3.2. $\phi$ est injective
Pour que $\phi$ soit injective, il faut que si deux classes d'équivalence ont la même image par $\phi$, alors ces classes sont égales.
Supposons que $\phi([(a,b)]) = \phi([(c,d)])$ pour deux classes d'équivalence $[(a,b)]$ et $[(c,d)]$ dans $E/\mathcal{R}$.
Par définition de l'application $\phi$, cette supposition signifie que :
$$ \frac{a}{b} = \frac{c}{d} $$
Puisque $b \in \mathbb{Z}^*$ et $d \in \mathbb{Z}^*$, nous pouvons multiplier les deux membres de cette égalité par $bd$ (qui est non nul).
$$ \frac{a}{b} \cdot bd = \frac{c}{d} \cdot bd $$
$$ ad = bc $$
D'après la définition de la relation $\mathcal{R}$, la condition $ad = bc$ signifie que $(a,b) \mathcal{R} (c,d)$.
Par conséquent, les classes d'équivalence correspondantes sont égales : $[(a,b)] = [(c,d)]$.
L'application $\phi$ est donc injective.

#### 3.3. $\phi$ est surjective
Pour que $\phi$ soit surjective, il faut que pour tout élément $q$ de l'ensemble d'arrivée $\mathbb{Q}$, il existe au moins une classe d'équivalence $[(a,b)] \in E/\mathcal{R}$ telle que $\phi([(a,b)]) = q$.
Soit $q$ un nombre rationnel arbitraire, c'est-à-dire $q \in \mathbb{Q}$.
Par définition des nombres rationnels, tout $q \in \mathbb{Q}$ peut être écrit sous la forme d'une fraction $\frac{a}{b}$, où $a \in \mathbb{Z}$ est un entier relatif et $b \in \mathbb{Z}^*$ est un entier relatif non nul.
Considérons le couple $(a,b)$. Ce couple appartient à l'ensemble $E = \mathbb{Z} \times \mathbb{Z}^*$ par construction.
La classe d'équivalence $[(a,b)]$ est un élément de l'ensemble quotient $E/\mathcal{R}$.
Par définition de l'application $\phi$, nous avons :
$$ \phi([(a,b)]) = \frac{a}{b} $$
Et par notre choix de $a$ et $b$, nous avons $\frac{a}{b} = q$.
Donc, pour tout $q \in \mathbb{Q}$, il existe une classe d'équivalence $[(a,b)]$ dont l'image par $\phi$ est $q$.
L'application $\phi$ est donc surjective.

#### 3.4. Conclusion sur l'ensemble quotient
Puisque l'application $\phi$ est bien définie, injective et surjective, c'est une bijection entre l'ensemble quotient $E/\mathcal{R}$ et l'ensemble des nombres rationnels $\mathbb{Q}$.
Par conséquent, l'ensemble quotient $E/\mathcal{R}$ est canoniquement identifiable à l'ensemble des nombres rationnels $\mathbb{Q}$.

#### 3.5. Identification à une structure algébrique
L'ensemble $\mathbb{Q}$ est non seulement un ensemble de nombres, mais il est également muni de deux opérations binaires internes, l'addition (+) et la multiplication ($\times$), qui lui confèrent une structure algébrique très importante.
L'ensemble $(\mathbb{Q}, +, \times)$ est un **corps commutatif**. Cela signifie qu'il satisfait les propriétés suivantes :
*   $(\mathbb{Q}, +)$ est un groupe abélien (l'addition est associative, commutative, possède un élément neutre 0 et chaque élément a un opposé).
*   $(\mathbb{Q} \setminus \{0\}, \times)$ est un groupe abélien (la multiplication est associative, commutative, possède un élément neutre 1 et chaque élément non nul a un inverse multiplicatif).
*   La multiplication est distributive sur l'addition.
Cette structure de corps est fondamentale en algèbre et en analyse.
Par conséquent, l'ensemble quotient $E/\mathcal{R}$ s'identifie au **corps des nombres rationnels $\mathbb{Q}$**.