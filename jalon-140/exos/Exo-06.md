---
uuid: "jalon-140-exo-06"
title: "Exercice 6 - Jalon 140"
---
# Exercice 6 : Minimisation de la Perte Exponentielle et Classifieur de Bayes
**Difficulté:** ★★★

## Énoncé
Soit un problème de classification binaire où la variable cible $Y$ prend ses valeurs dans l'ensemble $\{-1, 1\}$ et $X$ est une variable aléatoire représentant les caractéristiques.
On définit la probabilité conditionnelle $\eta(x) = P(Y=1|X=x)$ pour tout $x$ dans l'espace des caractéristiques.
Le classifieur de Bayes optimal $h^*(x)$ pour la perte 0-1 est donné par $h^*(x) = \text{sgn}(2\eta(x) - 1)$.

On considère la perte de substitution exponentielle (Exponential Loss) définie par $L_{exp}(y, f) = \exp(-y f)$, où $f$ est une fonction de score à valeurs réelles $f: \mathcal{X} \to \mathbb{R}$.
L'objectif est de trouver la fonction de score $f^*(x)$ qui minimise le risque attendu de la perte exponentielle, conditionnellement à $X=x$.
Formellement, nous cherchons $f^*(x) = \arg\min_{f \in \mathbb{R}} \mathbb{E}[L_{exp}(Y, f) | X=x]$.

1.  Exprimez l'espérance conditionnelle $\mathbb{E}[L_{exp}(Y, f) | X=x]$ en fonction de $\eta(x)$ et $f$.
2.  Calculez la dérivée de cette espérance conditionnelle par rapport à $f$.
3.  Déterminez la valeur de $f^*(x)$ qui minimise cette espérance conditionnelle.
4.  Montrez que le classifieur $\text{sgn}(f^*(x))$ est équivalent au classifieur de Bayes optimal $h^*(x)$.

## Correction Pas-à-Pas

### Question 1 : Expression de l'espérance conditionnelle
L'espérance conditionnelle $\mathbb{E}[L_{exp}(Y, f) | X=x]$ est calculée en sommant les valeurs de la perte exponentielle pondérées par les probabilités conditionnelles de $Y$:
$\mathbb{E}[L_{exp}(Y, f) | X=x] = \sum_{y \in \{-1, 1\}} L_{exp}(y, f) P(Y=y|X=x)$
Nous décomposons cette somme pour les deux valeurs possibles de $Y$:
$\mathbb{E}[L_{exp}(Y, f) | X=x] = L_{exp}(1, f) P(Y=1|X=x) + L_{exp}(-1, f) P(Y=-1|X=x)$

Nous utilisons les définitions suivantes :
$P(Y=1|X=x) = \eta(x)$
$P(Y=-1|X=x) = 1 - P(Y=1|X=x) = 1 - \eta(x)$
$L_{exp}(1, f) = \exp(-1 \cdot f) = \exp(-f)$
$L_{exp}(-1, f) = \exp(-(-1) \cdot f) = \exp(f)$

En substituant ces expressions dans l'équation de l'espérance conditionnelle, nous obtenons :
$\mathbb{E}[L_{exp}(Y, f) | X=x] = \exp(-f) \eta(x) + \exp(f) (1 - \eta(x))$

### Question 2 : Calcul de la dérivée de l'espérance conditionnelle
Soit $J(f, x)$ la fonction que nous souhaitons minimiser par rapport à $f$, pour un $x$ fixé :
$J(f, x) = \mathbb{E}[L_{exp}(Y, f) | X=x] = \exp(-f) \eta(x) + \exp(f) (1 - \eta(x))$

Nous calculons la dérivée partielle de $J(f, x)$ par rapport à $f$:
$\frac{\partial J(f, x)}{\partial f} = \frac{\partial}{\partial f} [\exp(-f) \eta(x) + \exp(f) (1 - \eta(x))]$
En utilisant la règle de dérivation de $\exp(ku)$ qui est $k \exp(ku)$:
$\frac{\partial}{\partial f} (\exp(-f) \eta(x)) = -\exp(-f) \eta(x)$
$\frac{\partial}{\partial f} (\exp(f) (1 - \eta(x))) = \exp(f) (1 - \eta(x))$

Donc, la dérivée de l'espérance conditionnelle par rapport à $f$ est :
$\frac{\partial J(f, x)}{\partial f} = -\exp(-f) \eta(x) + \exp(f) (1 - \eta(x))$

### Question 3 : Détermination de la valeur de $f^*(x)$
Pour trouver la valeur de $f^*(x)$ qui minimise l'espérance conditionnelle, nous égalisons la dérivée à zéro :
$-\exp(-f) \eta(x) + \exp(f) (1 - \eta(x)) = 0$

Nous réarrangeons l'équation pour isoler les termes :
$\exp(f) (1 - \eta(x)) = \exp(-f) \eta(x)$

Pour simplifier, nous multiplions les deux côtés de l'équation par $\exp(f)$ (qui est toujours positif et non nul) :
$\exp(f) \cdot \exp(f) (1 - \eta(x)) = \exp(f) \cdot \exp(-f) \eta(x)$
$\exp(2f) (1 - \eta(x)) = \exp(0) \eta(x)$
$\exp(2f) (1 - \eta(x)) = 1 \cdot \eta(x)$
$\exp(2f) (1 - \eta(x)) = \eta(x)$

