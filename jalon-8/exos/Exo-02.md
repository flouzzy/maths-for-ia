# Exercice 2 : Application linéaire de dérivation (Difficulté : *)

## Énoncé du problème

Soit $\mathbb{K}$ le corps des nombres réels, $\mathbb{K} = \mathbb{R}$.
On considère l'espace vectoriel $E = \mathbb{R}_2[X]$ des polynômes à coefficients réels de degré au plus 2. Autrement dit, $E = \{ a_0 + a_1 X + a_2 X^2 \mid a_0, a_1, a_2 \in \mathbb{R} \}$.

On définit l'application $D: E \to E$ par $D(P) = P'$, où $P'$ désigne le polynôme dérivé de $P$.

1.  Justifier que $D$ est une application linéaire.
2.  Déterminer le noyau de $D$, noté $\text{Ker}(D)$. En donner une base et sa dimension.
3.  Déterminer l'image de $D$, notée $\text{Im}(D)$. En donner une base et sa dimension.
4.  Vérifier le théorème du rang pour l'application $D$.

## Correction détaillée

### Question 1 : Justifier que $D$ est une application linéaire.

Pour démontrer que l'application $D: E \to E$ est une application linéaire, nous devons vérifier qu'elle satisfait deux propriétés fondamentales : l'additivité et l'homogénéité.

1.  **Additivité** : Pour tous polynômes $P, Q \in E$, nous devons montrer que $D(P+Q) = D(P) + D(Q)$.
    Soient $P(X)$ et $Q(X)$ deux polynômes arbitraires de l'espace vectoriel $E = \mathbb{R}_2[X]$.
    Par définition de $E$, ils s'écrivent sous la forme :
    $P(X) = a_0 + a_1 X + a_2 X^2$
    $Q(X) = b_0 + b_1 X + b_2 X^2$
    où $a_0, a_1, a_2, b_0, b_1, b_2$ sont des coefficients réels appartenant à $\mathbb{R}$.

    Calculons la somme $P(X) + Q(X)$ :
    $P(X) + Q(X) = (a_0 + a_1 X + a_2 X^2) + (b_0 + b_1 X + b_2 X^2)$
    $P(X) + Q(X) = (a_0+b_0) + (a_1+b_1)X + (a_2+b_2)X^2$
    Ce polynôme est bien un élément de $E$ car ses coefficients $(a_0+b_0), (a_1+b_1), (a_2+b_2)$ sont des réels.

    Appliquons l'opérateur $D$ à cette somme :
    $D(P+Q) = (P+Q)'$
    $D(P+Q) = ((a_0+b_0) + (a_1+b_1)X + (a_2+b_2)X^2)'$
    En utilisant les règles de dérivation des polynômes, la dérivée est :
    $D(P+Q) = (a_1+b_1) + 2(a_2+b_2)X$

    Calculons maintenant $D(P)$ et $D(Q)$ séparément :
    $D(P) = P' = (a_0 + a_1 X + a_2 X^2)' = a_1 + 2a_2 X$
    $D(Q) = Q' = (b_0 + b_1 X + b_2 X^2)' = b_1 + 2b_2 X$

    Calculons la somme $D(P) + D(Q)$ :
    $D(P) + D(Q) = (a_1 + 2a_2 X) + (b_1 + 2b_2 X)$
    $D(P) + D(Q) = (a_1+b_1) + (2a_2+2b_2)X$
    $D(P) + D(Q) = (a_1+b_1) + 2(a_2+b_2)X$

    En comparant les expressions obtenues pour $D(P+Q)$ et $D(P)+D(Q)$, nous constatons qu'elles sont identiques :
    $D(P+Q) = (a_1+b_1) + 2(a_2+b_2)X$
    $D(P) + D(Q) = (a_1+b_1) + 2(a_2+b_2)X$
    Donc, la propriété d'additivité $D(P+Q) = D(P) + D(Q)$ est vérifiée.

