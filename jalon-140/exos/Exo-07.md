---
uuid: "jalon-140-exo-07"
title: "Exercice 7 - Jalon 140"
---
# Exercice 7 : Relation entre le Classifieur de Bayes et la Minimisation de la Perte Quadratique
**Difficulté:** ★★★★

## Énoncé
Soit un problème de classification binaire où la variable de sortie $Y$ prend ses valeurs dans l'ensemble $\{-1, 1\}$ et la variable d'entrée $X$ est un vecteur dans $\mathbb{R}^d$.
Le classifieur de Bayes optimal $h_{\text{Bayes}}(x)$ est défini comme le classifieur qui minimise la probabilité d'erreur $P(h(X) \neq Y)$.

1.  Rappeler la forme du classifieur de Bayes optimal $h_{\text{Bayes}}(x)$ en fonction des probabilités a posteriori $P(Y=1|X=x)$ et $P(Y=-1|X=x)$. Exprimez-le sous la forme d'une fonction signe.
2.  Considérons une fonction de prédiction $f: \mathbb{R}^d \to \mathbb{R}$. Nous souhaitons trouver la fonction $f^*(x)$ qui minimise le risque attendu sous la perte quadratique (squared loss) $L(y, f(x)) = (y - f(x))^2$.
    Formellement, nous cherchons $f^*(x) = \underset{f(x)}{\text{argmin}} \, E[ (Y - f(X))^2 | X=x ]$.
    Dériver l'expression de $f^*(x)$.
3.  Montrer que si nous utilisons la fonction $f^*(x)$ obtenue à la question précédente pour la classification en définissant un classifieur $h_{\text{quad}}(x) = \text{sign}(f^*(x))$, alors $h_{\text{quad}}(x)$ est équivalent au classifieur de Bayes optimal $h_{\text{Bayes}}(x)$.

## Correction Pas-à-Pas

### Question 1 : Forme du classifieur de Bayes optimal

Le classifieur de Bayes optimal $h_{\text{Bayes}}(x)$ minimise la probabilité d'erreur $P(h(X) \neq Y)$. Pour un point $x$ donné, il choisit la classe $y$ qui maximise la probabilité a posteriori $P(Y=y|X=x)$.

Ainsi, pour un problème de classification binaire avec $Y \in \{-1, 1\}$ :
Si $P(Y=1|X=x) > P(Y=-1|X=x)$, alors $h_{\text{Bayes}}(x) = 1$.
Si $P(Y=-1|X=x) > P(Y=1|X=x)$, alors $h_{\text{Bayes}}(x) = -1$.
Si $P(Y=1|X=x) = P(Y=-1|X=x)$, le choix est arbitraire (par convention, on peut choisir $1$).

Nous pouvons exprimer cette règle de décision en utilisant la fonction signe.
L'inégalité $P(Y=1|X=x) > P(Y=-1|X=x)$ peut être réécrite.
Nous savons que $P(Y=-1|X=x) = 1 - P(Y=1|X=x)$ car $Y$ ne prend que deux valeurs.
Substituons cette expression :
$P(Y=1|X=x) > 1 - P(Y=1|X=x)$
$P(Y=1|X=x) + P(Y=1|X=x) > 1$
$2 \cdot P(Y=1|X=x) > 1$
$2 \cdot P(Y=1|X=x) - 1 > 0$

De même, l'inégalité $P(Y=-1|X=x) > P(Y=1|X=x)$ implique :
$1 - P(Y=1|X=x) > P(Y=1|X=x)$
$1 > 2 \cdot P(Y=1|X=x)$
$2 \cdot P(Y=1|X=x) - 1 < 0$

Par conséquent, le classifieur de Bayes optimal peut être exprimé comme :
$h_{\text{Bayes}}(x) = \text{sign}(2 \cdot P(Y=1|X=x) - 1)$

Une forme équivalente est :
$h_{\text{Bayes}}(x) = \text{sign}(P(Y=1|X=x) - P(Y=-1|X=x))$

### Question 2 : Dérivation de $f^*(x)$ pour la perte quadratique

