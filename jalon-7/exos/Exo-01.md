# Exercice 1 : Vérification d'un sous-espace vectoriel dans $\mathbb{R}^2$

## Énoncé

Chers étudiants,

Pour ce premier jalon concernant les espaces vectoriels abstraits, nous allons commencer par un exercice fondamental qui consiste à vérifier si un sous-ensemble donné d'un espace vectoriel connu est lui-même un sous-espace vectoriel. C'est une compétence essentielle pour la suite de votre parcours.

Soit $\mathbb{R}$ le corps des nombres réels, muni de ses lois d'addition et de multiplication usuelles.
Considérons l'espace vectoriel $E = \mathbb{R}^2$ sur le corps $\mathbb{R}$, muni de l'addition vectorielle et de la multiplication par un scalaire définies de la manière suivante pour tout $(x_1, y_1) \in \mathbb{R}^2$, tout $(x_2, y_2) \in \mathbb{R}^2$ et tout $\lambda \in \mathbb{R}$ :
*   Addition vectorielle : $(x_1, y_1) + (x_2, y_2) = (x_1 + x_2, y_1 + y_2)$
*   Multiplication par un scalaire : $\lambda \cdot (x_1, y_1) = (\lambda x_1, \lambda y_1)$

Soit $F$ le sous-ensemble de $E$ défini par :
$$F = \left\{ (x, y) \in \mathbb{R}^2 \mid y = 2x \right\}$$

Démontrer que $F$ est un sous-espace vectoriel de $E$.

## Correction Détaillée

Pour démontrer que $F$ est un sous-espace vectoriel de l'espace vectoriel $E = \mathbb{R}^2$ sur le corps $\mathbb{R}$, nous devons vérifier trois conditions fondamentales :
1.  $F$ est non vide, c'est-à-dire qu'il contient le vecteur nul de $E$.
2.  $F$ est stable par l'addition vectorielle de $E$.
3.  $F$ est stable par la multiplication par un scalaire de $E$.

Détaillons chacune de ces conditions.

---

**Condition 1 : $F$ contient le vecteur nul de $E$.**

Le vecteur nul de l'espace vectoriel $E = \mathbb{R}^2$ est le vecteur $\vec{0}_E = (0, 0)$.
Pour vérifier si $\vec{0}_E \in F$, nous devons vérifier si ses composantes $(x, y) = (0, 0)$ satisfont la condition de définition de $F$, qui est $y = 2x$.

Substituons les valeurs $x=0$ et $y=0$ dans l'équation $y = 2x$ :
$0 = 2 \times 0$
$0 = 0$

Cette égalité est vraie.
Par conséquent, le vecteur nul $\vec{0}_E = (0, 0)$ appartient bien à l'ensemble $F$.
La première condition est satisfaite.

---

**Condition 2 : $F$ est stable par l'addition vectorielle.**

Soient $\vec{u}$ et $\vec{v}$ deux vecteurs quelconques appartenant à l'ensemble $F$.
Soient $\vec{u} = (x_1, y_1)$ et $\vec{v} = (x_2, y_2)$ les composantes de ces vecteurs dans $\mathbb{R}^2$.

Puisque $\vec{u} \in F$, ses composantes satisfont la condition de définition de $F$ :
$y_1 = 2x_1$ (Équation 1)

Puisque $\vec{v} \in F$, ses composantes satisfont la condition de définition de $F$ :
$y_2 = 2x_2$ (Équation 2)

Calculons la somme vectorielle de $\vec{u}$ et $\vec{v}$ :
$\vec{u} + \vec{v} = (x_1, y_1) + (x_2, y_2)$
$\vec{u} + \vec{v} = (x_1 + x_2, y_1 + y_2)$

Pour que $\vec{u} + \vec{v}$ appartienne à $F$, ses composantes $(x_1 + x_2, y_1 + y_2)$ doivent satisfaire la condition $y = 2x$. C'est-à-dire, nous devons vérifier si $(y_1 + y_2) = 2(x_1 + x_2)$.

En utilisant l'Équation 1 et l'Équation 2, nous pouvons substituer $y_1$ et $y_2$ :
$y_1 + y_2 = (2x_1) + (2x_2)$
$y_1 + y_2 = 2x_1 + 2x_2$

Factorisons le terme $2$ dans le membre de droite :
$y_1 + y_2 = 2(x_1 + x_2)$

Cette égalité montre que la somme des composantes $y$ est égale à deux fois la somme des composantes $x$.
Par conséquent, le vecteur $\vec{u} + \vec{v}$ appartient bien à l'ensemble $F$.
La deuxième condition est satisfaite.

---

**Condition 3 : $F$ est stable par la multiplication par un scalaire.**

Soit $\lambda$ un scalaire quelconque appartenant au corps $\mathbb{R}$.
Soit $\vec{u}$ un vecteur quelconque appartenant à l'ensemble $F$.
Soient $\vec{u} = (x, y)$ les composantes de ce vecteur dans $\mathbb{R}^2$.

Puisque $\vec{u} \in F$, ses composantes satisfont la condition de définition de $F$ :
$y = 2x$ (Équation 3)

Calculons le produit du scalaire $\lambda$ par le vecteur $\vec{u}$ :
$\lambda \cdot \vec{u} = \lambda \cdot (x, y)$
$\lambda \cdot \vec{u} = (\lambda x, \lambda y)$

Pour que $\lambda \cdot \vec{u}$ appartienne à $F$, ses composantes $(\lambda x, \lambda y)$ doivent satisfaire la condition $y = 2x$. C'est-à-dire, nous devons vérifier si $(\lambda y) = 2(\lambda x)$.

En utilisant l'Équation 3, nous pouvons substituer $y$ :
$\lambda y = \lambda (2x)$
$\lambda y = 2 \lambda x$

Par la commutativité de la multiplication dans $\mathbb{R}$, nous pouvons réécrire le membre de droite :
$\lambda y = 2 (\lambda x)$

Cette égalité montre que la composante $y$ du vecteur $\lambda \vec{u}$ est égale à deux fois sa composante $x$.
Par conséquent, le vecteur $\lambda \cdot \vec{u}$ appartient bien à l'ensemble $F$.
La troisième condition est satisfaite.

---

**Conclusion :**

Puisque les trois conditions (contenir le vecteur nul, stabilité par addition vectorielle, stabilité par multiplication scalaire) sont toutes satisfaites, nous pouvons conclure que $F$ est un sous-espace vectoriel de $E = \mathbb{R}^2$.