2.  **Homogénéité** : Pour tout polynôme $P \in E$ et tout scalaire $\lambda \in \mathbb{R}$, nous devons montrer que $D(\lambda P) = \lambda D(P)$.
    Soit $P(X) = a_0 + a_1 X + a_2 X^2 \in E$, avec $a_0, a_1, a_2 \in \mathbb{R}$.
    Soit $\lambda \in \mathbb{R}$ un scalaire arbitraire.

    Calculons le produit scalaire $\lambda P(X)$ :
    $\lambda P(X) = \lambda (a_0 + a_1 X + a_2 X^2)$
    $\lambda P(X) = (\lambda a_0) + (\lambda a_1)X + (\lambda a_2)X^2$
    Ce polynôme est bien un élément de $E$ car ses coefficients $(\lambda a_0), (\lambda a_1), (\lambda a_2)$ sont des réels.

    Appliquons l'opérateur $D$ à ce produit scalaire :
    $D(\lambda P) = (\lambda P)'$
    $D(\lambda P) = ((\lambda a_0) + (\lambda a_1)X + (\lambda a_2)X^2)'$
    En utilisant les règles de dérivation des polynômes, la dérivée est :
    $D(\lambda P) = (\lambda a_1) + 2(\lambda a_2)X$

    Calculons maintenant $\lambda D(P)$ :
    $D(P) = P' = (a_0 + a_1 X + a_2 X^2)' = a_1 + 2a_2 X$
    $\lambda D(P) = \lambda (a_1 + 2a_2 X)$
    $\lambda D(P) = (\lambda a_1) + (\lambda \cdot 2a_2)X$
    $\lambda D(P) = (\lambda a_1) + 2(\lambda a_2)X$

    En comparant les expressions obtenues pour $D(\lambda P)$ et $\lambda D(P)$, nous constatons qu'elles sont identiques :
    $D(\lambda P) = (\lambda a_1) + 2(\lambda a_2)X$
    $\lambda D(P) = (\lambda a_1) + 2(\lambda a_2)X$
    Donc, la propriété d'homogénéité $D(\lambda P) = \lambda D(P)$ est vérifiée.

Puisque l'application $D$ satisfait à la fois la propriété d'additivité et la propriété d'homogénéité, nous concluons que $D$ est une application linéaire de $E$ dans $E$.

### Question 2 : Déterminer le noyau de $D$, $\text{Ker}(D)$. En donner une base et sa dimension.

Par définition, le noyau de l'application linéaire $D: E \to E$, noté $\text{Ker}(D)$, est l'ensemble de tous les polynômes $P \in E$ dont l'image par $D$ est le polynôme nul de $E$. Le polynôme nul de $E$, noté $0_E$, est le polynôme $0 + 0X + 0X^2$.

Formellement :
$\text{Ker}(D) = \{ P \in E \mid D(P) = 0_E \}$

Soit un polynôme $P(X) \in E$. Il s'écrit sous la forme générale :
$P(X) = a_0 + a_1 X + a_2 X^2$, où $a_0, a_1, a_2 \in \mathbb{R}$.

L'application $D$ est la dérivation, donc $D(P) = P'$.
Calculons la dérivée de $P(X)$ :
$P'(X) = (a_0 + a_1 X + a_2 X^2)'$
$P'(X) = 0 + a_1 \cdot 1 + a_2 \cdot (2X)$
$P'(X) = a_1 + 2a_2 X$

Pour que $P(X)$ appartienne au noyau de $D$, il faut que $P'(X) = 0_E$.
$P'(X) = 0_E \iff a_1 + 2a_2 X = 0 + 0X$

Par identification des coefficients des polynômes, pour que deux polynômes soient égaux, leurs coefficients respectifs doivent être égaux.
Le coefficient du terme constant ($X^0$) de $P'(X)$ est $a_1$. Le coefficient du terme constant de $0_E$ est $0$.
Donc, $a_1 = 0$.

Le coefficient du terme en $X$ ($X^1$) de $P'(X)$ est $2a_2$. Le coefficient du terme en $X$ de $0_E$ est $0$.
Donc, $2a_2 = 0$, ce qui implique $a_2 = 0$.

Ainsi, pour que $P(X)$ soit dans $\text{Ker}(D)$, les coefficients $a_1$ et $a_2$ doivent être nuls. Le coefficient $a_0$ n'est soumis à aucune contrainte.
Le polynôme $P(X)$ prend donc la forme :
$P(X) = a_0 + 0 \cdot X + 0 \cdot X^2$
$P(X) = a_0$

Le noyau de $D$ est l'ensemble de tous les polynômes constants :
$\text{Ker}(D) = \{ a_0 \mid a_0 \in \mathbb{R} \}$
Cet ensemble est l'espace vectoriel des polynômes de degré au plus 0, noté $\mathbb{R}_0[X]$.

**Détermination d'une base de $\text{Ker}(D)$ :**
Tout polynôme $P(X) \in \text{Ker}(D)$ peut s'écrire $P(X) = a_0 \cdot 1$, où $1$ est le polynôme constant égal à $1$.
Cela signifie que le polynôme $1$ engendre l'espace vectoriel $\text{Ker}(D)$.
Pour vérifier que $\{1\}$ est une base, nous devons également montrer qu'il est linéairement indépendant.
Considérons une combinaison linéaire du polynôme $1$ égale au polynôme nul :
$\alpha \cdot 1 = 0_E$, où $\alpha \in \mathbb{R}$.
Cette équation se réduit à $\alpha = 0$.
Puisque la seule solution est $\alpha = 0$, le polynôme $1$ est linéairement indépendant.
Par conséquent, l'ensemble $B_{\text{Ker}(D)} = \{1\}$ est une base de $\text{Ker}(D)$.