Nous cherchons la fonction $f^*(x)$ qui minimise le risque attendu sous la perte quadratique conditionnellement à $X=x$.
$f^*(x) = \underset{f(x)}{\text{argmin}} \, E[ (Y - f(X))^2 | X=x ]$

Pour un $x$ fixe, nous voulons minimiser l'expression $E[ (Y - f(x))^2 | X=x ]$.
Soit $g = f(x)$ une valeur scalaire. Nous cherchons à minimiser $E[ (Y - g)^2 | X=x ]$.
Développons l'espérance :
$E[ (Y - g)^2 | X=x ] = E[ Y^2 - 2 \cdot Y \cdot g + g^2 | X=x ]$
Par linéarité de l'espérance :
$E[ (Y - g)^2 | X=x ] = E[ Y^2 | X=x ] - 2 \cdot g \cdot E[ Y | X=x ] + E[ g^2 | X=x ]$
Puisque $g$ est une constante par rapport à l'espérance conditionnelle sur $Y$:
$E[ (Y - g)^2 | X=x ] = E[ Y^2 | X=x ] - 2 \cdot g \cdot E[ Y | X=x ] + g^2$

Pour trouver la valeur de $g$ qui minimise cette expression, nous dérivons par rapport à $g$ et nous égalisons la dérivée à zéro.
$\frac{\text{d}}{\text{d}g} \left( E[ Y^2 | X=x ] - 2 \cdot g \cdot E[ Y | X=x ] + g^2 \right) = 0$
$0 - 2 \cdot E[ Y | X=x ] + 2 \cdot g = 0$
$2 \cdot g = 2 \cdot E[ Y | X=x ]$
$g = E[ Y | X=x ]$

La fonction optimale $f^*(x)$ est donc donnée par :
$f^*(x) = E[ Y | X=x ]$

### Question 3 : Équivalence entre $h_{\text{quad}}(x)$ et $h_{\text{Bayes}}(x)$

Nous avons défini le classifieur $h_{\text{quad}}(x) = \text{sign}(f^*(x))$.
D'après la question précédente, $f^*(x) = E[ Y | X=x ]$.
Donc, $h_{\text{quad}}(x) = \text{sign}(E[ Y | X=x ])$.

Nous devons montrer que $h_{\text{quad}}(x)$ est équivalent à $h_{\text{Bayes}}(x) = \text{sign}(2 \cdot P(Y=1|X=x) - 1)$.

Calculons l'espérance conditionnelle $E[ Y | X=x ]$ pour $Y \in \{-1, 1\}$ :
$E[ Y | X=x ] = P(Y=1|X=x) \cdot 1 + P(Y=-1|X=x) \cdot (-1)$
$E[ Y | X=x ] = P(Y=1|X=x) - P(Y=-1|X=x)$

Comme précédemment, nous savons que $P(Y=-1|X=x) = 1 - P(Y=1|X=x)$.
Substituons cette expression dans $E[ Y | X=x ]$ :
$E[ Y | X=x ] = P(Y=1|X=x) - (1 - P(Y=1|X=x))$
$E[ Y | X=x ] = P(Y=1|X=x) - 1 + P(Y=1|X=x)$
$E[ Y | X=x ] = 2 \cdot P(Y=1|X=x) - 1$

Maintenant, substituons cette expression de $E[ Y | X=x ]$ dans la définition de $h_{\text{quad}}(x)$ :
$h_{\text{quad}}(x) = \text{sign}(E[ Y | X=x ])$
$h_{\text{quad}}(x) = \text{sign}(2 \cdot P(Y=1|X=x) - 1)$

En comparant cette expression avec celle de $h_{\text{Bayes}}(x)$ obtenue à la Question 1 :
$h_{\text{Bayes}}(x) = \text{sign}(2 \cdot P(Y=1|X=x) - 1)$

Nous constatons que $h_{\text{quad}}(x) = h_{\text{Bayes}}(x)$.
Ainsi, le classifieur obtenu en minimisant la perte quadratique et en prenant le signe de la prédiction est équivalent au classifieur de Bayes optimal.
