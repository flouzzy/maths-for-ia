---
uuid: jalon-140-exo-04
title: "Exercice 4 - Classifieur de Bayes"
type: Exercice
difficulty: 2
---

### Énoncé

Soit un problème de classification binaire où l'espace des caractéristiques est $(\mathcal{X}, \mathcal{A})$ et l'espace des labels est $\mathcal{Y} = \{-1, 1\}$. Nous considérons un couple de variables aléatoires $(X, Y)$ distribué selon une probabilité $P_{X,Y}$ sur l'espace mesurable produit $(\mathcal{X} \times \mathcal{Y}, \mathcal{A} \otimes \mathcal{P}(\mathcal{Y}))$.
Soit $\eta: \mathcal{X} \to [0, 1]$ la fonction de probabilité conditionnelle $P(Y=1|X=x)$. Par conséquent, $P(Y=-1|X=x) = 1 - \eta(x)$.

Pour la classification, nous utilisons la fonction de perte 0-1, définie par $L_{01}(y, \hat{y}) = \mathbf{1}_{y \neq \hat{y}}$ pour $y, \hat{y} \in \mathcal{Y}$. Le risque d'un classifieur $f: \mathcal{X} \to \mathcal{Y}$ est donné par $R(f) = \mathbb{E}[L_{01}(Y, f(X))]$.

1.  **Classifieur de Bayes :** Déterminez l'expression du classifieur de Bayes $f_B: \mathcal{X} \to \mathcal{Y}$, qui minimise le risque $R(f)$, en fonction de $\eta(x)$.
2.  **Risque de Bayes :** Calculez le risque de Bayes $R(f_B)$ correspondant à ce classifieur optimal.
3.  **Perte de substitution (Surrogate Loss) :** Considérons la perte exponentielle $L_{exp}: \mathcal{Y} \times \mathbb{R} \to \mathbb{R}^+$ définie par $L_{exp}(y, h) = \exp(-y h)$ pour $y \in \mathcal{Y}$ et $h \in \mathbb{R}$. Pour une fonction de score $h: \mathcal{X} \to \mathbb{R}$, le risque associé à cette perte est $R_{exp}(h) = \mathbb{E}[L_{exp}(Y, h(X))]$. Déterminez la fonction de score optimale $h^*: \mathcal{X} \to \mathbb{R}$ qui minimise $R_{exp}(h)$ point par point, c'est-à-dire qui minimise $\mathbb{E}[L_{exp}(Y, h(X))|X=x]$ pour tout $x \in \mathcal{X}$. Discutez brièvement du lien entre le signe de $h^*(x)$ et le classifieur de Bayes $f_B(x)$.

---

### Correction

1.  **Classifieur de Bayes $f_B(x)$ :**

    Le classifieur de Bayes $f_B(x)$ est défini comme la fonction qui minimise le risque conditionnel en chaque point $x \in \mathcal{X}$ :
    $$f_B(x) = \arg\min_{\hat{y} \in \{-1, 1\}} \mathbb{E}[L_{01}(Y, \hat{y})|X=x]$$

    Calculons les risques conditionnels pour $\hat{y}=1$ et $\hat{y}=-1$ :

    *   Pour $\hat{y} = 1$:
        $$ \mathbb{E}[L_{01}(Y, 1)|X=x] = \mathbb{E}[\mathbf{1}_{Y \neq 1}|X=x] $$
        $$ = P(Y=-1|X=x) $$
        $$ = 1 - \eta(x) $$

    *   Pour $\hat{y} = -1$:
        $$ \mathbb{E}[L_{01}(Y, -1)|X=x] = \mathbb{E}[\mathbf{1}_{Y \neq -1}|X=x] $$
        $$ = P(Y=1|X=x) $$
        $$ = \eta(x) $$

    Le classifieur de Bayes $f_B(x)$ choisit la valeur de $\hat{y}$ qui a le risque conditionnel minimal.
    Donc, $f_B(x) = 1$ si $1 - \eta(x) < \eta(x)$, et $f_B(x) = -1$ si $\eta(x) < 1 - \eta(x)$.
    Si $1 - \eta(x) = \eta(x)$, c'est-à-dire $\eta(x) = 1/2$, le choix est arbitraire (par convention, on peut choisir 1).

    Simplifions les inégalités :
    *   $1 - \eta(x) < \eta(x) \iff 1 < 2\eta(x) \iff \eta(x) > 1/2$. Dans ce cas, $f_B(x) = 1$.
    *   $\eta(x) < 1 - \eta(x) \iff 2\eta(x) < 1 \iff \eta(x) < 1/2$. Dans ce cas, $f_B(x) = -1$.
    *   Si $\eta(x) = 1/2$, alors $1 - \eta(x) = \eta(x)$, et le risque est égal pour les deux classes. Par convention, nous choisissons $f_B(x)=1$.

    Ainsi, nous pouvons exprimer le classifieur de Bayes comme :
    $$ f_B(x) = \begin{cases} 1 & \text{si } \eta(x) \ge 1/2 \\ -1 & \text{si } \eta(x) < 1/2 \end{cases} $$
    Une écriture compacte souvent utilisée est :
    $$ f_B(x) = \text{sgn}(2\eta(x) - 1) $$
    où $\text{sgn}(0)$ est défini comme 1.

