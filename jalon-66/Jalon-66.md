---
uuid: "jalon-66"
title: "Intégrale de Lebesgue pour les fonctions mesurables positives"
year: 2
trimester: 6
tags:
  - math/analyse
  - math/integration
  - ia/fondations
prev: "[[jalon-65/Jalon-65.md|Jalon 65 : Fonctions mesurables]]"
next: "[[jalon-67/Jalon-67.md|Jalon 67 : Démonstration du théorème de convergence monotone]]"
---

# Jalon 66 : Intégrale de Lebesgue pour les fonctions mesurables positives

## 1. Genèse de l'Intégrale de Lebesgue

Le développement de l'intégrale de Lebesgue, publié par Henri Lebesgue en 1902 dans sa thèse *Intégrale, longueur, aire*, répond à une crise profonde de l'analyse réelle à la fin du XIXe siècle. L'intégrale de Riemann, bien qu'efficace pour les fonctions continues ou continues par morceaux, souffrait d'un défaut fondamental : le manque d'invariance par les passages à la limite. Si l'on prend une suite de fonctions $(f_n)$ convergeant vers $f$, l'intégrale de Riemann de $f_n$ ne converge pas nécessairement vers l'intégrale de $f$, même si toutes les $f_n$ sont intégrables, à moins d'imposer des conditions restrictives comme la convergence uniforme.

Un exemple frappant de cette limite est la fonction indicatrice des rationnels, la fonction de Dirichlet, $\mathbf{1}_{\mathbb{Q}}$. Cette fonction est la limite ponctuelle d'une suite de fonctions en escalier, mais elle n'est pas Riemann-intégrable car ses sommes de Darboux inférieures et supérieures diffèrent sur tout intervalle.

La méthode de Riemann découpe l'axe des abscisses (le domaine de définition) en petits intervalles, et approche la fonction par des rectangles verticaux. Lebesgue renverse cette perspective de manière brillante : il découpe l'axe des **ordonnées** (les valeurs prises par la fonction). Au lieu de regrouper les points $x$ qui sont proches spatialement, il regroupe les points $x$ pour lesquels $f(x)$ prend à peu près la même valeur.

Pour calculer l'aire, il suffit alors de mesurer la "taille" de ces ensembles de points, ce qui nécessite une théorie robuste de la mesure (la mesure de Lebesgue). Cette construction ascendante commence par des fonctions très simples, qui ne prennent qu'un nombre fini de valeurs, pour s'étendre par des passages au supremum à toutes les fonctions mesurables positives.

## 2. Intégrale des fonctions simples positives

La construction de l'intégrale commence par l'ensemble des fonctions les plus élémentaires, que l'on appelle fonctions simples (ou étagées).

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.

Une fonction $s : X \to \mathbb{R}_+$ est dite **simple** si elle est mesurable et ne prend qu'un nombre fini de valeurs distinctes. Soient $a_1, a_2, \ldots, a_n$ ces valeurs distinctes strictement positives. Les ensembles $A_i = s^{-1}(\{a_i\}) = \{x \in X \mid s(x) = a_i\}$ forment une partition de l'ensemble $\{x \in X \mid s(x) > 0\}$, et appartiennent tous à la tribu $\mathcal{A}$ puisque $s$ est mesurable.

On peut donc exprimer $s$ sous sa **forme canonique** :
$$ s = \sum_{i=1}^n a_i \mathbf{1}_{A_i} $$
où $\mathbf{1}_{A_i}$ désigne la fonction indicatrice de l'ensemble $A_i$.

