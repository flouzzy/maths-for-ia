---
uuid: "jalon-140-exo-04"
title: "Exercice 4 - Jalon 140"
---
# Exercice 4 : Classifieur de Bayes Optimal pour Données Discrètes
**Difficulté:** ★★

## Énoncé
Considérons un problème de classification binaire où la variable de classe $Y$ peut prendre les valeurs $0$ ou $1$, et la variable d'entrée $X$ peut prendre les valeurs discrètes $x_1, x_2, x_3$.

Les probabilités a priori des classes sont données par :
$P(Y=0) = 0.6$
$P(Y=1) = 0.4$

Les probabilités conditionnelles de $X$ étant donné $Y$ sont les suivantes :
Pour la classe $Y=0$:
$P(X=x_1|Y=0) = 0.3$
$P(X=x_2|Y=0) = 0.5$
$P(X=x_3|Y=0) = 0.2$

Pour la classe $Y=1$:
$P(X=x_1|Y=1) = 0.6$
$P(X=x_2|Y=1) = 0.3$
$P(X=x_3|Y=1) = 0.1$

1.  Déterminez le classifieur de Bayes optimal $h^*(x)$ pour ce problème.
2.  Calculez le taux d'erreur de Bayes $R(h^*)$.

## Correction Pas-à-Pas

### Partie 1 : Détermination du classifieur de Bayes optimal $h^*(x)$

Le classifieur de Bayes optimal $h^*(x)$ est la fonction qui minimise le risque de classification pour une fonction de perte $0-1$. Il attribue à chaque $x$ la classe $y$ qui maximise la probabilité a posteriori $P(Y=y|X=x)$.
$h^*(x) = \operatorname{argmax}_{y \in \{0,1\}} P(Y=y|X=x)$

En utilisant le théorème de Bayes, la probabilité a posteriori peut être exprimée comme :
$P(Y=y|X=x) = \frac{P(X=x|Y=y) P(Y=y)}{P(X=x)}$

Puisque $P(X=x)$ est une constante positive pour un $x$ donné, la décision du classifieur de Bayes peut être simplifiée en maximisant le numérateur :
$h^*(x) = \operatorname{argmax}_{y \in \{0,1\}} P(X=x|Y=y) P(Y=y)$

Nous allons calculer $P(X=x|Y=y) P(Y=y)$ pour chaque valeur de $X$ et chaque classe $Y$.

#### Pour $X=x_1$:
Calculons $P(X=x_1|Y=0) P(Y=0)$ et $P(X=x_1|Y=1) P(Y=1)$.

Pour $Y=0$:
$P(X=x_1|Y=0) P(Y=0) = 0.3 \times 0.6$
$P(X=x_1|Y=0) P(Y=0) = 0.18$

Pour $Y=1$:
$P(X=x_1|Y=1) P(Y=1) = 0.6 \times 0.4$
$P(X=x_1|Y=1) P(Y=1) = 0.24$

Comparaison pour $X=x_1$:
$0.18 < 0.24$
La valeur $0.24$ est la plus grande. Elle correspond à $Y=1$.
Donc, pour $X=x_1$, le classifieur de Bayes attribue la classe $Y=1$.
$h^*(x_1) = 1$

#### Pour $X=x_2$:
Calculons $P(X=x_2|Y=0) P(Y=0)$ et $P(X=x_2|Y=1) P(Y=1)$.

Pour $Y=0$:
$P(X=x_2|Y=0) P(Y=0) = 0.5 \times 0.6$
$P(X=x_2|Y=0) P(Y=0) = 0.30$

Pour $Y=1$:
$P(X=x_2|Y=1) P(Y=1) = 0.3 \times 0.4$
$P(X=x_2|Y=1) P(Y=1) = 0.12$

Comparaison pour $X=x_2$:
$0.30 > 0.12$
La valeur $0.30$ est la plus grande. Elle correspond à $Y=0$.
Donc, pour $X=x_2$, le classifieur de Bayes attribue la classe $Y=0$.
$h^*(x_2) = 0$

