En tant que Professeur de Mathématiques Émérite, je vous présente l'exercice 9, conçu pour mettre à l'épreuve votre compréhension approfondie des relations d'équivalence, des ensembles quotients et des structures algébriques. La difficulté est maximale, exigeant une rigueur et une clarté irréprochables à chaque étape.

---

# Exercice 9 : Anneaux Quotients de Séquences à Support Quasi-Infini
**Difficulté :** ⭐⭐⭐⭐⭐

## Énoncé
Soit $E = \mathbb{R}^{\mathbb{N}}$ l'ensemble de toutes les suites réelles $u = (u_n)_{n \in \mathbb{N}}$. On munit $E$ des opérations d'addition et de multiplication terme à terme, ainsi que de la multiplication par un scalaire réel :
Pour $u = (u_n)$ et $v = (v_n)$ dans $E$, et $\lambda \in \mathbb{R}$:
$$ (u+v)_n = u_n + v_n $$
$$ (u \cdot v)_n = u_n v_n $$
$$ (\lambda u)_n = \lambda u_n $$
Nous admettons que $(E, +, \cdot)$ est un anneau commutatif unitaire (l'élément neutre pour la multiplication étant la suite $(1, 1, 1, \dots)$) et que $(E, +, \cdot_{\text{scalaire}})$ est un espace vectoriel sur $\mathbb{R}$.

On définit une relation $\sim$ sur $E$ par :
$$ u \sim v \quad \iff \quad \{ n \in \mathbb{N} \mid u_n \neq v_n \} \text{ est un ensemble fini.} $$
Autrement dit, deux suites sont équivalentes si elles diffèrent seulement sur un nombre fini d'indices.

1.  Démontrer que $\sim$ est une relation d'équivalence sur $E$.
2.  Soit $I = \{ u \in E \mid \{ n \in \mathbb{N} \mid u_n \neq 0 \} \text{ est un ensemble fini} \}$. Cet ensemble est appelé l'ensemble des suites à support fini.
    Démontrer que $I$ est un idéal de l'anneau $E$.
3.  En déduire que l'ensemble quotient $E/\sim$ peut être muni d'une structure d'anneau commutatif unitaire. Définir explicitement les opérations d'addition et de multiplication sur $E/\sim$ et démontrer que ces opérations sont bien définies.
4.  L'anneau quotient $(E/\sim, +, \cdot)$ est-il intègre ? Justifier rigoureusement votre réponse en produisant, si nécessaire, un contre-exemple explicite respectant la règle du "Zéro Ellipse Mathématique".
5.  L'anneau quotient $(E/\sim, +, \cdot)$ est-il un corps ? Justifier rigoureusement votre réponse.

## Correction Détaillée

### 1. Démontrer que $\sim$ est une relation d'équivalence sur $E$.

Pour démontrer que $\sim$ est une relation d'équivalence sur $E$, nous devons vérifier les trois propriétés suivantes : réflexivité, symétrie et transitivité.

#### Réflexivité : Pour tout $u \in E$, $u \sim u$.
Par définition de la relation $\sim$, $u \sim u$ si et seulement si l'ensemble des indices $n$ pour lesquels $u_n \neq u_n$ est fini.
L'ensemble $\{ n \in \mathbb{N} \mid u_n \neq u_n \}$ est l'ensemble vide, car pour tout $n \in \mathbb{N}$, $u_n = u_n$.
L'ensemble vide est un ensemble fini.
Par conséquent, la relation $\sim$ est réflexive.

#### Symétrie : Pour tout $u, v \in E$, si $u \sim v$, alors $v \sim u$.
Supposons que $u \sim v$.
Par définition de la relation $\sim$, cela signifie que l'ensemble $A = \{ n \in \mathbb{N} \mid u_n \neq v_n \}$ est un ensemble fini.
Pour montrer que $v \sim u$, nous devons démontrer que l'ensemble $B = \{ n \in \mathbb{N} \mid v_n \neq u_n \}$ est un ensemble fini.
Par définition de l'inégalité, $u_n \neq v_n$ est logiquement équivalent à $v_n \neq u_n$.
Par conséquent, l'ensemble $B$ est identique à l'ensemble $A$.
Puisque $A$ est un ensemble fini, $B$ est également un ensemble fini.
Par conséquent, $v \sim u$.
Ainsi, la relation $\sim$ est symétrique.

#### Transitivité : Pour tout $u, v, w \in E$, si $u \sim v$ et $v \sim w$, alors $u \sim w$.
Supposons que $u \sim v$ et $v \sim w$.
Par définition de la relation $\sim$, $u \sim v$ signifie que l'ensemble $A = \{ n \in \mathbb{N} \mid u_n \neq v_n \}$ est un ensemble fini.
De même, $v \sim w$ signifie que l'ensemble $B = \{ n \in \mathbb{N} \mid v_n \neq w_n \}$ est un ensemble fini.
Pour montrer que $u \sim w$, nous devons démontrer que l'ensemble $C = \{ n \in \mathbb{N} \mid u_n \neq w_n \}$ est un ensemble fini.

Considérons un indice $n \in \mathbb{N}$ tel que $n \notin A$ et $n \notin B$.
Si $n \notin A$, alors $u_n = v_n$.
Si $n \notin B$, alors $v_n = w_n$.
Par conséquent, si $n \notin A \cup B$, alors $u_n = v_n = w_n$, ce qui implique $u_n = w_n$.
Ceci signifie que si $u_n \neq w_n$, alors nécessairement $n$ doit appartenir à $A$ ou à $B$.
Autrement dit, l'ensemble $C = \{ n \in \mathbb{N} \mid u_n \neq w_n \}$ est un sous-ensemble de $A \cup B$.
Puisque $A$ et $B$ sont des ensembles finis, leur union $A \cup B$ est également un ensemble fini.
Tout sous-ensemble d'un ensemble fini est lui-même fini.
Par conséquent, $C$ est un ensemble fini.
Ainsi, $u \sim w$.
La relation $\sim$ est transitive.

Puisque la relation $\sim$ est réflexive, symétrique et transitive, c'est une relation d'équivalence sur $E$.

### 2. Démontrer que $I$ est un idéal de l'anneau $E$.

L'ensemble $I$ est défini comme $I = \{ u \in E \mid \{ n \in \mathbb{N} \mid u_n \neq 0 \} \text{ est un ensemble fini} \}$.
Pour démontrer que $I$ est un idéal de l'anneau commutatif unitaire $E$, nous devons vérifier deux propriétés :
1.  $(I, +)$ est un sous-groupe de $(E, +)$.
2.  Pour tout $u \in I$ et tout $v \in E$, le produit $u \cdot v$ appartient à $I$.

#### Propriété 1 : $(I, +)$ est un sous-groupe de $(E, +)$.
Pour cela, nous vérifions trois conditions :
*   **$I$ est non vide :**
    Considérons la suite nulle $0_E = (0, 0, 0, \dots)$.
    L'ensemble $\{ n \in \mathbb{N} \mid (0_E)_n \neq 0 \}$ est l'ensemble vide, car $(0_E)_n = 0$ pour tout $n$.
    L'ensemble vide est un ensemble fini.
    Donc, $0_E \in I$. Par conséquent, $I$ est non vide.

*   **Stabilité par addition :** Pour tout $u, v \in I$, $u+v \in I$.
    Supposons $u \in I$ et $v \in I$.
    Par définition, l'ensemble $S_u = \{ n \in \mathbb{N} \mid u_n \neq 0 \}$ est fini.
    De même, l'ensemble $S_v = \{ n \in \mathbb{N} \mid v_n \neq 0 \}$ est fini.
    Nous devons montrer que l'ensemble $S_{u+v} = \{ n \in \mathbb{N} \mid (u+v)_n \neq 0 \}$ est fini.
    Par définition de l'addition terme à terme, $(u+v)_n = u_n + v_n$.
    Si $(u+v)_n \neq 0$, alors $u_n + v_n \neq 0$.
    Ceci implique que $u_n$ ou $v_n$ doit être non nul. En effet, si $u_n=0$ et $v_n=0$, alors $u_n+v_n=0$.
    Donc, si $u_n+v_n \neq 0$, alors $u_n \neq 0$ ou $v_n \neq 0$.
    Par conséquent, l'ensemble $S_{u+v}$ est un sous-ensemble de $S_u \cup S_v$.
    Puisque $S_u$ et $S_v$ sont des ensembles finis, leur union $S_u \cup S_v$ est un ensemble fini.
    Tout sous-ensemble d'un ensemble fini est lui-même fini.
    Par conséquent, $S_{u+v}$ est un ensemble fini.
    Ainsi, $u+v \in I$.

*   **Stabilité par opposé (inverse additif) :** Pour tout $u \in I$, $-u \in I$.
    Supposons $u \in I$.
    Par définition, l'ensemble $S_u = \{ n \in \mathbb{N} \mid u_n \neq 0 \}$ est fini.
    Nous devons montrer que l'ensemble $S_{-u} = \{ n \in \mathbb{N} \mid (-u)_n \neq 0 \}$ est fini.
    Par définition de la multiplication par un scalaire, $(-u)_n = -u_n$.
    L'expression $-u_n \neq 0$ est logiquement équivalente à $u_n \neq 0$.
    Par conséquent, l'ensemble $S_{-u}$ est identique à l'ensemble $S_u$.
    Puisque $S_u$ est un ensemble fini, $S_{-u}$ est également un ensemble fini.
    Ainsi, $-u \in I$.

Donc, $(I, +)$ est un sous-groupe de $(E, +)$.

#### Propriété 2 : Absorption par multiplication : Pour tout $u \in I$ et tout $v \in E$, $u \cdot v \in I$.
Supposons $u \in I$ et $v \in E$.
Par définition, l'ensemble $S_u = \{ n \in \mathbb{N} \mid u_n \neq 0 \}$ est fini.
Nous devons montrer que l'ensemble $S_{u \cdot v} = \{ n \in \mathbb{N} \mid (u \cdot v)_n \neq 0 \}$ est fini.
Par définition de la multiplication terme à terme, $(u \cdot v)_n = u_n v_n$.
Si $(u \cdot v)_n \neq 0$, alors $u_n v_n \neq 0$.
Ceci implique que $u_n \neq 0$ et $v_n \neq 0$.
En particulier, si $u_n v_n \neq 0$, alors $u_n \neq 0$.
Par conséquent, l'ensemble $S_{u \cdot v}$ est un sous-ensemble de $S_u$.
Puisque $S_u$ est un ensemble fini, tout sous-ensemble de $S_u$ est également fini.
Par conséquent, $S_{u \cdot v}$ est un ensemble fini.
Ainsi, $u \cdot v \in I$.

Puisque $(I, +)$ est un sous-groupe de $(E, +)$ et que $I$ absorbe la multiplication de $E$, $I$ est un idéal de l'anneau $E$.

### 3. Structure d'anneau commutatif unitaire sur $E/\sim$. Définition et vérification des opérations.

La relation d'équivalence $\sim$ est directement liée à l'idéal $I$.
Nous avons $u \sim v \iff \{ n \in \mathbb{N} \mid u_n \neq v_n \}$ est fini.
Ceci est équivalent à dire que la suite $(u_n - v_n)$ est une suite dont l'ensemble des indices où les termes sont non nuls est fini.
Par définition de $I$, ceci signifie que $u-v \in I$.
Donc, la relation $\sim$ est la relation d'équivalence associée à l'idéal $I$.
L'ensemble quotient $E/\sim$ est donc l'anneau quotient $E/I$.
Puisque $I$ est un idéal de l'anneau $E$, l'ensemble quotient $E/I$ est naturellement muni d'une structure d'anneau.

Soit $[u]$ la classe d'équivalence d'une suite $u \in E$.
$$ [u] = \{ v \in E \mid v \sim u \} = \{ v \in E \mid v-u \in I \} = u+I $$

#### Définition des opérations sur $E/\sim$ :
*   **Addition :** Pour tout $[u], [v] \in E/\sim$, on définit leur somme par :
    $$ [u] + [v] = [u+v] $$
*   **Multiplication :** Pour tout $[u], [v] \in E/\sim$, on définit leur produit par :
    $$ [u] \cdot [v] = [u \cdot v] $$

#### Vérification que les opérations sont bien définies :
Nous devons montrer que le résultat de l'opération ne dépend pas du choix des représentants de la classe d'équivalence.

*   **Addition bien définie :**
    Soient $[u], [v] \in E/\sim$. Supposons que $[u] = [u']$ et $[v] = [v']$ pour d'autres représentants $u', v' \in E$.
    Puisque $[u] = [u']$, nous avons $u \sim u'$, ce qui signifie $u-u' \in I$.
    Puisque $[v] = [v']$, nous avons $v \sim v'$, ce qui signifie $v-v' \in I$.
    Nous devons montrer que $[u+v] = [u'+v']$, ce qui signifie $(u+v) \sim (u'+v')$, ou encore $(u+v) - (u'+v') \in I$.
    Considérons la différence :
    $$ (u+v) - (u'+v') = (u-u') + (v-v') $$
    Nous savons que $u-u' \in I$ et $v-v' \in I$.
    Puisque $I$ est un idéal, il est en particulier un sous-groupe additif de $E$. Donc, la somme de deux éléments de $I$ appartient à $I$.
    Par conséquent, $(u-u') + (v-v') \in I$.
    Ainsi, $(u+v) - (u'+v') \in I$, ce qui implique $[u+v] = [u'+v']$.
    L'addition est bien définie sur $E/\sim$.

*   **Multiplication bien définie :**
    Soient $[u], [v] \in E/\sim$. Supposons que $[u] = [u']$ et $[v] = [v']$ pour d'autres représentants $u', v' \in E$.
    Puisque $[u] = [u']$, nous avons $u-u' \in I$.
    Puisque $[v] = [v']$, nous avons $v-v' \in I$.
    Nous devons montrer que $[u \cdot v] = [u' \cdot v']$, ce qui signifie $(u \cdot v) \sim (u' \cdot v')$, ou encore $u \cdot v - u' \cdot v' \in I$.
    Considérons la différence :
    $$ u \cdot v - u' \cdot v' = u \cdot v - u' \cdot v + u' \cdot v - u' \cdot v' $$
    $$ u \cdot v - u' \cdot v' = (u-u') \cdot v + u' \cdot (v-v') $$
    Nous savons que $u-u' \in I$ et $v-v' \in I$.
    Puisque $I$ est un idéal, pour tout $x \in I$ et tout $y \in E$, le produit $x \cdot y$ appartient à $I$.
    Donc, $(u-u') \cdot v \in I$ (car $u-u' \in I$ et $v \in E$).
    De même, $u' \cdot (v-v') \in I$ (car $u' \in E$ et $v-v' \in I$).
    Puisque $I$ est un sous-groupe additif, la somme de deux éléments de $I$ appartient à $I$.
    Par conséquent, $(u-u') \cdot v + u' \cdot (v-v') \in I$.
    Ainsi, $u \cdot v - u' \cdot v' \in I$, ce qui implique $[u \cdot v] = [u' \cdot v']$.
    La multiplication est bien définie sur $E/\sim$.

Puisque les opérations d'addition et de multiplication sont bien définies, et puisque $E$ est un anneau commutatif unitaire et $I$ est un idéal, $E/\sim$ (qui est $E/I$) hérite naturellement de la structure d'anneau commutatif unitaire.
*   L'élément neutre pour l'addition est la classe de la suite nulle : $[0_E] = [(0,0,0,\dots)]$.
*   L'élément neutre pour la multiplication est la classe de la suite unitaire : $[1_E] = [(1,1,1,\dots)]$.
*   La commutativité et l'associativité des opérations, ainsi que la distributivité de la multiplication sur l'addition, découlent directement des propriétés correspondantes dans $E$ grâce à la définition des opérations sur les classes.

### 4. L'anneau quotient $(E/\sim, +, \cdot)$ est-il intègre ?

Un anneau commutatif unitaire est dit intègre (ou est un domaine d'intégrité) si le produit de deux éléments non nuls est toujours non nul. Autrement dit, pour tout $A, B \in E/\sim$, si $A \cdot B = [0_E]$, alors $A = [0_E]$ ou $B = [0_E]$.

Considérons deux classes d'équivalence non nulles $[u]$ et $[v]$ dans $E/\sim$.
Si $[u] \cdot [v] = [0_E]$, cela signifie que $[u \cdot v] = [0_E]$.
Par définition de la classe nulle, ceci signifie que $u \cdot v \in I$.
Autrement dit, l'ensemble $\{ n \in \mathbb{N} \mid (u \cdot v)_n \neq 0 \}$ est fini.
Puisque $(u \cdot v)_n = u_n v_n$, cela signifie que l'ensemble $\{ n \in \mathbb{N} \mid u_n v_n \neq 0 \}$ est fini.

Pour que $E/\sim$ ne soit pas intègre, nous devons trouver deux suites $u, v \in E$ telles que :
1.  $[u] \neq [0_E]$ (c'est-à-dire $u \notin I$)
2.  $[v] \neq [0_E]$ (c'est-à-dire $v \notin I$)
3.  $[u] \cdot [v] = [0_E]$ (c'est-à-dire $u \cdot v \in I$)

Considérons les suites suivantes :
Soit $u = (u_n)_{n \in \mathbb{N}}$ définie par :
$$ u_n = \begin{cases} 1 & \text{si } n \text{ est pair} \\ 0 & \text{si } n \text{ est impair} \end{cases} $$
Explicitons les premiers termes de $u$: $u = (1, 0, 1, 0, 1, 0, \dots)$.

Soit $v = (v_n)_{n \in \mathbb{N}}$ définie par :
$$ v_n = \begin{cases} 0 & \text{si } n \text{ est pair} \\ 1 & \text{si } n \text{ est impair} \end{cases} $$
Explicitons les premiers termes de $v$: $v = (0, 1, 0, 1, 0, 1, \dots)$.

Vérifions les conditions :
1.  **$[u] \neq [0_E]$ ?**
    L'ensemble $\{ n \in \mathbb{N} \mid u_n \neq 0 \}$ est l'ensemble de tous les entiers pairs $\mathbb{N}_{\text{pairs}} = \{0, 2, 4, \dots \}$.
    Cet ensemble est infini.
    Par conséquent, $u \notin I$, ce qui signifie $[u] \neq [0_E]$.

2.  **$[v] \neq [0_E]$ ?**
    L'ensemble $\{ n \in \mathbb{N} \mid v_n \neq 0 \}$ est l'ensemble de tous les entiers impairs $\mathbb{N}_{\text{impairs}} = \{1, 3, 5, \dots \}$.
    Cet ensemble est infini.
    Par conséquent, $v \notin I$, ce qui signifie $[v] \neq [0_E]$.

3.  **$[u] \cdot [v] = [0_E]$ ?**
    Calculons le produit terme à terme $u \cdot v = (u_n v_n)_{n \in \mathbb{N}}$.
    Pour tout $n \in \mathbb{N}$ :
    *   Si $n$ est pair, $u_n = 1$ et $v_n = 0$. Donc $(u \cdot v)_n = 1 \cdot 0 = 0$.
    *   Si $n$ est impair, $u_n = 0$ et $v_n = 1$. Donc $(u \cdot v)_n = 0 \cdot 1 = 0$.
    Par conséquent, $(u \cdot v)_n = 0$ pour tout $n \in \mathbb{N}$.
    La suite $u \cdot v$ est la suite nulle $0_E = (0, 0, 0, \dots)$.
    L'ensemble $\{ n \in \mathbb{N} \mid (u \cdot v)_n \neq 0 \}$ est l'ensemble vide, qui est fini.
    Par conséquent, $u \cdot v \in I$, ce qui signifie $[u \cdot v] = [0_E]$.

Nous avons trouvé deux éléments non nuls $[u]$ et $[v]$ dans $E/\sim$ dont le produit est l'élément nul $[0_E]$.
Par conséquent, l'anneau quotient $(E/\sim, +, \cdot)$ n'est pas intègre.

### 5. L'anneau quotient $(E/\sim, +, \cdot)$ est-il un corps ?

Un corps est un anneau commutatif unitaire où tout élément non nul possède un inverse multiplicatif. De plus, un corps est toujours un domaine d'intégrité (anneau intègre).

Nous avons démontré à la question 4 que l'anneau quotient $(E/\sim, +, \cdot)$ n'est pas intègre.
Puisqu'il n'est pas intègre, il ne peut pas être un corps.

Pour une justification plus directe, sans s'appuyer sur la non-intégrité (bien que ce soit suffisant), nous pouvons montrer qu'il existe un élément non nul dans $E/\sim$ qui n'a pas d'inverse multiplicatif.

Soit $[u]$ un élément non nul de $E/\sim$. Cela signifie que $u \notin I$, c'est-à-dire que l'ensemble $S_u = \{ n \in \mathbb{N} \mid u_n \neq 0 \}$ est infini.
Pour que $[u]$ ait un inverse multiplicatif $[v]$, il faut que $[u] \cdot [v] = [1_E]$, où $1_E = (1, 1, 1, \dots)$ est l'élément neutre multiplicatif de $E$.
Ceci signifie que $[u \cdot v] = [1_E]$.
Par définition de l'équivalence, cela signifie que $u \cdot v - 1_E \in I$.
Autrement dit, l'ensemble $\{ n \in \mathbb{N} \mid (u \cdot v)_n \neq (1_E)_n \}$ est fini.
Ceci implique qu'il existe un entier $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $(u \cdot v)_n = (1_E)_n = 1$.
Donc, pour tout $n \ge N$, $u_n v_n = 1$.
Ceci implique que pour tout $n \ge N$, $u_n \neq 0$ et $v_n = 1/u_n$.

Considérons à nouveau la suite $u = (u_n)_{n \in \mathbb{N}}$ définie par :
$$ u_n = \begin{cases} 1 & \text{si } n \text{ est pair} \\ 0 & \text{si } n \text{ est impair} \end{cases} $$
Nous avons déjà établi que $[u] \neq [0_E]$.
Pour que $[u]$ ait un inverse $[v]$, il faudrait qu'il existe un $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $u_n \neq 0$.
Cependant, pour la suite $u$ que nous avons choisie, $u_n = 0$ pour tous les indices impairs $n$.
Il y a une infinité d'indices impairs.
Donc, il n'existe aucun $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $u_n \neq 0$.
En particulier, pour tout $N \in \mathbb{N}$, nous pouvons trouver un indice impair $m \ge N$ (par exemple $m = 2N+1$ si $N$ est pair, $m=2N-1$ si $N$ est impair, ou simplement $m = \max(N, N+1)$ si l'un est impair) tel que $u_m = 0$.
Pour ces indices $m$, $u_m v_m = 0 \cdot v_m = 0 \neq 1$.
Par conséquent, il n'existe aucune suite $v \in E$ telle que $u \cdot v - 1_E \in I$.
Autrement dit, l'élément $[u]$ n'a pas d'inverse multiplicatif dans $E/\sim$.

Puisque nous avons trouvé un élément non nul $[u]$ dans $E/\sim$ qui ne possède pas d'inverse multiplicatif, l'anneau quotient $(E/\sim, +, \cdot)$ n'est pas un corps.