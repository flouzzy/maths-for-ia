---
uuid: jalon-140
title: "Classifieur de Bayes optimal"
year: "Année 3"
trimester: "Trimestre 12"
tags: [Machine_Learning, Statistiques, Optimisation, theorie_apprentissage, Bayes, surrogate_loss, consistance, ERM]
prev: "Jalon 139 (Notion de stabilité algorithmique)"
next: "Jalon 141 (Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC.)"
---

## 1. L'Intuition Première

Imaginez que vous êtes un expert médical chargé de diagnostiquer une maladie rare. Vous recevez un ensemble d'informations (symptômes, résultats d'analyses) pour un nouveau patient. Votre objectif est de déterminer si le patient est atteint de la maladie ou non. Comment prendriez-vous la "meilleure" décision ?

Intuitivement, vous voudriez minimiser le risque de faire une erreur. Si, d'après les informations disponibles, la probabilité que le patient soit malade est de 70%, et la probabilité qu'il soit sain est de 30%, votre décision la plus raisonnable serait de le diagnostiquer comme malade. Inversement, si la probabilité d'être sain est de 95% et celle d'être malade de 5%, vous le classeriez comme sain. Cette règle simple, consistant à choisir la classe la plus probable étant donné les observations, est au cœur du **classifieur de Bayes optimal**.

Géométriquement, considérons deux catégories de points (par exemple, des cercles bleus et des triangles rouges) dans un espace bidimensionnel. Lorsque vous observez un nouveau point, vous voulez le classer dans la catégorie à laquelle il est le plus susceptible d'appartenir. Si vous pouvez estimer la "densité" de points bleus et rouges à chaque endroit de l'espace, la frontière optimale de décision serait l'endroit où un nouveau point a une probabilité égale d'appartenir à l'une ou l'autre classe. D'un côté de cette frontière, une classe est majoritaire ; de l'autre, c'est l'autre classe. Cette frontière représente le point d'équilibre où le risque d'erreur est minimal.

Le classifieur de Bayes optimal est la référence théorique, la "meilleure" performance possible en classification binaire ou multi-classes, sous l'hypothèse que l'on connaît parfaitement la distribution de probabilité sous-jacente des données. Il agit comme une borne inférieure de l'erreur atteignable. Cependant, en pratique, nous ne connaissons jamais cette distribution ; nous devons l'estimer à partir des données, ce qui nous mène aux concepts de **fonctions de perte de substitution** (surrogate losses) et à la **consistance de la minimisation du risque empirique**.

## 2. Formalisation & Rigueur Académique

Nous nous plaçons dans le cadre de la théorie de l'apprentissage statistique. Soit un problème de classification où nous cherchons à apprendre une fonction $h$ (un **classifieur**) à partir de données.

1.  **Espaces Fondamentaux :**
    *   Soit $\mathcal{X}$ l'**espace d'entrée** (ou espace des caractéristiques), par exemple $\mathbb{R}^d$ muni de sa tribu borélienne $\mathcal{B}(\mathbb{R}^d)$. Chaque $x \in \mathcal{X}$ est un vecteur de caractéristiques.
    *   Soit $\mathcal{Y}$ l'**espace de sortie** (ou espace des étiquettes de classe), qui est un ensemble fini et discret, par exemple $\mathcal{Y} = \{-1, 1\}$ pour la classification binaire, ou $\mathcal{Y} = \{1, 2, \dots, K\}$ pour la classification multi-classes. Nous munissons $\mathcal{Y}$ de la tribu discrète $\mathcal{P}(\mathcal{Y})$.

2.  **Distribution Jointe :**
    *   Nous supposons qu'il existe une **distribution de probabilité jointe inconnue** $P_{X,Y}$ sur l'espace produit $\mathcal{X} \times \mathcal{Y}$ (muni de la tribu produit $\mathcal{B}(\mathcal{X}) \otimes \mathcal{P}(\mathcal{Y})$).
    *   Un **échantillon de données** $S = \{(X_1, Y_1), \dots, (X_n, Y_n)\}$ est constitué de $n$ réalisations indépendantes et identiquement distribuées (i.i.d.) tirées selon $P_{X,Y}$.

