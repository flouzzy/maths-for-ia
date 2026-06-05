---
uuid: jalon-140-exo-05
title: "Exercice 5 - Classifieur de Bayes"
type: Exercice
difficulty: 3
---

### Énoncé

Soit un problème de classification binaire où nous observons des paires $(X, Y)$ de variables aléatoires, avec $X$ prenant ses valeurs dans un espace mesurable $(\mathcal{X}, \mathcal{A})$ et $Y$ prenant ses valeurs dans $\mathcal{Y} = \{-1, 1\}$. Le couple $(X, Y)$ est régi par une distribution de probabilité $P$ sur l'espace mesurable produit $(\mathcal{X} \times \mathcal{Y}, \mathcal{A} \otimes \mathcal{B}(\mathcal{Y}))$.

La fonction de perte 0-1 est définie par $L_{01}(y, \hat{y}) = \mathbf{1}_{y \neq \hat{y}}$, où $\hat{y} \in \mathcal{Y}$ est la prédiction d'un classifieur. Le risque de Bayes associé à cette perte est $R_{01}^* = \min_{f: \mathcal{X} \to \mathcal{Y}} \mathbb{E}[L_{01}(Y, f(X))]$. Le classifieur de Bayes optimal, noté $f_{01}^*$, est donné par $f_{01}^*(x) = \text{sgn}(P(Y=1|X=x) - P(Y=-1|X=x))$. On note $\eta(x) = P(Y=1|X=x)$ la probabilité a posteriori.

Dans le cadre des fonctions de perte de substitution (surrogate loss functions), on considère la perte logistique (logistic loss) définie pour une étiquette $y \in \{-1, 1\}$ et un score $v \in \mathbb{R}$ par $\phi(y, v) = \log(1 + e^{-yv})$.

**Questions :**

1.  Démontrer formellement que la perte logistique est **Fisher consistante** par rapport à la perte 0-1 pour la classification binaire. C'est-à-dire, montrer que le minimiseur du risque conditionnel de la perte logistique, $v^*(x) = \arg\min_{v \in \mathbb{R}} \mathbb{E}[\phi(Y, v)|X=x]$, conduit à un classifieur $f^*(x) = \text{sgn}(v^*(x))$ qui est égal au classifieur de Bayes optimal $f_{01}^*(x)$ (à des points de mesure nulle près si $P(Y=1|X=x)=1/2$).
2.  Interpréter le résultat $v^*(x)$ en termes de **calibration** du modèle.

---

### Correction

#### Question 1 : Démonstration de la consistance de Fisher de la perte logistique

Soient $(\mathcal{X}, \mathcal{A})$ un espace mesurable pour les caractéristiques $X$, et $\mathcal{Y} = \{-1, 1\}$ pour les étiquettes $Y$.
Soit $P$ la mesure de probabilité sur $(\mathcal{X} \times \mathcal{Y}, \mathcal{A} \otimes \mathcal{P}(\mathcal{Y}))$ qui régit la distribution du couple $(X, Y)$.
On note $\eta(x) = P(Y=1|X=x)$ la probabilité a posteriori conditionnelle.
Le classifieur de Bayes optimal pour la perte 0-1 est donné par $f_{01}^*(x) = \text{sgn}(2\eta(x)-1)$, où par convention $\text{sgn}(0)$ peut être arbitrairement défini comme $1$ ou $-1$.

La perte logistique est définie par $\phi(y, v) = \log(1 + e^{-yv})$ pour $y \in \{-1, 1\}$ et $v \in \mathbb{R}$.

Nous cherchons à trouver $v^*(x) = \arg\min_{v \in \mathbb{R}} \mathbb{E}[\phi(Y, v)|X=x]$.
Le risque conditionnel de la perte logistique pour un $x$ fixe est :
$$ R_{\phi}(v|x) = \mathbb{E}[\phi(Y, v)|X=x] $$
En utilisant la définition de l'espérance conditionnelle pour une variable aléatoire discrète $Y$:
$$ R_{\phi}(v|x) = P(Y=1|X=x) \phi(1, v) + P(Y=-1|X=x) \phi(-1, v) $$
En substituant $\eta(x)$ et la définition de $\phi$:
$$ R_{\phi}(v|x) = \eta(x) \log(1 + e^{-1 \cdot v}) + (1 - \eta(x)) \log(1 + e^{-(-1) \cdot v}) $$
$$ R_{\phi}(v|x) = \eta(x) \log(1 + e^{-v}) + (1 - \eta(x)) \log(1 + e^{v}) $$

