Mes chers étudiants,

Bienvenue à ce premier jalon de notre exploration des Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC. Nous débutons par un exercice de difficulté modeste, mais dont l'importance est capitale pour asseoir les fondations de notre compréhension. Il s'agit de revisiter des concepts fondamentaux de la théorie des probabilités qui sous-tendent toute la machinerie des processus empiriques. La rigueur sera notre guide.

---

# Jalon 141 : Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC
## Exercice 1/10 : Espérance de la Mesure Empirique (Difficulté : 1/10)

### Énoncé Rigoureux et Formel

Soit $(\Omega, \mathcal{A}, \mathbb{P})$ un espace de probabilité.
Soit $(\mathcal{X}, \mathcal{B})$ un espace mesurable.
Considérons une suite de variables aléatoires $X_1, X_2, \dots, X_n$ définies sur $(\Omega, \mathcal{A}, \mathbb{P})$ et à valeurs dans $(\mathcal{X}, \mathcal{B})$, supposées indépendantes et identiquement distribuées (i.i.d.) selon une loi $\mu$ sur $(\mathcal{X}, \mathcal{B})$.
Soit $f: \mathcal{X} \to \mathbb{R}$ une fonction mesurable et intégrable par rapport à $\mu$, c'est-à-dire $\mathbb{E}[|f(X_1)|] < \infty$.

