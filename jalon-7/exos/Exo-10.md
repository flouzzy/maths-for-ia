# Exercice 10 : Opérateur de Différence Finie et Base de Newton

## Énoncé

Soit $\mathbb{K}$ un corps commutatif.
Soit $n \in \mathbb{N}^*$ un entier naturel non nul.
Soit $E = \mathbb{P}_n[X]$ le $\mathbb{K}$-espace vectoriel des polynômes de degré au plus $n$.
Soit $a \in \mathbb{K}$ un scalaire fixé et non nul (i.e., $a \neq 0$).

On définit une famille de polynômes $\mathcal{B} = (P_0(X), P_1(X), \dots, P_n(X))$ dans $E$ par :
$P_0(X) = 1$
et pour tout $k \in \{1, \dots, n\}$, $P_k(X) = \prod_{j=0}^{k-1} (X-ja)$.

On définit également l'opérateur de différence finie $D_a: E \to E$ par $D_a(P(X)) = \frac{P(X+a)-P(X)}{a}$ pour tout $P(X) \in E$.

1.  **Nature de la famille $\mathcal{B}$ :**
    Démontrer que la famille $\mathcal{B}$ est une base de $E$.

2.  **Action de l'opérateur $D_a$ sur $\mathcal{B}$ :**
    Pour tout $k \in \{0, \dots, n\}$, calculer $D_a(P_k(X))$ et exprimer le résultat en fonction des polynômes de la famille $\mathcal{B}$.

3.  **Coefficients de la série de Newton généralisée :**
    Soit $P(X)$ un polynôme quelconque de $E$.
    Puisque $\mathcal{B}$ est une base de $E$, il existe une unique famille de scalaires $(c_0, c_1, \dots, c_n) \in \mathbb{K}^{n+1}$ telle que $P(X) = \sum_{k=0}^n c_k P_k(X)$.
    Exprimer chaque coefficient $c_k$ en fonction de $P(X)$ et des applications successives de l'opérateur $D_a$ évaluées en $X=0$.

## Correction Détaillée

### 1. Nature de la famille $\mathcal{B}$

Soit $\mathbb{K}$ un corps commutatif.
Soit $n \in \mathbb{N}^*$.
Soit $E = \mathbb{P}_n[X]$ le $\mathbb{K}$-espace vectoriel des polynômes de degré au plus $n$.
La dimension de $E$ est $\dim(E) = n+1$.

La famille $\mathcal{B} = (P_0(X), P_1(X), \dots, P_n(X))$ est définie par :
$P_0(X) = 1$
et pour tout $k \in \{1, \dots, n\}$, $P_k(X) = \prod_{j=0}^{k-1} (X-ja)$.

Calculons le degré de chaque polynôme $P_k(X)$ :
Pour $k=0$, $P_0(X) = 1$. Le degré de $P_0(X)$ est $\deg(P_0) = 0$.
Pour $k \in \{1, \dots, n\}$, $P_k(X) = X(X-a)(X-2a)\dots(X-(k-1)a)$.
Ce polynôme est un produit de $k$ termes de la forme $(X-ja)$.
Le terme dominant de $P_k(X)$ est $X^k$.
Ainsi, le degré de $P_k(X)$ est $\deg(P_k) = k$.

La famille $\mathcal{B}$ est composée de $n+1$ polynômes : $P_0(X), P_1(X), \dots, P_n(X)$.
Les degrés de ces polynômes sont respectivement $0, 1, \dots, n$.
Puisque les degrés des polynômes de la famille $\mathcal{B}$ sont tous distincts, la famille $\mathcal{B}$ est une famille échelonnée en degrés.
Une famille échelonnée en degrés est toujours une famille libre.
De plus, la famille $\mathcal{B}$ contient $n+1$ vecteurs (polynômes) et la dimension de l'espace $E$ est $n+1$.
Une famille libre de $n+1$ vecteurs dans un espace de dimension $n+1$ est une base de cet espace.
Par conséquent, la famille $\mathcal{B}$ est une base de $E$.

### 2. Action de l'opérateur $D_a$ sur $\mathcal{B}$

Soit $a \in \mathbb{K}$ un scalaire non nul.
L'opérateur $D_a: E \to E$ est défini par $D_a(P(X)) = \frac{P(X+a)-P(X)}{a}$.

Calculons $D_a(P_k(X))$ pour chaque $k \in \{0, \dots, n\}$.

