---
uuid: "jalon-140-exo-09"
title: "Exercice 9 - Jalon 140"
---
# Exercice 9 : Calibration de la Perte Exponentielle et Classifieur de Bayes Optimal
**Difficulté:** ★★★★★

## Énoncé
Soit un problème de classification binaire où l'espace des entrées est $\mathcal{X}$ et l'espace des sorties est $\mathcal{Y} = \{-1, 1\}$. Nous disposons d'un vecteur de caractéristiques aléatoire $X \in \mathcal{X}$ et d'une étiquette de classe aléatoire $Y \in \mathcal{Y}$. La distribution conjointe de $(X, Y)$ est $P(X, Y)$. Nous définissons la probabilité conditionnelle $P(Y=1|X=x)$ par $\eta(x)$ et $P(Y=-1|X=x)$ par $1-\eta(x)$.

Un classifieur est une fonction $h: \mathcal{X} \to \mathcal{Y}$. La perte 0-1 est définie par $L_{01}(y, h(x)) = \mathbb{I}(y \neq h(x))$, où $\mathbb{I}(\cdot)$ est la fonction indicatrice qui vaut 1 si la condition est vraie et 0 sinon.

Une fonction de score $f: \mathcal{X} \to \mathbb{R}$ est utilisée pour prendre des décisions, où le classifieur associé est $h_f(x) = \text{sgn}(f(x))$. La perte exponentielle est définie par $L_{\text{exp}}(y, f(x)) = \exp(-y f(x))$.

1.  **Dérivation du Classifieur de Bayes Optimal :**
    Déterminez le classifieur de Bayes optimal $h^*(x)$ qui minimise le risque attendu $R_{01}(h) = E[L_{01}(Y, h(X))]$. Exprimez $h^*(x)$ en fonction de $\eta(x)$.

2.  **Minimisation du Risque Exponentiel Attendu :**
    Considérons le risque exponentiel attendu $R_{\text{exp}}(f) = E[L_{\text{exp}}(Y, f(X))]$. Pour un $x \in \mathcal{X}$ fixe, trouvez la fonction de score optimale $f^*(x)$ qui minimise le risque exponentiel conditionnel $E[L_{\text{exp}}(Y, f(X)) | X=x]$. Exprimez $f^*(x)$ en fonction de $\eta(x)$.

3.  **Démonstration de la Calibration :**
    Montrez que le classifieur $h_{f^*}^*(x) = \text{sgn}(f^*(x))$, obtenu à partir de la fonction de score optimale $f^*(x)$ de la perte exponentielle, est équivalent au classifieur de Bayes optimal $h^*(x)$ pour tout $x$ où $P(Y=1|X=x) \neq P(Y=-1|X=x)$.

## Correction Pas-à-Pas

### Partie 1 : Dérivation du Classifieur de Bayes Optimal

Le risque attendu pour la perte 0-1 est défini comme l'espérance de la perte 0-1 sur la distribution conjointe de $(X, Y)$ :
$R_{01}(h) = E[L_{01}(Y, h(X))]$

Par la loi de l'espérance totale, nous pouvons décomposer cette espérance en une espérance conditionnelle :
$R_{01}(h) = E[E[L_{01}(Y, h(X)) | X]]$

Pour minimiser le risque total $R_{01}(h)$, il est suffisant de minimiser le risque conditionnel $E[L_{01}(Y, h(X)) | X=x]$ pour chaque valeur $x \in \mathcal{X}$ indépendamment.
Soit $R_{01}(h|X=x)$ le risque conditionnel pour un $x$ fixe :
$R_{01}(h|X=x) = E[L_{01}(Y, h(x)) | X=x]$

Le classifieur $h(x)$ peut prendre deux valeurs : $1$ ou $-1$. Nous allons évaluer le risque conditionnel pour chacun de ces choix.

