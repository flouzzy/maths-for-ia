---
uuid: "jalon-140"
title: "Classifieur de Bayes optimal, fonctions de perte de substitution (Surrogate losses) et consistance de la minimisation du risque empirique"
year: 3
trimester: 12
tags:
  - math/fondations
  - ia/theorie
prev: "[[Jalon-139_Notion_de_stabilite_algorithmique.md]]"
next: "[[Jalon-141.md]]"
---

# Jalon 140 : Classifieur de Bayes optimal, fonctions de perte de substitution (Surrogate losses) et consistance de la minimisation du risque empirique

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*
- **La Métaphore :** Imaginez que vous êtes un chef d'orchestre qui doit décider si une note jouée par un musicien est "juste" ou "fausse". Vous avez une oreille absolue, vous savez exactement comment chaque instrument *devrait* sonner. Si vous pouviez écouter la note parfaite et la comparer à celle jouée, votre décision serait infaillible. Ce "chef d'orchestre à l'oreille absolue" qui connaît la vérité ultime (la distribution de probabilité sous-jacente) et prend la meilleure décision possible, c'est le **Classifieur de Bayes optimal**. C'est notre idéal, notre référence absolue.

Maintenant, imaginez que vous n'avez pas l'oreille absolue, mais que vous avez des outils pour vous aider. Par exemple, un appareil qui mesure la fréquence de la note et vous donne un score. Cet appareil ne vous dit pas directement "juste" ou "faux", mais il vous donne une valeur numérique (par exemple, "très proche de la bonne fréquence", "un peu éloigné", "très éloigné"). Vous utilisez ce score pour prendre votre décision. Ces "scores intermédiaires" qui ne mesurent pas directement l'erreur finale (juste/faux) mais qui sont plus faciles à manipuler (par exemple, ils sont continus et dérivables), ce sont les **fonctions de perte de substitution (surrogate losses)**. Elles sont comme des proxys, des remplaçants de la "vraie" erreur, conçus pour être plus pratiques à optimiser.

Enfin, la **consistance de la minimisation du risque empirique**, c'est l'idée que si vous donnez de plus en plus de notes à votre chef d'orchestre (même s'il n'a pas l'oreille absolue et utilise des outils), et qu'il apprend de chaque note pour affiner sa décision, alors à la fin, avec suffisamment de pratique, il deviendra *presque aussi bon* que le chef d'orchestre à l'oreille absolue. C'est la promesse que nos algorithmes d'apprentissage, même s'ils ne connaissent pas la vérité absolue et travaillent avec des données limitées, peuvent converger vers la performance optimale si on leur donne suffisamment de données.

- **Le "Pourquoi on a inventé ça" :** Le problème fondamental en apprentissage automatique est de prendre la meilleure décision possible (par exemple, classer un email comme spam ou non-spam) à partir de données. La "meilleure décision" est celle qui minimise le nombre d'erreurs. Mais pour prendre la *vraiment* meilleure décision, il faudrait connaître toutes les probabilités sous-jacentes (par exemple, la probabilité qu'un email avec tel mot soit spam). Or, en pratique, on ne connaît jamais ces probabilités exactes ; on n'a que des échantillons (des emails déjà classés).
    *   Le Classifieur de Bayes optimal a été inventé pour définir la *limite théorique* de performance. C'est le Saint Graal, la meilleure performance qu'on puisse espérer atteindre, même si on ne peut jamais le calculer directement dans la vraie vie. Il nous donne un point de comparaison.
    *   Les fonctions de perte de substitution sont apparues parce que la "vraie" fonction de perte (compter simplement les erreurs, la perte 0-1) est très difficile à optimiser mathématiquement (elle n'est pas lisse, pas dérivable). Les mathématiciens et ingénieurs ont cherché des fonctions "similaires" mais plus "gentilles" (continues, dérivables, convexes) qui permettraient d'utiliser des outils d'optimisation puissants.
    *   La consistance de la minimisation du risque empirique est une question de confiance : est-ce que les méthodes que nous utilisons (qui apprennent à partir d'un nombre fini d'exemples) sont *garanties* de s'améliorer et de se rapprocher de l'optimum théorique à mesure que nous leur fournissons plus de données ? C'est crucial pour savoir si nos algorithmes ont une base théorique solide.

- **Visualisation :** Imaginez un graphique avec des points de deux couleurs différentes (par exemple, des cercles rouges et des carrés bleus) représentant deux classes. Ces points sont mélangés, mais il y a une tendance.
    *   Le **Classifieur de Bayes optimal** tracerait une frontière imaginaire qui sépare parfaitement les deux classes de manière à minimiser le nombre de points mal classés *si l'on connaissait la vraie distribution des points*. Cette frontière serait la "meilleure" possible, même si elle est parfois complexe et irrégulière.
    *   Les **fonctions de perte de substitution** permettraient de tracer une frontière. Par exemple, une fonction de perte de substitution pourrait encourager la frontière à être une ligne droite ou une courbe lisse, car c'est plus facile à calculer. Cette frontière pourrait être légèrement différente de la frontière de Bayes, mais elle serait plus simple à trouver.
    *   La **consistance** signifierait que si vous ajoutez de plus en plus de points à votre graphique, la frontière que votre algorithme trace (en utilisant une fonction de perte de substitution et en minimisant le risque empirique) se rapprocherait de plus en plus de la frontière idéale du Classifieur de Bayes optimal. Visuellement, la frontière apprise "convergerait" vers la frontière théoriquement parfaite.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles

Soient $\mathcal{X}$ l'espace des caractéristiques (features) et $\mathcal{Y}$ l'espace des étiquettes (labels). Dans le cadre de la classification binaire, nous avons généralement $\mathcal{Y} = \{-1, 1\}$ ou $\mathcal{Y} = \{0, 1\}$.
Nous considérons un couple de variables aléatoires $(X, Y)$ défini sur un espace de probabilité $(\Omega, \mathcal{A}, P)$, où $X$ prend ses valeurs dans $\mathcal{X}$ et $Y$ prend ses valeurs dans $\mathcal{Y}$. La distribution de probabilité conjointe de $(X, Y)$ est notée $P_{X,Y}$.

1.  **Fonction de perte (Loss Function) :**
    Une fonction de perte $\ell: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}_{\ge 0}$ quantifie le coût d'une erreur de prédiction. Pour la classification, la perte la plus naturelle est la **perte 0-1** (ou perte de misclassification) :
    $$ \ell_{0-1}(y', y) = \begin{cases} 0 & \text{si } y' = y \\ 1 & \text{si } y' \neq y \end{cases} $$
    où $y'$ est la prédiction et $y$ est la vraie étiquette.

2.  **Classifieur (Classifier) :**
    Un classifieur est une fonction mesurable $h: \mathcal{X} \to \mathcal{Y}$ qui assigne une étiquette à chaque point de l'espace des caractéristiques.

3.  **Risque Vrai (True Risk / Generalization Error) :**
    Le risque vrai d'un classifieur $h$ est l'espérance de la perte 0-1 sous la distribution $P_{X,Y}$ :
    $$ R(h) = \mathbb{E}[\ell_{0-1}(h(X), Y)] = P(h(X) \neq Y) $$
    Le risque vrai représente la probabilité qu'un classifieur $h$ fasse une erreur sur une nouvelle observation $(X, Y)$ tirée selon $P_{X,Y}$.

4.  **Risque Conditionnel (Conditional Risk) :**
    Le risque conditionnel d'un classifieur $h$ en un point $x \in \mathcal{X}$ est l'espérance de la perte 0-1 conditionnellement à $X=x$ :
    $$ R(h(x)|X=x) = \mathbb{E}[\ell_{0-1}(h(x), Y)|X=x] = P(h(x) \neq Y|X=x) $$
    Pour un classifieur $h(x) = y'$, ce risque conditionnel est $P(Y \neq y'|X=x)$.
    En utilisant la loi des probabilités totales, le risque vrai peut être exprimé comme :
    $$ R(h) = \mathbb{E}_X[R(h(X)|X)] = \int_{\mathcal{X}} P(h(x) \neq Y|X=x) dP_X(x) $$

