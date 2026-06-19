# Exercice 9 : Analyse d'un Sous-Espace de Polynômes à Contraintes Mixtes

## Énoncé

Soit $\mathbb{K}$ un corps commutatif.
Soit $n$ un entier naturel tel que $n \ge 1$.
On considère le $\mathbb{K}$-espace vectoriel $E = \mathbb{K}_n[X]$, l'ensemble des polynômes à coefficients dans $\mathbb{K}$ de degré inférieur ou égal à $n$.
Soient $a$ et $b$ deux scalaires distincts de $\mathbb{K}$, c'est-à-dire $a \in \mathbb{K}$, $b \in \mathbb{K}$ et $a \ne b$.

On définit l'ensemble $F$ comme suit :
$$F = \{ P \in E \mid P(a) = 0 \text{ et } P'(b) = 0 \}$$
où $P'(X)$ désigne le polynôme dérivé de $P(X)$.

1.  Démontrer rigoureusement que $F$ est un sous-espace vectoriel de $E$.
2.  Déterminer la dimension de $F$. On justifiera chaque étape de manière exhaustive.
3.  Construire une base explicite de $F$. On prouvera la nature de base de la famille construite.

## Correction Détaillée

Cher(ère) étudiant(e), abordons cet exercice avec la rigueur et la précision qui s'imposent en algèbre linéaire.

### Question 1 : Démontrer que $F$ est un sous-espace vectoriel de $E$.

Pour démontrer que $F$ est un sous-espace vectoriel de $E$, nous devons vérifier trois propriétés fondamentales :
1.  $F$ est non vide (il contient le vecteur nul de $E$).
2.  $F$ est stable par addition vectorielle.
3.  $F$ est stable par multiplication par un scalaire.

**1. $F$ est non vide :**
Considérons le polynôme nul, noté $0_E$, qui est l'élément neutre de l'addition dans $E$.
Le polynôme nul est défini par $0_E(X) = 0$ pour tout $X \in \mathbb{K}$.
Sa dérivée est $0_E'(X) = 0$ pour tout $X \in \mathbb{K}$.
Évaluons les conditions pour $0_E$:
$0_E(a) = 0$.
$0_E'(b) = 0$.
Les deux conditions sont satisfaites. Par conséquent, $0_E \in F$.
$F$ est donc un sous-ensemble non vide de $E$.

**2. $F$ est stable par addition vectorielle :**
Soient $P_1$ et $P_2$ deux polynômes quelconques appartenant à $F$.
Par définition de $F$, nous avons :
$P_1(a) = 0$ et $P_1'(b) = 0$.
$P_2(a) = 0$ et $P_2'(b) = 0$.
Considérons la somme $P_1 + P_2$. Puisque $P_1 \in E$ et $P_2 \in E$, et que $E$ est un $\mathbb{K}$-espace vectoriel, $P_1+P_2 \in E$.
Nous devons vérifier si $P_1+P_2$ satisfait les conditions de $F$.
Évaluons $(P_1+P_2)(a)$ :
$(P_1+P_2)(a) = P_1(a) + P_2(a)$ (par propriété d'évaluation des polynômes).
$(P_1+P_2)(a) = 0 + 0$ (en utilisant les conditions pour $P_1$ et $P_2$).
$(P_1+P_2)(a) = 0$.
Évaluons $(P_1+P_2)'(b)$ :
$(P_1+P_2)'(X) = P_1'(X) + P_2'(X)$ (par propriété de linéarité de la dérivation).
$(P_1+P_2)'(b) = P_1'(b) + P_2'(b)$ (par propriété d'évaluation des polynômes).
$(P_1+P_2)'(b) = 0 + 0$ (en utilisant les conditions pour $P_1$ et $P_2$).
$(P_1+P_2)'(b) = 0$.
Les deux conditions sont satisfaites. Donc, $P_1+P_2 \in F$.
$F$ est stable par addition vectorielle.

**3. $F$ est stable par multiplication par un scalaire :**
Soit $P$ un polynôme appartenant à $F$, et soit $\lambda$ un scalaire quelconque de $\mathbb{K}$.
Par définition de $F$, nous avons :
$P(a) = 0$ et $P'(b) = 0$.
Considérons le produit $\lambda P$. Puisque $P \in E$ et que $E$ est un $\mathbb{K}$-espace vectoriel, $\lambda P \in E$.
Nous devons vérifier si $\lambda P$ satisfait les conditions de $F$.
Évaluons $(\lambda P)(a)$ :
$(\lambda P)(a) = \lambda \cdot P(a)$ (par propriété d'évaluation des polynômes).
$(\lambda P)(a) = \lambda \cdot 0$ (en utilisant la condition pour $P$).
$(\lambda P)(a) = 0$.
Évaluons $(\lambda P)'(b)$ :
$(\lambda P)'(X) = \lambda \cdot P'(X)$ (par propriété de linéarité de la dérivation).
$(\lambda P)'(b) = \lambda \cdot P'(b)$ (par propriété d'évaluation des polynômes).
$(\lambda P)'(b) = \lambda \cdot 0$ (en utilisant la condition pour $P$).
$(\lambda P)'(b) = 0$.
Les deux conditions sont satisfaites. Donc, $\lambda P \in F$.
$F$ est stable par multiplication par un scalaire.

Puisque $F$ est non vide, stable par addition et stable par multiplication par un scalaire, $F$ est bien un sous-espace vectoriel de $E$.

### Question 2 : Déterminer la dimension de $F$.

Pour déterminer la dimension de $F$, nous allons utiliser le théorème du rang.
Considérons les applications linéaires suivantes :
Soit $\phi_1: E \to \mathbb{K}$ l'application définie par $\phi_1(P) = P(a)$.
Soit $\phi_2: E \to \mathbb{K}$ l'application définie par $\phi_2(P) = P'(b)$.
Ces deux applications sont des formes linéaires (linéaires de $E$ vers $\mathbb{K}$).
En effet, pour tout $P_1, P_2 \in E$ et tout $\lambda \in \mathbb{K}$:
$\phi_1(P_1 + \lambda P_2) = (P_1 + \lambda P_2)(a) = P_1(a) + \lambda P_2(a) = \phi_1(P_1) + \lambda \phi_1(P_2)$.
$\phi_2(P_1 + \lambda P_2) = (P_1 + \lambda P_2)'(b) = (P_1' + \lambda P_2')(b) = P_1'(b) + \lambda P_2'(b) = \phi_2(P_1) + \lambda \phi_2(P_2)$.

L'ensemble $F$ peut être exprimé comme l'intersection des noyaux de ces formes linéaires :
$F = \ker(\phi_1) \cap \ker(\phi_2)$.

Considérons l'application linéaire $\Phi: E \to \mathbb{K}^2$ définie par $\Phi(P) = (P(a), P'(b))$.
Le noyau de $\Phi$ est précisément $F$:
$\ker(\Phi) = \{ P \in E \mid \Phi(P) = (0,0) \} = \{ P \in E \mid P(a)=0 \text{ et } P'(b)=0 \} = F$.

D'après le théorème du rang, nous avons :
$\dim(E) = \dim(\ker(\Phi)) + \dim(\text{Im}(\Phi))$.
Nous savons que $\dim(E) = n+1$ (car la famille $(X^k)_{0 \le k \le n}$ est une base de $E$).
Donc, $\dim(F) = (n+1) - \dim(\text{Im}(\Phi))$.

Pour déterminer $\dim(\text{Im}(\Phi))$, nous devons trouver le rang de $\Phi$. L'espace d'arrivée est $\mathbb{K}^2$, donc $\dim(\text{Im}(\Phi))$ peut être 0, 1 ou 2.
Nous allons montrer que $\Phi$ est surjective, c'est-à-dire que $\text{Im}(\Phi) = \mathbb{K}^2$. Cela signifie que pour tout $(y_1, y_2) \in \mathbb{K}^2$, il existe un polynôme $P \in E$ tel que $P(a)=y_1$ et $P'(b)=y_2$.
Il suffit de trouver deux polynômes $P_1, P_2 \in E$ tels que leurs images par $\Phi$ forment une base de $\mathbb{K}^2$, par exemple $(1,0)$ et $(0,1)$.

**Construction de $P_1$ tel que $\Phi(P_1) = (1,0)$ :**
Nous cherchons $P_1 \in E$ tel que $P_1(a)=1$ et $P_1'(b)=0$.
Considérons le polynôme constant $P_1(X) = 1$.
$P_1(X)$ est de degré 0, donc $P_1 \in E$ puisque $n \ge 1$.
$P_1(a) = 1$.
$P_1'(X) = 0$, donc $P_1'(b) = 0$.
Ainsi, $P_1(X)=1$ satisfait les conditions.

**Construction de $P_2$ tel que $\Phi(P_2) = (0,1)$ :**
Nous cherchons $P_2 \in E$ tel que $P_2(a)=0$ et $P_2'(b)=1$.
Puisque $P_2(a)=0$, le polynôme $(X-a)$ doit être un facteur de $P_2(X)$.
Posons $P_2(X) = c(X-a)$ pour un certain scalaire $c \in \mathbb{K}$.
$P_2(X)$ est de degré 1, donc $P_2 \in E$ puisque $n \ge 1$.
$P_2(a) = c(a-a) = 0$. Cette condition est satisfaite.
Calculons la dérivée : $P_2'(X) = c$.
Nous voulons $P_2'(b)=1$, donc $c=1$.
Ainsi, $P_2(X) = X-a$ satisfait les conditions.

Puisque $P_1(X)=1$ et $P_2(X)=X-a$ sont des polynômes de $E$ (pour $n \ge 1$), et que $\Phi(P_1)=(1,0)$ et $\Phi(P_2)=(0,1)$, l'image de $\Phi$ contient une base de $\mathbb{K}^2$.
Par conséquent, $\text{Im}(\Phi) = \mathbb{K}^2$.
La dimension de l'image est $\dim(\text{Im}(\Phi)) = \dim(\mathbb{K}^2) = 2$.

En appliquant le théorème du rang :
$\dim(F) = \dim(E) - \dim(\text{Im}(\Phi))$
$\dim(F) = (n+1) - 2$
$\dim(F) = n-1$.

Cette dimension est valable pour $n \ge 1$.
(Note : Si $n=0$, $E=\mathbb{K}_0[X]=\mathbb{K}$. $P(X)=c_0$. $P'(X)=0$. $F = \{c_0 \in \mathbb{K} \mid c_0=0 \text{ et } 0=0\} = \{0\}$. $\dim(F)=0$. La formule $n-1$ donnerait $-1$, ce qui n'est pas correct. L'hypothèse $n \ge 1$ est donc cruciale pour la formule $n-1$.)

### Question 3 : Construire une base explicite de $F$.

Nous savons que $\dim(F) = n-1$. Nous devons donc trouver $n-1$ polynômes dans $F$ qui sont linéairement indépendants.

Un polynôme $P \in E$ appartient à $F$ si et seulement si $P(a)=0$ et $P'(b)=0$.
La condition $P(a)=0$ implique, d'après le théorème de factorisation des polynômes, qu'il existe un unique polynôme $Q \in \mathbb{K}_{n-1}[X]$ tel que $P(X) = (X-a)Q(X)$.
Puisque $P \in \mathbb{K}_n[X]$, $Q$ doit être dans $\mathbb{K}_{n-1}[X]$.

Maintenant, substituons cette expression de $P(X)$ dans la deuxième condition $P'(b)=0$.
Calculons $P'(X)$ :
$P'(X) = \frac{d}{dX}((X-a)Q(X)) = 1 \cdot Q(X) + (X-a)Q'(X)$.
La condition $P'(b)=0$ devient :
$Q(b) + (b-a)Q'(b) = 0$.

Définissons un nouvel espace $G$ :
$G = \{ Q \in \mathbb{K}_{n-1}[X] \mid Q(b) + (b-a)Q'(b) = 0 \}$.
Il existe une correspondance bijective entre $F$ et $G$ via l'application $\Psi: G \to F$ définie par $\Psi(Q) = (X-a)Q(X)$. Cette application est un isomorphisme de $\mathbb{K}$-espaces vectoriels.
Par conséquent, $\dim(G) = \dim(F) = n-1$.

Nous allons trouver une base de $G$.
Considérons l'application linéaire $\Lambda: \mathbb{K}_{n-1}[X] \to \mathbb{K}$ définie par $\Lambda(Q) = Q(b) + (b-a)Q'(b)$.
Alors $G = \ker(\Lambda)$.
$\dim(\mathbb{K}_{n-1}[X]) = n$.
Pour appliquer le théorème du rang, nous devons vérifier que $\Lambda$ est surjective.
Considérons le polynôme constant $Q_0(X) = 1$.
$\Lambda(Q_0) = Q_0(b) + (b-a)Q_0'(b) = 1 + (b-a) \cdot 0 = 1$.
Puisque $\Lambda(1)=1 \ne 0$, $\Lambda$ est surjective.
Donc, $\dim(G) = \dim(\mathbb{K}_{n-1}[X]) - \dim(\text{Im}(\Lambda)) = n - 1$. Ceci est cohérent avec notre calcul précédent.

Pour construire une base de $G$, nous allons utiliser la base de Taylor centrée en $b$ pour $\mathbb{K}_{n-1}[X]$.
Tout polynôme $Q \in \mathbb{K}_{n-1}[X]$ peut s'écrire de manière unique sous la forme :
$Q(X) = \sum_{k=0}^{n-1} c_k (X-b)^k$, où $c_k = \frac{Q^{(k)}(b)}{k!}$.
Calculons $Q(b)$ et $Q'(b)$ à partir de cette forme :
$Q(b) = c_0$.
$Q'(X) = \sum_{k=1}^{n-1} c_k k(X-b)^{k-1}$.
$Q'(b) = c_1$.

La condition $Q(b) + (b-a)Q'(b) = 0$ se traduit par :
$c_0 + (b-a)c_1 = 0$.

Nous cherchons $n-1$ polynômes linéairement indépendants dans $G$.
Observons les coefficients $c_k$:
*   Pour $k \ge 2$, si nous choisissons $Q(X) = (X-b)^k$, alors $c_k=1$ et tous les autres $c_j=0$. En particulier, $c_0=0$ et $c_1=0$.
    La condition $c_0 + (b-a)c_1 = 0$ est satisfaite ($0 + (b-a) \cdot 0 = 0$).
    Donc, les polynômes $(X-b)^k$ pour $k=2, 3, \dots, n-1$ appartiennent à $G$.
    Il y a $(n-1) - 2 + 1 = n-2$ tels polynômes.
    Notons ces polynômes $Q_k(X) = (X-b)^k$ pour $k \in \{2, \dots, n-1\}$.
    Cette famille $\{Q_2, \dots, Q_{n-1}\}$ est une famille libre car elle est extraite d'une base (la base de Taylor).

*   Nous avons besoin d'un polynôme supplémentaire pour compléter la base de $G$. Ce polynôme doit satisfaire $c_0 + (b-a)c_1 = 0$ et être linéairement indépendant des $Q_k$ déjà trouvés.
    Nous pouvons choisir $c_1=1$. Alors $c_0 = -(b-a) = a-b$.
    Nous choisissons $c_k=0$ pour $k \ge 2$.
    Le polynôme correspondant est $Q_1^*(X) = c_0 + c_1(X-b) = (a-b) + 1 \cdot (X-b) = X-2b+a$.
    Vérifions que $Q_1^*(X) \in G$:
    $Q_1^*(b) = b-2b+a = a-b$.
    $Q_1^{*'}(X) = 1$, donc $Q_1^{*'}(b) = 1$.
    $Q_1^*(b) + (b-a)Q_1^{*'}(b) = (a-b) + (b-a) \cdot 1 = (a-b) - (a-b) = 0$.
    Donc $Q_1^*(X) \in G$.

La famille $\mathcal{B}_G = \{ Q_1^*(X), Q_2(X), \dots, Q_{n-1}(X) \}$ est constituée de $1 + (n-2) = n-1$ polynômes.
$\mathcal{B}_G = \{ X-2b+a, (X-b)^2, (X-b)^3, \dots, (X-b)^{n-1} \}$.
Prouvons que cette famille est libre.
Supposons qu'il existe des scalaires $\lambda_1, \lambda_2, \dots, \lambda_{n-1}$ tels que :
$\lambda_1 (X-2b+a) + \sum_{k=2}^{n-1} \lambda_k (X-b)^k = 0_E$.
Le polynôme $X-2b+a$ est de degré 1. Les polynômes $(X-b)^k$ pour $k \ge 2$ sont de degré $k \ge 2$.
Si $\lambda_1 \ne 0$, alors le polynôme $\lambda_1 (X-2b+a)$ est de degré 1.
Les autres termes $\sum_{k=2}^{n-1} \lambda_k (X-b)^k$ sont soit nuls, soit de degré supérieur ou égal à 2.
Une somme d'un polynôme de degré 1 et de polynômes de degré $\ge 2$ ne peut être le polynôme nul que si le polynôme de degré 1 est nul et la somme des autres est nulle.
Plus formellement, évaluons l'équation en $X=b$:
$\lambda_1 (b-2b+a) + \sum_{k=2}^{n-1} \lambda_k (b-b)^k = 0$.
$\lambda_1 (a-b) + \sum_{k=2}^{n-1} \lambda_k \cdot 0 = 0$.
$\lambda_1 (a-b) = 0$.
Puisque $a \ne b$, nous avons $a-b \ne 0$.
Par conséquent, $\lambda_1 = 0$.
L'équation devient alors :
$\sum_{k=2}^{n-1} \lambda_k (X-b)^k = 0_E$.
La famille $\{ (X-b)^k \mid k=2, \dots, n-1 \}$ est une famille libre (c'est une partie d'une base de Taylor).
Donc, tous les $\lambda_k$ pour $k=2, \dots, n-1$ doivent être nuls.
Ainsi, tous les scalaires $\lambda_1, \dots, \lambda_{n-1}$ sont nuls.
La famille $\mathcal{B}_G$ est donc une famille libre de $n-1$ vecteurs dans $G$, qui est de dimension $n-1$. C'est donc une base de $G$.

Maintenant, nous construisons une base de $F$ en multipliant chaque polynôme de $\mathcal{B}_G$ par $(X-a)$.
Soit $\mathcal{B}_F = \{ (X-a)Q_1^*(X), (X-a)Q_2(X), \dots, (X-a)Q_{n-1}(X) \}$.
$\mathcal{B}_F = \{ (X-a)(X-2b+a), (X-a)(X-b)^2, \dots, (X-a)(X-b)^{n-1} \}$.
Cette famille contient $n-1$ polynômes.
Chaque polynôme $P_k(X) = (X-a)Q_k(X)$ est dans $F$ par construction.
Vérifions la linéarité indépendante de $\mathcal{B}_F$.
Supposons qu'il existe des scalaires $\mu_1, \mu_2, \dots, \mu_{n-1}$ tels que :
$\mu_1 (X-a)(X-2b+a) + \sum_{k=2}^{n-1} \mu_k (X-a)(X-b)^k = 0_E$.
Nous pouvons factoriser $(X-a)$ :
$(X-a) \left( \mu_1 (X-2b+a) + \sum_{k=2}^{n-1} \mu_k (X-b)^k \right) = 0_E$.
Puisque $X-a$ est un polynôme non nul, il s'ensuit que le facteur entre parenthèses doit être le polynôme nul :
$\mu_1 (X-2b+a) + \sum_{k=2}^{n-1} \mu_k (X-b)^k = 0_E$.
Cette expression est exactement la combinaison linéaire des éléments de $\mathcal{B}_G$.
Puisque $\mathcal{B}_G$ est une base de $G$, elle est linéairement indépendante.
Par conséquent, tous les scalaires $\mu_1, \mu_2, \dots, \mu_{n-1}$ doivent être nuls.
La famille $\mathcal{B}_F$ est donc une famille libre de $n-1$ vecteurs dans $F$, qui est de dimension $n-1$.
C'est donc une base de $F$.

**Conclusion :**
Une base explicite de $F$ est la famille $\mathcal{B}_F = \{ P_k(X) \mid k=1, \dots, n-1 \}$ où :
$P_1(X) = (X-a)(X-2b+a)$
et pour $k \in \{2, \dots, n-1\}$, $P_k(X) = (X-a)(X-b)^k$.