**Cas 1 :** $h(x) = 1$
Le risque conditionnel est :
$R_{01}(1|X=x) = E[\mathbb{I}(Y \neq 1) | X=x]$
Par définition de l'espérance pour une variable indicatrice, ceci est la probabilité de l'événement :
$R_{01}(1|X=x) = P(Y \neq 1 | X=x)$
Puisque $Y \in \{-1, 1\}$, l'événement $Y \neq 1$ est équivalent à $Y=-1$ :
$R_{01}(1|X=x) = P(Y=-1 | X=x)$
En utilisant la notation $\eta(x) = P(Y=1|X=x)$, nous savons que $P(Y=-1|X=x) = 1 - P(Y=1|X=x) = 1 - \eta(x)$.
Donc, $R_{01}(1|X=x) = 1 - \eta(x)$.

**Cas 2 :** $h(x) = -1$
Le risque conditionnel est :
$R_{01}(-1|X=x) = E[\mathbb{I}(Y \neq -1) | X=x]$
Ceci est la probabilité de l'événement :
$R_{01}(-1|X=x) = P(Y \neq -1 | X=x)$
Puisque $Y \in \{-1, 1\}$, l'événement $Y \neq -1$ est équivalent à $Y=1$ :
$R_{01}(-1|X=x) = P(Y=1 | X=x)$
En utilisant la notation $\eta(x) = P(Y=1|X=x)$ :
Donc, $R_{01}(-1|X=x) = \eta(x)$.

Le classifieur de Bayes optimal $h^*(x)$ est celui qui minimise ce risque conditionnel. Il choisit la classe qui a la plus faible probabilité d'erreur :
$h^*(x) = \begin{cases} 1 & \text{si } R_{01}(1|X=x) < R_{01}(-1|X=x) \\ -1 & \text{si } R_{01}(-1|X=x) < R_{01}(1|X=x) \\ 1 \text{ (ou -1, choix arbitraire)} & \text{si } R_{01}(1|X=x) = R_{01}(-1|X=x) \end{cases}$

En substituant les expressions des risques conditionnels :
$h^*(x) = \begin{cases} 1 & \text{si } 1 - \eta(x) < \eta(x) \\ -1 & \text{si } \eta(x) < 1 - \eta(x) \\ 1 \text{ (ou -1)} & \text{si } 1 - \eta(x) = \eta(x) \end{cases}$

Simplifions les conditions :
1.  $1 - \eta(x) < \eta(x) \implies 1 < 2\eta(x) \implies \eta(x) > \frac{1}{2}$
2.  $\eta(x) < 1 - \eta(x) \implies 2\eta(x) < 1 \implies \eta(x) < \frac{1}{2}$
3.  $1 - \eta(x) = \eta(x) \implies 2\eta(x) = 1 \implies \eta(x) = \frac{1}{2}$

Ainsi, le classifieur de Bayes optimal est :
$h^*(x) = \begin{cases} 1 & \text{si } \eta(x) > \frac{1}{2} \\ -1 & \text{si } \eta(x) < \frac{1}{2} \\ 1 \text{ (ou -1)} & \text{si } \eta(x) = \frac{1}{2} \end{cases}$

Cette expression peut être reformulée en utilisant la fonction signe. Nous savons que $\eta(x) = P(Y=1|X=x)$ et $1-\eta(x) = P(Y=-1|X=x)$.
Alors, la différence $P(Y=1|X=x) - P(Y=-1|X=x)$ est égale à $\eta(x) - (1-\eta(x)) = 2\eta(x) - 1$.
*   Si $\eta(x) > \frac{1}{2}$, alors $2\eta(x) - 1 > 0$.
*   Si $\eta(x) < \frac{1}{2}$, alors $2\eta(x) - 1 < 0$.
*   Si $\eta(x) = \frac{1}{2}$, alors $2\eta(x) - 1 = 0$.

Par conséquent, le classifieur de Bayes optimal $h^*(x)$ peut être exprimé comme :
$h^*(x) = \text{sgn}(P(Y=1|X=x) - P(Y=-1|X=x))$
Ou de manière équivalente :
$h^*(x) = \text{sgn}(2\eta(x) - 1)$
où la fonction $\text{sgn}(z)$ est définie comme $1$ si $z>0$, $-1$ si $z<0$, et $0$ (ou une valeur arbitraire comme $1$ ou $-1$) si $z=0$.

### Partie 2 : Minimisation du Risque Exponentiel Attendu

Le risque exponentiel attendu est $R_{\text{exp}}(f) = E[L_{\text{exp}}(Y, f(X))] = E[\exp(-Y f(X))]$.

