---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]"
next: "[[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo Levi)

## 1. Genèse et Concepts Physiques

Historiquement, l'intégrale de Riemann posait un problème majeur pour le passage à la limite sous le signe intégral. Si l'on dispose d'une suite de fonctions intégrables au sens de Riemann qui converge simplement vers une fonction limite, cette limite n'est pas nécessairement intégrable, et même si elle l'est, l'intégrale de la limite n'est pas forcément égale à la limite des intégrales. L'intégrale de Lebesgue apporte une flexibilité et une robustesse remarquables à ce problème, et le Théorème de Convergence Monotone (dû à l'école italienne, notamment Beppo Levi) en est la clé de voûte.

De façon intuitive, imaginez que l'on construit un volume par l'accumulation de couches successives positives. Si chaque étape de la construction augmente le volume total, l'aire (ou le volume) finale sous la fonction limite est précisément égale à la limite des aires mesurées à chaque étape. Ce résultat garantit l'invariance de la mesure face à une accumulation monotone infinie, jetant ainsi les bases de la théorie moderne de l'intégration et des probabilités.

## 2. Définitions, Théorèmes et Exemples Concrets

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Théorème de Convergence Monotone (Beppo Levi)

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
Si la suite est croissante presque partout :
$$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \quad \text{p.p.}$$
Alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable et :
$$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

**Dissection des Variables :**
- $X$ : l'espace de base (par exemple $\mathbb{R}$).
- $\mathcal{F}$ : la tribu d'ensembles mesurables sur $X$.
- $\mu$ : la mesure sur $(X, \mathcal{F})$ (ex: mesure de Lebesgue ou mesure de comptage).
- $f_n$ : fonctions positives à valeurs dans $[0, +\infty]$. La valeur $+\infty$ est permise.

### Exemples d'Application Immédiats

**Exemple 1 : Accumulation de marches d'escalier.**
Soit $f_n = \mathbb{1}_{[0, 1 - 1/n]}$. Les $f_n$ sont croissantes et tendent vers $f = \mathbb{1}_{[0, 1[}$.
On a $\int f_n = 1 - 1/n$.
Par Beppo Levi, $\int f = \lim (1 - 1/n) = 1$, ce qui correspond bien à la mesure de $[0, 1[$.

**Exemple 2 : Somme géométrique sur un intervalle.**
Soit $f_n(x) = \sum_{k=0}^n x^k$ sur $X = [0, 1/2]$. Les $f_n$ sont croissantes car les termes ajoutés sont positifs. La limite est $f(x) = \frac{1}{1-x}$.
$\lim_{n\to\infty} \int_0^{1/2} f_n(x) dx = \int_0^{1/2} \frac{1}{1-x} dx = [-\ln(1-x)]_0^{1/2} = \ln(2)$.

**Exemple 3 : Échappement de masse vers l'infini (Contre-exemple sans croissance).**
Soit $f_n = n \mathbb{1}_{]0, 1/n[}$. On a $\int f_n = 1$ pour tout $n$.
La limite simple est $f = 0$ partout. L'intégrale de la limite est $0$, mais la limite des intégrales est $1$.
Le théorème de Beppo Levi ne s'applique pas car la suite $f_n$ n'est pas croissante : $f_1(1/2) = 0$ mais $f_2(1/2) = 0$, et $f_1(1/3) = 0$ tandis que $f_3(1/3)$ diverge. (C'est un classique qui montre l'importance de la condition de croissance).

**Exemple 4 : Fonctions dont l'intégrale diverge.**
Soit $f_n(x) = n \mathbb{1}_{[0, 1]}$. La suite est croissante. $\lim \int f_n = +\infty$. La fonction limite $f = +\infty \cdot \mathbb{1}_{[0, 1]}$. L'intégrale de $f$ vaut $+\infty \cdot 1 = +\infty$. L'égalité est vérifiée dans $\overline{\mathbb{R}}$.

**Exemple 5 : Mesure de comptage et séries à termes positifs.**
Soit $X = \mathbb{N}$ muni de la mesure de comptage. Soit $a_{n, k} \ge 0$.
Soit $f_n(k) = \sum_{j=0}^n a_{j, k}$. La suite $(f_n)$ est croissante en $n$ pour chaque $k$.
Le théorème de Beppo Levi stipule que :
$\sum_{k=0}^\infty \left( \sum_{j=0}^\infty a_{j,k} \right) = \sum_{j=0}^\infty \left( \sum_{k=0}^\infty a_{j,k} \right)$.
C'est le théorème de Fubini pour les séries à termes positifs.

### Corollaire (Sommation terme à terme)

Pour toute suite de fonctions mesurables **positives** $(u_n)_{n \in \mathbb{N}}$ :
$$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$

Ce corollaire est une application directe de Beppo Levi aux sommes partielles $S_N = \sum_{n=0}^N u_n$, qui forment bien une suite croissante de fonctions positives.

## 3. Démonstrations Rigoureuses

### Preuve du Théorème de Beppo Levi

**Étape 1 : Mesurabilité et existence de la limite.**
Puisque pour chaque $x \in X$, la suite $(f_n(x))$ est croissante et à valeurs dans $[0, +\infty]$, elle admet nécessairement une limite $f(x) \in [0, +\infty]$. La fonction $f = \sup_{n} f_n$ est mesurable comme supremum dénombrable de fonctions mesurables.

**Étape 2 : Inégalité $\int f_n \le \int f$.**
Pour tout $n$, on a $f_n \le f$. Par croissance de l'intégrale de Lebesgue, on obtient $\int f_n d\mu \le \int f d\mu$.
En passant à la limite (qui existe car la suite des intégrales est croissante), on obtient :
$$\lim_{n \to \infty} \int_X f_n d\mu \le \int_X f d\mu$$

**Étape 3 : Inégalité inverse (Le cœur de la preuve).**
Soit $s = \sum_{i=1}^k c_i \mathbb{1}_{A_i}$ une fonction simple étagée telle que $0 \le s \le f$.
Soit $\alpha \in ]0, 1[$. On définit l'ensemble $E_n = \{x \in X \mid f_n(x) \ge \alpha s(x)\}$.
Puisque $f_n \le f_{n+1}$, la suite d'ensembles $(E_n)$ est croissante : $E_n \subset E_{n+1}$.
De plus, comme $f_n(x) \to f(x)$ et que $\alpha < 1$, si $s(x) > 0$ alors $\alpha s(x) < f(x)$, donc pour $n$ assez grand, $f_n(x) \ge \alpha s(x)$. Si $s(x) = 0$, $x \in E_n$ pour tout $n$.
Ainsi, $\bigcup_{n=1}^\infty E_n = X$.

Par définition de l'intégrale et positivité de $f_n$ :
$$\int_X f_n d\mu \ge \int_{E_n} f_n d\mu \ge \int_{E_n} \alpha s d\mu = \alpha \sum_{i=1}^k c_i \mu(A_i \cap E_n)$$
Par continuité croissante de la mesure $\mu$, puisque $A_i \cap E_n \uparrow A_i$, on a $\lim_{n \to \infty} \mu(A_i \cap E_n) = \mu(A_i)$.
Ainsi, en passant à la limite quand $n \to \infty$ :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \alpha \sum_{i=1}^k c_i \mu(A_i) = \alpha \int_X s d\mu$$
Cette inégalité étant vraie pour tout $\alpha \in ]0, 1[$, on peut faire tendre $\alpha \to 1$ pour obtenir :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \int_X s d\mu$$

**Étape 4 : Conclusion par passage au supremum.**
L'inégalité précédente est valable pour toute fonction simple $s$ telle que $0 \le s \le f$.
Par définition de l'intégrale des fonctions positives (qui est le supremum des intégrales des fonctions simples minorantes), on obtient :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \sup_{0 \le s \le f} \int_X s d\mu = \int_X f d\mu$$
Les deux inégalités (Étapes 2 et 4) prouvent l'égalité formelle du Théorème de Beppo Levi.

## 4. Applications en Intelligence Artificielle et Théorie de la Décision

En apprentissage statistique et en théorie de la décision, on manipule en permanence des espérances mathématiques, qui ne sont rien d'autre que des intégrales de Lebesgue par rapport à une mesure de probabilité $\mathbb{P}$.

**Approximation des risques empiriques :**
Lorsqu'on entraîne un réseau de neurones avec un volume de données croissant ou une architecture qui s'affine itérativement, les fonctions de risque empirique peuvent être construites de manière monotone. Le TCM garantit que le risque limite est exactement la limite des risques, permettant de valider les garanties de généralisation asymptotiques.

**Modèles de Markov cachés et Espérance conditionnelle :**
Dans le calcul des probabilités de transition infinies et des processus stochastiques sous-jacents aux MDP (Markov Decision Processes) ou l'apprentissage par renforcement, les sommes d'espérances de récompenses futures actualisées (discounted rewards) reposent fondamentalement sur le corollaire du TCM. On s'assure ainsi que l'interversion de la somme (temporelle infinie) et de l'espérance est licite, validant ainsi l'équation de Bellman.

**Méthodes à noyaux (Kernel Methods) :**
Les noyaux définis positifs comme le noyau RBF génèrent des espaces de Hilbert (RKHS) de dimension infinie. Le produit scalaire est une série de fonctions propres. Le TCM permet de prouver que les propriétés de reproductibilité se conservent à la limite, assurant la stabilité numérique et analytique des SVMs (Support Vector Machines).