2.  **Risque de Bayes $R(f_B)$ :**

    Le risque de Bayes est le risque du classifieur de Bayes :
    $$ R(f_B) = \mathbb{E}[L_{01}(Y, f_B(X))] $$
    Par la loi de l'espérance totale, on peut écrire :
    $$ R(f_B) = \mathbb{E}_X[\mathbb{E}[L_{01}(Y, f_B(X))|X]] $$
    Pour un $x$ fixé, $\mathbb{E}[L_{01}(Y, f_B(X))|X=x]$ est le minimum des risques conditionnels que nous avons calculés.
    $$ \mathbb{E}[L_{01}(Y, f_B(x))|X=x] = \min(\eta(x), 1 - \eta(x)) $$
    Donc, le risque de Bayes s'exprime par :
    $$ R(f_B) = \mathbb{E}_X[\min(\eta(X), 1 - \eta(X))] $$
    Alternativement, en utilisant la propriété $\min(a, b) = \frac{a+b - |a-b|}{2}$:
    $$ \min(\eta(x), 1 - \eta(x)) = \frac{\eta(x) + (1-\eta(x)) - |\eta(x) - (1-\eta(x))|}{2} $$
    $$ = \frac{1 - |2\eta(x) - 1|}{2} $$
    Ainsi, le risque de Bayes peut également s'écrire :
    $$ R(f_B) = \mathbb{E}_X\left[\frac{1 - |2\eta(X) - 1|}{2}\right] = \frac{1}{2} - \frac{1}{2}\mathbb{E}_X[|2\eta(X) - 1|] $$