5.  **Classifieur de Bayes Optimal ($h^*$) :**
    Le classifieur de Bayes optimal est le classifieur qui minimise le risque vrai $R(h)$ sur l'ensemble de tous les classifieurs mesurables. Son risque est appelé le **risque de Bayes** $R^* = R(h^*)$.

6.  **Fonction de Score (Score Function) :**
    Souvent, un classifieur est construit à partir d'une fonction de score $f: \mathcal{X} \to \mathbb{R}$. Pour la classification binaire, la décision est prise en comparant le score à un seuil (souvent 0) :
    $$ h_f(x) = \begin{cases} 1 & \text{si } f(x) \ge 0 \\ -1 & \text{si } f(x) < 0 \end{cases} $$
    ou $h_f(x) = \text{sign}(f(x))$ si $f(x) \neq 0$.

7.  **Fonction de Perte de Substitution (Surrogate Loss Function) :**
    Une fonction de perte de substitution $\ell_s: \mathcal{Y} \times \mathbb{R} \to \mathbb{R}_{\ge 0}$ est une fonction utilisée pour optimiser une fonction de score $f$. Elle prend en entrée la vraie étiquette $y \in \mathcal{Y}$ et la valeur de la fonction de score $f(x) \in \mathbb{R}$.
    Exemples courants pour $\mathcal{Y} = \{-1, 1\}$ :
    *   **Perte Logistique (Logistic Loss) :** $\ell_s(y, f(x)) = \log(1 + \exp(-y f(x)))$
    *   **Perte Charnière (Hinge Loss) :** $\ell_s(y, f(x)) = \max(0, 1 - y f(x))$
    *   **Perte Exponentielle (Exponential Loss) :** $\ell_s(y, f(x)) = \exp(-y f(x))$

8.  **Risque de Substitution (Surrogate Risk) :**
    Le risque de substitution d'une fonction de score $f$ est l'espérance de la perte de substitution sous la distribution $P_{X,Y}$ :
    $$ R_s(f) = \mathbb{E}[\ell_s(Y, f(X))] $$

9.  **Minimisation du Risque Empirique (Empirical Risk Minimization - ERM) :**
    Étant donné un ensemble d'apprentissage (training set) $D_n = \{(X_1, Y_1), \dots, (X_n, Y_n)\}$ de $n$ observations indépendantes et identiquement distribuées (i.i.d.) selon $P_{X,Y}$, le risque empirique d'un classifieur $h$ est la moyenne des pertes sur cet ensemble :
    $$ R_n(h) = \frac{1}{n} \sum_{i=1}^n \ell_{0-1}(h(X_i), Y_i) $$
    De même, le risque de substitution empirique d'une fonction de score $f$ est :
    $$ R_{s,n}(f) = \frac{1}{n} \sum_{i=1}^n \ell_s(Y_i, f(X_i)) $$
    L'approche ERM consiste à choisir un classifieur $h_n$ (ou une fonction de score $f_n$) à partir d'une classe d'hypothèses $\mathcal{H}$ (ou $\mathcal{F}$) en minimisant le risque empirique (ou le risque de substitution empirique) :
    $$ h_n = \arg\min_{h \in \mathcal{H}} R_n(h) \quad \text{ou} \quad f_n = \arg\min_{f \in \mathcal{F}} R_{s,n}(f) $$

10. **Consistance de l'ERM (Consistency of ERM) :**
    Un algorithme d'apprentissage est dit consistant si, lorsque le nombre d'échantillons $n$ tend vers l'infini, le risque vrai du classifieur appris $h_n$ converge vers le risque de Bayes $R^*$. Formellement, l'ERM est consistante si :
    $$ \lim_{n \to \infty} R(h_n) = R^* \quad \text{en probabilité ou presque sûrement.} $$
    Si l'on utilise une fonction de perte de substitution, on parle de consistance si $R(h_{f_n}) \to R^*$ où $h_{f_n}$ est le classifieur dérivé de $f_n$.

### B. Théorèmes, Propositions & Lemmes

> **Théorème 1 (Classifieur de Bayes Optimal) :**
> Soit $(X, Y)$ un couple de variables aléatoires avec $X \in \mathcal{X}$ et $Y \in \mathcal{Y} = \{-1, 1\}$. Le classifieur de Bayes optimal $h^*: \mathcal{X} \to \mathcal{Y}$ qui minimise le risque vrai $R(h) = \mathbb{E}[\ell_{0-1}(h(X), Y)]$ est donné par :
> $$ h^*(x) = \begin{cases} 1 & \text{si } P(Y=1|X=x) \ge P(Y=-1|X=x) \\ -1 & \text{si } P(Y=1|X=x) < P(Y=-1|X=x) \end{cases} $$
> Le risque de Bayes $R^*$ est alors :
> $$ R^* = \mathbb{E}_X[\min(P(Y=1|X), P(Y=-1|X))] $$

