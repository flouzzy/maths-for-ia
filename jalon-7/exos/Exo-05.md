# Exercice 5 : Analyse d'un Sous-Espace de Polynômes par Contraintes Intégrale et Différentielle

## Énoncé

Mes chers étudiants,

Nous allons aujourd'hui approfondir notre compréhension des espaces vectoriels abstraits en nous penchant sur un sous-espace particulier de polynômes. Cet exercice vous demandera d'appliquer rigoureusement les définitions et propriétés des espaces vectoriels, des familles libres, génératrices et des bases.

Soit $\mathbb{R}$ le corps des nombres réels.
Soit $E$ le $\mathbb{R}$-espace vectoriel des polynômes à coefficients réels de degré au plus 2, noté $\mathbb{R}_2[X]$.
Nous considérons le sous-ensemble $F$ de $E$ défini par :
$$ F = \left\{ P \in E \mid \int_0^1 P(t) dt = 0 \quad \text{et} \quad P'(0) = 0 \right\} $$
où $P'(X)$ désigne le polynôme dérivé de $P(X)$.

1.  Démontrer que $F$ est un sous-espace vectoriel de $E$.
2.  Déterminer une base de $F$ et en déduire sa dimension.
3.  Considérons la famille de polynômes $\mathcal{B}' = (P_1, P_2)$ où $P_1(X) = X^2 - \frac{1}{3}$ et $P_2(X) = X^2 - X$. La famille $\mathcal{B}'$ est-elle une base de $F$ ? Justifier votre réponse avec toute la rigueur nécessaire.

## Correction Détaillée

Chers étudiants, abordons cette correction avec la précision et la clarté qui s'imposent.

### Question 1 : Démontrer que $F$ est un sous-espace vectoriel de $E$.

Pour démontrer que $F$ est un sous-espace vectoriel de $E$, nous devons vérifier trois conditions :
(i) $F$ est un sous-ensemble de $E$.
(ii) Le vecteur nul de $E$ appartient à $F$.
(iii) $F$ est stable par combinaison linéaire.

**Condition (i) : $F \subseteq E$**
Par définition de $F$, tout élément $P$ de $F$ est un polynôme appartenant à $E = \mathbb{R}_2[X]$. Ainsi, $F$ est bien un sous-ensemble de $E$.

**Condition (ii) : Le vecteur nul de $E$ appartient à $F$**
Soit $0_E$ le polynôme nul de $E$. Nous avons $0_E(X) = 0$ pour tout $X \in \mathbb{R}$.
Vérifions les deux conditions définissant $F$ pour $0_E$:
*   **Première condition :** $\int_0^1 0_E(t) dt = \int_0^1 0 dt$.
    Le calcul de cette intégrale donne :
    $\int_0^1 0 dt = [C]_0^1 = C - C = 0$, où $C$ est une constante d'intégration.
    Ainsi, $\int_0^1 0_E(t) dt = 0$.
*   **Deuxième condition :** $0_E'(0) = 0$.
    Le polynôme dérivé de $0_E(X)$ est $0_E'(X) = 0$.
    L'évaluation de ce polynôme en $X=0$ donne $0_E'(0) = 0$.
Les deux conditions sont satisfaites pour le polynôme nul. Par conséquent, $0_E \in F$.

**Condition (iii) : $F$ est stable par combinaison linéaire**
Soient $P_1$ et $P_2$ deux polynômes appartenant à $F$.
Soient $\lambda_1$ et $\lambda_2$ deux scalaires appartenant à $\mathbb{R}$.
Nous devons montrer que le polynôme $Q = \lambda_1 P_1 + \lambda_2 P_2$ appartient également à $F$.

Puisque $P_1 \in E$ et $P_2 \in E$, et que $E$ est un $\mathbb{R}$-espace vectoriel, toute combinaison linéaire de $P_1$ et $P_2$ appartient à $E$. Donc $Q \in E$.

Vérifions les deux conditions définissant $F$ pour $Q$:
*   **Première condition :** $\int_0^1 Q(t) dt = 0$.
    Par linéarité de l'intégrale définie, nous avons :
    $\int_0^1 Q(t) dt = \int_0^1 (\lambda_1 P_1(t) + \lambda_2 P_2(t)) dt$
    $\int_0^1 Q(t) dt = \int_0^1 \lambda_1 P_1(t) dt + \int_0^1 \lambda_2 P_2(t) dt$
    $\int_0^1 Q(t) dt = \lambda_1 \int_0^1 P_1(t) dt + \lambda_2 \int_0^1 P_2(t) dt$
    Puisque $P_1 \in F$, nous savons que $\int_0^1 P_1(t) dt = 0$.
    Puisque $P_2 \in F$, nous savons que $\int_0^1 P_2(t) dt = 0$.
    En substituant ces valeurs, nous obtenons :
    $\int_0^1 Q(t) dt = \lambda_1 \cdot 0 + \lambda_2 \cdot 0$
    $\int_0^1 Q(t) dt = 0 + 0$
    $\int_0^1 Q(t) dt = 0$.
    La première condition est satisfaite.

*   **Deuxième condition :** $Q'(0) = 0$.
    Par linéarité de l'opérateur de dérivation, nous avons :
    $Q'(X) = (\lambda_1 P_1(X) + \lambda_2 P_2(X))'$
    $Q'(X) = \lambda_1 P_1'(X) + \lambda_2 P_2'(X)$
    Évaluons $Q'(X)$ en $X=0$:
    $Q'(0) = \lambda_1 P_1'(0) + \lambda_2 P_2'(0)$
    Puisque $P_1 \in F$, nous savons que $P_1'(0) = 0$.
    Puisque $P_2 \in F$, nous savons que $P_2'(0) = 0$.
    En substituant ces valeurs, nous obtenons :
    $Q'(0) = \lambda_1 \cdot 0 + \lambda_2 \cdot 0$
    $Q'(0) = 0 + 0$
    $Q'(0) = 0$.
    La deuxième condition est satisfaite.

Puisque les trois conditions sont vérifiées, nous pouvons conclure que $F$ est un sous-espace vectoriel de $E = \mathbb{R}_2[X]$.

### Question 2 : Déterminer une base de $F$ et en déduire sa dimension.

Soit $P(X)$ un polynôme arbitraire appartenant à $E = \mathbb{R}_2[X]$.
Nous pouvons écrire $P(X)$ sous la forme $P(X) = aX^2 + bX + c$, où $a, b, c$ sont des scalaires réels.

Pour que $P(X)$ appartienne à $F$, il doit satisfaire les deux conditions :
(1) $\int_0^1 P(t) dt = 0$
(2) $P'(0) = 0$

Commençons par la deuxième condition, car elle est souvent plus simple à évaluer.
Le polynôme dérivé de $P(X)$ est $P'(X) = \frac{d}{dX}(aX^2 + bX + c) = 2aX + b$.
Évaluons $P'(X)$ en $X=0$:
$P'(0) = 2a(0) + b = b$.
La condition (2) $P'(0) = 0$ implique donc $b = 0$.

Maintenant, nous savons que tout polynôme $P(X) \in F$ doit être de la forme $P(X) = aX^2 + c$.
Appliquons la première condition à cette forme simplifiée de $P(X)$:
$\int_0^1 P(t) dt = \int_0^1 (at^2 + c) dt$.
Calculons cette intégrale :
$\int_0^1 (at^2 + c) dt = \left[ a \frac{t^3}{3} + ct \right]_0^1$
$\int_0^1 (at^2 + c) dt = \left( a \frac{1^3}{3} + c(1) \right) - \left( a \frac{0^3}{3} + c(0) \right)$
$\int_0^1 (at^2 + c) dt = \left( \frac{a}{3} + c \right) - (0 + 0)$
$\int_0^1 (at^2 + c) dt = \frac{a}{3} + c$.
La condition (1) $\int_0^1 P(t) dt = 0$ implique donc $\frac{a}{3} + c = 0$.
De cette équation, nous pouvons exprimer $c$ en fonction de $a$: $c = -\frac{a}{3}$.

En substituant les valeurs de $b$ et $c$ dans l'expression générale de $P(X)$, nous obtenons :
$P(X) = aX^2 + (0)X + \left(-\frac{a}{3}\right)$
$P(X) = aX^2 - \frac{a}{3}$
$P(X) = a \left( X^2 - \frac{1}{3} \right)$.

Cela signifie que tout polynôme $P(X)$ appartenant à $F$ peut s'écrire comme un multiple scalaire du polynôme $X^2 - \frac{1}{3}$.
Par conséquent, la famille $\mathcal{B} = \left( X^2 - \frac{1}{3} \right)$ est une famille génératrice de $F$.
Nous avons $F = \text{Vect}\left( X^2 - \frac{1}{3} \right)$.

Pour qu'une famille génératrice soit une base, elle doit également être libre.
La famille $\mathcal{B}$ est composée d'un seul vecteur, le polynôme $P_0(X) = X^2 - \frac{1}{3}$.
Puisque $P_0(X)$ n'est pas le polynôme nul (par exemple, $P_0(1) = 1 - 1/3 = 2/3 \neq 0$), la famille $\mathcal{B}$ est une famille libre.

Étant à la fois génératrice et libre, la famille $\mathcal{B} = \left( X^2 - \frac{1}{3} \right)$ est une base de $F$.
La dimension d'un espace vectoriel est le nombre de vecteurs dans n'importe quelle base de cet espace.
Puisque la base $\mathcal{B}$ contient un seul polynôme, la dimension de $F$ est 1.
Nous notons $\text{dim}(F) = 1$.

### Question 3 : La famille $\mathcal{B}' = (P_1, P_2)$ est-elle une base de $F$ ?

Nous avons la famille $\mathcal{B}' = (P_1, P_2)$ avec $P_1(X) = X^2 - \frac{1}{3}$ et $P_2(X) = X^2 - X$.

Pour qu'une famille de vecteurs soit une base d'un espace vectoriel, tous les vecteurs de cette famille doivent appartenir à l'espace en question. Commençons par vérifier si $P_1$ et $P_2$ appartiennent à $F$.

**Vérification pour $P_1(X) = X^2 - \frac{1}{3}$ :**
*   **Première condition :** $\int_0^1 P_1(t) dt = 0$.
    $\int_0^1 \left( t^2 - \frac{1}{3} \right) dt = \left[ \frac{t^3}{3} - \frac{t}{3} \right]_0^1$
    $= \left( \frac{1^3}{3} - \frac{1}{3} \right) - \left( \frac{0^3}{3} - \frac{0}{3} \right)$
    $= \left( \frac{1}{3} - \frac{1}{3} \right) - (0 - 0)$
    $= 0 - 0 = 0$.
    La première condition est satisfaite.
*   **Deuxième condition :** $P_1'(0) = 0$.
    Le polynôme dérivé de $P_1(X)$ est $P_1'(X) = \frac{d}{dX}(X^2 - \frac{1}{3}) = 2X$.
    Évaluons $P_1'(X)$ en $X=0$:
    $P_1'(0) = 2(0) = 0$.
    La deuxième condition est satisfaite.
Puisque les deux conditions sont satisfaites, $P_1 \in F$.

**Vérification pour $P_2(X) = X^2 - X$ :**
*   **Première condition :** $\int_0^1 P_2(t) dt = 0$.
    $\int_0^1 (t^2 - t) dt = \left[ \frac{t^3}{3} - \frac{t^2}{2} \right]_0^1$
    $= \left( \frac{1^3}{3} - \frac{1^2}{2} \right) - \left( \frac{0^3}{3} - \frac{0^2}{2} \right)$
    $= \left( \frac{1}{3} - \frac{1}{2} \right) - (0 - 0)$
    $= \frac{2}{6} - \frac{3}{6} = -\frac{1}{6}$.
    La première condition n'est pas satisfaite, car $\int_0^1 P_2(t) dt = -\frac{1}{6} \neq 0$.

Puisque $P_2(X)$ ne satisfait pas la première condition de définition de $F$, le polynôme $P_2(X)$ n'appartient pas à $F$.

Pour qu'une famille de vecteurs soit une base d'un espace vectoriel, tous les vecteurs de cette famille doivent impérativement appartenir à cet espace vectoriel. Étant donné que $P_2 \notin F$, la famille $\mathcal{B}' = (P_1, P_2)$ ne peut pas être une base de $F$.

Il n'est donc pas nécessaire de vérifier les propriétés de liberté ou de famille génératrice pour $\mathcal{B}'$ par rapport à $F$, car la condition d'appartenance des vecteurs à l'espace n'est pas remplie.
