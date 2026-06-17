En tant que Professeur de Mathématiques Émérite, je vous propose l'exercice suivant, qui explore la construction rigoureuse d'un corps bien connu à partir d'un anneau quotient.

---

# Exercice 7 : Construction du Corps des Nombres Complexes comme Anneau Quotient
**Difficulté :** ⭐⭐⭐⭐

## Énoncé
Soit $\mathbb{R}[X]$ l'anneau des polynômes à coefficients réels, muni des opérations usuelles d'addition et de multiplication.
On considère le polynôme $P(X) = X^2+1 \in \mathbb{R}[X]$.
Soit $I$ l'idéal principal de $\mathbb{R}[X]$ engendré par $P(X)$, c'est-à-dire $I = \{Q(X) \cdot P(X) \mid Q(X) \in \mathbb{R}[X]\}$.

1.  Démontrer que la relation $\sim$ définie sur $\mathbb{R}[X]$ par $A(X) \sim B(X)$ si et seulement si $A(X) - B(X) \in I$ est une relation d'équivalence.
2.  Décrire explicitement les éléments de l'ensemble quotient $E = \mathbb{R}[X]/I$. Montrer que chaque classe d'équivalence contient un unique représentant de degré au plus 1.
3.  On munit $E$ des opérations d'addition et de multiplication induites par celles de $\mathbb{R}[X]$:
    Pour $[A(X)], [B(X)] \in E$, on définit $[A(X)] + [B(X)] = [A(X) + B(X)]$ et $[A(X)] \cdot [B(X)] = [A(X) \cdot B(X)]$.
    Démontrer que ces opérations sont bien définies, c'est-à-dire qu'elles ne dépendent pas du choix des représentants.
4.  Démontrer que $(E, +, \cdot)$ est un corps. Vous devrez notamment montrer l'existence d'un inverse multiplicatif pour tout élément non nul.
5.  Établir un isomorphisme explicite entre le corps $(E, +, \cdot)$ et le corps des nombres complexes $(\mathbb{C}, +, \cdot)$.

## Correction Détaillée

### 1. Démonstration que $\sim$ est une relation d'équivalence

Pour que $\sim$ soit une relation d'équivalence sur $\mathbb{R}[X]$, elle doit satisfaire les trois propriétés suivantes : réflexivité, symétrie et transitivité.

**a) Réflexivité :**
Pour tout polynôme $A(X) \in \mathbb{R}[X]$, nous devons montrer que $A(X) \sim A(X)$.
Par définition de $\sim$, cela signifie que $A(X) - A(X) \in I$.
Nous avons :
$$A(X) - A(X) = 0$$
L'idéal $I$ est défini comme l'ensemble des multiples de $P(X)$. Puisque $0 = 0 \cdot P(X)$ et que $0 \in \mathbb{R}[X]$, le polynôme nul $0$ est un élément de l'idéal $I$.
Par conséquent, $A(X) - A(X) \in I$.
La relation $\sim$ est donc réflexive.

**b) Symétrie :**
Pour tout polynôme $A(X), B(X) \in \mathbb{R}[X]$, supposons que $A(X) \sim B(X)$. Nous devons montrer que $B(X) \sim A(X)$.
Par hypothèse, $A(X) \sim B(X)$ signifie que $A(X) - B(X) \in I$.
Par définition de l'idéal $I$, il existe un polynôme $Q(X) \in \mathbb{R}[X]$ tel que :
$$A(X) - B(X) = Q(X) \cdot P(X)$$
Nous voulons montrer que $B(X) - A(X) \in I$. Nous pouvons écrire :
$$B(X) - A(X) = -(A(X) - B(X))$$
En substituant l'expression de $A(X) - B(X)$, nous obtenons :
$$B(X) - A(X) = -(Q(X) \cdot P(X)) = (-Q(X)) \cdot P(X)$$
Puisque $Q(X) \in \mathbb{R}[X]$, alors $-Q(X)$ est également un polynôme dans $\mathbb{R}[X]$.
Ainsi, $B(X) - A(X)$ est un multiple de $P(X)$, ce qui signifie que $B(X) - A(X) \in I$.
La relation $\sim$ est donc symétrique.