3.  **Classifieur :**
    *   Un **classifieur** est une fonction mesurable $h: \mathcal{X} \to \mathcal{Y}$. Son rôle est d'assigner une étiquette de classe $\hat{y} = h(x)$ à une entrée $x \in \mathcal{X}$.

4.  **Fonction de Perte :**
    *   La **fonction de perte** (ou fonction coût) $L: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}^+$ mesure le coût d'une erreur de classification. $L(y, \hat{y})$ est le coût associé à la prédiction $\hat{y}$ lorsque la vraie étiquette est $y$.
    *   Pour la classification, la **perte 0-1** est la plus naturelle :
        $$L_{0-1}(y, \hat{y}) = \mathbb{I}(y \neq \hat{y})$$
        où $\mathbb{I}(\cdot)$ est la fonction indicatrice qui vaut 1 si l'argument est vrai et 0 sinon.

5.  **Risque Vrai (ou Risque Attendu) :**
    *   Le **risque vrai** (ou risque attendu) d'un classifieur $h$ est l'espérance de la perte sur des nouvelles données $(X, Y)$ tirées selon $P_{X,Y}$. Il est défini comme :
        $$R(h) = \mathbb{E}_{(X,Y) \sim P_{X,Y}}[L(Y, h(X))]$$
        Plus formellement, si $P_{X,Y}$ admet une densité de probabilité $p_{X,Y}(x,y)$ par rapport à une mesure de référence $\mu \otimes \nu$ sur $\mathcal{X} \times \mathcal{Y}$ (où $\mu$ est une mesure sur $\mathcal{X}$ et $\nu$ une mesure de comptage sur $\mathcal{Y}$), alors :
        $$R(h) = \sum_{y \in \mathcal{Y}} \int_{\mathcal{X}} L(y, h(x)) p_{X,Y}(x,y) \, d\mu(x)$$

6.  **Risque de Bayes et Classifieur de Bayes Optimal :**
    *   L'objectif ultime en classification est de trouver le classifieur $h^*$ qui minimise le risque vrai $R(h)$. Ce classifieur est appelé le **classifieur de Bayes optimal**.
    *   Le risque minimum associé à ce classifieur est appelé le **risque de Bayes** :
        $$R_{Bayes} = \inf_{h: \mathcal{X} \to \mathcal{Y}} R(h)$$
    *   Le classifieur de Bayes $h_{Bayes}$ est la fonction qui atteint ce minimum.

7.  **Fonctions de Perte de Substitution (Surrogate Losses) :**
    *   Le risque $R(h)$ avec la perte 0-1 est souvent difficile à minimiser directement car la fonction indicatrice n'est ni continue ni différentiable, et donc non convexe.
    *   Les **fonctions de perte de substitution** (surrogate losses) sont des fonctions $L_S: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}^+$ qui sont plus "agréables" mathématiquement (par exemple, convexes, différentiables) et que l'on minimise à la place de la perte 0-1.
    *   Exemples : perte logistique, perte charnière (hinge loss), perte quadratique.
    *   La question centrale est de savoir si la minimisation du risque avec une perte de substitution mène au même classifieur de Bayes optimal (ou à un classifieur dont le risque 0-1 est proche du risque de Bayes). Ceci est lié à la notion de **consistance** de la perte de substitution.

