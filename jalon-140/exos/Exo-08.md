---
uuid: "jalon-140-exo-08"
title: "Exercice 8 - Jalon 140"
---
# Exercice 8 : Minimisation de la Perte Logistique et Classifieur de Bayes
**Difficulté:** ★★★★

## Énoncé
Soit un problème de classification binaire où la variable de sortie $Y \in \{-1, 1\}$ et la variable d'entrée $X \in \mathcal{X}$.
On note $\eta(x) = P(Y=1|X=x)$ la probabilité conditionnelle de la classe positive.
La fonction de perte logistique (binary cross-entropy) pour une prédiction $f(x) \in \mathbb{R}$ et une vraie étiquette $y \in \{-1, 1\}$ est définie par $L_{log}(y, f(x)) = \log(1 + \exp(-y f(x)))$.

1.  Déterminez la fonction $f^*(x)$ qui minimise l'espérance de la perte logistique conditionnellement à $X=x$. C'est-à-dire, trouvez $f^*(x) = \arg\min_{f \in \mathbb{R}} \mathbb{E}[L_{log}(Y, f)|X=x]$.
2.  Montrez que le signe de cette fonction $f^*(x)$ correspond au classifieur de Bayes optimal $h^*(x)$ pour la perte 0-1, défini par $h^*(x) = \text{sgn}(\eta(x) - 0.5)$.

## Correction Pas-à-Pas

### Partie 1 : Détermination de $f^*(x)$

L'objectif est de minimiser l'espérance de la perte logistique conditionnellement à $X=x$.
Soit $f$ une valeur réelle représentant $f(x)$ pour un $x$ fixe.
L'espérance conditionnelle de la perte logistique est donnée par :
$\mathbb{E}[L_{log}(Y, f)|X=x] = P(Y=1|X=x) \cdot L_{log}(1, f) + P(Y=-1|X=x) \cdot L_{log}(-1, f)$

Nous savons que $P(Y=1|X=x) = \eta(x)$ et $P(Y=-1|X=x) = 1 - \eta(x)$.
Substituons ces probabilités et la définition de la perte logistique dans l'expression de l'espérance conditionnelle :
$\mathbb{E}[L_{log}(Y, f)|X=x] = \eta(x) \cdot \log(1 + \exp(-1 \cdot f)) + (1 - \eta(x)) \cdot \log(1 + \exp(-(-1) \cdot f))$
$\mathbb{E}[L_{log}(Y, f)|X=x] = \eta(x) \cdot \log(1 + \exp(-f)) + (1 - \eta(x)) \cdot \log(1 + \exp(f))$

Pour trouver le minimum de cette fonction par rapport à $f$, nous allons calculer sa dérivée première par rapport à $f$ et l'égaliser à zéro.
Soit $L(f|x) = \eta(x) \cdot \log(1 + \exp(-f)) + (1 - \eta(x)) \cdot \log(1 + \exp(f))$.

Calculons la dérivée de chaque terme séparément :

Dérivée du premier terme :
$\frac{\partial}{\partial f} \left[ \eta(x) \cdot \log(1 + \exp(-f)) \right]$
$= \eta(x) \cdot \frac{1}{1 + \exp(-f)} \cdot \frac{\partial}{\partial f} (1 + \exp(-f))$
$= \eta(x) \cdot \frac{1}{1 + \exp(-f)} \cdot (-\exp(-f))$
$= \eta(x) \cdot \frac{-\exp(-f)}{1 + \exp(-f)}$
Pour simplifier l'expression $\frac{\exp(-f)}{1 + \exp(-f)}$, nous pouvons multiplier le numérateur et le dénominateur par $\exp(f)$ :
$\frac{\exp(-f) \cdot \exp(f)}{(1 + \exp(-f)) \cdot \exp(f)} = \frac{1}{\exp(f) + 1}$
Donc, la dérivée du premier terme devient :
$\eta(x) \cdot \frac{-1}{1 + \exp(f)}$