**c) Transitivité :**
Pour tout polynôme $A(X), B(X), C(X) \in \mathbb{R}[X]$, supposons que $A(X) \sim B(X)$ et $B(X) \sim C(X)$. Nous devons montrer que $A(X) \sim C(X)$.
Par hypothèse :
1.  $A(X) \sim B(X)$ implique que $A(X) - B(X) \in I$. Il existe donc $Q_1(X) \in \mathbb{R}[X]$ tel que $A(X) - B(X) = Q_1(X) \cdot P(X)$.
2.  $B(X) \sim C(X)$ implique que $B(X) - C(X) \in I$. Il existe donc $Q_2(X) \in \mathbb{R}[X]$ tel que $B(X) - C(X) = Q_2(X) \cdot P(X)$.
Nous voulons montrer que $A(X) - C(X) \in I$. Nous pouvons écrire :
$$A(X) - C(X) = (A(X) - B(X)) + (B(X) - C(X))$$
En substituant les expressions précédentes, nous obtenons :
$$A(X) - C(X) = Q_1(X) \cdot P(X) + Q_2(X) \cdot P(X)$$
En factorisant $P(X)$ :
$$A(X) - C(X) = (Q_1(X) + Q_2(X)) \cdot P(X)$$
Puisque $Q_1(X) \in \mathbb{R}[X]$ et $Q_2(X) \in \mathbb{R}[X]$, leur somme $Q_1(X) + Q_2(X)$ est également un polynôme dans $\mathbb{R}[X]$.
Ainsi, $A(X) - C(X)$ est un multiple de $P(X)$, ce qui signifie que $A(X) - C(X) \in I$.
La relation $\sim$ est donc transitive.

Puisque la relation $\sim$ est réflexive, symétrique et transitive, c'est bien une relation d'équivalence sur $\mathbb{R}[X]$.

### 2. Description des éléments de l'ensemble quotient $E = \mathbb{R}[X]/I$

L'ensemble quotient $E$ est l'ensemble des classes d'équivalence de $\mathbb{R}[X]$ modulo $I$. Une classe d'équivalence d'un polynôme $A(X)$ est notée $[A(X)]$.

Soit $A(X) \in \mathbb{R}[X]$ un polynôme quelconque. Nous pouvons effectuer la division euclidienne de $A(X)$ par $P(X) = X^2+1$ dans l'anneau $\mathbb{R}[X]$, car $P(X)$ est un polynôme unitaire et non nul.
Il existe des polynômes uniques $Q(X)$ (quotient) et $R(X)$ (reste) dans $\mathbb{R}[X]$ tels que :
$$A(X) = Q(X) \cdot P(X) + R(X)$$
avec la condition $\deg(R(X)) < \deg(P(X))$.
Puisque $\deg(P(X)) = \deg(X^2+1) = 2$, le reste $R(X)$ doit avoir un degré strictement inférieur à 2.
Par conséquent, $R(X)$ est un polynôme de la forme $aX+b$, où $a, b \in \mathbb{R}$.

De l'équation de la division euclidienne, nous pouvons écrire :
$$A(X) - R(X) = Q(X) \cdot P(X)$$
Par définition de l'idéal $I$, cela signifie que $A(X) - R(X) \in I$.
Par la définition de la relation d'équivalence $\sim$, ceci implique que $A(X) \sim R(X)$.
Donc, la classe d'équivalence $[A(X)]$ est égale à la classe d'équivalence $[R(X)]$.
Chaque classe d'équivalence contient au moins un polynôme de degré au plus 1. Ce polynôme est de la forme $aX+b$ pour certains $a, b \in \mathbb{R}$.

**Démonstration de l'unicité du représentant de degré au plus 1 :**
Supposons qu'une classe d'équivalence $[A(X)]$ contienne deux représentants de degré au plus 1, disons $R_1(X) = a_1X+b_1$ et $R_2(X) = a_2X+b_2$, où $a_1, b_1, a_2, b_2 \in \mathbb{R}$.
Si $R_1(X)$ et $R_2(X)$ sont dans la même classe d'équivalence, alors $R_1(X) \sim R_2(X)$.
Cela signifie que $R_1(X) - R_2(X) \in I$.
Donc, il existe un polynôme $Q(X) \in \mathbb{R}[X]$ tel que :
$$R_1(X) - R_2(X) = Q(X) \cdot P(X)$$
Nous avons $\deg(R_1(X)) \le 1$ et $\deg(R_2(X)) \le 1$.
Par conséquent, $\deg(R_1(X) - R_2(X)) \le 1$.

