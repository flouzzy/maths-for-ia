# Exercice 10 : L'Anneau Quotient des Séquences Réelles Éventuellement Égales
**Difficulté :** ⭐⭐⭐⭐⭐

## Énoncé

Soit $E = \mathbb{R}^{\mathbb{N}}$ l'ensemble de toutes les suites de nombres réels $u = (u_n)_{n \in \mathbb{N}}$.
Nous munissons $E$ des opérations d'addition et de multiplication définies terme à terme :
Pour $u = (u_n)$ et $v = (v_n)$ dans $E$ :
$$u + v = (u_n + v_n)_{n \in \mathbb{N}}$$
$$u \cdot v = (u_n \cdot v_n)_{n \in \mathbb{N}}$$
On admet que $(E, +, \cdot)$ est un anneau commutatif unitaire. L'élément neutre pour l'addition est la suite nulle $(0)_{n \in \mathbb{N}}$, et l'élément neutre pour la multiplication est la suite constante $(1)_{n \in \mathbb{N}}$.

Nous définissons une relation $\mathcal{R}$ sur $E$ de la manière suivante :
Pour $u = (u_n)$ et $v = (v_n)$ dans $E$, $u \mathcal{R} v$ si et seulement s'il existe un entier naturel $N_0$ tel que pour tout $n \ge N_0$, $u_n = v_n$.
En d'autres termes, deux suites sont en relation si elles sont éventuellement égales.

**Questions :**

1.  Démontrer que $\mathcal{R}$ est une relation d'équivalence sur $E$.
2.  Démontrer que la relation $\mathcal{R}$ est compatible avec les opérations d'addition et de multiplication de $E$. C'est-à-dire, si $u \mathcal{R} u'$ et $v \mathcal{R} v'$, alors $(u+v) \mathcal{R} (u'+v')$ et $(u \cdot v) \mathcal{R} (u' \cdot v')$.
3.  En déduire que l'ensemble quotient $E/\mathcal{R}$ peut être muni d'une structure d'anneau. On notera $\overline{u}$ la classe d'équivalence de la suite $u$. Démontrer explicitement les huit axiomes qui font de $(E/\mathcal{R}, +, \cdot)$ un anneau commutatif unitaire.
4.  L'anneau $E/\mathcal{R}$ est-il un anneau intègre ? Est-ce un corps ? Justifier rigoureusement votre réponse.

## Correction Détaillée

**Hypothèses de régularité et de structure :**
Nous considérons l'ensemble $E = \mathbb{R}^{\mathbb{N}}$ des suites de nombres réels. L'ensemble $\mathbb{R}$ est un corps commutatif. Les opérations d'addition et de multiplication sur $E$ sont définies terme à terme. Il est admis que $(E, +, \cdot)$ est un anneau commutatif unitaire.

---

### 1. Démonstration que $\mathcal{R}$ est une relation d'équivalence sur $E$

Pour démontrer que $\mathcal{R}$ est une relation d'équivalence, nous devons prouver qu'elle est réflexive, symétrique et transitive.

#### 1.1. Réflexivité
Une relation $\mathcal{R}$ est réflexive si pour tout élément $u \in E$, $u \mathcal{R} u$.
**Démonstration :**
Soit $u = (u_n)_{n \in \mathbb{N}}$ une suite arbitraire dans $E$.
Nous devons montrer qu'il existe un entier naturel $N_0$ tel que pour tout $n \ge N_0$, $u_n = u_n$.
Choisissons $N_0 = 0$.
L'égalité dans $E$ (qui est $\mathbb{K}$) est réflexive. Ainsi, pour tout entier $n \ge 0$, l'identité $u_n = u_n$ est rigoureusement satisfaite.
Par conséquent, $u \mathcal{R} u$.
La relation $\mathcal{R}$ est réflexive.

