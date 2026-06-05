---
uuid: jalon-140-exo-08
title: "Exercice 8 - Classifieur de Bayes"
type: Exercice
difficulty: 4
---

### Énoncé

Soit un problème de classification binaire où l'espace des entrées est $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$ et l'espace des étiquettes est $\mathcal{Y} = \{-1, 1\}$. Nous considérons une variable aléatoire $(X, Y)$ définie sur un espace de probabilité $(\Omega, \mathcal{A}, P)$, avec $X$ prenant ses valeurs dans $\mathcal{X}$ et $Y$ dans $\mathcal{Y}$. La distribution conjointe de $(X, Y)$ est notée $P_{XY}$.
Pour chaque $x \in \mathcal{X}$, nous définissons la probabilité conditionnelle $\eta(x) = P(Y=1|X=x)$.

Le risque de classification classique est défini par la perte $0-1$, $L_{01}(y', y) = \mathbb{I}(y' \neq y)$, où $\mathbb{I}(\cdot)$ est la fonction indicatrice. Pour un classifieur $h: \mathcal{X} \to \mathcal{Y}$, le risque est $R(h) = \mathbb{E}_{X,Y}[L_{01}(h(X), Y)]$.

Nous introduisons une fonction de score $f: \mathcal{X} \to \mathbb{R}$ et une fonction de perte de substitution (surrogate loss) $\phi: \mathbb{R} \to \mathbb{R}_+$. La fonction de perte de substitution que nous étudierons est la **perte charnière (Hinge Loss)**, définie par $\phi(z) = \max(0, 1-z)$. Le risque associé à une fonction de score $f$ et une perte $\phi$ est $R_{\phi}(f) = \mathbb{E}_{X,Y}[\phi(Y f(X))]$.

**Question 1 : Classifieur de Bayes Optimal et Risque de Bayes**

1.  Définir formellement le classifieur de Bayes optimal $h^*: \mathcal{X} \to \mathcal{Y}$ qui minimise le risque $R(h)$ pour la perte $0-1$. Justifier rigoureusement votre définition.
2.  Exprimer le risque de Bayes $R(h^*)$ en fonction de $\eta(X)$.

**Question 2 : Minimisation de la Perte Charnière Conditionnelle**