D'autre part, $P(X) = X^2+1$ a un degré 2.
Si $Q(X)$ n'est pas le polynôme nul, alors $\deg(Q(X) \cdot P(X)) = \deg(Q(X)) + \deg(P(X)) \ge 0 + 2 = 2$.
L'égalité $R_1(X) - R_2(X) = Q(X) \cdot P(X)$ implique que le polynôme de gauche a un degré au plus 1, tandis que le polynôme de droite a un degré au moins 2 (si $Q(X) \neq 0$).
Cette situation est seulement possible si le polynôme des deux côtés est le polynôme nul.
Donc, $Q(X)$ doit être le polynôme nul.
Si $Q(X) = 0$, alors $R_1(X) - R_2(X) = 0 \cdot P(X) = 0$.
Ceci implique $R_1(X) = R_2(X)$.
Ainsi, chaque classe d'équivalence $[A(X)]$ contient un unique représentant de degré au plus 1.

Les éléments de l'ensemble quotient $E$ sont donc les classes d'équivalence de la forme $[aX+b]$, où $a, b \in \mathbb{R}$.
$$E = \{ [aX+b] \mid a, b \in \mathbb{R} \}$$

### 3. Démonstration que les opérations sont bien définies

Soient $[A_1(X)], [A_2(X)], [B_1(X)], [B_2(X)] \in E$.
Supposons que $[A_1(X)] = [A_2(X)]$ et $[B_1(X)] = [B_2(X)]$.
Par définition de l'équivalence, cela signifie que $A_1(X) \sim A_2(X)$ et $B_1(X) \sim B_2(X)$.
C'est-à-dire, $A_1(X) - A_2(X) \in I$ et $B_1(X) - B_2(X) \in I$.

**a) Opération d'addition :**
Nous voulons montrer que $[A_1(X) + B_1(X)] = [A_2(X) + B_2(X)]$.
Cela revient à montrer que $(A_1(X) + B_1(X)) - (A_2(X) + B_2(X)) \in I$.
Considérons la différence :
$$(A_1(X) + B_1(X)) - (A_2(X) + B_2(X)) = (A_1(X) - A_2(X)) + (B_1(X) - B_2(X))$$
Nous savons que $A_1(X) - A_2(X) \in I$ et $B_1(X) - B_2(X) \in I$.
Puisque $I$ est un idéal, il est fermé sous l'addition. C'est-à-dire, la somme de deux éléments de $I$ est un élément de $I$.
Par conséquent, $(A_1(X) - A_2(X)) + (B_1(X) - B_2(X)) \in I$.
Ainsi, $[A_1(X) + B_1(X)] = [A_2(X) + B_2(X)]$.
L'opération d'addition est bien définie.

**b) Opération de multiplication :**
Nous voulons montrer que $[A_1(X) \cdot B_1(X)] = [A_2(X) \cdot B_2(X)]$.
Cela revient à montrer que $A_1(X) \cdot B_1(X) - A_2(X) \cdot B_2(X) \in I$.
Considérons la différence :
$$A_1(X) \cdot B_1(X) - A_2(X) \cdot B_2(X)$$
Nous pouvons ajouter et soustraire le terme $A_2(X) \cdot B_1(X)$ pour factoriser :
$$A_1(X) \cdot B_1(X) - A_2(X) \cdot B_2(X) = A_1(X) \cdot B_1(X) - A_2(X) \cdot B_1(X) + A_2(X) \cdot B_1(X) - A_2(X) \cdot B_2(X)$$
$$= (A_1(X) - A_2(X)) \cdot B_1(X) + A_2(X) \cdot (B_1(X) - B_2(X))$$
Nous savons que $A_1(X) - A_2(X) \in I$. Puisque $I$ est un idéal, tout multiple d'un élément de $I$ par un polynôme de $\mathbb{R}[X]$ est aussi dans $I$.
Donc, $(A_1(X) - A_2(X)) \cdot B_1(X) \in I$.
De même, nous savons que $B_1(X) - B_2(X) \in I$.
Donc, $A_2(X) \cdot (B_1(X) - B_2(X)) \in I$.
Puisque $I$ est fermé sous l'addition, la somme de ces deux éléments est dans $I$.
Par conséquent, $(A_1(X) - A_2(X)) \cdot B_1(X) + A_2(X) \cdot (B_1(X) - B_2(X)) \in I$.
Ainsi, $[A_1(X) \cdot B_1(X)] = [A_2(X) \cdot B_2(X)]$.
L'opération de multiplication est bien définie.