**Définition 1 (Intégrale d'une fonction simple positive) :**
Pour une fonction simple positive $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ (sous forme canonique), son intégrale par rapport à la mesure $\mu$ est définie par :
$$ \int_X s \, d\mu = \sum_{i=1}^n a_i \mu(A_i) $$
Si l'un des ensembles $A_i$ est de mesure infinie et $a_i > 0$, l'intégrale vaut $+\infty$. On utilise la convention fondamentale $0 \cdot (+\infty) = 0$, ce qui signifie que si $A_i$ est un ensemble de mesure infinie mais que la fonction y est nulle, la contribution à l'intégrale est nulle.

### Exemple numérique calculé

Considérons l'espace $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$, où $\lambda$ est la mesure de Lebesgue.
Soit $s(x)$ la fonction définie par :
- $s(x) = 2$ si $x \in [0, 1] \cup [3, 4]$
- $s(x) = 5$ si $x \in [1, 2]$
- $s(x) = 0$ ailleurs.

La forme canonique de $s$ est $s = 2 \cdot \mathbf{1}_{A_1} + 5 \cdot \mathbf{1}_{A_2}$, où $A_1 = [0, 1] \cup [3, 4]$ et $A_2 = [1, 2]$.
Calculons la mesure de ces ensembles :
- $\lambda(A_1) = \lambda([0, 1]) + \lambda([3, 4]) = (1 - 0) + (4 - 3) = 1 + 1 = 2$.
- $\lambda(A_2) = \lambda([1, 2]) = 2 - 1 = 1$.

L'intégrale de $s$ est :
$$ \int_{\mathbb{R}} s \, d\lambda = 2 \cdot \lambda(A_1) + 5 \cdot \lambda(A_2) = 2 \cdot 2 + 5 \cdot 1 = 4 + 5 = 9 $$

### Propriétés fondamentales de l'intégrale des fonctions simples

Pour toutes fonctions simples positives $s$ et $t$, et pour tout $\alpha \ge 0$, on a :
1. **Positivité :** $\int s \, d\mu \ge 0$.
2. **Homogénéité :** $\int (\alpha s) \, d\mu = \alpha \int s \, d\mu$.
3. **Additivité :** $\int (s + t) \, d\mu = \int s \, d\mu + \int t \, d\mu$.
4. **Croissance :** Si $s \le t$ presque partout, alors $\int s \, d\mu \le \int t \, d\mu$.

## 3. Extension aux fonctions mesurables positives

Nous pouvons maintenant étendre l'intégrale à toute fonction mesurable positive en utilisant une approche d'approximation par le bas. L'idée est que l'aire sous le graphe d'une fonction $f \ge 0$ doit être la plus grande aire sous le graphe de n'importe quelle fonction simple positive qui reste sous $f$.

Soit $\mathcal{M}^+$ l'ensemble des fonctions mesurables de $X$ dans $[0, +\infty]$.

**Définition 2 (Intégrale de Lebesgue) :**
Pour toute fonction $f \in \mathcal{M}^+$, l'intégrale de $f$ par rapport à $\mu$ est définie par le supremum :
$$ \int_X f \, d\mu = \sup \left\lbrace \int_X s \, d\mu \ \middle|\ s \text{ est simple}, \ 0 \le s \le f \right\rbrace $$

Cette intégrale peut prendre la valeur $+\infty$. Si $\int_X f \, d\mu < +\infty$, on dit que $f$ est **intégrable** (au sens de Lebesgue) ou sommable.

### Exemple concret et cas de la fonction de Dirichlet

Reprenons l'exemple de la fonction de Dirichlet sur l'intervalle $[0, 1]$ : $f = \mathbf{1}_{\mathbb{Q} \cap [0, 1]}$.
Cette fonction est mesurable (car l'ensemble des rationnels est borélien) et positive. De plus, elle est déjà une fonction simple ! Elle ne prend que les valeurs 1 (sur $A_1 = \mathbb{Q} \cap [0, 1]$) et 0 (sur $A_0 = ([0, 1] \setminus \mathbb{Q})$).

Calculons son intégrale avec la mesure de Lebesgue $\lambda$ :
$$ \int_{[0,1]} f \, d\lambda = 1 \cdot \lambda(\mathbb{Q} \cap [0, 1]) $$
L'ensemble $\mathbb{Q} \cap [0, 1]$ est dénombrable. Or, la mesure de Lebesgue d'un ensemble dénombrable est toujours nulle, c'est-à-dire $\lambda(\mathbb{Q} \cap [0, 1]) = 0$.
Par conséquent :
$$ \int_{[0,1]} \mathbf{1}_{\mathbb{Q} \cap [0, 1]} \, d\lambda = 1 \cdot 0 = 0 $$
Ainsi, la fonction de Dirichlet est intégrable au sens de Lebesgue et son intégrale vaut 0.

### Théorème : Approximation par des fonctions simples (Théorème fondamental d'approximation)

Toute la puissance de la définition repose sur le théorème suivant, qui justifie que toute fonction de $\mathcal{M}^+$ peut être atteinte par une suite croissante de fonctions simples.

**Théorème :**
Pour toute fonction $f \in \mathcal{M}^+$, il existe une suite $(s_n)_{n \in \mathbb{N}}$ de fonctions simples positives, croissante ($s_n \le s_{n+1}$ pour tout $n$), qui converge simplement vers $f$ en tout point de $X$ :
$$ \forall x \in X, \quad \lim_{n \to \infty} s_n(x) = f(x) $$

**Construction explicite :**
Pour un entier $n \ge 1$, on découpe l'intervalle $[0, n]$ en $n 2^n$ sous-intervalles de longueur $2^{-n}$. On définit la fonction simple $s_n$ par :
$$ s_n(x) = \sum_{k=0}^{n 2^n - 1} \frac{k}{2^n} \mathbf{1}_{\left\lbrace x \in X \mid \frac{k}{2^n} \le f(x) < \frac{k+1}{2^n} \right\rbrace}(x) + n \mathbf{1}_{\{x \in X \mid f(x) \ge n\}}(x) $$

Cette construction explicite montre bien comment on "découpe l'axe des ordonnées". Si $f(x)$ est fini, pour un $n$ suffisamment grand (dès que $n > f(x)$), la valeur $s_n(x)$ est l'approximation de $f(x)$ par défaut à la précision $2^{-n}$ près, donc $|f(x) - s_n(x)| < 2^{-n}$, ce qui prouve la convergence.

## 4. Démonstrations et Propriétés de base

Les propriétés de l'intégrale pour les fonctions de $\mathcal{M}^+$ se déduisent de la définition par supremum et des propriétés des fonctions simples.

**Proposition 1 :** Pour $f, g \in \mathcal{M}^+$ et $c \ge 0$ :
1. $\int (cf) \, d\mu = c \int f \, d\mu$.
2. Si $f \le g$, alors $\int f \, d\mu \le \int g \, d\mu$ (croissance).
3. Si $A \in \mathcal{A}$, $\int_A f \, d\mu = \int_X f \mathbf{1}_A \, d\mu$.

**Démonstration détaillée de la croissance (2) :**
Supposons que $f, g \in \mathcal{M}^+$ avec $f \le g$.
Soit $s$ une fonction simple positive telle que $0 \le s \le f$.
Puisque $f \le g$, on a nécessairement $0 \le s \le g$.
Ainsi, l'ensemble sur lequel on prend le supremum pour $f$ est inclus dans l'ensemble sur lequel on prend le supremum pour $g$ :
$$ \left\lbrace \int_X s \, d\mu \ \middle|\ s \text{ simple}, \ 0 \le s \le f \right\rbrace \subseteq \left\lbrace \int_X s \, d\mu \ \middle|\ s \text{ simple}, \ 0 \le s \le g \right\rbrace $$
Le supremum du premier ensemble est donc inférieur ou égal au supremum du second ensemble.
Par conséquent, $\int_X f \, d\mu \le \int_X g \, d\mu$. $\blacksquare$

### Inégalité de Markov

L'inégalité de Markov est un résultat fondamental qui relie la mesure des ensembles de niveau d'une fonction à son intégrale.

**Théorème (Inégalité de Markov) :**
Soit $f \in \mathcal{M}^+$. Pour tout réel $t > 0$, on a :
$$ \mu(\{x \in X \mid f(x) \ge t\}) \le \frac{1}{t} \int_X f \, d\mu $$

**Démonstration ligne par ligne :**
Soit $t > 0$ fixé. Notons $A_t = \{x \in X \mid f(x) \ge t\}$. L'ensemble $A_t$ est mesurable car $f$ est mesurable.
Sur l'ensemble $A_t$, la fonction $f$ est supérieure ou égale à $t$.
Sur le complémentaire de $A_t$, la fonction $f$ est positive ou nulle.
On peut donc écrire la minoration suivante valable pour tout $x \in X$ :
$$ f(x) \ge t \cdot \mathbf{1}_{A_t}(x) $$
En effet :
- Si $x \in A_t$, alors $f(x) \ge t$ et $t \cdot \mathbf{1}_{A_t}(x) = t \cdot 1 = t$, donc $f(x) \ge t$.
- Si $x \notin A_t$, alors $f(x) \ge 0$ et $t \cdot \mathbf{1}_{A_t}(x) = t \cdot 0 = 0$, donc $f(x) \ge 0$.

Par la propriété de croissance de l'intégrale (démontrée précédemment), on intègre cette inégalité :
$$ \int_X f \, d\mu \ge \int_X (t \cdot \mathbf{1}_{A_t}) \, d\mu $$
Or $t \cdot \mathbf{1}_{A_t}$ est une fonction simple, son intégrale est exactement $t \cdot \mu(A_t)$. D'où :
$$ \int_X f \, d\mu \ge t \cdot \mu(A_t) $$
En divisant par $t$ (qui est strictement positif), on obtient le résultat :
$$ \mu(\{x \in X \mid f(x) \ge t\}) \le \frac{1}{t} \int_X f \, d\mu $$
$\blacksquare$

### Fonctions d'intégrale nulle

**Théorème :** Soit $f \in \mathcal{M}^+$.
$$ \int_X f \, d\mu = 0 \iff f = 0 \text{ presque partout } (\mu\text{-p.p.}) $$

**Démonstration explicite :**
$(\impliedby)$ Supposons que $f = 0$ $\mu$-p.p. Soit $N = \{x \in X \mid f(x) > 0\}$. On a $\mu(N) = 0$.
Soit $s$ une fonction simple positive telle que $0 \le s \le f$. Alors $s$ s'annule aussi en dehors de $N$.
Écrivons $s = \sum_{i=1}^k a_i \mathbf{1}_{A_i}$ avec $a_i > 0$. Les ensembles $A_i$ sont inclus dans $N$, donc $\mu(A_i) \le \mu(N) = 0$.
Ainsi, $\int s \, d\mu = \sum a_i \mu(A_i) = 0$. Le supremum sur de telles fonctions $s$ est donc 0, soit $\int f \, d\mu = 0$.

$(\implies)$ Supposons que $\int_X f \, d\mu = 0$.
On veut montrer que l'ensemble $N = \{x \in X \mid f(x) > 0\}$ est de mesure nulle.
Exprimons $N$ comme une union dénombrable :
$$ N = \bigcup_{n=1}^\infty A_n \quad \text{où} \quad A_n = \left\lbrace x \in X \ \middle|\ f(x) \ge \frac{1}{n} \right\rbrace $$
D'après l'inégalité de Markov appliquée à $t = \frac{1}{n}$ :
$$ \mu(A_n) \le \frac{1}{1/n} \int_X f \, d\mu = n \cdot 0 = 0 $$
Ainsi, chaque ensemble $A_n$ est de mesure nulle. Par $\sigma$-sous-additivité de la mesure :
$$ \mu(N) = \mu\left( \bigcup_{n=1}^\infty A_n \right) \le \sum_{n=1}^\infty \mu(A_n) = \sum_{n=1}^\infty 0 = 0 $$
Donc $\mu(N) = 0$, ce qui signifie que $f = 0$ presque partout. $\blacksquare$

## 5. Applications en Physique, Probabilités & IA

La construction rigoureuse de l'intégrale pour des fonctions positives n'est pas qu'un exercice d'abstraction. Elle fournit le langage unifié pour les mathématiques modernes et le Machine Learning.

1. **Unification des variables aléatoires (Discrètes vs Continues) :** En théorie des probabilités (basée sur Kolmogorov), l'espérance d'une variable aléatoire positive $X$ (qui est une fonction mesurable de $\Omega$ dans $\mathbb{R}_+$) est définie par l'intégrale de Lebesgue : $\mathbb{E}[X] = \int_{\Omega} X \, d\mathbb{P}$. Ce formalisme met fin à la séparation artificielle entre variables discrètes (traitées par des sommes) et continues (traitées par des intégrales de Riemann). La somme n'est qu'une intégrale par rapport à la mesure de comptage.
2. **Calcul de la Cross-Entropy et Divergence KL :** Dans l'entraînement des réseaux de neurones, la perte de Cross-Entropy et la divergence de Kullback-Leibler mesurent la différence entre deux distributions de probabilité. Ces quantités intègrent des fonctions positives (les log-vraisemblances). L'intégrale de Lebesgue garantit que ces quantités sont mathématiquement bien définies et positives, même pour des distributions singulières (par exemple, des réseaux génératifs adversaires - GANs - dont le support des probabilités peut être concentré sur des sous-variétés de mesure de Lebesgue nulle dans $\mathbb{R}^n$).
3. **Optimisation stochastique :** Dans la descente de gradient stochastique (SGD), le risque empirique est défini comme une intégrale de la fonction de perte (souvent positive, comme la perte MSE ou Hinge) sur la distribution des données. Les inégalités de concentration (Markov, puis Tchebychev et Hoeffding) qui reposent sur ce formalisme permettent de garantir que l'erreur estimée sur un batch converge vers l'erreur généralisée.