Pour trouver le minimiseur $v^*(x)$, nous devons calculer la dérivée de $R_{\phi}(v|x)$ par rapport à $v$ et l'égaler à zéro.
La fonction $\log(1+e^{-v})$ a pour dérivée :
$$ \frac{d}{dv} \log(1+e^{-v}) = \frac{1}{1+e^{-v}} \cdot (-e^{-v}) = \frac{-e^{-v}}{1+e^{-v}} = \frac{-1}{e^v+1} $$
La fonction $\log(1+e^{v})$ a pour dérivée :
$$ \frac{d}{dv} \log(1+e^{v}) = \frac{1}{1+e^{v}} \cdot (e^{v}) = \frac{e^{v}}{1+e^{v}} $$

Maintenant, calculons la dérivée de $R_{\phi}(v|x)$ par rapport à $v$:
$$ \frac{\partial}{\partial v} R_{\phi}(v|x) = \eta(x) \left( \frac{-1}{e^v+1} \right) + (1 - \eta(x)) \left( \frac{e^{v}}{e^{v}+1} \right) $$
Pour trouver le minimiseur, nous fixons cette dérivée à zéro :
$$ \frac{-\eta(x)}{e^v+1} + \frac{(1 - \eta(x))e^{v}}{e^{v}+1} = 0 $$
Puisque $e^v+1 > 0$ pour tout $v \in \mathbb{R}$, nous pouvons multiplier par $e^v+1$:
$$ -\eta(x) + (1 - \eta(x))e^{v} = 0 $$
$$ (1 - \eta(x))e^{v} = \eta(x) $$

Deux cas se présentent :
1.  Si $\eta(x) = 1$, alors $0 \cdot e^v = 1$, ce qui est impossible. Cependant, si $\eta(x)=1$, alors $P(Y=-1|X=x)=0$, et le risque conditionnel est $\log(1+e^{-v})$. Sa dérivée est $\frac{-1}{e^v+1}$ qui ne peut être nulle. Dans ce cas, $v \to \infty$ minimise la perte logistique, car $\log(1+e^{-v}) \to \log(1) = 0$ quand $v \to \infty$. Si $v^*(x) = \infty$, alors $\text{sgn}(v^*(x))=1$. Le classifieur de Bayes optimal est $f_{01}^*(x) = \text{sgn}(2(1)-1) = \text{sgn}(1) = 1$. Il y a consistance.
2.  Si $\eta(x) = 0$, alors $1 \cdot e^v = 0$, ce qui est impossible. Cependant, si $\eta(x)=0$, alors $P(Y=1|X=x)=0$, et le risque conditionnel est $\log(1+e^v)$. Sa dérivée est $\frac{e^v}{e^v+1}$ qui ne peut être nulle. Dans ce cas, $v \to -\infty$ minimise la perte logistique, car $\log(1+e^{v}) \to \log(1) = 0$ quand $v \to -\infty$. Si $v^*(x) = -\infty$, alors $\text{sgn}(v^*(x))=-1$. Le classifieur de Bayes optimal est $f_{01}^*(x) = \text{sgn}(2(0)-1) = \text{sgn}(-1) = -1$. Il y a consistance.

3.  Si $0 < \eta(x) < 1$:
    $$ e^{v^*(x)} = \frac{\eta(x)}{1 - \eta(x)} $$
    En prenant le logarithme naturel des deux côtés :
    $$ v^*(x) = \log\left(\frac{\eta(x)}{1 - \eta(x)}\right) $$
    Pour vérifier que c'est bien un minimum, on peut calculer la seconde dérivée :
    $$ \frac{\partial^2}{\partial v^2} R_{\phi}(v|x) = \frac{\partial}{\partial v} \left( \frac{-\eta(x) + (1 - \eta(x))e^{v}}{e^{v}+1} \right) $$
    $$ = \frac{(1-\eta(x))e^v(e^v+1) - ( (1-\eta(x))e^v - \eta(x) )e^v}{(e^v+1)^2} $$
    $$ = \frac{e^v}{(e^v+1)^2} [ (1-\eta(x))(e^v+1) - ((1-\eta(x))e^v - \eta(x)) ] $$
    $$ = \frac{e^v}{(e^v+1)^2} [ (1-\eta(x))e^v + (1-\eta(x)) - (1-\eta(x))e^v + \eta(x) ] $$
    $$ = \frac{e^v}{(e^v+1)^2} [ 1-\eta(x) + \eta(x) ] = \frac{e^v}{(e^v+1)^2} $$
    Puisque $\frac{e^v}{(e^v+1)^2} > 0$ pour tout $v \in \mathbb{R}$, le point critique est bien un minimum.