8.  **Consistance de la Minimisation du Risque Empirique (ERM) :**
    *   En pratique, la distribution $P_{X,Y}$ est inconnue. Nous ne pouvons pas calculer $R(h)$ directement.
    *   Nous utilisons un **risque empirique** $R_n(h)$ basé sur l'échantillon $S_n = \{(X_1, Y_1), \dots, (X_n, Y_n)\}$ :
        $$R_n(h) = \frac{1}{n} \sum_{i=1}^n L(Y_i, h(X_i))$$
    *   La **minimisation du risque empirique (ERM)** consiste à choisir un classifieur $h_n$ dans une classe d'hypothèses $\mathcal{H}$ qui minimise ce risque empirique :
        $$h_n = \arg\min_{h \in \mathcal{H}} R_n(h)$$
    *   La **consistance de l'ERM** est une propriété fondamentale qui garantit que le risque vrai du classifieur obtenu par ERM, $R(h_n)$, converge vers le risque de Bayes (ou le meilleur risque possible dans $\mathcal{H}$, $R_{\mathcal{H}} = \inf_{h \in \mathcal{H}} R(h)$) lorsque le nombre d'échantillons $n$ tend vers l'infini. C'est une condition nécessaire pour qu'un algorithme d'apprentissage soit fiable.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

Nous allons démontrer la forme explicite du classifieur de Bayes optimal pour la perte 0-1.

### 3.1. Dérivation du Classifieur de Bayes Optimal pour la Perte 0-1

Soit un espace de probabilité $(\Omega, \mathcal{F}, \mathbb{P})$. Nous considérons des variables aléatoires $X: \Omega \to \mathcal{X}$ et $Y: \Omega \to \mathcal{Y}$, où $\mathcal{X}$ est un espace mesurable et $\mathcal{Y}$ est un ensemble fini d'étiquettes de classe. La loi jointe de $(X, Y)$ est notée $P_{X,Y}$.

Le risque vrai d'un classifieur mesurable $h: \mathcal{X} \to \mathcal{Y}$ avec la perte 0-1, $L_{0-1}(y, \hat{y}) = \mathbb{I}(y \neq \hat{y})$, est donné par :
$$R(h) = \mathbb{E}_{(X,Y) \sim P_{X,Y}}[L_{0-1}(Y, h(X))] = \mathbb{E}[\mathbb{I}(Y \neq h(X))]$$

Pour minimiser $R(h)$, nous pouvons utiliser la loi de l'espérance totale. Soit $\mathbb{E}[Z]$ l'espérance d'une variable aléatoire $Z$. Nous avons $\mathbb{E}[Z] = \mathbb{E}_X[\mathbb{E}_Y[Z | X]]$. Appliquons ceci à $Z = \mathbb{I}(Y \neq h(X))$ :
$$R(h) = \mathbb{E}_X[\mathbb{E}_Y[\mathbb{I}(Y \neq h(X)) | X]]$$