Nous devons considérer le cas où $1 - \eta(x) = 0$, c'est-à-dire $\eta(x) = 1$. Dans ce cas, l'équation devient $\exp(2f) \cdot 0 = 1$, ce qui est $0=1$, une contradiction. Cela signifie que si $\eta(x)=1$, il n'y a pas de $f$ fini qui annule la dérivée. Si $\eta(x)=1$, alors $J(f,x) = \exp(-f)$. Pour minimiser $\exp(-f)$, $f$ doit tendre vers $+\infty$.
De même, si $\eta(x)=0$, alors $J(f,x) = \exp(f)$. Pour minimiser $\exp(f)$, $f$ doit tendre vers $-\infty$.
Ces cas limites sont cohérents avec l'intuition.

En supposant que $1 - \eta(x) \neq 0$ (c'est-à-dire $\eta(x) \neq 1$), nous pouvons diviser par $(1 - \eta(x))$ :
$\exp(2f) = \frac{\eta(x)}{1 - \eta(x)}$

Pour résoudre pour $f$, nous appliquons le logarithme naturel (ln) des deux côtés de l'équation :
$\ln(\exp(2f)) = \ln\left(\frac{\eta(x)}{1 - \eta(x)}\right)$
$2f = \ln\left(\frac{\eta(x)}{1 - \eta(x)}\right)$

Enfin, nous isolons $f$ pour obtenir la fonction de score optimale $f^*(x)$ :
$f^*(x) = \frac{1}{2} \ln\left(\frac{\eta(x)}{1 - \eta(x)}\right)$

Pour confirmer qu'il s'agit bien d'un minimum, nous calculons la seconde dérivée de $J(f, x)$ par rapport à $f$:
$\frac{\partial^2 J(f, x)}{\partial f^2} = \frac{\partial}{\partial f} [-\exp(-f) \eta(x) + \exp(f) (1 - \eta(x))]$
$\frac{\partial^2 J(f, x)}{\partial f^2} = -(-\exp(-f)) \eta(x) + \exp(f) (1 - \eta(x))$
$\frac{\partial^2 J(f, x)}{\partial f^2} = \exp(-f) \eta(x) + \exp(f) (1 - \eta(x))$
Puisque $\eta(x) \in [0, 1]$, $\exp(-f) > 0$, $\exp(f) > 0$, $\eta(x) \ge 0$, et $1-\eta(x) \ge 0$, la seconde dérivée est toujours positive (strictement positive si $\eta(x) \in (0,1)$). Cela confirme que $f^*(x)$ correspond bien à un minimum global.

### Question 4 : Équivalence avec le classifieur de Bayes optimal
Le classifieur basé sur la fonction de score $f^*(x)$ est $\text{sgn}(f^*(x))$.
Nous avons trouvé $f^*(x) = \frac{1}{2} \ln\left(\frac{\eta(x)}{1 - \eta(x)}\right)$.
Le signe de $f^*(x)$ est déterminé par le signe de $\ln\left(\frac{\eta(x)}{1 - \eta(x)}\right)$, car $\frac{1}{2}$ est une constante positive.

Le signe de $\ln(u)$ est positif si $u > 1$, négatif si $0 < u < 1$, et nul si $u = 1$.
Nous analysons le signe de l'argument du logarithme, $\frac{\eta(x)}{1 - \eta(x)}$ :

1.  **Cas où $\frac{\eta(x)}{1 - \eta(x)} > 1$ :**
    $\eta(x) > 1 - \eta(x)$
    $2\eta(x) > 1$
    $\eta(x) > \frac{1}{2}$
    Dans ce cas, $\ln\left(\frac{\eta(x)}{1 - \eta(x)}\right) > 0$, donc $f^*(x) > 0$.
    Par conséquent, $\text{sgn}(f^*(x)) = 1$.

2.  **Cas où $\frac{\eta(x)}{1 - \eta(x)} < 1$ :**
    $\eta(x) < 1 - \eta(x)$
    $2\eta(x) < 1$
    $\eta(x) < \frac{1}{2}$
    Dans ce cas, $\ln\left(\frac{\eta(x)}{1 - \eta(x)}\right) < 0$, donc $f^*(x) < 0$.
    Par conséquent, $\text{sgn}(f^*(x)) = -1$.

3.  **Cas où $\frac{\eta(x)}{1 - \eta(x)} = 1$ :**
    $\eta(x) = 1 - \eta(x)$
    $2\eta(x) = 1$
    $\eta(x) = \frac{1}{2}$
    Dans ce cas, $\ln\left(\frac{\eta(x)}{1 - \eta(x)}\right) = \ln(1) = 0$, donc $f^*(x) = 0$.
    Par conséquent, $\text{sgn}(f^*(x))$ est 0.

Comparons ces résultats avec le classifieur de Bayes optimal $h^*(x) = \text{sgn}(2\eta(x) - 1)$ :
*   Si $\eta(x) > \frac{1}{2}$, alors $2\eta(x) - 1 > 0$, donc $h^*(x) = 1$. Cela correspond à $\text{sgn}(f^*(x)) = 1$.
*   Si $\eta(x) < \frac{1}{2}$, alors $2\eta(x) - 1 < 0$, donc $h^*(x) = -1$. Cela correspond à $\text{sgn}(f^*(x)) = -1$.
*   Si $\eta(x) = \frac{1}{2}$, alors $2\eta(x) - 1 = 0$, donc $h^*(x)$ est généralement défini comme 1 (ou -1, la décision n'affecte pas la perte 0-1 dans ce cas d'égalité). Le fait que $\text{sgn}(f^*(x))$ soit 0 dans ce cas ne change pas la classification pratique, car la frontière de décision est la même.

En conclusion, le classifieur $\text{sgn}(f^*(x))$ prend la même décision de classification que le classifieur de Bayes optimal $h^*(x)$ pour toutes les valeurs de $x$.
Par conséquent, le classifieur $\text{sgn}(f^*(x))$ est équivalent au classifieur de Bayes optimal $h^*(x)$.