**Cas $k=0$ :**
$P_0(X) = 1$.
$D_a(P_0(X)) = \frac{P_0(X+a)-P_0(X)}{a} = \frac{1-1}{a} = \frac{0}{a} = 0$.
Donc, $D_a(P_0(X)) = 0$.

**Cas $k \ge 1$ :**
Pour $k \in \{1, \dots, n\}$, $P_k(X) = \prod_{j=0}^{k-1} (X-ja)$.
Calculons $P_k(X+a)$:
$P_k(X+a) = \prod_{j=0}^{k-1} ((X+a)-ja)$
$P_k(X+a) = (X+a)(X+a-a)(X+a-2a)\dots(X+a-(k-1)a)$
$P_k(X+a) = (X+a)X(X-a)\dots(X-(k-2)a)$.

Maintenant, calculons la différence $P_k(X+a) - P_k(X)$:
$P_k(X+a) - P_k(X) = (X+a)X(X-a)\dots(X-(k-2)a) - X(X-a)\dots(X-(k-1)a)$.
On peut factoriser le terme $X(X-a)\dots(X-(k-2)a)$ :
$P_k(X+a) - P_k(X) = \left( \prod_{j=0}^{k-2} (X-ja) \right) \left[ (X+a) - (X-(k-1)a) \right]$.
Le terme $\prod_{j=0}^{k-2} (X-ja)$ est précisément $P_{k-1}(X)$.
Le terme entre crochets est :
$(X+a) - (X-(k-1)a) = X+a-X+(k-1)a = a+(k-1)a = ka$.

Donc, pour $k \ge 1$:
$P_k(X+a) - P_k(X) = P_{k-1}(X) \cdot (ka)$.

Enfin, nous pouvons calculer $D_a(P_k(X))$ :
$D_a(P_k(X)) = \frac{P_k(X+a)-P_k(X)}{a} = \frac{ka \cdot P_{k-1}(X)}{a}$.
Puisque $a \neq 0$, nous pouvons simplifier par $a$:
$D_a(P_k(X)) = k P_{k-1}(X)$ pour $k \ge 1$.

En résumé :
$D_a(P_0(X)) = 0$
$D_a(P_k(X)) = k P_{k-1}(X)$ pour $k \in \{1, \dots, n\}$.

### 3. Coefficients de la série de Newton généralisée

Soit $P(X)$ un polynôme quelconque de $E$.
Puisque $\mathcal{B}$ est une base de $E$, il existe une unique famille de scalaires $(c_0, c_1, \dots, c_n) \in \mathbb{K}^{n+1}$ telle que $P(X) = \sum_{k=0}^n c_k P_k(X)$.

Nous allons exprimer chaque coefficient $c_k$ en fonction de $P(X)$ et des applications successives de l'opérateur $D_a$ évaluées en $X=0$.

Tout d'abord, évaluons les polynômes $P_k(X)$ en $X=0$:
$P_0(0) = 1$.
Pour $k \ge 1$, $P_k(X) = X(X-a)\dots(X-(k-1)a)$.
Donc, $P_k(0) = 0 \cdot (-a) \cdot (-2a) \dots (-(k-1)a) = 0$ pour $k \ge 1$.

Maintenant, appliquons l'opérateur $D_a$ de manière répétée à $P(X)$ et évaluons en $X=0$.

**Pour $c_0$ :**
$P(X) = c_0 P_0(X) + c_1 P_1(X) + \dots + c_n P_n(X)$.
Évaluons en $X=0$:
$P(0) = c_0 P_0(0) + c_1 P_1(0) + \dots + c_n P_n(0)$.
En utilisant les valeurs de $P_k(0)$:
$P(0) = c_0 \cdot 1 + c_1 \cdot 0 + \dots + c_n \cdot 0$.
Donc, $c_0 = P(0)$.