> **Théorème 2 (Consistance de Fisher / Classification Calibration) :**
> Soit $\ell_s: \mathcal{Y} \times \mathbb{R} \to \mathbb{R}_{\ge 0}$ une fonction de perte de substitution pour la classification binaire avec $\mathcal{Y} = \{-1, 1\}$. On dit que $\ell_s$ est **consistante de Fisher** (ou "classification calibrated") si, pour toute distribution $P_{X,Y}$, tout minimiseur $f^*$ du risque de substitution $R_s(f) = \mathbb{E}[\ell_s(Y, f(X))]$ a la propriété que le classifieur $h_{f^*}(x) = \text{sign}(f^*(x))$ est un classifieur de Bayes optimal.
> Plus formellement, $\ell_s$ est consistante de Fisher si pour toute fonction mesurable $\eta: \mathcal{X} \to [0, 1]$ où $\eta(x) = P(Y=1|X=x)$, et pour toute fonction $f: \mathcal{X} \to \mathbb{R}$, si $f^*$ minimise $\mathbb{E}_X[\mathbb{E}_Y[\ell_s(Y, f(X))|X]]$, alors $h_{f^*}(x) = \text{sign}(f^*(x))$ est égal à $h^*(x)$ presque partout par rapport à $P_X$.
>
> **Proposition (Exemple de Consistance de Fisher pour la perte logistique) :**
> La perte logistique $\ell_s(y, f(x)) = \log(1 + \exp(-y f(x)))$ est consistante de Fisher.
> Pour toute valeur $\eta \in [0, 1]$ (représentant $P(Y=1|X=x)$), la fonction $g_{\eta}(f_0) = \eta \log(1 + \exp(-f_0)) + (1-\eta) \log(1 + \exp(f_0))$ (qui est le risque conditionnel de substitution pour un $x$ donné) est minimisée lorsque $f_0 = \log\left(\frac{\eta}{1-\eta}\right)$.
> Le signe de ce $f_0$ est positif si $\eta > 1/2$ et négatif si $\eta < 1/2$. Or, $P(Y=1|X=x) > P(Y=-1|X=x)$ est équivalent à $\eta > 1/2$. Donc, le signe de $f_0$ correspond à la décision du classifieur de Bayes.

> **Théorème 3 (Consistance de la Minimisation du Risque Empirique pour une classe finie) :**
> Soit $\mathcal{H} = \{h_1, \dots, h_M\}$ une classe finie de $M$ classifieurs. Soit $D_n = \{(X_1, Y_1), \dots, (X_n, Y_n)\}$ un ensemble d'apprentissage de $n$ échantillons i.i.d.
> Soit $h_n = \arg\min_{h \in \mathcal{H}} R_n(h)$ le classifieur obtenu par ERM, et $h^*_{\mathcal{H}} = \arg\min_{h \in \mathcal{H}} R(h)$ le meilleur classifieur dans $\mathcal{H}$.
> Alors, pour tout $\epsilon > 0$,
> $$ P(R(h_n) - R(h^*_{\mathcal{H}}) > \epsilon) \to 0 \quad \text{quand } n \to \infty $$
> C'est-à-dire que l'ERM est consistante pour une classe d'hypothèses finie.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Classifieur de Bayes Optimal
1.  **Initialisation / Cadre :**
    Nous cherchons à trouver le classifieur $h^*: \mathcal{X} \to \mathcal{Y}$ qui minimise le risque vrai $R(h) = \mathbb{E}[\ell_{0-1}(h(X), Y)]$.
    Nous pouvons réécrire le risque vrai en utilisant la loi de l'espérance totale :
    $$ R(h) = \mathbb{E}_X[\mathbb{E}_Y[\ell_{0-1}(h(X), Y)|X]] $$
    Pour minimiser $R(h)$, il suffit de minimiser l'expression interne $\mathbb{E}_Y[\ell_{0-1}(h(x), Y)|X=x]$ pour chaque $x \in \mathcal{X}$ indépendamment. Soit $h(x)$ une valeur fixe $y' \in \mathcal{Y}$. Nous devons minimiser $P(Y \neq y'|X=x)$.

2.  **Étape 1 : Minimisation du risque conditionnel pour un $x$ donné**
    Pour un $x$ fixé, nous devons choisir $y' \in \mathcal{Y}$ pour minimiser $P(Y \neq y'|X=x)$.
    L'espace des étiquettes est $\mathcal{Y} = \{-1, 1\}$.
    Si nous choisissons $y' = 1$, le risque conditionnel est :
    $$ P(Y \neq 1|X=x) = P(Y=-1|X=x) $$
    Si nous choisissons $y' = -1$, le risque conditionnel est :
    $$ P(Y \neq -1|X=x) = P(Y=1|X=x) $$
    Pour minimiser le risque conditionnel, nous devons choisir $y'$ tel que $P(Y \neq y'|X=x)$ soit le plus petit possible.