3.  **Perte de substitution (Surrogate Loss) :**

    Nous cherchons la fonction de score $h^*: \mathcal{X} \to \mathbb{R}$ qui minimise $R_{exp}(h) = \mathbb{E}[L_{exp}(Y, h(X))]$.
    Comme pour le classifieur de Bayes, nous pouvons minimiser le risque conditionnel point par point. Soit $h_x = h(x)$ la valeur du score pour un $x$ donné. Nous voulons minimiser :
    $$ \mathbb{E}[L_{exp}(Y, h_x)|X=x] = \mathbb{E}[\exp(-Y h_x)|X=x] $$
    En décomposant par les valeurs possibles de $Y$:
    $$ \mathbb{E}[\exp(-Y h_x)|X=x] = P(Y=1|X=x) \exp(-1 \cdot h_x) + P(Y=-1|X=x) \exp(-(-1) \cdot h_x) $$
    $$ = \eta(x) \exp(-h_x) + (1 - \eta(x)) \exp(h_x) $$
    Soit $g(h_x) = \eta(x) \exp(-h_x) + (1 - \eta(x)) \exp(h_x)$. Pour trouver le minimum, nous calculons la dérivée première par rapport à $h_x$ et la mettons à zéro :
    $$ \frac{d}{dh_x} g(h_x) = -\eta(x) \exp(-h_x) + (1 - \eta(x)) \exp(h_x) $$
    En égalant la dérivée à zéro :
    $$ -\eta(x) \exp(-h_x) + (1 - \eta(x)) \exp(h_x) = 0 $$
    $$ (1 - \eta(x)) \exp(h_x) = \eta(x) \exp(-h_x) $$
    Multiplions les deux côtés par $\exp(h_x)$ (valide car $\exp(h_x) > 0$):
    $$ (1 - \eta(x)) \exp(2h_x) = \eta(x) $$
    Pour $\eta(x) \in (0, 1)$, $1-\eta(x) \neq 0$. Nous pouvons diviser :
    $$ \exp(2h_x) = \frac{\eta(x)}{1 - \eta(x)} $$
    Prenons le logarithme naturel des deux côtés :
    $$ 2h_x = \log\left(\frac{\eta(x)}{1 - \eta(x)}\right) $$
    La fonction de score optimale $h^*(x)$ est donc :
    $$ h^*(x) = \frac{1}{2} \log\left(\frac{\eta(x)}{1 - \eta(x)}\right) $$
    (Note : cette solution est définie pour $\eta(x) \in (0, 1)$. Si $\eta(x)=0$, le terme devient $\log(0)$ ce qui tend vers $-\infty$. Si $\eta(x)=1$, le terme devient $\log(\infty)$ ce qui tend vers $+\infty$. Ces cas extrêmes indiquent une classification parfaite pour la perte exponentielle, où le score doit être $-\infty$ ou $+\infty$ pour minimiser le risque.)

    Pour vérifier que c'est bien un minimum, calculons la dérivée seconde :
    $$ \frac{d^2}{dh_x^2} g(h_x) = \eta(x) \exp(-h_x) + (1 - \eta(x)) \exp(h_x) $$
    Comme $\eta(x) \in [0, 1]$ et les fonctions exponentielles sont toujours positives, la dérivée seconde est toujours positive (strictement positive pour $\eta(x) \in (0,1)$). Il s'agit donc bien d'un minimum global.

    **Lien avec le classifieur de Bayes $f_B(x)$ :**

    Analysons le signe de $h^*(x)$ :
    *   Si $\eta(x) > 1/2$: alors $2\eta(x) - 1 > 0$. De plus, $1 - \eta(x) < \eta(x)$, donc $\frac{\eta(x)}{1 - \eta(x)} > 1$. Par conséquent, $\log\left(\frac{\eta(x)}{1 - \eta(x)}\right) > 0$, ce qui implique $h^*(x) > 0$.
    *   Si $\eta(x) < 1/2$: alors $2\eta(x) - 1 < 0$. De plus, $1 - \eta(x) > \eta(x)$, donc $\frac{\eta(x)}{1 - \eta(x)} < 1$. Par conséquent, $\log\left(\frac{\eta(x)}{1 - \eta(x)}\right) < 0$, ce qui implique $h^*(x) < 0$.
    *   Si $\eta(x) = 1/2$: alors $2\eta(x) - 1 = 0$. De plus, $\frac{\eta(x)}{1 - \eta(x)} = 1$. Par conséquent, $\log(1) = 0$, ce qui implique $h^*(x) = 0$.

    En comparant avec l'expression du classifieur de Bayes $f_B(x) = \text{sgn}(2\eta(x) - 1)$:
    *   Si $h^*(x) > 0$, alors $\eta(x) > 1/2$, et $f_B(x) = 1$.
    *   Si $h^*(x) < 0$, alors $\eta(x) < 1/2$, et $f_B(x) = -1$.
    *   Si $h^*(x) = 0$, alors $\eta(x) = 1/2$, et $f_B(x) = 1$ (par convention, $\text{sgn}(0)=1$).

    On observe que le signe de la fonction de score optimale $h^*(x)$ est cohérent avec le classifieur de Bayes $f_B(x)$. Plus précisément, si on définit un classifieur $\hat{f}(x) = \text{sgn}(h(x))$, alors le classifieur $\hat{f}^*(x) = \text{sgn}(h^*(x))$ est équivalent au classifieur de Bayes $f_B(x)$.
    Cette propriété est connue sous le nom de **consistance de Fisher** (ou *Fisher consistency*). Elle signifie que la minimisation du risque de la perte de substitution (ici la perte exponentielle) conduit à un prédicteur dont le signe est optimal par rapport à la perte 0-1, ce qui en fait une bonne perte de substitution pour la classification binaire.