Nous définissons la **mesure empirique** (ou plus précisément, l'espérance empirique de $f$) pour un échantillon de taille $n \in \mathbb{N}^*$ comme :
$$ \mathbb{P}_n f := \frac{1}{n} \sum_{i=1}^n f(X_i) $$
Et l'**espérance vraie** de $f$ comme :
$$ \mathbb{P} f := \mathbb{E}[f(X_1)] $$

**Question 1 :** Démontrer que l'espérance de la mesure empirique de $f$ est égale à l'espérance vraie de $f$. C'est-à-dire, montrer que $\mathbb{E}[\mathbb{P}_n f] = \mathbb{P} f$.

**Question 2 :** Soit $\Delta_n f := \mathbb{P}_n f - \mathbb{P} f$ la déviation de la mesure empirique par rapport à l'espérance vraie. Démontrer que l'espérance de cette déviation est nulle, c'est-à-dire $\mathbb{E}[\Delta_n f] = 0$.

### Analyse Détaillée

Cet exercice, bien que d'une difficulté apparente très faible, est absolument fondamental. Il établit la propriété d'**absence de biais** de l'estimateur $\mathbb{P}_n f$ pour le paramètre $\mathbb{P} f$. En d'autres termes, en moyenne, la moyenne empirique de $f$ est égale à la vraie moyenne de $f$.

Le Théorème de Glivenko-Cantelli, dans sa forme la plus simple, affirme la convergence uniforme de la fonction de répartition empirique vers la vraie fonction de répartition. Les généralisations que nous étudierons concernent la convergence uniforme de $\mathbb{P}_n f$ vers $\mathbb{P} f$ pour *toutes* les fonctions $f$ appartenant à une certaine classe $\mathcal{F}$ (les classes VC).

Avant de nous attaquer à la convergence *uniforme* sur une classe de fonctions, il est impératif de comprendre la convergence *ponctuelle* pour une fonction donnée. La première étape de cette compréhension est de s'assurer que l'estimateur est non biaisé. C'est précisément l'objet de cet exercice.

Les outils nécessaires sont élémentaires :
1.  La **linéarité de l'espérance** : Pour des variables aléatoires $Y_1, \dots, Y_k$ et des constantes $c_1, \dots, c_k$, $\mathbb{E}[\sum_{j=1}^k c_j Y_j] = \sum_{j=1}^k c_j \mathbb{E}[Y_j]$.
2.  La propriété d'**identiquement distribuées** (i.i.d.) des $X_i$, qui implique que $\mathbb{E}[f(X_i)]$ est la même pour tout $i \in \{1, \dots, n\}$.

La Question 1 démontre que $\mathbb{P}_n f$ est un estimateur non biaisé de $\mathbb{P} f$. La Question 2 en est une conséquence directe et reformule cette propriété en termes de déviation, ce qui est la perspective adoptée dans l'étude des processus empiriques (où l'on s'intéresse à la magnitude de $\mathbb{P}_n f - \mathbb{P} f$).

### Correction Pas-à-Pas (Zéro Ellipse Mathématique)

Nous allons procéder avec la plus grande rigueur, en détaillant chaque étape de calcul et en justifiant l'application de chaque propriété.

#### Question 1 : Démontrer que $\mathbb{E}[\mathbb{P}_n f] = \mathbb{P} f$.

**Étape 1 :** Commençons par la définition de l'espérance de la mesure empirique $\mathbb{P}_n f$.
$$ \mathbb{E}[\mathbb{P}_n f] = \mathbb{E}\left[\frac{1}{n} \sum_{i=1}^n f(X_i)\right] $$

**Étape 2 :** Appliquons la propriété de linéarité de l'espérance. Plus précisément, la propriété $\mathbb{E}[c Y] = c \mathbb{E}[Y]$ pour une constante $c \in \mathbb{R}$ et une variable aléatoire $Y$. Ici, $c = \frac{1}{n}$ et $Y = \sum_{i=1}^n f(X_i)$.
$$ \mathbb{E}\left[\frac{1}{n} \sum_{i=1}^n f(X_i)\right] = \frac{1}{n} \mathbb{E}\left[\sum_{i=1}^n f(X_i)\right] $$

**Étape 3 :** Appliquons la propriété de linéarité de l'espérance pour une somme de variables aléatoires : $\mathbb{E}[\sum_{i=1}^n Y_i] = \sum_{i=1}^n \mathbb{E}[Y_i]$. Ici, $Y_i = f(X_i)$.
$$ \frac{1}{n} \mathbb{E}\left[\sum_{i=1}^n f(X_i)\right] = \frac{1}{n} \sum_{i=1}^n \mathbb{E}[f(X_i)] $$

**Étape 4 :** Les variables aléatoires $X_1, X_2, \dots, X_n$ sont supposées identiquement distribuées. Cela signifie que la loi de $X_i$ est la même pour tout $i \in \{1, \dots, n\}$. Par conséquent, l'espérance de $f(X_i)$ est la même pour tout $i$.
$$ \mathbb{E}[f(X_i)] = \mathbb{E}[f(X_1)] \quad \text{pour tout } i \in \{1, \dots, n\} $$
Nous pouvons donc remplacer chaque terme $\mathbb{E}[f(X_i)]$ par $\mathbb{E}[f(X_1)]$.
$$ \frac{1}{n} \sum_{i=1}^n \mathbb{E}[f(X_i)] = \frac{1}{n} \sum_{i=1}^n \mathbb{E}[f(X_1)] $$

**Étape 5 :** La somme $\sum_{i=1}^n \mathbb{E}[f(X_1)]$ est une somme de $n$ termes identiques, chacun étant $\mathbb{E}[f(X_1)]$.
$$ \frac{1}{n} \sum_{i=1}^n \mathbb{E}[f(X_1)] = \frac{1}{n} \left( n \cdot \mathbb{E}[f(X_1)] \right) $$

**Étape 6 :** Simplifions l'expression.
$$ \frac{1}{n} \left( n \cdot \mathbb{E}[f(X_1)] \right) = \mathbb{E}[f(X_1)] $$

**Étape 7 :** Par définition, $\mathbb{P} f = \mathbb{E}[f(X_1)]$.
$$ \mathbb{E}[f(X_1)] = \mathbb{P} f $$

**Conclusion de la Question 1 :** Nous avons démontré, étape par étape, que :
$$ \mathbb{E}[\mathbb{P}_n f] = \mathbb{P} f $$

#### Question 2 : Démontrer que $\mathbb{E}[\Delta_n f] = 0$.

**Étape 1 :** Commençons par la définition de $\Delta_n f$.
$$ \mathbb{E}[\Delta_n f] = \mathbb{E}[\mathbb{P}_n f - \mathbb{P} f] $$

**Étape 2 :** Appliquons la propriété de linéarité de l'espérance pour une différence de variables aléatoires : $\mathbb{E}[Y - Z] = \mathbb{E}[Y] - \mathbb{E}[Z]$. Ici, $Y = \mathbb{P}_n f$ et $Z = \mathbb{P} f$.
$$ \mathbb{E}[\mathbb{P}_n f - \mathbb{P} f] = \mathbb{E}[\mathbb{P}_n f] - \mathbb{E}[\mathbb{P} f] $$

**Étape 3 :** Nous savons par la Question 1 que $\mathbb{E}[\mathbb{P}_n f] = \mathbb{P} f$.
$$ \mathbb{E}[\mathbb{P}_n f] - \mathbb{E}[\mathbb{P} f] = \mathbb{P} f - \mathbb{E}[\mathbb{P} f] $$

**Étape 4 :** Le terme $\mathbb{P} f$ est une constante (c'est un nombre réel, pas une variable aléatoire). L'espérance d'une constante est la constante elle-même : $\mathbb{E}[c] = c$ pour $c \in \mathbb{R}$.
$$ \mathbb{P} f - \mathbb{E}[\mathbb{P} f] = \mathbb{P} f - \mathbb{P} f $$

**Étape 5 :** Effectuons la soustraction.
$$ \mathbb{P} f - \mathbb{P} f = 0 $$

**Conclusion de la Question 2 :** Nous avons démontré, étape par étape, que :
$$ \mathbb{E}[\Delta_n f] = 0 $$

---

Voilà, mes chers étudiants. Cet exercice, bien que simple, est la pierre angulaire de notre édifice. Il nous assure que, en moyenne, notre estimateur empirique ne dévie pas de la vraie valeur. La prochaine étape sera de quantifier la *variance* de cette déviation, puis d'étendre ces notions à des classes entières de fonctions.

Poursuivez avec la même rigueur.