**Détermination de la dimension de $\text{Ker}(D)$ :**
La dimension d'un espace vectoriel est le nombre de vecteurs dans n'importe laquelle de ses bases.
Puisque la base $B_{\text{Ker}(D)}$ contient un seul vecteur, la dimension du noyau est :
$\dim(\text{Ker}(D)) = 1$.

### Question 3 : Déterminer l'image de $D$, $\text{Im}(D)$. En donner une base et sa dimension.

Par définition, l'image de l'application linéaire $D: E \to E$, notée $\text{Im}(D)$, est l'ensemble de tous les polynômes $Q \in E$ pour lesquels il existe au moins un polynôme $P \in E$ tel que $D(P) = Q$.

Formellement :
$\text{Im}(D) = \{ Q \in E \mid \exists P \in E \text{ tel que } D(P) = Q \}$

Soit un polynôme $P(X) \in E$. Il s'écrit sous la forme :
$P(X) = a_0 + a_1 X + a_2 X^2$, où $a_0, a_1, a_2 \in \mathbb{R}$.

L'image de $P(X)$ par $D$ est $D(P) = P'(X)$.
$D(P) = P'(X) = a_1 + 2a_2 X$.

Tout polynôme $Q(X)$ dans l'image de $D$ est donc de la forme $a_1 + 2a_2 X$.
Posons $b_0 = a_1$ et $b_1 = 2a_2$. Puisque $a_1$ et $a_2$ peuvent prendre n'importe quelle valeur réelle, $b_0$ peut être n'importe quel réel, et $b_1$ peut être n'importe quel réel.
Ainsi, tout polynôme dans l'image est de la forme $b_0 + b_1 X$, où $b_0, b_1 \in \mathbb{R}$.
Ceci correspond à la définition de l'espace vectoriel des polynômes de degré au plus 1, noté $\mathbb{R}_1[X]$.
Donc, nous avons montré que $\text{Im}(D) \subseteq \mathbb{R}_1[X]$.

Pour montrer l'égalité $\text{Im}(D) = \mathbb{R}_1[X]$, nous devons également prouver que $\mathbb{R}_1[X] \subseteq \text{Im}(D)$. C'est-à-dire, pour tout polynôme $Q(X) \in \mathbb{R}_1[X]$, il existe un polynôme $P(X) \in E$ tel que $D(P) = Q$.

Soit $Q(X)$ un polynôme arbitraire dans $\mathbb{R}_1[X]$. Il s'écrit sous la forme :
$Q(X) = b_0 + b_1 X$, où $b_0, b_1 \in \mathbb{R}$.

Nous cherchons un polynôme $P(X) = c_0 + c_1 X + c_2 X^2 \in E$ (avec $c_0, c_1, c_2 \in \mathbb{R}$) tel que $P'(X) = Q(X)$.
La dérivée de $P(X)$ est $P'(X) = c_1 + 2c_2 X$.
Nous voulons que $c_1 + 2c_2 X = b_0 + b_1 X$.

Par identification des coefficients :
Le coefficient du terme constant : $c_1 = b_0$.
Le coefficient du terme en $X$ : $2c_2 = b_1$, ce qui implique $c_2 = \frac{b_1}{2}$.

Le coefficient $c_0$ n'est pas déterminé par cette équation. Nous pouvons choisir n'importe quelle valeur réelle pour $c_0$. Par exemple, choisissons $c_0 = 0$.
Alors, le polynôme $P(X)$ est :
$P(X) = 0 + b_0 X + \frac{b_1}{2} X^2 = b_0 X + \frac{b_1}{2} X^2$.

Puisque $b_0 \in \mathbb{R}$ et $b_1 \in \mathbb{R}$, il s'ensuit que $b_0 \in \mathbb{R}$ et $\frac{b_1}{2} \in \mathbb{R}$.
Le polynôme $P(X) = b_0 X + \frac{b_1}{2} X^2$ est bien un polynôme de degré au plus 2 à coefficients réels, donc $P(X) \in E$.
Et sa dérivée est $D(P) = (b_0 X + \frac{b_1}{2} X^2)' = b_0 + 2 \cdot \frac{b_1}{2} X = b_0 + b_1 X = Q(X)$.
Ceci prouve que tout polynôme de $\mathbb{R}_1[X]$ est l'image d'un polynôme de $E$ par $D$.
Donc, $\mathbb{R}_1[X] \subseteq \text{Im}(D)$.