**Pour $c_1$ :**
Appliquons $D_a$ à $P(X)$:
$D_a(P(X)) = D_a\left(\sum_{k=0}^n c_k P_k(X)\right)$.
Par linéarité de $D_a$:
$D_a(P(X)) = \sum_{k=0}^n c_k D_a(P_k(X))$.
En utilisant les résultats de la partie 2 :
$D_a(P(X)) = c_0 D_a(P_0(X)) + \sum_{k=1}^n c_k D_a(P_k(X))$
$D_a(P(X)) = c_0 \cdot 0 + \sum_{k=1}^n c_k \cdot k P_{k-1}(X)$
$D_a(P(X)) = \sum_{k=1}^n c_k k P_{k-1}(X)$.
Évaluons en $X=0$:
$D_a(P(0)) = \sum_{k=1}^n c_k k P_{k-1}(0)$.
Le seul terme non nul dans cette somme est lorsque $k-1=0$, c'est-à-dire $k=1$:
$D_a(P(0)) = c_1 \cdot 1 \cdot P_0(0) + c_2 \cdot 2 \cdot P_1(0) + \dots + c_n \cdot n \cdot P_{n-1}(0)$.
$D_a(P(0)) = c_1 \cdot 1 \cdot 1 + c_2 \cdot 2 \cdot 0 + \dots + c_n \cdot n \cdot 0$.
Donc, $c_1 = D_a(P(0))$.

**Pour $c_2$ :**
Appliquons $D_a$ une deuxième fois à $P(X)$, c'est-à-dire $D_a^2(P(X)) = D_a(D_a(P(X)))$.
Nous avons $D_a(P(X)) = \sum_{k=1}^n c_k k P_{k-1}(X)$.
$D_a^2(P(X)) = D_a\left(\sum_{k=1}^n c_k k P_{k-1}(X)\right) = \sum_{k=1}^n c_k k D_a(P_{k-1}(X))$.
En utilisant les résultats de la partie 2 :
$D_a^2(P(X)) = c_1 \cdot 1 \cdot D_a(P_0(X)) + \sum_{k=2}^n c_k k D_a(P_{k-1}(X))$
$D_a^2(P(X)) = c_1 \cdot 1 \cdot 0 + \sum_{k=2}^n c_k k (k-1) P_{k-2}(X)$
$D_a^2(P(X)) = \sum_{k=2}^n c_k k(k-1) P_{k-2}(X)$.
Évaluons en $X=0$:
$D_a^2(P(0)) = \sum_{k=2}^n c_k k(k-1) P_{k-2}(0)$.
Le seul terme non nul dans cette somme est lorsque $k-2=0$, c'est-à-dire $k=2$:
$D_a^2(P(0)) = c_2 \cdot 2(2-1) P_0(0) + c_3 \cdot 3(2) P_1(0) + \dots$.
$D_a^2(P(0)) = c_2 \cdot 2 \cdot 1 \cdot 1 + c_3 \cdot 6 \cdot 0 + \dots$.
Donc, $c_2 = \frac{D_a^2(P(0))}{2}$.

**Généralisation pour $c_m$ :**
Nous pouvons observer un schéma. Appliquons l'opérateur $D_a$ $m$ fois.
$D_a^m(P(X)) = D_a^{m-1}(D_a(P(X)))$.
En répétant le processus, on obtient :
$D_a^m(P(X)) = \sum_{k=m}^n c_k k(k-1)\dots(k-m+1) P_{k-m}(X)$.
Le produit $k(k-1)\dots(k-m+1)$ peut s'écrire $\frac{k!}{(k-m)!}$.
$D_a^m(P(X)) = \sum_{k=m}^n c_k \frac{k!}{(k-m)!} P_{k-m}(X)$.
Évaluons en $X=0$:
$D_a^m(P(0)) = \sum_{k=m}^n c_k \frac{k!}{(k-m)!} P_{k-m}(0)$.
Le seul terme non nul dans cette somme est lorsque $k-m=0$, c'est-à-dire $k=m$:
$D_a^m(P(0)) = c_m \frac{m!}{(m-m)!} P_0(0) + \sum_{k=m+1}^n c_k \frac{k!}{(k-m)!} P_{k-m}(0)$.
$D_a^m(P(0)) = c_m \frac{m!}{0!} \cdot 1 + \sum_{k=m+1}^n c_k \frac{k!}{(k-m)!} \cdot 0$.
$D_a^m(P(0)) = c_m \cdot m!$.

Par conséquent, pour tout $m \in \{0, \dots, n\}$:
$c_m = \frac{D_a^m(P(0))}{m!}$.
(Pour $m=0$, $D_a^0(P(X)) = P(X)$, et $0!=1$, donc $c_0 = \frac{P(0)}{1} = P(0)$, ce qui est cohérent).

Ces coefficients sont les coefficients de la série de Newton généralisée (ou série de différences finies) de $P(X)$ par rapport au point $0$ et au pas $a$.