Dérivée du second terme :
$\frac{\partial}{\partial f} \left[ (1 - \eta(x)) \cdot \log(1 + \exp(f)) \right]$
$= (1 - \eta(x)) \cdot \frac{1}{1 + \exp(f)} \cdot \frac{\partial}{\partial f} (1 + \exp(f))$
$= (1 - \eta(x)) \cdot \frac{1}{1 + \exp(f)} \cdot (\exp(f))$
$= (1 - \eta(x)) \cdot \frac{\exp(f)}{1 + \exp(f)}$

Maintenant, nous sommons les deux dérivées pour obtenir la dérivée totale $\frac{\partial L(f|x)}{\partial f}$ :
$\frac{\partial L(f|x)}{\partial f} = \eta(x) \cdot \frac{-1}{1 + \exp(f)} + (1 - \eta(x)) \cdot \frac{\exp(f)}{1 + \exp(f)}$
$\frac{\partial L(f|x)}{\partial f} = \frac{-\eta(x) + (1 - \eta(x)) \exp(f)}{1 + \exp(f)}$

Pour trouver le minimum, nous égalisons la dérivée à zéro :
$\frac{-\eta(x) + (1 - \eta(x)) \exp(f)}{1 + \exp(f)} = 0$
Puisque le dénominateur $1 + \exp(f)$ est toujours strictement positif pour tout $f \in \mathbb{R}$, le numérateur doit être nul :
$-\eta(x) + (1 - \eta(x)) \exp(f) = 0$
$(1 - \eta(x)) \exp(f) = \eta(x)$