3.  **Étape 2 (Transition micro-calculatoire) : Comparaison des probabilités conditionnelles**
    Nous comparons les deux valeurs possibles du risque conditionnel :
    *   Si $P(Y=-1|X=x) < P(Y=1|X=x)$, alors le choix $y' = -1$ donne un risque plus grand que le choix $y' = 1$. Donc, nous choisissons $y' = 1$.
    *   Si $P(Y=-1|X=x) > P(Y=1|X=x)$, alors le choix $y' = 1$ donne un risque plus grand que le choix $y' = -1$. Donc, nous choisissons $y' = -1$.
    *   Si $P(Y=-1|X=x) = P(Y=1|X=x)$, alors les deux choix donnent le même risque. Nous pouvons choisir arbitrairement l'une des deux étiquettes, par convention nous choisissons souvent $1$.

    Nous pouvons reformuler ces conditions en termes de $P(Y=1|X=x)$ et $P(Y=-1|X=x)$.
    Nous savons que $P(Y=1|X=x) + P(Y=-1|X=x) = 1$.
    Donc, $P(Y=-1|X=x) = 1 - P(Y=1|X=x)$.
    La condition $P(Y=1|X=x) \ge P(Y=-1|X=x)$ devient :
    $$ P(Y=1|X=x) \ge 1 - P(Y=1|X=x) $$
    $$ 2 P(Y=1|X=x) \ge 1 $$
    $$ P(Y=1|X=x) \ge \frac{1}{2} $$
    Dans ce cas, nous choisissons $h^*(x) = 1$.

    La condition $P(Y=1|X=x) < P(Y=-1|X=x)$ devient :
    $$ P(Y=1|X=x) < 1 - P(Y=1|X=x) $$
    $$ 2 P(Y=1|X=x) < 1 $$
    $$ P(Y=1|X=x) < \frac{1}{2} $$
    Dans ce cas, nous choisissons $h^*(x) = -1$.

    Ainsi, le classifieur de Bayes optimal est défini par :
    $$ h^*(x) = \begin{cases} 1 & \text{si } P(Y=1|X=x) \ge P(Y=-1|X=x) \\ -1 & \text{si } P(Y=1|X=x) < P(Y=-1|X=x) \end{cases} $$
    Ce qui est équivalent à :
    $$ h^*(x) = \begin{cases} 1 & \text{si } P(Y=1|X=x) \ge \frac{1}{2} \\ -1 & \text{si } P(Y=1|X=x) < \frac{1}{2} \end{cases} $$

4.  **Conclusion :**
    Le classifieur de Bayes optimal $h^*(x)$ est celui qui, pour chaque point $x$, assigne l'étiquette $y$ qui a la plus forte probabilité conditionnelle $P(Y=y|X=x)$.
    Le risque de Bayes $R^*$ est alors obtenu en substituant $h^*(x)$ dans la formule du risque vrai :
    $$ R^* = \mathbb{E}_X[P(h^*(X) \neq Y|X)] $$
    Pour chaque $x$, $P(h^*(x) \neq Y|X=x)$ est la probabilité de l'étiquette minoritaire.
    $$ P(h^*(x) \neq Y|X=x) = \min(P(Y=1|X=x), P(Y=-1|X=x)) $$
    Donc,
    $$ R^* = \mathbb{E}_X[\min(P(Y=1|X), P(Y=-1|X))] $$
    La démonstration est complète.

### Démonstration du Théorème Pivot : Consistance de Fisher pour la perte logistique
1.  **Initialisation / Cadre :**
    Nous voulons montrer que la perte logistique $\ell_s(y, f(x)) = \log(1 + \exp(-y f(x)))$ est consistante de Fisher. Cela signifie que si $f^*$ minimise le risque de substitution $R_s(f) = \mathbb{E}[\ell_s(Y, f(X))]$, alors le classifieur $h_{f^*}(x) = \text{sign}(f^*(x))$ est équivalent au classifieur de Bayes optimal $h^*(x)$ presque partout.
    Comme pour le risque 0-1, nous pouvons minimiser le risque de substitution $R_s(f)$ en minimisant le risque de substitution conditionnel pour chaque $x$ indépendamment.
    Soit $\eta(x) = P(Y=1|X=x)$ la probabilité conditionnelle de la classe positive. Alors $P(Y=-1|X=x) = 1 - \eta(x)$.
    Pour un $x$ fixé, nous cherchons à minimiser la fonction $g_{\eta(x)}(f_0)$ par rapport à $f_0 \in \mathbb{R}$, où $f_0$ est la valeur de $f(x)$ pour ce $x$.
    $$ g_{\eta(x)}(f_0) = \mathbb{E}[\ell_s(Y, f_0)|X=x] $$
    $$ g_{\eta(x)}(f_0) = P(Y=1|X=x) \ell_s(1, f_0) + P(Y=-1|X=x) \ell_s(-1, f_0) $$
    $$ g_{\eta(x)}(f_0) = \eta(x) \log(1 + \exp(-f_0)) + (1-\eta(x)) \log(1 + \exp(f_0)) $$
    Pour simplifier la notation, nous écrirons $\eta$ au lieu de $\eta(x)$ et $f_0$ au lieu de $f(x)$.

2.  **Étape 1 : Calcul de la dérivée première**
    Pour trouver le minimum de $g_{\eta}(f_0)$, nous calculons sa dérivée par rapport à $f_0$ et l'égalons à zéro.
    $$ \frac{d}{df_0} \log(1 + \exp(-f_0)) = \frac{-\exp(-f_0)}{1 + \exp(-f_0)} = \frac{-1}{\exp(f_0) + 1} $$
    $$ \frac{d}{df_0} \log(1 + \exp(f_0)) = \frac{\exp(f_0)}{1 + \exp(f_0)} $$
    Donc,
    $$ \frac{d g_{\eta}(f_0)}{df_0} = \eta \left( \frac{-1}{\exp(f_0) + 1} \right) + (1-\eta) \left( \frac{\exp(f_0)}{1 + \exp(f_0)} \right) $$
    $$ \frac{d g_{\eta}(f_0)}{df_0} = \frac{-\eta + (1-\eta)\exp(f_0)}{1 + \exp(f_0)} $$

3.  **Étape 2 (Transition micro-calculatoire) : Recherche du point critique**
    Nous égalons la dérivée à zéro pour trouver les points critiques :
    $$ \frac{-\eta + (1-\eta)\exp(f_0)}{1 + \exp(f_0)} = 0 $$
    Puisque $1 + \exp(f_0) > 0$, le numérateur doit être nul :
    $$ -\eta + (1-\eta)\exp(f_0) = 0 $$
    $$ (1-\eta)\exp(f_0) = \eta $$
    Si $\eta = 1$, alors $0 = 1$, ce qui est impossible. Cela signifie que si $P(Y=1|X=x)=1$, la fonction $g_{1}(f_0) = \log(1 + \exp(-f_0))$ est minimisée lorsque $f_0 \to \infty$.
    Si $\eta = 0$, alors $\exp(f_0) = 0$, ce qui est impossible. Cela signifie que si $P(Y=-1|X=x)=1$, la fonction $g_{0}(f_0) = \log(1 + \exp(f_0))$ est minimisée lorsque $f_0 \to -\infty$.
    Pour $0 < \eta < 1$ :
    $$ \exp(f_0) = \frac{\eta}{1-\eta} $$
    En prenant le logarithme naturel des deux côtés :
    $$ f_0^* = \log\left(\frac{\eta}{1-\eta}\right) $$
    Cette fonction $f_0^*$ est le log-odds ratio, ou logit de $\eta$.