#### Pour $X=x_3$:
Calculons $P(X=x_3|Y=0) P(Y=0)$ et $P(X=x_3|Y=1) P(Y=1)$.

Pour $Y=0$:
$P(X=x_3|Y=0) P(Y=0) = 0.2 \times 0.6$
$P(X=x_3|Y=0) P(Y=0) = 0.12$

Pour $Y=1$:
$P(X=x_3|Y=1) P(Y=1) = 0.1 \times 0.4$
$P(X=x_3|Y=1) P(Y=1) = 0.04$

Comparaison pour $X=x_3$:
$0.12 > 0.04$
La valeur $0.12$ est la plus grande. Elle correspond à $Y=0$.
Donc, pour $X=x_3$, le classifieur de Bayes attribue la classe $Y=0$.
$h^*(x_3) = 0$

En résumé, le classifieur de Bayes optimal $h^*(x)$ est défini comme suit :
$h^*(x_1) = 1$
$h^*(x_2) = 0$
$h^*(x_3) = 0$

### Partie 2 : Calcul du taux d'erreur de Bayes $R(h^*)$

Le taux d'erreur de Bayes $R(h^*)$ est la probabilité que le classifieur de Bayes fasse une erreur. Il est donné par l'espérance de la fonction indicatrice d'erreur :
$R(h^*) = E[1_{h^*(X) \neq Y}]$
Pour des variables discrètes, cela se traduit par la somme des probabilités d'erreur pour chaque valeur de $X$:
$R(h^*) = \sum_{x} P(X=x, h^*(x) \neq Y)$
$R(h^*) = \sum_{x} P(X=x) P(h^*(x) \neq Y | X=x)$
La probabilité d'erreur conditionnelle $P(h^*(x) \neq Y | X=x)$ est la plus petite des probabilités a posteriori pour un $x$ donné :
$P(h^*(x) \neq Y | X=x) = \min(P(Y=0|X=x), P(Y=1|X=x))$
Donc, le taux d'erreur de Bayes est :
$R(h^*) = \sum_{x} P(X=x) \min(P(Y=0|X=x), P(Y=1|X=x))$

Pour utiliser cette formule, nous devons d'abord calculer $P(X=x)$ pour chaque $x$, puis $P(Y=y|X=x)$.

#### Calcul de $P(X=x)$ pour chaque $x$:
La probabilité marginale $P(X=x)$ est calculée en sommant sur les classes $Y$:
$P(X=x) = P(X=x|Y=0) P(Y=0) + P(X=x|Y=1) P(Y=1)$

Pour $X=x_1$:
$P(X=x_1) = P(X=x_1|Y=0) P(Y=0) + P(X=x_1|Y=1) P(Y=1)$
$P(X=x_1) = (0.3 \times 0.6) + (0.6 \times 0.4)$
$P(X=x_1) = 0.18 + 0.24$
$P(X=x_1) = 0.42$

Pour $X=x_2$:
$P(X=x_2) = P(X=x_2|Y=0) P(Y=0) + P(X=x_2|Y=1) P(Y=1)$
$P(X=x_2) = (0.5 \times 0.6) + (0.3 \times 0.4)$
$P(X=x_2) = 0.30 + 0.12$
$P(X=x_2) = 0.42$

Pour $X=x_3$:
$P(X=x_3) = P(X=x_3|Y=0) P(Y=0) + P(X=x_3|Y=1) P(Y=1)$
$P(X=x_3) = (0.2 \times 0.6) + (0.1 \times 0.4)$
$P(X=x_3) = 0.12 + 0.04$
$P(X=x_3) = 0.16$

Vérification de la somme des probabilités marginales de $X$:
$P(X=x_1) + P(X=x_2) + P(X=x_3) = 0.42 + 0.42 + 0.16 = 1.00$. La somme est correcte.

#### Calcul de $P(Y=y|X=x)$ pour chaque $x$ et $y$:
Nous utilisons la formule $P(Y=y|X=x) = \frac{P(X=x|Y=y) P(Y=y)}{P(X=x)}$.