#### 1.2. Symétrie
Une relation $\mathcal{R}$ est symétrique si pour tout $u, v \in E$, si $u \mathcal{R} v$, alors $v \mathcal{R} u$.
**Démonstration :**
Soient $u = (u_n)_{n \in \mathbb{N}}$ et $v = (v_n)_{n \in \mathbb{N}}$ deux suites dans $E$.
Supposons que $u \mathcal{R} v$.
Par définition de $\mathcal{R}$, cela signifie qu'il existe un entier naturel $N_0$ tel que pour tout $n \ge N_0$, $u_n = v_n$.
L'égalité des nombres réels est une relation symétrique. Par conséquent, si $u_n = v_n$, alors $v_n = u_n$.
Ainsi, pour le même entier naturel $N_0$, il est vrai que pour tout $n \ge N_0$, $v_n = u_n$.
Par définition de $\mathcal{R}$, cela signifie que $v \mathcal{R} u$.
La relation $\mathcal{R}$ est symétrique.

#### 1.3. Transitivité
Une relation $\mathcal{R}$ est transitive si pour tout $u, v, w \in E$, si $u \mathcal{R} v$ et $v \mathcal{R} w$, alors $u \mathcal{R} w$.
**Démonstration :**
Soient $u = (u_n)_{n \in \mathbb{N}}$, $v = (v_n)_{n \in \mathbb{N}}$ et $w = (w_n)_{n \in \mathbb{N}}$ trois suites dans $E$.
Supposons que $u \mathcal{R} v$. Par définition, il existe un entier naturel $N_1$ tel que pour tout $n \ge N_1$, $u_n = v_n$.
Supposons que $v \mathcal{R} w$. Par définition, il existe un entier naturel $N_2$ tel que pour tout $n \ge N_2$, $v_n = w_n$.
Nous devons montrer qu'il existe un entier naturel $N_0$ tel que pour tout $n \ge N_0$, $u_n = w_n$.
Choisissons $N_0 = \max(N_1, N_2)$.
Alors, pour tout entier $n$ tel que $n \ge N_0$, nous avons à la fois $n \ge N_1$ et $n \ge N_2$.
Puisque $n \ge N_1$, nous avons $u_n = v_n$.
Puisque $n \ge N_2$, nous avons $v_n = w_n$.
L'égalité des nombres réels est une relation transitive. Par conséquent, si $u_n = v_n$ et $v_n = w_n$, alors $u_n = w_n$.
Ainsi, pour tout $n \ge N_0$, nous avons $u_n = w_n$.
Par définition de $\mathcal{R}$, cela signifie que $u \mathcal{R} w$.
La relation $\mathcal{R}$ est transitive.

Puisque $\mathcal{R}$ est réflexive, symétrique et transitive, $\mathcal{R}$ est une relation d'équivalence sur $E$.

---

### 2. Compatibilité de $\mathcal{R}$ avec les opérations d'addition et de multiplication

Nous devons prouver que $\mathcal{R}$ est compatible avec l'addition et la multiplication définies sur $E$.

#### 2.1. Compatibilité avec l'addition
Nous devons montrer que si $u \mathcal{R} u'$ et $v \mathcal{R} v'$, alors $(u+v) \mathcal{R} (u'+v')$.
**Démonstration :**
Soient $u, u', v, v'$ des suites dans $E$.
Supposons que $u \mathcal{R} u'$. Par définition, il existe un entier naturel $N_1$ tel que pour tout $n \ge N_1$, $u_n = u'_n$.
Supposons que $v \mathcal{R} v'$. Par définition, il existe un entier naturel $N_2$ tel que pour tout $n \ge N_2$, $v_n = v'_n$.
Nous devons montrer qu'il existe un entier naturel $N_0$ tel que pour tout $n \ge N_0$, $(u+v)_n = (u'+v')_n$.
Choisissons $N_0 = \max(N_1, N_2)$.
Pour tout entier $n$ tel que $n \ge N_0$, nous avons à la fois $n \ge N_1$ et $n \ge N_2$.
Puisque $n \ge N_1$, nous avons $u_n = u'_n$.
Puisque $n \ge N_2$, nous avons $v_n = v'_n$.
L'addition des nombres réels est une opération bien définie. Par conséquent, pour tout $n \ge N_0$, $u_n + v_n = u'_n + v'_n$.
Par définition de l'addition des suites, $(u+v)_n = u_n + v_n$ et $(u'+v')_n = u'_n + v'_n$.
Donc, pour tout $n \ge N_0$, $(u+v)_n = (u'+v')_n$.
Par définition de $\mathcal{R}$, cela signifie que $(u+v) \mathcal{R} (u'+v')$.
La relation $\mathcal{R}$ est compatible avec l'addition.