4.  **Étape 3 : Vérification que c'est un minimum et lien avec Bayes**
    Pour vérifier que c'est un minimum, nous pouvons calculer la dérivée seconde :
    $$ \frac{d^2 g_{\eta}(f_0)}{df_0^2} = \frac{d}{df_0} \left( \frac{-\eta + (1-\eta)\exp(f_0)}{1 + \exp(f_0)} \right) $$
    En utilisant la règle du quotient $(u/v)' = (u'v - uv')/v^2$:
    $u = -\eta + (1-\eta)\exp(f_0) \implies u' = (1-\eta)\exp(f_0)$
    $v = 1 + \exp(f_0) \implies v' = \exp(f_0)$
    $$ \frac{d^2 g_{\eta}(f_0)}{df_0^2} = \frac{(1-\eta)\exp(f_0)(1 + \exp(f_0)) - (-\eta + (1-\eta)\exp(f_0))\exp(f_0)}{(1 + \exp(f_0))^2} $$
    Au point critique, le numérateur $(-\eta + (1-\eta)\exp(f_0))$ est nul. Donc, la dérivée seconde au point critique $f_0^*$ est :
    $$ \frac{d^2 g_{\eta}(f_0^*)}{df_0^2} = \frac{(1-\eta)\exp(f_0^*)(1 + \exp(f_0^*))}{(1 + \exp(f_0^*))^2} = \frac{(1-\eta)\exp(f_0^*)}{1 + \exp(f_0^*)} $$
    Puisque $0 < \eta < 1$, $(1-\eta) > 0$. Aussi, $\exp(f_0^*) > 0$ et $1 + \exp(f_0^*) > 0$. Donc, la dérivée seconde est strictement positive, ce qui confirme que $f_0^*$ est bien un minimum global.

    Maintenant, nous devons vérifier si le signe de $f_0^*$ correspond à la décision de Bayes.
    Le classifieur de Bayes optimal $h^*(x)$ choisit $1$ si $P(Y=1|X=x) \ge P(Y=-1|X=x)$, ce qui est équivalent à $\eta \ge 1/2$. Il choisit $-1$ si $\eta < 1/2$.
    Considérons le signe de $f_0^* = \log\left(\frac{\eta}{1-\eta}\right)$ :
    *   Si $\eta > 1/2$, alors $\frac{\eta}{1-\eta} > 1$. Donc $\log\left(\frac{\eta}{1-\eta}\right) > 0$. Le signe de $f_0^*$ est positif.
    *   Si $\eta < 1/2$, alors $\frac{\eta}{1-\eta} < 1$. Donc $\log\left(\frac{\eta}{1-\eta}\right) < 0$. Le signe de $f_0^*$ est négatif.
    *   Si $\eta = 1/2$, alors $\frac{\eta}{1-\eta} = 1$. Donc $\log\left(\frac{\eta}{1-\eta}\right) = 0$. Le signe de $f_0^*$ est nul.

    Dans tous les cas, le signe de $f_0^*$ correspond exactement à la décision du classifieur de Bayes optimal $h^*(x)$.
    Pour les cas limites $\eta=1$ et $\eta=0$:
    *   Si $\eta=1$, $P(Y=1|X=x)=1$. Le classifieur de Bayes est $h^*(x)=1$. Le minimiseur de $g_1(f_0)$ est $f_0 \to \infty$, dont le signe est positif.
    *   Si $\eta=0$, $P(Y=-1|X=x)=1$. Le classifieur de Bayes est $h^*(x)=-1$. Le minimiseur de $g_0(f_0)$ est $f_0 \to -\infty$, dont le signe est négatif.
    Ainsi, la correspondance est maintenue pour tous les $\eta \in [0,1]$.

5.  **Conclusion :**
    Nous avons montré que pour chaque $x$, la valeur $f_0^*$ qui minimise le risque de substitution conditionnel pour la perte logistique est $f_0^* = \log\left(\frac{P(Y=1|X=x)}{P(Y=-1|X=x)}\right)$. Le signe de cette valeur $f_0^*$ est positif si $P(Y=1|X=x) > P(Y=-1|X=x)$, négatif si $P(Y=1|X=x) < P(Y=-1|X=x)$, et nul si $P(Y=1|X=x) = P(Y=-1|X=x)$. Cette règle de décision est précisément celle du classifieur de Bayes optimal. Par conséquent, la perte logistique est consistante de Fisher. La démonstration est complète.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe
**Énoncé :**
Considérons un problème de classification binaire où $\mathcal{Y} = \{-1, 1\}$. La variable $X$ est unidimensionnelle, $X \in \mathbb{R}$. Les probabilités conditionnelles sont données par :
$P(Y=1|X=x) = \frac{1}{1 + \exp(-x)}$
$P(Y=-1|X=x) = 1 - P(Y=1|X=x)$
1.  Déterminez le classifieur de Bayes optimal $h^*(x)$.
2.  Calculez le risque de Bayes $R^*$ si $X$ suit une distribution uniforme sur l'intervalle $[-2, 2]$.

**Correction Détaillée :**
*   *Analyse de l'énoncé :* Nous devons appliquer la règle du classifieur de Bayes optimal, qui consiste à choisir l'étiquette avec la plus grande probabilité conditionnelle. Pour le calcul du risque de Bayes, nous devrons intégrer la probabilité d'erreur minimale sur l'intervalle donné pour $X$.