Nous devons considérer le cas où $1 - \eta(x) = 0$. Si $1 - \eta(x) = 0$, alors $\eta(x) = 1$. L'équation devient $0 \cdot \exp(f) = 1$, ce qui est impossible. Dans ce cas, la perte est $\log(1 + \exp(-f))$, qui est minimisée lorsque $f \to \infty$.
Si $1 - \eta(x) \neq 0$ (c'est-à-dire $\eta(x) \neq 1$), nous pouvons diviser par $1 - \eta(x)$ :
$\exp(f) = \frac{\eta(x)}{1 - \eta(x)}$

Pour résoudre pour $f$, nous prenons le logarithme naturel des deux côtés :
$f^*(x) = \log\left(\frac{\eta(x)}{1 - \eta(x)}\right)$

Cette fonction $f^*(x)$ est le minimisateur de l'espérance conditionnelle de la perte logistique. C'est la fonction logit des probabilités conditionnelles.
Pour confirmer que c'est bien un minimum, nous pouvons calculer la dérivée seconde.
$\frac{\partial^2 L(f|x)}{\partial f^2} = \frac{\partial}{\partial f} \left[ \frac{-\eta(x) + (1 - \eta(x)) \exp(f)}{1 + \exp(f)} \right]$
En utilisant la règle du quotient $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ avec $u = -\eta(x) + (1 - \eta(x)) \exp(f)$ et $v = 1 + \exp(f)$.
$u' = (1 - \eta(x)) \exp(f)$
$v' = \exp(f)$
$\frac{\partial^2 L(f|x)}{\partial f^2} = \frac{((1 - \eta(x)) \exp(f))(1 + \exp(f)) - (-\eta(x) + (1 - \eta(x)) \exp(f))(\exp(f))}{(1 + \exp(f))^2}$
Au point où la dérivée première est nulle, nous avons $-\eta(x) + (1 - \eta(x)) \exp(f) = 0$.
Par conséquent, le second terme du numérateur s'annule.
$\frac{\partial^2 L(f|x)}{\partial f^2} = \frac{((1 - \eta(x)) \exp(f))(1 + \exp(f))}{(1 + \exp(f))^2}$
$\frac{\partial^2 L(f|x)}{\partial f^2} = \frac{(1 - \eta(x)) \exp(f)}{1 + \exp(f)}$
Puisque $\eta(x) \in [0, 1]$, alors $1 - \eta(x) \ge 0$. De plus, $\exp(f) > 0$ et $1 + \exp(f) > 0$.
Donc, $\frac{\partial^2 L(f|x)}{\partial f^2} \ge 0$. Plus précisément, si $\eta(x) < 1$, la dérivée seconde est strictement positive, ce qui confirme que $f^*(x)$ est un minimum global (la fonction est convexe). Si $\eta(x)=1$, la dérivée seconde est 0, ce qui est cohérent avec la limite $f \to \infty$.

### Partie 2 : Lien avec le classifieur de Bayes optimal

Le classifieur de Bayes optimal $h^*(x)$ pour la perte 0-1 est défini par :
$h^*(x) = \text{sgn}(\eta(x) - 0.5)$

Nous devons montrer que le signe de $f^*(x)$ correspond à $h^*(x)$.
Nous avons trouvé $f^*(x) = \log\left(\frac{\eta(x)}{1 - \eta(x)}\right)$.

Analysons le signe de $f^*(x)$ en fonction de $\eta(x)$ :

**Cas 1 : $\eta(x) > 0.5$**
Si $\eta(x) > 0.5$, alors $1 - \eta(x) < 0.5$.
Par conséquent, $\eta(x) > 1 - \eta(x)$.
La fraction $\frac{\eta(x)}{1 - \eta(x)}$ est donc strictement supérieure à 1.
Puisque la fonction logarithme naturel ($\log$) est strictement croissante, $\log\left(\frac{\eta(x)}{1 - \eta(x)}\right) > \log(1)$.
Nous savons que $\log(1) = 0$.
Donc, $f^*(x) > 0$.
Dans ce cas, $\text{sgn}(f^*(x)) = 1$.
Pour le classifieur de Bayes : $\eta(x) - 0.5 > 0$, donc $h^*(x) = \text{sgn}(\eta(x) - 0.5) = 1$.
Le signe de $f^*(x)$ correspond à $h^*(x)$.

**Cas 2 : $\eta(x) < 0.5$**
Si $\eta(x) < 0.5$, alors $1 - \eta(x) > 0.5$.
Par conséquent, $\eta(x) < 1 - \eta(x)$.
La fraction $\frac{\eta(x)}{1 - \eta(x)}$ est donc strictement inférieure à 1 (et strictement positive, car $\eta(x) \ge 0$).
Puisque la fonction logarithme naturel ($\log$) est strictement croissante, $\log\left(\frac{\eta(x)}{1 - \eta(x)}\right) < \log(1)$.
Nous savons que $\log(1) = 0$.
Donc, $f^*(x) < 0$.
Dans ce cas, $\text{sgn}(f^*(x)) = -1$.
Pour le classifieur de Bayes : $\eta(x) - 0.5 < 0$, donc $h^*(x) = \text{sgn}(\eta(x) - 0.5) = -1$.
Le signe de $f^*(x)$ correspond à $h^*(x)$.

**Cas 3 : $\eta(x) = 0.5$**
Si $\eta(x) = 0.5$, alors $1 - \eta(x) = 0.5$.
La fraction $\frac{\eta(x)}{1 - \eta(x)}$ est donc égale à $\frac{0.5}{0.5} = 1$.
$f^*(x) = \log(1) = 0$.
Dans ce cas, $\text{sgn}(f^*(x)) = 0$.
Pour le classifieur de Bayes : $\eta(x) - 0.5 = 0.5 - 0.5 = 0$, donc $h^*(x) = \text{sgn}(0) = 0$.
Le signe de $f^*(x)$ correspond à $h^*(x)$.

Dans tous les cas, nous avons démontré que $\text{sgn}(f^*(x)) = h^*(x)$.
Ainsi, la fonction $f^*(x)$ qui minimise l'espérance de la perte logistique est telle que son signe est égal au classifieur de Bayes optimal pour la perte 0-1.