#### 2.2. Compatibilité avec la multiplication
Nous devons montrer que si $u \mathcal{R} u'$ et $v \mathcal{R} v'$, alors $(u \cdot v) \mathcal{R} (u' \cdot v')$.
**Démonstration :**
Soient $u, u', v, v'$ des suites dans $E$.
Supposons que $u \mathcal{R} u'$. Par définition, il existe un entier naturel $N_1$ tel que pour tout $n \ge N_1$, $u_n = u'_n$.
Supposons que $v \mathcal{R} v'$. Par définition, il existe un entier naturel $N_2$ tel que pour tout $n \ge N_2$, $v_n = v'_n$.
Nous devons montrer qu'il existe un entier naturel $N_0$ tel que pour tout $n \ge N_0$, $(u \cdot v)_n = (u' \cdot v')_n$.
Choisissons $N_0 = \max(N_1, N_2)$.
Pour tout entier $n$ tel que $n \ge N_0$, nous avons à la fois $n \ge N_1$ et $n \ge N_2$.
Puisque $n \ge N_1$, nous avons $u_n = u'_n$.
Puisque $n \ge N_2$, nous avons $v_n = v'_n$.
La multiplication des nombres réels est une opération bien définie. Par conséquent, pour tout $n \ge N_0$, $u_n \cdot v_n = u'_n \cdot v'_n$.
Par définition de la multiplication des suites, $(u \cdot v)_n = u_n \cdot v_n$ et $(u' \cdot v')_n = u'_n \cdot v'_n$.
Donc, pour tout $n \ge N_0$, $(u \cdot v)_n = (u' \cdot v')_n$.
Par définition de $\mathcal{R}$, cela signifie que $(u \cdot v) \mathcal{R} (u' \cdot v')$.
La relation $\mathcal{R}$ est compatible avec la multiplication.

---

### 3. Structure d'anneau de $E/\mathcal{R}$

Puisque $\mathcal{R}$ est une relation d'équivalence compatible avec les opérations d'addition et de multiplication de $E$, l'ensemble quotient $E/\mathcal{R}$ peut être muni d'opérations d'addition et de multiplication induites, définies comme suit :
Pour $\overline{u}, \overline{v} \in E/\mathcal{R}$ :
$$\overline{u} + \overline{v} = \overline{u+v}$$
$$\overline{u} \cdot \overline{v} = \overline{u \cdot v}$$
La compatibilité prouvée dans la partie 2 garantit que ces opérations sont bien définies, c'est-à-dire que le résultat ne dépend pas du choix des représentants $u$ et $v$ des classes $\overline{u}$ et $\overline{v}$.

Nous devons maintenant prouver que $(E/\mathcal{R}, +, \cdot)$ est un anneau commutatif unitaire en vérifiant les huit axiomes.

Soient $\overline{u}, \overline{v}, \overline{w}$ des éléments arbitraires de $E/\mathcal{R}$, où $u, v, w$ sont des représentants de ces classes.

#### 3.1. Axiomes pour l'addition