Pour un $x \in \mathcal{X}$ donné (fixe), la fonction $h(X)$ devient une valeur fixe $h(x) \in \mathcal{Y}$. Nous devons donc minimiser, pour chaque $x \in \mathcal{X}$, l'expression suivante :
$$\mathbb{E}_Y[\mathbb{I}(Y \neq h(x)) | X=x]$$
Cette quantité représente la probabilité conditionnelle que le classifieur $h(x)$ fasse une erreur pour une entrée $x$ donnée. On peut la développer comme suit :
$$\mathbb{E}_Y[\mathbb{I}(Y \neq h(x)) | X=x] = \sum_{y' \in \mathcal{Y}} \mathbb{I}(y' \neq h(x)) P(Y=y' | X=x)$$
L'objectif est de choisir la valeur $h(x)$ qui minimise cette somme pour chaque $x$.
Soit $h_{Bayes}(x)$ le classifieur de Bayes optimal pour un $x$ donné. Il doit satisfaire :
$$h_{Bayes}(x) = \arg\min_{\hat{y} \in \mathcal{Y}} \left( \sum_{y' \in \mathcal{Y}} \mathbb{I}(y' \neq \hat{y}) P(Y=y' | X=x) \right)$$
Décomposons la somme :
$$\sum_{y' \in \mathcal{Y}} \mathbb{I}(y' \neq \hat{y}) P(Y=y' | X=x) = \sum_{y' \in \mathcal{Y}, y' \neq \hat{y}} P(Y=y' | X=x)$$
Cette somme représente la probabilité conditionnelle d'erreur si nous classons $x$ comme appartenant à la classe $\hat{y}$.
Nous savons que $\sum_{y' \in \mathcal{Y}} P(Y=y' | X=x) = 1$.
Donc, nous pouvons réécrire la somme comme :
$$\sum_{y' \in \mathcal{Y}, y' \neq \hat{y}} P(Y=y' | X=x) = \left( \sum_{y' \in \mathcal{Y}} P(Y=y' | X=x) \right) - P(Y=\hat{y} | X=x)$$
$$= 1 - P(Y=\hat{y} | X=x)$$
Pour minimiser $1 - P(Y=\hat{y} | X=x)$, nous devons maximiser $P(Y=\hat{y} | X=x)$.
Par conséquent, le classifieur de Bayes optimal $h_{Bayes}(x)$ est défini pour chaque $x \in \mathcal{X}$ par :
$$h_{Bayes}(x) = \arg\max_{\hat{y} \in \mathcal{Y}} P(Y=\hat{y} | X=x)$$
En cas d'égalité des probabilités maximales pour plusieurs classes, n'importe laquelle de ces classes peut être choisie arbitrairement.

Le **risque de Bayes** $R_{Bayes}$ est la valeur minimale du risque. Il est obtenu en substituant $h_{Bayes}(x)$ dans la formule du risque :
$$R_{Bayes} = R(h_{Bayes}) = \mathbb{E}_X\left[ \sum_{y' \in \mathcal{Y}, y' \neq h_{Bayes}(X)} P(Y=y' | X=X) \right]$$
$$R_{Bayes} = \mathbb{E}_X\left[ 1 - \max_{\hat{y} \in \mathcal{Y}} P(Y=\hat{y} | X=X) \right]$$

Ainsi, le classifieur de Bayes optimal choisit simplement la classe qui a la plus forte probabilité conditionnelle étant donné l'entrée $x$.

### 3.2. Introduction aux Fonctions de Perte de Substitution (Surrogate Losses)

Comme évoqué, la perte 0-1 est problématique pour l'optimisation numérique car elle est non-convexe et non-différentiable. Les **fonctions de perte de substitution** $L_S(\cdot, \cdot)$ sont introduites pour pallier ce problème. L'idée est de trouver une perte $L_S$ telle que la minimisation du risque $R_S(h) = \mathbb{E}[L_S(Y, h(X))]$ conduise à un classifieur $h$ qui minimise aussi (ou presque) le risque 0-1 $R(h)$.

Pour la classification binaire $\mathcal{Y} = \{-1, 1\}$, de nombreuses pertes de substitution sont conçues pour des modèles qui produisent une "score" de confiance $f(x) \in \mathbb{R}$, et le classifieur final est $h(x) = \mathrm{sgn}(f(x))$. Dans ce contexte, la perte de substitution est souvent définie comme $L_S(y, f(x))$, où $y$ est la vraie étiquette et $f(x)$ le score.

Quelques exemples de pertes de substitution pour la classification binaire :

1.  **Perte Charnière (Hinge Loss) :** Utilisée dans les machines à vecteurs de support (SVM).
    $$L_{Hinge}(y, f(x)) = \max(0, 1 - y \cdot f(x))$$
    Typage : $y \in \{-1, 1\}$, $f(x) \in \mathbb{R}$. La fonction $y \cdot f(x)$ est appelée la "marge". Minimiser cette perte encourage une marge positive pour les bonnes classifications.

2.  **Perte Logistique (Logistic Loss) :** Utilisée dans la régression logistique.
    $$L_{Logistique}(y, f(x)) = \log(1 + \exp(-y \cdot f(x)))$$
    Typage : $y \in \{-1, 1\}$, $f(x) \in \mathbb{R}$. Elle peut être interprétée comme le négatif du log-vraisemblance dans un modèle de régression logistique.

3.  **Perte Exponentielle (Exponential Loss) :** Utilisée dans les algorithmes de boosting (par exemple, AdaBoost).
    $$L_{Exp}(y, f(x)) = \exp(-y \cdot f(x))$$
    Typage : $y \in \{-1, 1\}$, $f(x) \in \mathbb{R}$.

Ces pertes sont toutes convexes et continues (parfois différentiables, comme la perte logistique, ou sous-différentiables, comme la perte charnière), ce qui les rend compatibles avec les méthodes d'optimisation basées sur le gradient.

Une perte de substitution $L_S$ est dite **consistante** (ou plus précisément, *class-consistent* ou *Fisher consistent*) si minimiser le risque $R_S(f) = \mathbb{E}[L_S(Y, f(X))]$ sur l'ensemble de toutes les fonctions mesurables $f: \mathcal{X} \to \mathbb{R}$ conduit à un classifieur $h(x) = \mathrm{sgn}(f(x))$ qui est équivalent au classifieur de Bayes optimal. C'est-à-dire, si $f_{S}^* = \arg\min_f R_S(f)$, alors $h_{S}^*(x) = \mathrm{sgn}(f_{S}^*(x))$ est égal (presque partout) à $h_{Bayes}(x)$.
Cette consistance assure que l'optimisation d'un objectif calculable nous rapproche de l'objectif idéal non calculable.

### 3.3. Consistance de la Minimisation du Risque Empirique (ERM)

Le principe de la **minimisation du risque empirique (ERM)** est un paradigme fondamental en apprentissage statistique. L'idée est que, si nous ne connaissons pas la vraie distribution $P_{X,Y}$, nous pouvons approximer le risque vrai $R(h)$ par le risque empirique $R_n(h)$ calculé sur un échantillon de données $S_n$.

Soit $\mathcal{H}$ une **classe d'hypothèses** (un ensemble de classifieurs possibles $h: \mathcal{X} \to \mathcal{Y}$). L'algorithme ERM cherche le meilleur classifieur dans $\mathcal{H}$ par rapport au risque empirique :
$$h_n = \arg\min_{h \in \mathcal{H}} R_n(h) = \arg\min_{h \in \mathcal{H}} \left( \frac{1}{n} \sum_{i=1}^n L(Y_i, h(X_i)) \right)$$

La **consistance de l'ERM** est la propriété selon laquelle, lorsque le nombre d'échantillons $n$ tend vers l'infini, le risque vrai du classifieur $h_n$ (produit par ERM) converge vers le risque minimum atteignable par un classifieur de la classe $\mathcal{H}$.
Formellement, l'ERM est dit consistant si :
$$\lim_{n \to \infty} R(h_n) = \inf_{h \in \mathcal{H}} R(h)$$
Si la classe d'hypothèses $\mathcal{H}$ est "riche" au point d'inclure le classifieur de Bayes optimal (ou de l'approcher arbitrairement bien), c'est-à-dire si $R_{Bayes} = \inf_{h \in \mathcal{H}} R(h)$, alors la consistance de l'ERM signifie que $R(h_n)$ converge vers le risque de Bayes.

Des conditions pour la consistance de l'ERM sont généralement formulées en termes de la complexité de la classe d'hypothèses $\mathcal{H}$ (par exemple, sa dimension de Vapnik-Chervonenkis ou VC dimension, sa complexité de Rademacher) et du comportement de la perte. Intuitivement, si $\mathcal{H}$ n'est pas trop complexe, alors $R_n(h)$ est une bonne approximation de $R(h)$ pour tout $h \in \mathcal{H}$, et la convergence de $R_n(h_n)$ vers $\inf_{h \in \mathcal{H}} R(h)$ implique la convergence de $R(h_n)$ vers $\inf_{h \in \mathcal{H}} R(h)$.

La relation entre le risque empirique et le risque vrai est donnée par le théorème fondamental de la théorie de l'apprentissage statistique :
Pour toute classe $\mathcal{H}$ et pour tout $\delta > 0$, il existe $N_0$ tel que pour tout $n \ge N_0$, avec une probabilité d'au moins $1-\delta$ :
$$|R_n(h) - R(h)| \le \epsilon_n(\mathcal{H}, \delta)$$
où $\epsilon_n(\mathcal{H}, \delta)$ est un terme d'erreur qui dépend de la complexité de $\mathcal{H}$ et de $n$, et qui tend vers 0 lorsque $n \to \infty$.
Ce résultat est crucial car il justifie l'utilisation de $R_n(h)$ comme substitut à $R(h)$. La consistance est alors une conséquence de la capacité de l'ERM à trouver une fonction qui généralise bien sur des données futures.

En résumé, pour implémenter un classifieur de manière pratique, nous:
1.  Choisisons une fonction de perte de substitution $L_S$ qui soit optimisable.
2.  Définissons une classe d'hypothèses $\mathcal{H}$ (par exemple, les réseaux de neurones d'une certaine taille, les fonctions linéaires, etc.).
3.  Utilisons l'ERM pour trouver $h_n = \arg\min_{h \in \mathcal{H}} \frac{1}{n} \sum_{i=1}^n L_S(Y_i, h(X_i))$.
La théorie de la consistance nous garantit que, sous certaines conditions, $R(h_n)$ se rapprochera du risque de Bayes au fur et à mesure que nous aurons plus de données.

## 4. Exercices d'Application & Pratique de Concours

Les exercices pour ce jalon, couvrant la dérivation du classifieur de Bayes optimal, l'analyse de différentes fonctions de perte de substitution et l'exploration de la consistance de l'ERM, sont disponibles dans le dossier `exos/`. Ils incluront des problèmes théoriques et des calculs pas-à-pas pour renforcer votre compréhension.

## 5. Ancrage & Application en Intelligence Artificielle

Les applications pratiques de ces concepts en intelligence artificielle sont omniprésentes :

*   **Reconnaissance d'Images et Traitement du Langage Naturel :** Les modèles modernes de classification (réseaux de neurones profonds, SVM) visent tous à approcher le classifieur de Bayes optimal en minimisant une perte de substitution (e.g., perte d'entropie croisée, une variante de la perte logistique) sur de vastes jeux de données.
*   **Systèmes de Recommandation :** La prédiction d'une préférence utilisateur pour un article (classification binaire ou multi-classes) est un problème de classification où l'on cherche la prédiction la plus probable.
*   **Diagnostic Médical :** Comme dans notre intuition de départ, classer un patient comme "malade" ou "sain" est une tâche directe de classification où le classifieur de Bayes représente la décision optimale si toutes les probabilités étaient connues.
*   **Détection de Fraude :** Identifier une transaction frauduleuse parmi d'autres est un problème de classification binaire, où la minimisation des faux positifs et faux négatifs est cruciale.
*   **Robotique :** La classification d'objets ou d'états de l'environnement pour la prise de décision d'un robot repose sur les mêmes principes.

Les travaux pratiques associés à ce jalon, explorant l'implémentation de classifieurs basés sur le principe de Bayes (naïf ou avec des estimations de densité), la comparaison de différentes fonctions de perte de substitution et l'observation de la consistance de l'ERM sur des données synthétiques ou réelles, sont disponibles dans le dossier `tp/`.

## 6. Liens Sémantiques & Maillage Obsidian

*   [[Jalon 139 (Notion de stabilité algorithmique)]]
*   [[Jalon 141 (Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC.)]]
*   [[Théorie de l'Apprentissage Statistique]]
*   [[Inférence Bayésienne]]
*   [[Fonctions de perte]]
*   [[Minimisation du Risque Empirique (ERM)]]
*   [[Divergence de Kullback-Leibler]]
*   [[Complexité de Rademacher]]
*   [[Dimension VC]]
*   [[Théorème de l'Apprentissage Fondamental]]