De manière similaire à la Partie 1, pour minimiser $R_{\text{exp}}(f)$, nous minimisons le risque exponentiel conditionnel $E[\exp(-Y f(X)) | X=x]$ pour chaque $x \in \mathcal{X}$ indépendamment.
Soit $R_{\text{exp}}(f|X=x)$ le risque exponentiel conditionnel pour un $x$ fixe :
$R_{\text{exp}}(f|X=x) = E[\exp(-Y f(x)) | X=x]$

En utilisant la définition de l'espérance conditionnelle pour une variable discrète $Y$ prenant les valeurs $1$ et $-1$ :
$R_{\text{exp}}(f|X=x) = P(Y=1|X=x) \cdot \exp(-1 \cdot f(x)) + P(Y=-1|X=x) \cdot \exp(-(-1) \cdot f(x))$
En substituant $\eta(x) = P(Y=1|X=x)$ et $1-\eta(x) = P(Y=-1|X=x)$ :
$R_{\text{exp}}(f|X=x) = \eta(x) \exp(-f(x)) + (1-\eta(x)) \exp(f(x))$

Pour trouver la fonction de score optimale $f^*(x)$, nous dérivons $R_{\text{exp}}(f|X=x)$ par rapport à $f(x)$ et nous égalisons la dérivée à zéro.
Soit $g(f) = \eta(x) e^{-f} + (1-\eta(x)) e^f$.
La première dérivée de $g(f)$ par rapport à $f$ est :
$\frac{d}{df} g(f) = \frac{d}{df} (\eta(x) e^{-f}) + \frac{d}{df} ((1-\eta(x)) e^f)$
$\frac{d}{df} g(f) = \eta(x) (-e^{-f}) + (1-\eta(x)) (e^f)$
$\frac{d}{df} g(f) = -\eta(x) e^{-f} + (1-\eta(x)) e^f$

Nous égalisons la dérivée à zéro pour trouver les points critiques :
$-\eta(x) e^{-f} + (1-\eta(x)) e^f = 0$
$(1-\eta(x)) e^f = \eta(x) e^{-f}$

Pour résoudre pour $f$, nous multiplions les deux côtés de l'équation par $e^f$ (qui est toujours strictement positif, donc l'opération est valide et ne change pas le signe) :
$(1-\eta(x)) e^f \cdot e^f = \eta(x) e^{-f} \cdot e^f$
$(1-\eta(x)) e^{2f} = \eta(x) e^0$
$(1-\eta(x)) e^{2f} = \eta(x)$

En supposant que $1-\eta(x) \neq 0$ (c'est-à-dire $\eta(x) \neq 1$), nous pouvons diviser par $1-\eta(x)$ :
$e^{2f} = \frac{\eta(x)}{1-\eta(x)}$

Nous prenons le logarithme naturel (ln) des deux côtés de l'équation :
$\ln(e^{2f}) = \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)$
En utilisant la propriété $\ln(e^A) = A$ :
$2f = \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)$

Enfin, nous isolons $f$ pour obtenir la fonction de score optimale $f^*(x)$ :
$f^*(x) = \frac{1}{2} \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)$

Pour confirmer qu'il s'agit bien d'un minimum, nous calculons la seconde dérivée de $g(f)$ par rapport à $f$ :
$\frac{d^2}{df^2} g(f) = \frac{d}{df} (-\eta(x) e^{-f} + (1-\eta(x)) e^f)$
$\frac{d^2}{df^2} g(f) = -\eta(x) (-e^{-f}) + (1-\eta(x)) (e^f)$
$\frac{d^2}{df^2} g(f) = \eta(x) e^{-f} + (1-\eta(x)) e^f$
Puisque $\eta(x) \in [0, 1]$ et les termes $e^{-f}$ et $e^f$ sont toujours strictement positifs, la seconde dérivée est toujours positive pour $\eta(x) \in (0,1)$. Si $\eta(x)=0$ ou $\eta(x)=1$, la fonction est monotone et le minimum est atteint à l'infini ou moins l'infini, mais pour $\eta(x) \in (0,1)$, la seconde dérivée est strictement positive, confirmant que $f^*(x)$ correspond à un minimum local.