Ayant montré $\text{Im}(D) \subseteq \mathbb{R}_1[X]$ et $\mathbb{R}_1[X] \subseteq \text{Im}(D)$, nous concluons que :
$\text{Im}(D) = \mathbb{R}_1[X]$.

**Détermination d'une base de $\text{Im}(D)$ :**
L'espace vectoriel $\mathbb{R}_1[X]$ est l'ensemble des polynômes de degré au plus 1.
Les polynômes $1$ et $X$ sont des éléments de $\mathbb{R}_1[X]$.
Pour montrer que $B_{\text{Im}(D)} = \{1, X\}$ est une base de $\text{Im}(D)$, nous devons prouver qu'ils engendrent $\text{Im}(D)$ et qu'ils sont linéairement indépendants.

1.  **Engendrement** : Tout polynôme $Q(X) = b_0 + b_1 X \in \mathbb{R}_1[X]$ peut être écrit comme une combinaison linéaire de $1$ et $X$ :
    $Q(X) = b_0 \cdot 1 + b_1 \cdot X$.
    Donc, $\{1, X\}$ engendre $\text{Im}(D)$.

2.  **Indépendance linéaire** : Considérons une combinaison linéaire de $1$ et $X$ égale au polynôme nul $0_E$:
    $\alpha_0 \cdot 1 + \alpha_1 \cdot X = 0_E$, où $\alpha_0, \alpha_1 \in \mathbb{R}$.
    Cette équation s'écrit $\alpha_0 + \alpha_1 X = 0 + 0X$.
    Par identification des coefficients, nous obtenons :
    $\alpha_0 = 0$
    $\alpha_1 = 0$
    Puisque la seule solution est $\alpha_0 = 0$ et $\alpha_1 = 0$, les polynômes $1$ et $X$ sont linéairement indépendants.

Par conséquent, l'ensemble $B_{\text{Im}(D)} = \{1, X\}$ est une base de $\text{Im}(D)$.

**Détermination de la dimension de $\text{Im}(D)$ :**
La dimension de l'image est le nombre de vecteurs dans sa base.
Puisque la base $B_{\text{Im}(D)}$ contient deux vecteurs, la dimension de l'image est :
$\dim(\text{Im}(D)) = 2$.

### Question 4 : Vérifier le théorème du rang pour l'application $D$.

Le théorème du rang est un résultat fondamental en algèbre linéaire qui relie la dimension de l'espace de départ, la dimension du noyau et la dimension de l'image d'une application linéaire. Pour une application linéaire $L: V \to W$, le théorème du rang stipule que :
$\dim(V) = \dim(\text{Ker}(L)) + \dim(\text{Im}(L))$.

Dans notre cas, l'application linéaire est $D: E \to E$. L'espace de départ est $V = E = \mathbb{R}_2[X]$.

1.  **Détermination de la dimension de l'espace de départ $E$ :**
    L'espace vectoriel $E = \mathbb{R}_2[X]$ est l'ensemble des polynômes de degré au plus 2.
    Une base canonique de $\mathbb{R}_2[X]$ est l'ensemble des polynômes $\{1, X, X^2\}$.
    Cet ensemble est composé de trois vecteurs linéairement indépendants qui engendrent $E$.
    Par conséquent, la dimension de l'espace de départ $E$ est :
    $\dim(E) = 3$.

2.  **Récupération de la dimension du noyau $\text{Ker}(D)$ :**
    D'après les résultats de la Question 2, nous avons déterminé que $\dim(\text{Ker}(D)) = 1$.

3.  **Récupération de la dimension de l'image $\text{Im}(D)$ :**
    D'après les résultats de la Question 3, nous avons déterminé que $\dim(\text{Im}(D)) = 2$.

4.  **Vérification du théorème du rang :**
    Nous devons vérifier si l'égalité $\dim(E) = \dim(\text{Ker}(D)) + \dim(\text{Im}(D))$ est satisfaite avec les valeurs obtenues.
    Substituons les dimensions calculées dans l'équation du théorème du rang :
    $\dim(\text{Ker}(D)) + \dim(\text{Im}(D)) = 1 + 2$
    $\dim(\text{Ker}(D)) + \dim(\text{Im}(D)) = 3$

    Nous comparons ce résultat avec la dimension de l'espace de départ :
    $\dim(E) = 3$.

    Nous constatons que :
    $\dim(E) = 3$
    $\dim(\text{Ker}(D)) + \dim(\text{Im}(D)) = 3$

    L'égalité $\dim(E) = \dim(\text{Ker}(D)) + \dim(\text{Im}(D))$ est donc satisfaite.
    Par conséquent, le théorème du rang est vérifié pour l'application linéaire $D$.