Maintenant, nous devons vérifier si $\text{sgn}(v^*(x))$ est égal à $f_{01}^*(x)$.
$$ \text{sgn}(v^*(x)) = \text{sgn}\left(\log\left(\frac{\eta(x)}{1 - \eta(x)}\right)\right) $$
Le signe d'une valeur $u$ est positif si $u > 0$, négatif si $u < 0$, et nul si $u=0$.
1.  Si $\frac{\eta(x)}{1 - \eta(x)} > 1$:
    Ceci implique $\eta(x) > 1 - \eta(x)$, ce qui signifie $2\eta(x) > 1$, ou $\eta(x) > 1/2$.
    Dans ce cas, $\log\left(\frac{\eta(x)}{1 - \eta(x)}\right) > 0$, donc $\text{sgn}(v^*(x)) = 1$.
    Le classifieur de Bayes optimal est $f_{01}^*(x) = \text{sgn}(2\eta(x)-1) = \text{sgn}(>0) = 1$.
2.  Si $\frac{\eta(x)}{1 - \eta(x)} < 1$:
    Ceci implique $\eta(x) < 1 - \eta(x)$, ce qui signifie $2\eta(x) < 1$, ou $\eta(x) < 1/2$.
    Dans ce cas, $\log\left(\frac{\eta(x)}{1 - \eta(x)}\right) < 0$, donc $\text{sgn}(v^*(x)) = -1$.
    Le classifieur de Bayes optimal est $f_{01}^*(x) = \text{sgn}(2\eta(x)-1) = \text{sgn}(<0) = -1$.
3.  Si $\frac{\eta(x)}{1 - \eta(x)} = 1$:
    Ceci implique $\eta(x) = 1 - \eta(x)$, ce qui signifie $2\eta(x) = 1$, ou $\eta(x) = 1/2$.
    Dans ce cas, $\log\left(\frac{\eta(x)}{1 - \eta(x)}\right) = \log(1) = 0$, donc $v^*(x) = 0$.
    Le classifieur de Bayes optimal est $f_{01}^*(x) = \text{sgn}(2\eta(x)-1) = \text{sgn}(0)$. Dans ce cas, la perte 0-1 est la même quelle que soit la classe prédite.

En résumé, si l'on ignore le cas $\eta(x)=1/2$ (qui est un ensemble de mesure nulle pour les distributions continues, ou un cas d'égalité où la prédiction n'affecte pas le risque de Bayes), nous avons montré que $\text{sgn}(v^*(x)) = f_{01}^*(x)$.
Par conséquent, la perte logistique est Fisher consistante.

#### Question 2 : Interprétation en termes de calibration

Le résultat $v^*(x) = \log\left(\frac{\eta(x)}{1 - \eta(x)}\right)$ est extrêmement significatif. C'est le **log-odds** de la probabilité conditionnelle $\eta(x) = P(Y=1|X=x)$.

On peut résoudre cette équation pour $\eta(x)$:
$$ e^{v^*(x)} = \frac{\eta(x)}{1 - \eta(x)} $$
$$ (1 - \eta(x))e^{v^*(x)} = \eta(x) $$
$$ e^{v^*(x)} - \eta(x)e^{v^*(x)} = \eta(x) $$
$$ e^{v^*(x)} = \eta(x) (1 + e^{v^*(x)}) $$
$$ \eta(x) = \frac{e^{v^*(x)}}{1 + e^{v^*(x)}} $$
Cette expression est précisément la fonction sigmoïde logistique standard, souvent notée $\sigma(v^*(x))$.

Cela signifie que le minimiseur $v^*(x)$ du risque conditionnel de la perte logistique n'est pas seulement un score dont le signe donne le classifieur optimal, mais il est une transformation directe de la probabilité a posteriori $\eta(x)$. Plus précisément, $v^*(x)$ modélise le log-odds de la probabilité de la classe positive.

Un modèle est dit **calibré** si ses sorties de probabilité correspondent aux probabilités réelles des événements. Pour un classifieur qui sort un score $g(x) \in \mathbb{R}$, on dit que le modèle est bien calibré si $P(Y=1|g(X)=v) = \sigma(v)$ pour tout $v \in \mathbb{R}$ dans le support de $g(X)$.
Le fait que $v^*(x)$ soit précisément le log-odds de $\eta(x)$ indique que si un modèle est capable de minimiser parfaitement la perte logistique conditionnelle, alors ses sorties (les $v^*(x)$) sont directement interprétables comme les log-odds des probabilités conditionnelles vraies. En appliquant la fonction sigmoïde à $v^*(x)$, on obtient une estimation directe de $P(Y=1|X=x)$.

Par conséquent, la perte logistique encourage non seulement la consistance de Fisher pour la classification (c'est-à-dire, trouver le bon classifieur), mais elle promeut également la **calibration** des scores de sortie, en les forçant à s'aligner sur les log-odds des probabilités a posteriori. C'est une propriété plus forte que la simple consistance de Fisher et est très utile lorsque l'on souhaite des estimations de probabilités fiables en plus des classifications.