### Partie 3 : Démonstration de la Calibration

Le classifieur obtenu à partir de la fonction de score optimale $f^*(x)$ est $h_{f^*}^*(x) = \text{sgn}(f^*(x))$.
Nous substituons l'expression de $f^*(x)$ trouvée dans la Partie 2 :
$h_{f^*}^*(x) = \text{sgn}\left(\frac{1}{2} \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)\right)$

Le signe d'une constante positive (ici $\frac{1}{2}$) ne change pas le signe de l'expression. Donc :
$h_{f^*}^*(x) = \text{sgn}\left(\ln\left(\frac{\eta(x)}{1-\eta(x)}\right)\right)$

Nous analysons le signe de la fonction logarithme naturel $\ln(u)$ :
*   $\ln(u) > 0$ si et seulement si $u > 1$.
*   $\ln(u) < 0$ si et seulement si $0 < u < 1$.
*   $\ln(u) = 0$ si et seulement si $u = 1$.

Appliquons ces conditions à l'argument du logarithme, $u = \frac{\eta(x)}{1-\eta(x)}$ :

**Cas 1 :** $\frac{\eta(x)}{1-\eta(x)} > 1$
Puisque $\eta(x) \in [0, 1]$, le dénominateur $1-\eta(x)$ est positif (strictement positif si $\eta(x) \neq 1$).
Multiplions par $1-\eta(x)$ des deux côtés de l'inégalité :
$\eta(x) > 1-\eta(x)$
Ajoutons $\eta(x)$ des deux côtés :
$2\eta(x) > 1$
Divisons par 2 :
$\eta(x) > \frac{1}{2}$
Dans ce cas, $\ln\left(\frac{\eta(x)}{1-\eta(x)}\right) > 0$, donc $h_{f^*}^*(x) = 1$.

**Cas 2 :** $\frac{\eta(x)}{1-\eta(x)} < 1$
Puisque $1-\eta(x)$ est positif (strictement positif si $\eta(x) \neq 1$).
Multiplions par $1-\eta(x)$ des deux côtés de l'inégalité :
$\eta(x) < 1-\eta(x)$
Ajoutons $\eta(x)$ des deux côtés :
$2\eta(x) < 1$
Divisons par 2 :
$\eta(x) < \frac{1}{2}$
Dans ce cas, $\ln\left(\frac{\eta(x)}{1-\eta(x)}\right) < 0$, donc $h_{f^*}^*(x) = -1$.

**Cas 3 :** $\frac{\eta(x)}{1-\eta(x)} = 1$
Multiplions par $1-\eta(x)$ des deux côtés de l'égalité :
$\eta(x) = 1-\eta(x)$
Ajoutons $\eta(x)$ des deux côtés :
$2\eta(x) = 1$
Divisons par 2 :
$\eta(x) = \frac{1}{2}$
Dans ce cas, $\ln\left(\frac{\eta(x)}{1-\eta(x)}\right) = \ln(1) = 0$. Le signe est 0, ce qui signifie que le classifieur $h_{f^*}^*(x)$ est indifférent (sa valeur est 0, ou peut être définie comme 1 ou -1 arbitrairement).

Comparons ces résultats avec le classifieur de Bayes optimal $h^*(x)$ dérivé dans la Partie 1 :
$h^*(x) = \begin{cases} 1 & \text{si } \eta(x) > \frac{1}{2} \\ -1 & \text{si } \eta(x) < \frac{1}{2} \\ 1 \text{ (ou -1)} & \text{si } \eta(x) = \frac{1}{2} \end{cases}$

Nous observons que pour tout $x$ où $\eta(x) \neq \frac{1}{2}$ (ce qui est équivalent à $P(Y=1|X=x) \neq P(Y=-1|X=x)$), le classifieur $h_{f^*}^*(x)$ est identique au classifieur de Bayes optimal $h^*(x)$.
Lorsque $\eta(x) = \frac{1}{2}$, les deux classifieurs sont indifférents, car les deux classes ont une probabilité égale, et la décision optimale est arbitraire.

Par conséquent, la perte exponentielle est calibrée, car la minimisation de son risque attendu conduit à un classifieur qui est équivalent au classifieur de Bayes optimal.