### 4. Démonstration que $(E, +, \cdot)$ est un corps

L'ensemble $\mathbb{R}[X]$ est un anneau commutatif unitaire. Puisque $I$ est un idéal de $\mathbb{R}[X]$, l'ensemble quotient $E = \mathbb{R}[X]/I$ muni des opérations induites est un anneau commutatif unitaire.
*   L'élément neutre pour l'addition est $[0] = [0X+0]$.
*   L'élément neutre pour la multiplication est $[1] = [0X+1]$.

Pour montrer que $(E, +, \cdot)$ est un corps, il faut démontrer que tout élément non nul de $E$ possède un inverse multiplicatif.
Soit $[aX+b] \in E$ un élément non nul. Cela signifie que $aX+b \notin I$.
Comme $aX+b$ est de degré au plus 1, et $P(X)=X^2+1$ est de degré 2, $aX+b$ ne peut être un multiple de $P(X)$ à moins que $aX+b$ ne soit le polynôme nul.
Donc, si $[aX+b] \neq [0]$, alors $aX+b$ n'est pas le polynôme nul, ce qui implique que $a \neq 0$ ou $b \neq 0$.

Nous cherchons un élément $[cX+d] \in E$ tel que $[aX+b] \cdot [cX+d] = [1]$.
Par définition de la multiplication dans $E$, cela signifie que $[(aX+b)(cX+d)] = [1]$.
C'est équivalent à dire que $(aX+b)(cX+d) - 1 \in I$.
Autrement dit, $(aX+b)(cX+d) \equiv 1 \pmod{X^2+1}$.

Développons le produit $(aX+b)(cX+d)$ :
$$(aX+b)(cX+d) = acX^2 + adX + bcX + bd = acX^2 + (ad+bc)X + bd$$
Puisque $X^2+1 \in I$, nous avons $X^2+1 \equiv 0 \pmod{X^2+1}$, ce qui implique $X^2 \equiv -1 \pmod{X^2+1}$.
En substituant $X^2$ par $-1$ dans l'expression du produit :
$$acX^2 + (ad+bc)X + bd \equiv ac(-1) + (ad+bc)X + bd \pmod{X^2+1}$$
$$\equiv (bd-ac) + (ad+bc)X \pmod{X^2+1}$$
Nous voulons que cette expression soit équivalente à $1 \pmod{X^2+1}$.
Par l'unicité du représentant de degré au plus 1 (démontrée en partie 2), nous devons avoir :
$$(bd-ac) + (ad+bc)X = 1 \cdot X^0 + 0 \cdot X^1$$
Ceci nous conduit au système d'équations linéaires en $c$ et $d$ :
1.  $ad + bc = 0$
2.  $bd - ac = 1$

Nous résolvons ce système pour $c$ et $d$. Multiplions la première équation par $d$ et la seconde par $a$ :
1.  $ad^2 + bcd = 0$
2.  $abd - a^2c = a$

Multiplions la première équation par $b$ et la seconde par $d$ :
1.  $abd + b^2c = 0$
2.  $bd^2 - acd = d$

Revenons au système de base :
$bc + ad = 0 \quad (L_1)$
$-ac + bd = 1 \quad (L_2)$

Multiplions $(L_1)$ par $b$ et $(L_2)$ par $a$ :
$b^2c + abd = 0$
$-a^2c + abd = a$
Soustraire la deuxième de la première :
$(b^2c + abd) - (-a^2c + abd) = 0 - a$
$(b^2+a^2)c = -a$
Donc, $c = \frac{-a}{a^2+b^2}$.

Multiplions $(L_1)$ par $a$ et $(L_2)$ par $b$ :
$abc + a^2d = 0$
$-abc + b^2d = b$
Additionner les deux équations :
$(abc + a^2d) + (-abc + b^2d) = 0 + b$
$(a^2+b^2)d = b$
Donc, $d = \frac{b}{a^2+b^2}$.