Pour $X=x_1$:
$P(Y=0|X=x_1) = \frac{P(X=x_1|Y=0) P(Y=0)}{P(X=x_1)} = \frac{0.18}{0.42} = \frac{18}{42} = \frac{3}{7}$
$P(Y=1|X=x_1) = \frac{P(X=x_1|Y=1) P(Y=1)}{P(X=x_1)} = \frac{0.24}{0.42} = \frac{24}{42} = \frac{4}{7}$
Vérification : $3/7 + 4/7 = 7/7 = 1$. Correct.
Pour $X=x_1$, le classifieur de Bayes $h^*(x_1)=1$. La probabilité d'erreur pour $X=x_1$ est $\min(P(Y=0|X=x_1), P(Y=1|X=x_1)) = P(Y=0|X=x_1) = 3/7$.

Pour $X=x_2$:
$P(Y=0|X=x_2) = \frac{P(X=x_2|Y=0) P(Y=0)}{P(X=x_2)} = \frac{0.30}{0.42} = \frac{30}{42} = \frac{5}{7}$
$P(Y=1|X=x_2) = \frac{P(X=x_2|Y=1) P(Y=1)}{P(X=x_2)} = \frac{0.12}{0.42} = \frac{12}{42} = \frac{2}{7}$
Vérification : $5/7 + 2/7 = 7/7 = 1$. Correct.
Pour $X=x_2$, le classifieur de Bayes $h^*(x_2)=0$. La probabilité d'erreur pour $X=x_2$ est $\min(P(Y=0|X=x_2), P(Y=1|X=x_2)) = P(Y=1|X=x_2) = 2/7$.

Pour $X=x_3$:
$P(Y=0|X=x_3) = \frac{P(X=x_3|Y=0) P(Y=0)}{P(X=x_3)} = \frac{0.12}{0.16} = \frac{12}{16} = \frac{3}{4}$
$P(Y=1|X=x_3) = \frac{P(X=x_3|Y=1) P(Y=1)}{P(X=x_3)} = \frac{0.04}{0.16} = \frac{4}{16} = \frac{1}{4}$
Vérification : $3/4 + 1/4 = 4/4 = 1$. Correct.
Pour $X=x_3$, le classifieur de Bayes $h^*(x_3)=0$. La probabilité d'erreur pour $X=x_3$ est $\min(P(Y=0|X=x_3), P(Y=1|X=x_3)) = P(Y=1|X=x_3) = 1/4$.

#### Calcul du taux d'erreur de Bayes $R(h^*)$:
$R(h^*) = P(X=x_1) \times \min(P(Y=0|X=x_1), P(Y=1|X=x_1)) + P(X=x_2) \times \min(P(Y=0|X=x_2), P(Y=1|X=x_2)) + P(X=x_3) \times \min(P(Y=0|X=x_3), P(Y=1|X=x_3))$

En substituant les valeurs calculées :
$R(h^*) = P(X=x_1) \times P(Y=0|X=x_1) + P(X=x_2) \times P(Y=1|X=x_2) + P(X=x_3) \times P(Y=1|X=x_3)$

$R(h^*) = 0.42 \times \frac{3}{7} + 0.42 \times \frac{2}{7} + 0.16 \times \frac{1}{4}$

Pour faciliter le calcul, convertissons les décimales en fractions :
$0.42 = \frac{42}{100}$
$0.16 = \frac{16}{100}$

$R(h^*) = \frac{42}{100} \times \frac{3}{7} + \frac{42}{100} \times \frac{2}{7} + \frac{16}{100} \times \frac{1}{4}$

Simplifions les fractions :
$R(h^*) = \frac{6 \times 7}{100} \times \frac{3}{7} + \frac{6 \times 7}{100} \times \frac{2}{7} + \frac{4 \times 4}{100} \times \frac{1}{4}$

$R(h^*) = \frac{6 \times 3}{100} + \frac{6 \times 2}{100} + \frac{4 \times 1}{100}$

$R(h^*) = \frac{18}{100} + \frac{12}{100} + \frac{4}{100}$

$R(h^*) = 0.18 + 0.12 + 0.04$

$R(h^*) = 0.34$

Le taux d'erreur de Bayes optimal pour ce problème est $0.34$.