*   *Résolution pas-à-pas :*
    1.  **Détermination du classifieur de Bayes optimal $h^*(x)$ :**
        Le classifieur de Bayes optimal $h^*(x)$ est défini par :
        $$ h^*(x) = \begin{cases} 1 & \text{si } P(Y=1|X=x) \ge P(Y=-1|X=x) \\ -1 & \text{si } P(Y=1|X=x) < P(Y=-1|X=x) \end{cases} $$
        Nous savons que $P(Y=1|X=x) \ge P(Y=-1|X=x)$ est équivalent à $P(Y=1|X=x) \ge \frac{1}{2}$.
        Substituons l'expression donnée pour $P(Y=1|X=x)$ :
        $$ \frac{1}{1 + \exp(-x)} \ge \frac{1}{2} $$
        Puisque $1 + \exp(-x)$ est toujours positif, nous pouvons inverser les termes et l'inégalité :
        $$ 1 + \exp(-x) \le 2 $$
        $$ \exp(-x) \le 1 $$
        En prenant le logarithme naturel des deux côtés (la fonction $\ln$ est croissante) :
        $$ -x \le \ln(1) $$
        $$ -x \le 0 $$
        $$ x \ge 0 $$
        Donc, le classifieur de Bayes optimal est :
        $$ h^*(x) = \begin{cases} 1 & \text{si } x \ge 0 \\ -1 & \text{si } x < 0 \end{cases} $$

    2.  **Calcul du risque de Bayes $R^*$ :**
        Le risque de Bayes est donné par :
        $$ R^* = \mathbb{E}_X[\min(P(Y=1|X), P(Y=-1|X))] $$
        Pour $x \ge 0$, nous avons $P(Y=1|X=x) \ge P(Y=-1|X=x)$, donc $\min(P(Y=1|X=x), P(Y=-1|X=x)) = P(Y=-1|X=x)$.
        $$ P(Y=-1|X=x) = 1 - P(Y=1|X=x) = 1 - \frac{1}{1 + \exp(-x)} = \frac{1 + \exp(-x) - 1}{1 + \exp(-x)} = \frac{\exp(-x)}{1 + \exp(-x)} $$
        Pour $x < 0$, nous avons $P(Y=1|X=x) < P(Y=-1|X=x)$, donc $\min(P(Y=1|X=x), P(Y=-1|X=x)) = P(Y=1|X=x)$.
        $$ P(Y=1|X=x) = \frac{1}{1 + \exp(-x)} $$
        Nous remarquons que $\frac{\exp(-x)}{1 + \exp(-x)} = \frac{1}{\exp(x) + 1}$.
        Et $\frac{1}{1 + \exp(-x)} = \frac{\exp(x)}{\exp(x) + 1}$.
        Pour $x \ge 0$, $\exp(x) \ge 1$, donc $\frac{1}{\exp(x) + 1} \le \frac{1}{2}$.
        Pour $x < 0$, $\exp(x) < 1$, donc $\frac{\exp(x)}{\exp(x) + 1} < \frac{1}{2}$.
        En fait, la fonction $\min(P(Y=1|X=x), P(Y=-1|X=x))$ peut être écrite de manière compacte.
        Si $x \ge 0$, $\min(\frac{\exp(x)}{\exp(x)+1}, \frac{1}{\exp(x)+1}) = \frac{1}{\exp(x)+1}$.
        Si $x < 0$, $\min(\frac{\exp(x)}{\exp(x)+1}, \frac{1}{\exp(x)+1}) = \frac{\exp(x)}{\exp(x)+1}$.
        On peut aussi écrire $\min(P(Y=1|X=x), P(Y=-1|X=x)) = \frac{1}{1+\exp(|x|)}$.
        Vérifions :
        Si $x \ge 0$, $|x|=x$, donc $\frac{1}{1+\exp(x)}$. C'est bien $P(Y=-1|X=x)$.
        Si $x < 0$, $|x|=-x$, donc $\frac{1}{1+\exp(-x)}$. C'est bien $P(Y=1|X=x)$.
        La densité de probabilité de $X$ est $p_X(x) = \frac{1}{2 - (-2)} = \frac{1}{4}$ pour $x \in [-2, 2]$ et $0$ ailleurs.
        $$ R^* = \int_{-2}^{2} \min(P(Y=1|X=x), P(Y=-1|X=x)) p_X(x) dx $$
        $$ R^* = \int_{-2}^{2} \frac{1}{1 + \exp(|x|)} \frac{1}{4} dx $$
        $$ R^* = \frac{1}{4} \left( \int_{-2}^{0} \frac{1}{1 + \exp(-x)} dx + \int_{0}^{2} \frac{1}{1 + \exp(x)} dx \right) $$
        Effectuons un changement de variable dans la première intégrale : $u = -x$, $du = -dx$. Quand $x=-2, u=2$. Quand $x=0, u=0$.
        $$ \int_{-2}^{0} \frac{1}{1 + \exp(-x)} dx = \int_{2}^{0} \frac{1}{1 + \exp(u)} (-du) = \int_{0}^{2} \frac{1}{1 + \exp(u)} du $$
        Donc,
        $$ R^* = \frac{1}{4} \left( \int_{0}^{2} \frac{1}{1 + \exp(x)} dx + \int_{0}^{2} \frac{1}{1 + \exp(x)} dx \right) $$
        $$ R^* = \frac{1}{4} \left( 2 \int_{0}^{2} \frac{1}{1 + \exp(x)} dx \right) = \frac{1}{2} \int_{0}^{2} \frac{1}{1 + \exp(x)} dx $$
        Pour calculer l'intégrale :
        $$ \int \frac{1}{1 + \exp(x)} dx = \int \frac{1 + \exp(x) - \exp(x)}{1 + \exp(x)} dx = \int \left( 1 - \frac{\exp(x)}{1 + \exp(x)} \right) dx $$
        $$ = x - \ln(1 + \exp(x)) + C $$
        Appliquons les bornes :
        $$ \int_{0}^{2} \frac{1}{1 + \exp(x)} dx = \left[ x - \ln(1 + \exp(x)) \right]_{0}^{2} $$
        $$ = (2 - \ln(1 + \exp(2))) - (0 - \ln(1 + \exp(0))) $$
        $$ = 2 - \ln(1 + \exp(2)) - (-\ln(1 + 1)) $$
        $$ = 2 - \ln(1 + \exp(2)) + \ln(2) $$
        $$ = 2 + \ln\left(\frac{2}{1 + \exp(2)}\right) $$
        Finalement, le risque de Bayes $R^*$ est :
        $$ R^* = \frac{1}{2} \left( 2 + \ln\left(\frac{2}{1 + \exp(2)}\right) \right) $$
        $$ R^* = 1 + \frac{1}{2} \ln\left(\frac{2}{1 + \exp(2)}\right) $$
        $$ R^* = 1 + \ln\left(\sqrt{\frac{2}{1 + \exp(2)}}\right) $$
        Numériquement, $\exp(2) \approx 7.389$.
        $R^* \approx 1 + \frac{1}{2} \ln\left(\frac{2}{1 + 7.389}\right) = 1 + \frac{1}{2} \ln\left(\frac{2}{8.389}\right) \approx 1 + \frac{1}{2} \ln(0.238) \approx 1 + \frac{1}{2}(-1.435) \approx 1 - 0.7175 = 0.2825$.