Puisque $[aX+b] \neq [0]$, nous avons $a \neq 0$ ou $b \neq 0$, ce qui implique $a^2+b^2 \neq 0$.
Par conséquent, $c$ et $d$ sont des nombres réels bien définis.
L'inverse de $[aX+b]$ est donc $\left[\frac{-a}{a^2+b^2}X + \frac{b}{a^2+b^2}\right]$.
Puisque tout élément non nul de $E$ possède un inverse multiplicatif, $(E, +, \cdot)$ est un corps.

### 5. Établissement d'un isomorphisme avec le corps des nombres complexes

Nous allons définir une application $\phi: E \to \mathbb{C}$ et montrer qu'elle est un isomorphisme de corps.
Rappelons que les éléments de $E$ sont de la forme $[aX+b]$ où $a,b \in \mathbb{R}$.
Les nombres complexes sont de la forme $x+yi$ où $x,y \in \mathbb{R}$.

Définissons $\phi$ par :
$$\phi([aX+b]) = b + ai$$

**a) $\phi$ est bien définie :**
Comme chaque classe d'équivalence $[A(X)]$ a un unique représentant de la forme $aX+b$ (démontré en partie 2), l'application $\phi$ associe une valeur unique à chaque élément de $E$. Donc $\phi$ est bien définie.

**b) $\phi$ est un homomorphisme d'anneaux :**
Nous devons montrer que $\phi$ préserve l'addition et la multiplication.

*   **Préservation de l'addition :**
    Soient $[aX+b], [cX+d] \in E$.
    $$\phi([aX+b] + [cX+d]) = \phi([(a+c)X + (b+d)])$$
    Par définition de $\phi$ :
    $$= (b+d) + (a+c)i$$
    D'autre part :
    $$\phi([aX+b]) + \phi([cX+d]) = (b+ai) + (d+ci)$$
    $$= (b+d) + (a+c)i$$
    Les deux expressions sont égales, donc $\phi$ est un homomorphisme additif.

*   **Préservation de la multiplication :**
    Soient $[aX+b], [cX+d] \in E$.
    Nous avons montré en partie 4 que $[aX+b] \cdot [cX+d] = [(bd-ac) + (ad+bc)X]$.
    Donc :
    $$\phi([aX+b] \cdot [cX+d]) = \phi([(ad+bc)X + (bd-ac)])$$
    Par définition de $\phi$ :
    $$= (bd-ac) + (ad+bc)i$$
    D'autre part, calculons le produit dans $\mathbb{C}$ :
    $$\phi([aX+b]) \cdot \phi([cX+d]) = (b+ai) \cdot (d+ci)$$
    $$= bd + bci + adi + aci^2$$
    Comme $i^2 = -1$ :
    $$= bd + (bc+ad)i - ac$$
    $$= (bd-ac) + (ad+bc)i$$
    Les deux expressions sont égales, donc $\phi$ est un homomorphisme multiplicatif.

Puisque $\phi$ préserve l'addition et la multiplication, c'est un homomorphisme d'anneaux.

**c) $\phi$ est bijectif :**
*   **Injectivité :**
    Supposons que $\phi([aX+b]) = \phi([cX+d])$.
    Cela signifie $b+ai = d+ci$.
    Puisque $a, b, c, d$ sont des nombres réels, l'égalité de deux nombres complexes implique l'égalité de leurs parties réelles et de leurs parties imaginaires.
    Donc, $b=d$ et $a=c$.
    Ceci implique que $aX+b = cX+d$.
    Par conséquent, $[aX+b] = [cX+d]$.
    L'application $\phi$ est donc injective.

*   **Surjectivité :**
    Soit un nombre complexe arbitraire $z = x+yi \in \mathbb{C}$, où $x, y \in \mathbb{R}$.
    Nous cherchons un élément $[aX+b] \in E$ tel que $\phi([aX+b]) = x+yi$.
    En posant $a=y$ et $b=x$, nous avons $[yX+x] \in E$.
    Alors $\phi([yX+x]) = x+yi$.
    Tout nombre complexe $x+yi$ est l'image d'un élément de $E$ sous $\phi$.
    L'application $\phi$ est donc surjective.

Puisque $\phi$ est un homomorphisme d'anneaux bijectif, c'est un isomorphisme d'anneaux.
Comme $E$ et $\mathbb{C}$ sont des corps, $\phi$ est un isomorphisme de corps.
Ainsi, le corps $(E, +, \cdot)$ est isomorphe au corps des nombres complexes $(\mathbb{C}, +, \cdot)$.

---