1.  Pour un $x \in \mathcal{X}$ fixé, définir le risque conditionnel de la perte charnière pour une valeur de score $f' \in \mathbb{R}$, soit $R_{\phi}(f'|X=x) = \mathbb{E}_{Y|X=x}[\phi(Y f')]$.
2.  Déterminer les valeurs $f_x^*$ qui minimisent $R_{\phi}(f'|X=x)$. Les solutions doivent être exprimées en fonction de $\eta(x)$.

**Question 3 : Consistance de Fisher de la Perte Charnière**

1.  Définir la consistance de Fisher pour une perte de substitution $\phi$ par rapport à la perte $0-1$. Pour la classification, nous utiliserons la fonction de signe classifiant $\text{sgn}_{\text{cls}}: \mathbb{R} \to \{-1, 1\}$ définie par $\text{sgn}_{\text{cls}}(z) = 1$ si $z \ge 0$ et $\text{sgn}_{\text{cls}}(z) = -1$ si $z < 0$.
2.  Démontrer que la perte charnière est Fisher consistante.

---

### Correction

Soit $(\Omega, \mathcal{A}, P)$ un espace de probabilité. Soient $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$ et $(\mathcal{Y}, \mathcal{B}_{\mathcal{Y}})$ des espaces mesurables, où $\mathcal{Y} = \{-1, 1\}$ et $\mathcal{B}_{\mathcal{Y}} = \mathcal{P}(\mathcal{Y})$.
Soit $(X, Y): \Omega \to \mathcal{X} \times \mathcal{Y}$ une variable aléatoire bivariée dont la loi est $P_{XY}$.
La densité conditionnelle de $Y$ sachant $X=x$ est $P(Y=y|X=x)$. Pour simplifier, nous notons $\eta(x) = P(Y=1|X=x)$. Par conséquent, $P(Y=-1|X=x) = 1 - \eta(x)$.

**Question 1 : Classifieur de Bayes Optimal et Risque de Bayes**

1.  Pour un classifieur $h: \mathcal{X} \to \mathcal{Y}$, le risque $R(h)$ est donné par :
    $$ R(h) = \mathbb{E}_{X,Y}[L_{01}(h(X), Y)] = \mathbb{E}_{X,Y}[\mathbb{I}(h(X) \neq Y)] $$
    En utilisant la loi de l'espérance totale (ou le théorème de Fubini), nous pouvons écrire :
    $$ R(h) = \mathbb{E}_{X}[\mathbb{E}_{Y|X}[\mathbb{I}(h(X) \neq Y)]] $$
    Pour minimiser $R(h)$, il suffit de minimiser l'espérance conditionnelle $\mathbb{E}_{Y|X}[\mathbb{I}(h(X) \neq Y)]$ pour chaque $x \in \mathcal{X}$ séparément. Soit $\hat{y} = h(x)$ la prédiction pour un $x$ donné. L'espérance conditionnelle est alors :
    $$ R(h(x)|X=x) = \mathbb{E}_{Y|X=x}[\mathbb{I}(\hat{y} \neq Y)] $$
    Nous avons deux cas possibles pour $\hat{y}$:
    *   Si $\hat{y} = 1$: Le coût est $P(Y=-1|X=x) = 1 - \eta(x)$.
    *   Si $\hat{y} = -1$: Le coût est $P(Y=1|X=x) = \eta(x)$.

    Le classifieur optimal $h^*(x)$ choisit $\hat{y}$ pour minimiser ce coût conditionnel :
    *   Si $1 - \eta(x) < \eta(x) \implies 1 < 2\eta(x) \implies \eta(x) > 1/2$, alors $h^*(x) = 1$.
    *   Si $\eta(x) < 1 - \eta(x) \implies 2\eta(x) < 1 \implies \eta(x) < 1/2$, alors $h^*(x) = -1$.
    *   Si $\eta(x) = 1/2$, alors $1 - \eta(x) = \eta(x) = 1/2$. Dans ce cas, les deux choix ($1$ ou $-1$) donnent le même coût minimal. Par convention pour la classification binaire, on peut choisir $h^*(x) = 1$.

    Ainsi, le classifieur de Bayes optimal est défini comme :
    $$ h^*(x) = \begin{cases} 1 & \text{si } \eta(x) \ge 1/2 \\ -1 & \text{si } \eta(x) < 1/2 \end{cases} $$

2.  Le risque de Bayes $R(h^*)$ est l'espérance du risque conditionnel minimal :
    $$ R(h^*) = \mathbb{E}_{X}[\min(P(Y=1|X), P(Y=-1|X))] $$
    $$ R(h^*) = \mathbb{E}_{X}[\min(\eta(X), 1 - \eta(X))] $$
    Ce risque représente l'erreur minimale possible pour ce problème de classification.

**Question 2 : Minimisation de la Perte Charnière Conditionnelle**

1.  Pour un $x \in \mathcal{X}$ fixé et une valeur de score $f' \in \mathbb{R}$, le risque conditionnel de la perte charnière est :
    $$ R_{\phi}(f'|X=x) = \mathbb{E}_{Y|X=x}[\phi(Y f')] = \mathbb{E}_{Y|X=x}[\max(0, 1 - Y f')] $$
    En utilisant la définition de $\eta(x)$, nous avons :
    $$ R_{\phi}(f'|X=x) = P(Y=1|X=x) \max(0, 1 - (1)f') + P(Y=-1|X=x) \max(0, 1 - (-1)f') $$
    $$ R_{\phi}(f'|X=x) = \eta(x) \max(0, 1 - f') + (1 - \eta(x)) \max(0, 1 + f') $$

2.  Nous cherchons $f_x^* = \text{argmin}_{f' \in \mathbb{R}} R_{\phi}(f'|X=x)$. Soit $g(f') = \eta(x) \max(0, 1 - f') + (1 - \eta(x)) \max(0, 1 + f')$.
    La fonction $g(f')$ est convexe, car elle est une somme de fonctions convexes composées avec des fonctions affines. Nous pouvons trouver son minimum en analysant sa dérivée (ou ses sous-gradients) par morceaux.
    Les points de non-dérivabilité sont $f' = -1$ et $f' = 1$.

    *   **Cas 1 : $f' < -1$**
        Alors $1 - f' > 0$ et $1 + f' < 0$.
        $g(f') = \eta(x) (1 - f') + (1 - \eta(x)) \cdot 0 = \eta(x) (1 - f')$
        $g'(f') = -\eta(x)$

    *   **Cas 2 : $-1 \le f' \le 1$**
        Alors $1 - f' \ge 0$ et $1 + f' \ge 0$.
        $g(f') = \eta(x) (1 - f') + (1 - \eta(x)) (1 + f')$
        $g(f') = \eta(x) - \eta(x)f' + 1 - \eta(x) + (1 - \eta(x))f'$
        $g(f') = 1 + (1 - 2\eta(x))f'$
        $g'(f') = 1 - 2\eta(x)$

    *   **Cas 3 : $f' > 1$**
        Alors $1 - f' < 0$ et $1 + f' > 0$.
        $g(f') = \eta(x) \cdot 0 + (1 - \eta(x)) (1 + f') = (1 - \eta(x)) (1 + f')$
        $g'(f') = 1 - \eta(x)$

    Maintenant, analysons les signes des dérivées en fonction de $\eta(x)$ :

    *   **Sous-cas A : $\eta(x) > 1/2$**
        $1 - 2\eta(x) < 0$.
        $g'(f')$ est $-\eta(x) < 0$ pour $f' < -1$.
        $g'(f')$ est $1 - 2\eta(x) < 0$ pour $-1 < f' < 1$.
        $g'(f')$ est $1 - \eta(x) > 0$ pour $f' > 1$.
        La dérivée est négative, puis négative, puis devient positive à $f'=1$. Donc le minimum est atteint en $f_x^* = 1$.

    *   **Sous-cas B : $\eta(x) < 1/2$**
        $1 - 2\eta(x) > 0$.
        $g'(f')$ est $-\eta(x) < 0$ pour $f' < -1$.
        $g'(f')$ est $1 - 2\eta(x) > 0$ pour $-1 < f' < 1$.
        $g'(f')$ est $1 - \eta(x) > 0$ pour $f' > 1$.
        La dérivée est négative, puis devient positive à $f'=-1$. Donc le minimum est atteint en $f_x^* = -1$.

    *   **Sous-cas C : $\eta(x) = 1/2$**
        $1 - 2\eta(x) = 0$.
        $g'(f')$ est $-\eta(x) = -1/2 < 0$ pour $f' < -1$.
        $g'(f')$ est $1 - 2\eta(x) = 0$ pour $-1 < f' < 1$.
        $g'(f')$ est $1 - \eta(x) = 1/2 > 0$ pour $f' > 1$.
        La fonction $g(f')$ décroît pour $f' < -1$, est constante sur l'intervalle $[-1, 1]$, puis croît pour $f' > 1$.
        Le minimum est donc atteint pour tout $f' \in [-1, 1]$. On a $f_x^* \in [-1, 1]$.

    En résumé, les minimiseurs $f_x^*$ de la perte charnière conditionnelle sont :
    $$ f_x^* = \begin{cases} 1 & \text{si } \eta(x) > 1/2 \\ -1 & \text{si } \eta(x) < 1/2 \\ \text{tout } f' \in [-1, 1] & \text{si } \eta(x) = 1/2 \end{cases} $$

**Question 3 : Consistance de Fisher de la Perte Charnière**

1.  **Définition de la consistance de Fisher :**
    Une perte de substitution $\phi$ est dite Fisher consistante par rapport à la perte $0-1$ si, pour tout espace de probabilité $(\Omega, \mathcal{A}, P)$ et toute distribution $P_{XY}$ sur $\mathcal{X} \times \mathcal{Y}$, pour tout $x \in \mathcal{X}$, tout minimiseur $f_x^*$ du risque conditionnel $R_{\phi}(f'|X=x)$ donne une classification qui est Bayes optimale. Plus précisément, nous disons que $\phi$ est Fisher consistante si pour chaque $x \in \mathcal{X}$, il existe un $f_x^*$ qui minimise $R_{\phi}(f'|X=x)$ tel que la classification $\text{sgn}_{\text{cls}}(f_x^*)$ est égale au classifieur de Bayes $h^*(x)$ pour $L_{01}$.
    La fonction de signe classifiant est définie par $\text{sgn}_{\text{cls}}(z) = 1$ si $z \ge 0$ et $\text{sgn}_{\text{cls}}(z) = -1$ si $z < 0$.
    Le classifieur de Bayes optimal est $h^*(x) = 1$ si $\eta(x) \ge 1/2$, et $h^*(x) = -1$ si $\eta(x) < 1/2$.

2.  **Démonstration de la consistance de Fisher pour la perte charnière :**
    Nous devons vérifier si $\text{sgn}_{\text{cls}}(f_x^*)$ correspond à $h^*(x)$ pour tous les cas de $\eta(x)$.

    *   **Cas 1 : $\eta(x) > 1/2$**
        Le classifieur de Bayes optimal est $h^*(x) = 1$.
        D'après la Question 2, le minimiseur unique de la perte charnière conditionnelle est $f_x^* = 1$.
        Alors $\text{sgn}_{\text{cls}}(f_x^*) = \text{sgn}_{\text{cls}}(1) = 1$.
        Dans ce cas, $\text{sgn}_{\text{cls}}(f_x^*) = h^*(x)$.

    *   **Cas 2 : $\eta(x) < 1/2$**
        Le classifieur de Bayes optimal est $h^*(x) = -1$.
        D'après la Question 2, le minimiseur unique de la perte charnière conditionnelle est $f_x^* = -1$.
        Alors $\text{sgn}_{\text{cls}}(f_x^*) = \text{sgn}_{\text{cls}}(-1) = -1$.
        Dans ce cas, $\text{sgn}_{\text{cls}}(f_x^*) = h^*(x)$.

    *   **Cas 3 : $\eta(x) = 1/2$**
        Le classifieur de Bayes optimal est $h^*(x) = 1$ (par convention).
        D'après la Question 2, l'ensemble des minimiseurs est l'intervalle $f_x^* \in [-1, 1]$.
        Nous devons vérifier s'il existe un $f' \in [-1, 1]$ tel que $\text{sgn}_{\text{cls}}(f') = 1$.
        Oui, nous pouvons choisir n'importe quel $f' \in [0, 1]$ (par exemple, $f'=0$). Pour un tel $f'$, nous avons $\text{sgn}_{\text{cls}}(f') = 1$.
        Dans ce cas, nous pouvons choisir un $f_x^*$ qui donne $\text{sgn}_{\text{cls}}(f_x^*) = h^*(x)$.

    Puisque dans tous les cas, la classification dérivée d'un minimiseur de la perte charnière conditionnelle correspond à la classification Bayes optimale, nous pouvons conclure que la perte charnière est **Fisher consistante** par rapport à la perte $0-1$.

Cette consistance est cruciale car elle garantit que si nous pouvons trouver une fonction de score $f$ qui minimise le risque avec la perte charnière (comme le fait une Machine à Vecteurs de Support, SVM), alors la fonction de classification résultante $h(x) = \text{sgn}_{\text{cls}}(f(x))$ se rapprochera du classifieur de Bayes optimal à mesure que le nombre de données d'entraînement augmente.