### Exercice 2 : Niveau Avancé (Inspiré Concours X / ENS / MIT)
**Énoncé :**
Considérons la perte exponentielle (Exponential Loss) pour la classification binaire avec $\mathcal{Y} = \{-1, 1\}$, définie par $\ell_s(y, f(x)) = \exp(-y f(x))$.
1.  Montrez que la perte exponentielle est consistante de Fisher. C'est-à-dire, montrez que le minimiseur $f_0^*$ du risque de substitution conditionnel $g_{\eta}(f_0) = \eta \exp(-f_0) + (1-\eta) \exp(f_0)$ a un signe qui correspond à la décision du classifieur de Bayes optimal, où $\eta = P(Y=1|X=x)$.
2.  Comparez la sensibilité de la perte exponentielle et de la perte logistique aux erreurs de classification lorsque $|f_0|$ est grand.

**Correction Détaillée :**
*   *Analyse de l'énoncé :* La première partie demande de reproduire la démonstration de consistance de Fisher pour une nouvelle fonction de perte. La deuxième partie requiert une analyse comparative des comportements asymptotiques des fonctions de perte.

*   *Résolution pas-à-pas :*
    1.  **Consistance de Fisher de la perte exponentielle :**
        Pour un $x$ fixé, nous cherchons à minimiser $g_{\eta}(f_0)$ par rapport à $f_0 \in \mathbb{R}$, où $\eta = P(Y=1|X=x)$.
        $$ g_{\eta}(f_0) = \eta \exp(-f_0) + (1-\eta) \exp(f_0) $$
        Calculons la dérivée première par rapport à $f_0$ :
        $$ \frac{d g_{\eta}(f_0)}{df_0} = \eta (-\exp(-f_0)) + (1-\eta) (\exp(f_0)) $$
        $$ \frac{d g_{\eta}(f_0)}{df_0} = -\eta \exp(-f_0) + (1-\eta) \exp(f_0) $$
        Égalons la dérivée à zéro pour trouver le point critique $f_0^*$ :
        $$ -\eta \exp(-f_0^*) + (1-\eta) \exp(f_0^*) = 0 $$
        $$ (1-\eta) \exp(f_0^*) = \eta \exp(-f_0^*) $$
        Multiplions les deux côtés par $\exp(f_0^*)$ :
        $$ (1-\eta) \exp(f_0^*) \exp(f_0^*) = \eta \exp(-f_0^*) \exp(f_0^*) $$
        $$ (1-\eta) \exp(2f_0^*) = \eta $$
        Si $\eta = 1$, alors $0 = 1$, impossible. Cela signifie que si $P(Y=1|X=x)=1$, $g_1(f_0) = \exp(-f_0)$ est minimisée lorsque $f_0 \to \infty$.
        Si $\eta = 0$, alors $\exp(2f_0^*) = 0$, impossible. Cela signifie que si $P(Y=-1|X=x)=1$, $g_0(f_0) = \exp(f_0)$ est minimisée lorsque $f_0 \to -\infty$.
        Pour $0 < \eta < 1$ :
        $$ \exp(2f_0^*) = \frac{\eta}{1-\eta} $$
        Prenons le logarithme naturel des deux côtés :
        $$ 2f_0^* = \ln\left(\frac{\eta}{1-\eta}\right) $$
        $$ f_0^* = \frac{1}{2} \ln\left(\frac{\eta}{1-\eta}\right) $$
        Calculons la dérivée seconde pour confirmer que c'est un minimum :
        $$ \frac{d^2 g_{\eta}(f_0)}{df_0^2} = \frac{d}{df_0} (-\eta \exp(-f_0) + (1-\eta) \exp(f_0)) $$
        $$ = -\eta (-\exp(-f_0)) + (1-\eta) (\exp(f_0)) $$
        $$ = \eta \exp(-f_0) + (1-\eta) \exp(f_0) $$
        Puisque $\eta \in [0,1]$, $\exp(-f_0) > 0$ et $\exp(f_0) > 0$, la dérivée seconde est toujours positive (sauf si $\eta=0$ et $f_0 \to -\infty$ ou $\eta=1$ et $f_0 \to \infty$, où elle tend vers 0). Cela confirme que $f_0^*$ est un minimum global.

        Maintenant, vérifions le signe de $f_0^*$ par rapport à la règle de Bayes :
        *   Si $\eta > 1/2$, alors $\frac{\eta}{1-\eta} > 1$. Donc $\ln\left(\frac{\eta}{1-\eta}\right) > 0$. Par conséquent, $f_0^* > 0$.
        *   Si $\eta < 1/2$, alors $\frac{\eta}{1-\eta} < 1$. Donc $\ln\left(\frac{\eta}{1-\eta}\right) < 0$. Par conséquent, $f_0^* < 0$.
        *   Si $\eta = 1/2$, alors $\frac{\eta}{1-\eta} = 1$. Donc $\ln\left(\frac{\eta}{1-\eta}\right) = 0$. Par conséquent, $f_0^* = 0$.
        Les cas limites $\eta=1$ et $\eta=0$ donnent $f_0^* \to \infty$ et $f_0^* \to -\infty$ respectivement, ce qui correspond aux décisions de Bayes.
        Le signe de $f_0^*$ correspond donc exactement à la décision du classifieur de Bayes optimal. La perte exponentielle est consistante de Fisher.

    2.  **Comparaison de la sensibilité aux erreurs lorsque $|f_0|$ est grand :**
        Nous comparons la perte logistique $\ell_{log}(y, f_0) = \log(1 + \exp(-y f_0))$ et la perte exponentielle $\ell_{exp}(y, f_0) = \exp(-y f_0)$.
        Considérons le cas où la prédiction est correcte, c'est-à-dire $y f_0 > 0$.
        *   Si $y f_0 \to \infty$ (prédiction correcte avec une grande confiance) :
            $\ell_{log}(y, f_0) = \log(1 + \exp(-y f_0)) \approx \log(1) = 0$.
            $\ell_{exp}(y, f_0) = \exp(-y f_0) \to 0$.
            Les deux pertes tendent vers zéro, ce qui est souhaitable.

        Considérons le cas où la prédiction est incorrecte, c'est-à-dire $y f_0 < 0$.
        *   Si $y f_0 \to -\infty$ (prédiction incorrecte avec une grande confiance) :
            Pour la perte logistique :
            $\ell_{log}(y, f_0) = \log(1 + \exp(-y f_0))$. Puisque $-y f_0 \to \infty$,
            $\ell_{log}(y, f_0) \approx \log(\exp(-y f_0)) = -y f_0$.
            La perte logistique croît linéairement avec l'ampleur de l'erreur.
            Pour la perte exponentielle :
            $\ell_{exp}(y, f_0) = \exp(-y f_0)$. Puisque $-y f_0 \to \infty$,
            $\ell_{exp}(y, f_0)$ croît exponentiellement avec l'ampleur de l'erreur.

        **Conclusion de la comparaison :**
        La perte exponentielle est beaucoup plus sensible aux erreurs de classification avec une grande confiance (c'est-à-dire lorsque $y f_0$ est un grand nombre négatif) que la perte logistique. Elle pénalise les erreurs "graves" de manière exponentielle, tandis que la perte logistique les pénalise de manière linéaire.
        Cette propriété rend la perte exponentielle (utilisée par exemple dans AdaBoost) très sensible aux points aberrants (outliers) ou aux données mal étiquetées, car elle leur attribue un poids très élevé. La perte logistique est plus robuste dans ce scénario.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Le classifieur de Bayes optimal est la pierre angulaire théorique de toute la classification en apprentissage automatique. Il représente la performance maximale atteignable par n'importe quel algorithme de classification pour une distribution de données donnée. En pratique, nous ne connaissons jamais la vraie distribution $P_{X,Y}$, donc nous ne pouvons pas construire $h^*$ directement. Cependant, il nous fournit une borne inférieure pour le risque de n'importe quel classifieur, ce qui est essentiel pour évaluer la performance de nos modèles. Si un modèle atteint un risque proche du risque de Bayes, nous savons qu'il est très performant.

Les fonctions de perte de substitution sont le pont entre la théorie de Bayes et la pratique de l'optimisation. La perte 0-1, bien que intuitivement correcte, est discontinue et non-différentiable, ce qui la rend impossible à optimiser directement avec des méthodes de descente de gradient, qui sont le moteur de la plupart des algorithmes d'apprentissage automatique modernes (réseaux de neurones, SVM, régression logistique, etc.). Les pertes de substitution (comme la perte logistique, la perte charnière, la perte exponentielle) sont choisies parce qu'elles sont des approximations convexes et/ou différentiables de la perte 0-1. La propriété de **consistance de Fisher** est cruciale : elle garantit que minimiser le risque de substitution (qui est optimisable) conduit à un classifieur dont la règle de décision est la même que celle du classifieur de Bayes optimal (qui est la meilleure possible). C'est la justification théorique de l'utilisation de ces pertes "indirectes".

Enfin, la **consistance de la minimisation du risque empirique (ERM)** est la garantie fondamentale que nos algorithmes d'apprentissage peuvent réellement apprendre. L'ERM est le principe sous-jacent à presque tous les algorithmes d'apprentissage supervisé : nous minimisons une erreur (empirique) sur les données d'entraînement dans l'espoir que cela réduira l'erreur (vraie) sur les nouvelles données. La consistance nous assure que, sous certaines conditions (par exemple, une classe d'hypothèses pas trop complexe et un nombre suffisant de données), cette stratégie fonctionne et que le classifieur appris se rapproche de l'optimum théorique. Sans cette garantie, l'apprentissage à partir de données serait une démarche sans fondement mathématique solide.

- **Exemple Concret :**
    *   **Régression Logistique :** C'est un exemple parfait d'utilisation d'une fonction de perte de substitution consistante de Fisher. La régression logistique modélise $P(Y=1|X=x)$ directement via la fonction sigmoïde : $P(Y=1|X=x) = \sigma(w^T x + b) = \frac{1}{1 + \exp(-(w^T x + b))}$. Elle optimise les paramètres $w$ et $b$ en minimisant la **perte logistique** (qui est la négation de la log-vraisemblance) sur les données d'entraînement. Comme nous l'avons démontré, la perte logistique est consistante de Fisher. Cela signifie que le classifieur résultant $h(x) = \text{sign}(w^T x + b)$ est une approximation du classifieur de Bayes optimal *dans la classe des modèles linéaires*. Si la vraie frontière de Bayes est linéaire, la régression logistique peut la retrouver.

    *   **Machines à Vecteurs de Support (SVM) :** Les SVM utilisent la **perte charnière (hinge loss)**, $\ell_s(y, f(x)) = \max(0, 1 - y f(x))$. Cette perte est également consistante de Fisher. Elle pénalise les points mal classés et les points correctement classés mais avec une faible marge. L'optimisation de la perte charnière (souvent avec une régularisation L2) permet aux SVM de trouver une frontière de décision qui maximise la marge entre les classes, ce qui est une heuristique puissante pour se rapprocher du classifieur de Bayes optimal, surtout lorsque les classes sont bien séparées.

    *   **Réseaux de Neurones pour la Classification :** Pour la classification binaire ou multi-classes, les réseaux de neurones utilisent généralement la **perte d'entropie croisée (cross-entropy loss)**, qui est une généralisation de la perte logistique. Cette perte est également consistante de Fisher. La minimisation de cette perte via la descente de gradient (et ses variantes) sur un grand ensemble de données permet aux réseaux de neurones d'apprendre des fonctions de score $f(x)$ très complexes, dont le signe (ou la classe prédite) se rapproche de la décision de Bayes optimal pour des problèmes non-linéaires.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 139 (Notion de stabilité algorithmique)]], [[Jalon 105 (Espérance conditionnelle et théorème de Radon-Nikodym)]], [[Jalon 110 (Théorie de la mesure et intégration de Lebesgue)]], [[Jalon 120 (Convergence des variables aléatoires (presque sûre, en probabilité, en loi, en moyenne L^p))]]
- **Concepts Futurs dépendants :** [[Jalon-141]], [[Jalon 142 (Bornes d'erreur de généralisation (Hoeffding, McDiarmid, Rademacher, VC-dimension))]], [[Jalon 145 (Algorithmes de boosting (AdaBoost, Gradient Boosting))]], [[Jalon 150 (Régression Logistique et SVM : fondements théoriques)]]