##### 3.1.1. Associativité de l'addition
Nous devons montrer que $(\overline{u} + \overline{v}) + \overline{w} = \overline{u} + (\overline{v} + \overline{w})$.
**Démonstration :**
$$(\overline{u} + \overline{v}) + \overline{w} = \overline{u+v} + \overline{w} \quad \text{(par définition de l'addition dans } E/\mathcal{R})$$
$$= \overline{(u+v)+w} \quad \text{(par définition de l'addition dans } E/\mathcal{R})$$
L'anneau $(E, +, \cdot)$ est commutatif et unitaire. En particulier, l'addition dans $E$ est associative.
Donc, la suite $(u+v)+w$ est égale à la suite $u+(v+w)$.
$$= \overline{u+(v+w)} \quad \text{(par associativité de l'addition dans } E)$$
$$= \overline{u} + \overline{v+w} \quad \text{(par définition de l'addition dans } E/\mathcal{R})$$
$$= \overline{u} + (\overline{v} + \overline{w}) \quad \text{(par définition de l'addition dans } E/\mathcal{R})$$
L'addition dans $E/\mathcal{R}$ est associative.

##### 3.1.2. Commutativité de l'addition
Nous devons montrer que $\overline{u} + \overline{v} = \overline{v} + \overline{u}$.
**Démonstration :**
$$\overline{u} + \overline{v} = \overline{u+v} \quad \text{(par définition de l'addition dans } E/\mathcal{R})$$
L'anneau $(E, +, \cdot)$ est commutatif et unitaire. En particulier, l'addition dans $E$ est commutative.
Donc, la suite $u+v$ est égale à la suite $v+u$.
$$= \overline{v+u} \quad \text{(par commutativité de l'addition dans } E)$$
$$= \overline{v} + \overline{u} \quad \text{(par définition de l'addition dans } E/\mathcal{R})$$
L'addition dans $E/\mathcal{R}$ est commutative.

##### 3.1.3. Élément neutre pour l'addition
Nous devons trouver un élément $\overline{0_E} \in E/\mathcal{R}$ tel que pour tout $\overline{u} \in E/\mathcal{R}$, $\overline{u} + \overline{0_E} = \overline{u}$.
**Démonstration :**
Soit $0_E = (0)_{n \in \mathbb{N}}$ la suite nulle dans $E$.
Considérons la classe $\overline{0_E}$.
Pour toute classe $\overline{u} \in E/\mathcal{R}$ :
$$\overline{u} + \overline{0_E} = \overline{u+0_E} \quad \text{(par définition de l'addition dans } E/\mathcal{R})$$
L'élément $0_E$ est l'élément neutre pour l'addition dans $E$. Donc, $u+0_E = u$.
$$= \overline{u} \quad \text{(par propriété de l'élément neutre dans } E)$$
De même, $\overline{0_E} + \overline{u} = \overline{0_E+u} = \overline{u}$.
L'élément $\overline{0_E}$ est l'élément neutre pour l'addition dans $E/\mathcal{R}$.

##### 3.1.4. Existence d'un opposé pour l'addition
Pour tout $\overline{u} \in E/\mathcal{R}$, il existe un élément $\overline{-u} \in E/\mathcal{R}$ tel que $\overline{u} + \overline{-u} = \overline{0_E}$.
**Démonstration :**
Soit $\overline{u} \in E/\mathcal{R}$. Soit $-u = (-u_n)_{n \in \mathbb{N}}$ la suite dont les termes sont les opposés des termes de $u$.
L'élément $-u$ est l'opposé de $u$ dans $E$.
Considérons la classe $\overline{-u}$.
$$\overline{u} + \overline{-u} = \overline{u+(-u)} \quad \text{(par définition de l'addition dans } E/\mathcal{R})$$
Puisque $-u$ est l'opposé de $u$ dans $E$, $u+(-u) = 0_E$.
$$= \overline{0_E} \quad \text{(par propriété de l'opposé dans } E)$$
L'élément $\overline{-u}$ est l'opposé de $\overline{u}$ dans $E/\mathcal{R}$.

#### 3.2. Axiomes pour la multiplication

##### 3.2.1. Associativité de la multiplication
Nous devons montrer que $(\overline{u} \cdot \overline{v}) \cdot \overline{w} = \overline{u} \cdot (\overline{v} \cdot \overline{w})$.
**Démonstration :**
$$(\overline{u} \cdot \overline{v}) \cdot \overline{w} = \overline{u \cdot v} \cdot \overline{w} \quad \text{(par définition de la multiplication dans } E/\mathcal{R})$$
$$= \overline{(u \cdot v) \cdot w} \quad \text{(par définition de la multiplication dans } E/\mathcal{R})$$
L'anneau $(E, +, \cdot)$ est commutatif et unitaire. En particulier, la multiplication dans $E$ est associative.
Donc, la suite $(u \cdot v) \cdot w$ est égale à la suite $u \cdot (v \cdot w)$.
$$= \overline{u \cdot (v \cdot w)} \quad \text{(par associativité de la multiplication dans } E)$$
$$= \overline{u} \cdot \overline{v \cdot w} \quad \text{(par définition de la multiplication dans } E/\mathcal{R})$$
$$= \overline{u} \cdot (\overline{v} \cdot \overline{w}) \quad \text{(par définition de la multiplication dans } E/\mathcal{R})$$
La multiplication dans $E/\mathcal{R}$ est associative.

##### 3.2.2. Commutativité de la multiplication
Nous devons montrer que $\overline{u} \cdot \overline{v} = \overline{v} \cdot \overline{u}$.
**Démonstration :**
$$\overline{u} \cdot \overline{v} = \overline{u \cdot v} \quad \text{(par définition de la multiplication dans } E/\mathcal{R})$$
L'anneau $(E, +, \cdot)$ est commutatif et unitaire. En particulier, la multiplication dans $E$ est commutative.
Donc, la suite $u \cdot v$ est égale à la suite $v \cdot u$.
$$= \overline{v \cdot u} \quad \text{(par commutativité de la multiplication dans } E)$$
$$= \overline{v} \cdot \overline{u} \quad \text{(par définition de la multiplication dans } E/\mathcal{R})$$
La multiplication dans $E/\mathcal{R}$ est commutative.

##### 3.2.3. Élément neutre pour la multiplication (unité)
Nous devons trouver un élément $\overline{1_E} \in E/\mathcal{R}$ tel que pour tout $\overline{u} \in E/\mathcal{R}$, $\overline{u} \cdot \overline{1_E} = \overline{u}$.
**Démonstration :**
Soit $1_E = (1)_{n \in \mathbb{N}}$ la suite constante égale à 1 dans $E$.
Considérons la classe $\overline{1_E}$.
Pour toute classe $\overline{u} \in E/\mathcal{R}$ :
$$\overline{u} \cdot \overline{1_E} = \overline{u \cdot 1_E} \quad \text{(par définition de la multiplication dans } E/\mathcal{R})$$
L'élément $1_E$ est l'élément neutre pour la multiplication dans $E$. Donc, $u \cdot 1_E = u$.
$$= \overline{u} \quad \text{(par propriété de l'élément neutre dans } E)$$
De même, $\overline{1_E} \cdot \overline{u} = \overline{1_E \cdot u} = \overline{u}$.
L'élément $\overline{1_E}$ est l'élément neutre (unité) pour la multiplication dans $E/\mathcal{R}$.

##### 3.2.4. Distributivité de la multiplication sur l'addition
Nous devons montrer que $\overline{u} \cdot (\overline{v} + \overline{w}) = (\overline{u} \cdot \overline{v}) + (\overline{u} \cdot \overline{w})$.
**Démonstration :**
$$\overline{u} \cdot (\overline{v} + \overline{w}) = \overline{u} \cdot \overline{v+w} \quad \text{(par définition de l'addition dans } E/\mathcal{R})$$
$$= \overline{u \cdot (v+w)} \quad \text{(par définition de la multiplication dans } E/\mathcal{R})$$
L'anneau $(E, +, \cdot)$ est commutatif et unitaire. En particulier, la multiplication est distributive sur l'addition dans $E$.
Donc, la suite $u \cdot (v+w)$ est égale à la suite $(u \cdot v) + (u \cdot w)$.
$$= \overline{(u \cdot v) + (u \cdot w)} \quad \text{(par distributivité dans } E)$$
$$= \overline{u \cdot v} + \overline{u \cdot w} \quad \text{(par définition de l'addition dans } E/\mathcal{R})$$
$$= (\overline{u} \cdot \overline{v}) + (\overline{u} \cdot \overline{w}) \quad \text{(par définition de la multiplication dans } E/\mathcal{R})$$
La distributivité est vérifiée dans $E/\mathcal{R}$.

Puisque tous les axiomes sont vérifiés, $(E/\mathcal{R}, +, \cdot)$ est un anneau commutatif unitaire.

---

### 4. Propriétés de l'anneau $E/\mathcal{R}$

#### 4.1. L'anneau $E/\mathcal{R}$ est-il un anneau intègre ?

Un anneau intègre est un anneau commutatif unitaire non trivial (c'est-à-dire $0 \neq 1$) qui n'a pas de diviseurs de zéro. Un élément $x \neq 0$ est un diviseur de zéro s'il existe $y \neq 0$ tel que $x \cdot y = 0$.

Nous avons déjà prouvé que $E/\mathcal{R}$ est un anneau commutatif unitaire.
L'anneau $E/\mathcal{R}$ est non trivial car $\overline{0_E} \neq \overline{1_E}$. En effet, la suite nulle $(0)_{n \in \mathbb{N}}$ n'est pas éventuellement égale à la suite constante $(1)_{n \in \mathbb{N}}$ (aucun $N_0$ ne peut satisfaire $0_n = 1_n$ pour $n \ge N_0$).

Nous allons chercher des diviseurs de zéro dans $E/\mathcal{R}$.
**Démonstration :**
Considérons la suite $u = (u_n)_{n \in \mathbb{N}}$ définie par :
$$u_n = \begin{cases} 1 & \text{si } n=0 \\ 0 & \text{si } n > 0 \end{cases}$$
La classe $\overline{u}$ n'est pas la classe nulle $\overline{0_E}$. En effet, la suite $u$ n'est pas éventuellement nulle car $u_0 = 1 \neq 0$. Si $u \mathcal{R} 0_E$, il existerait $N_0$ tel que $u_n=0$ pour $n \ge N_0$. Si $N_0=0$, $u_0=0$ ce qui est faux. Si $N_0>0$, $u_0=0$ ce qui est faux.
Donc $\overline{u} \neq \overline{0_E}$.

Considérons la suite $v = (v_n)_{n \in \mathbb{N}}$ définie par :
$$v_n = \begin{cases} 0 & \text{si } n=0 \\ 1 & \text{si } n > 0 \end{cases}$$
La classe $\overline{v}$ n'est pas la classe nulle $\overline{0_E}$. En effet, la suite $v$ n'est pas éventuellement nulle car $v_1 = 1 \neq 0$. Si $v \mathcal{R} 0_E$, il existerait $N_0$ tel que $v_n=0$ pour $n \ge N_0$. Si $N_0=0$, $v_0=0$ est vrai, mais $v_1=0$ est faux. Si $N_0=1$, $v_1=0$ est faux. Si $N_0>0$, $v_{N_0}=0$ est faux.
Donc $\overline{v} \neq \overline{0_E}$.

Maintenant, calculons le produit $\overline{u} \cdot \overline{v}$ :
$$\overline{u} \cdot \overline{v} = \overline{u \cdot v} \quad \text{(par définition de la multiplication dans } E/\mathcal{R})$$
La suite $u \cdot v = (u_n \cdot v_n)_{n \in \mathbb{N}}$ a pour termes :
Pour $n=0$, $u_0 \cdot v_0 = 1 \cdot 0 = 0$.
Pour $n > 0$, $u_n \cdot v_n = 0 \cdot 1 = 0$.
Ainsi, la suite $u \cdot v$ est la suite nulle $0_E = (0)_{n \in \mathbb{N}}$.
Par conséquent :
$$\overline{u} \cdot \overline{v} = \overline{0_E}$$
Nous avons trouvé deux classes non nulles, $\overline{u}$ et $\overline{v}$, dont le produit est la classe nulle.
Ceci signifie que $\overline{u}$ et $\overline{v}$ sont des diviseurs de zéro dans $E/\mathcal{R}$.
Par définition, un anneau possédant des diviseurs de zéro n'est pas un anneau intègre.
**Conclusion :** L'anneau $E/\mathcal{R}$ n'est pas un anneau intègre.

#### 4.2. L'anneau $E/\mathcal{R}$ est-il un corps ?

Un corps est un anneau commutatif unitaire dans lequel tout élément non nul possède un inverse multiplicatif. Un corps est nécessairement un anneau intègre.

**Démonstration :**
Puisque nous avons démontré dans la partie 4.1 que l'anneau $E/\mathcal{R}$ n'est pas un anneau intègre (il contient des diviseurs de zéro), il ne peut pas être un corps.
Pour qu'un anneau soit un corps, il faut que tout élément non nul soit inversible. Or, un diviseur de zéro non nul ne peut jamais être inversible.
En effet, si $\overline{x} \neq \overline{0_E}$ est un diviseur de zéro, alors il existe $\overline{y} \neq \overline{0_E}$ tel que $\overline{x} \cdot \overline{y} = \overline{0_E}$.
Si $\overline{x}$ était inversible, il existerait $\overline{x^{-1}}$ tel que $\overline{x} \cdot \overline{x^{-1}} = \overline{1_E}$.
Alors, en multipliant l'équation $\overline{x} \cdot \overline{y} = \overline{0_E}$ par $\overline{x^{-1}}$ à gauche :
$$\overline{x^{-1}} \cdot (\overline{x} \cdot \overline{y}) = \overline{x^{-1}} \cdot \overline{0_E}$$
Par associativité :
$$(\overline{x^{-1}} \cdot \overline{x}) \cdot \overline{y} = \overline{0_E}$$
Par définition de l'inverse et de l'élément neutre de la multiplication :
$$\overline{1_E} \cdot \overline{y} = \overline{0_E}$$
$$\overline{y} = \overline{0_E}$$
Ceci contredit l'hypothèse que $\overline{y} \neq \overline{0_E}$.
Par conséquent, un diviseur de zéro non nul ne peut pas être inversible.
Puisque $E/\mathcal{R}$ contient des diviseurs de zéro non nuls, il ne peut pas être un corps.

**Conclusion :** L'anneau $E/\mathcal{R}$ n'est pas un corps.

---
**Remarque sur la structure de $E/\mathcal{R}$ :**
La relation d'équivalence $u \mathcal{R} v$ est équivalente à dire que la suite $(u_n - v_n)_{n \in \mathbb{N}}$ est éventuellement nulle.
Soit $I$ l'ensemble des suites de $E$ qui sont éventuellement nulles (c'est-à-dire qui sont $0$ à partir d'un certain rang).
$I = \{ (u_n)_{n \in \mathbb{N}} \in E \mid \exists N_0 \in \mathbb{N}, \forall n \ge N_0, u_n = 0 \}$.
Il est possible de démontrer que $I$ est un idéal de l'anneau $E$.
Alors, la relation $u \mathcal{R} v$ est équivalente à $u - v \in I$.
Par la construction standard des anneaux quotients, l'anneau $E/\mathcal{R}$ est canoniquement isomorphe à l'anneau quotient $E/I$.
La non-intégrité de $E/I$ est une propriété connue des anneaux de suites (ou de fonctions) où l'idéal $I$ n'est pas maximal.