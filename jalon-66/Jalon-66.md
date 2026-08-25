---
uuid: "jalon-66"
title: "Intégrale de Lebesgue pour les fonctions positives"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 65 (Fonctions mesurables).md]]"
next: "[[Jalon 67 (Démonstration du théorème de convergence monotone).md]]"
---

# Jalon 66 : Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives

## 1. Genèse et motivation géométrique

L'intégrale de Riemann, bien qu'élégante et suffisante pour de nombreuses applications élémentaires, souffre de limitations fondamentales qui entravent le développement d'une théorie robuste de l'analyse fonctionnelle. Le cœur du problème riemannien réside dans sa méthode de partitionnement : en découpant le domaine de départ (l'axe des abscisses), on tente d'approcher l'aire sous la courbe par des rectangles verticaux. Cette approche s'effondre lorsque la fonction oscille trop violemment ou est discontinue partout, comme l'illustre la célèbre fonction indicatrice de $\mathbb{Q}$ (fonction de Dirichlet).

Pour pallier ce défaut, Henri Lebesgue introduit en 1901 une idée d'une simplicité et d'une puissance remarquables : au lieu de découper l'espace de départ, il faut partitionner l'espace d'arrivée (l'axe des ordonnées). En découpant les valeurs que prend la fonction et en mesurant (via la mesure de Lebesgue construite précédemment) la "taille" des ensembles de points de l'espace de départ où la fonction prend ces valeurs, on s'affranchit des contraintes de régularité topologique de la fonction. Cette inversion de perspective permet d'intégrer des fonctions extrêmement pathologiques et, surtout, d'obtenir des théorèmes de passage à la limite sous le signe intégral d'une généralité sans précédent.

## 2. Intégration des fonctions étagées positives

Avant de définir l'intégrale pour des fonctions mesurables générales, il est impératif de la définir sur une classe de fonctions simples qui serviront de briques élémentaires : les fonctions étagées.

**Définition (Fonction étagée) :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Une fonction $s : X \to \mathbb{R}$ est dite étagée si elle ne prend qu'un nombre fini de valeurs réelles et si elle est mesurable, c'est-à-dire que pour toute valeur $a \in \mathbb{R}$, l'ensemble $s^{-1}(\{a\}) \in \mathcal{A}$. Toute fonction étagée positive $s$ peut s'écrire sous forme canonique :
$$ s(x) = \sum_{i=1}^{n} \alpha_i \mathbf{1}_{A_i}(x) $$
où $\alpha_1, \dots, \alpha_n$ sont des réels strictement positifs deux à deux distincts, et les $A_i = s^{-1}(\{\alpha_i\})$ forment une partition mesurable du support de $s$.

**Définition (Intégrale d'une fonction étagée positive) :**
Soit $s : X \to [0, +\infty[$ une fonction étagée positive sous sa forme canonique $s = \sum_{i=1}^{n} \alpha_i \mathbf{1}_{A_i}$. L'intégrale de $s$ par rapport à la mesure $\mu$ est définie par :
$$ \int_X s \, d\mu = \sum_{i=1}^{n} \alpha_i \mu(A_i) $$
Cette quantité est un élément de $[0, +\infty]$. On adopte la convention formelle $0 \times (+\infty) = 0$, signifiant que l'intégrale d'une fonction identiquement nulle sur un ensemble de mesure infinie est nulle.

**Exemple concret calculatoire :**
Considérons l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ où $\lambda$ est la mesure de Lebesgue. Soit la fonction étagée :
$$ s(x) = 3 \cdot \mathbf{1}_{[0, 2]}(x) + 5 \cdot \mathbf{1}_{[4, 5]}(x) $$
Les valeurs prises sont $\alpha_1 = 3$ sur $A_1 = [0, 2]$ et $\alpha_2 = 5$ sur $A_2 = [4, 5]$. La forme canonique est respectée (si on ajoute $\alpha_0 = 0$ sur $A_0 = \mathbb{R} \setminus ([0, 2] \cup [4, 5])$ dont l'apport est nul).
Calculons l'intégrale :
$$ \int_{\mathbb{R}} s \, d\lambda = 3 \cdot \lambda([0, 2]) + 5 \cdot \lambda([4, 5]) = 3 \cdot (2 - 0) + 5 \cdot (5 - 4) = 3(2) + 5(1) = 11 $$

**Linéarité sur les fonctions étagées positives :**
Soient $s, t$ deux fonctions étagées positives sur $X$ et $c \geq 0$. Alors :
1. $\int_X (s+t) \, d\mu = \int_X s \, d\mu + \int_X t \, d\mu$
2. $\int_X (cs) \, d\mu = c \int_X s \, d\mu$
La démonstration repose sur le raffinement des partitions définissant $s$ et $t$ pour exprimer $s+t$ sur une partition commune.

## 3. L'intégrale de Lebesgue des fonctions mesurables positives

Nous étendons maintenant la définition par un processus d'approximation supremum.

**Définition (Intégrale de Lebesgue) :**
Soit $f : X \to [0, +\infty]$ une fonction mesurable. L'intégrale de $f$ par rapport à $\mu$ est définie par :
$$ \int_X f \, d\mu = \sup \left\lbrace \int_X s \, d\mu \mid s \text{ est étagée}, \ 0 \leq s \leq f \right\rbrace $$
Cette définition garantit que l'intégrale est toujours bien définie dans $[0, +\infty]$.

**Propriétés immédiates :**
1. **Positivité :** Si $f \geq 0$, alors $\int_X f \, d\mu \geq 0$.
2. **Croissance :** Si $0 \leq f \leq g$, alors $\int_X f \, d\mu \leq \int_X g \, d\mu$.
3. **Invariance de mesure nulle :** Si $\mu(A) = 0$, alors $\int_A f \, d\mu = \int_X f \mathbf{1}_A \, d\mu = 0$ pour toute fonction mesurable positive $f$.

**Exemple : L'indicatrice de $\mathbb{Q}$**
Soit $f(x) = \mathbf{1}_{\mathbb{Q} \cap [0,1]}(x)$ sur l'espace $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$.
La fonction $f$ ne prend que les valeurs $0$ et $1$. Elle est donc étagée et sa forme canonique sur $[0,1]$ est :
$$ f = 1 \cdot \mathbf{1}_{\mathbb{Q} \cap [0,1]} + 0 \cdot \mathbf{1}_{([0,1] \setminus \mathbb{Q})} $$
L'intégrale de Lebesgue vaut :
$$ \int_{[0,1]} f \, d\lambda = 1 \cdot \lambda(\mathbb{Q} \cap [0,1]) + 0 \cdot \lambda([0,1] \setminus \mathbb{Q}) $$
Puisque $\mathbb{Q}$ est dénombrable, $\lambda(\mathbb{Q} \cap [0,1]) = 0$. Ainsi,
$$ \int_{[0,1]} \mathbf{1}_{\mathbb{Q}} \, d\lambda = 1 \cdot 0 + 0 \cdot 1 = 0 $$
L'intégrale de Lebesgue résout instantanément la pathologie riemannienne.

## 4. Lemme d'approximation par des fonctions étagées

Pour manipuler rigoureusement l'intégrale définie par un supremum, un théorème d'approximation est indispensable.

**Théorème (Approximation par des étagées) :**
Soit $f : X \to [0, +\infty]$ une fonction mesurable. Il existe une suite $(s_n)_{n \in \mathbb{N}}$ de fonctions étagées positives telles que :
1. $\forall x \in X, \forall n \in \mathbb{N}, \ s_n(x) \leq s_{n+1}(x)$ (la suite est croissante).
2. $\forall x \in X, \ \lim_{n \to \infty} s_n(x) = f(x)$ (convergence ponctuelle).
De plus, si $f$ est bornée, la convergence est uniforme.

**Construction (Démonstration explicite) :**
Pour chaque entier $n \geq 1$, on découpe l'axe des ordonnées $[0, n]$ en sous-intervalles de largeur $2^{-n}$. Pour $x \in X$, on définit :
$$ s_n(x) = \begin{cases} \frac{k}{2^n} & \text{si } \frac{k}{2^n} \leq f(x) < \frac{k+1}{2^n} \text{ pour un certain } 0 \leq k < n2^n \\ n & \text{si } f(x) \geq n \end{cases} $$
Plus formellement, $s_n$ s'écrit :
$$ s_n(x) = \sum_{k=0}^{n2^n-1} \frac{k}{2^n} \mathbf{1}_{A_{n,k}}(x) + n \mathbf{1}_{B_n}(x) $$
où $A_{n,k} = f^{-1}\left(\left[\frac{k}{2^n}, \frac{k+1}{2^n}\right[\right)$ et $B_n = f^{-1}([n, +\infty])$.
Les ensembles $A_{n,k}$ et $B_n$ sont mesurables car $f$ est mesurable. Donc $s_n$ est étagée.
- **Croissance :** L'intervalle de définition de $s_n$ pour une valeur est divisé en deux pour $s_{n+1}$, dont la borne inférieure est soit conservée, soit augmentée. Par construction, $s_n \leq s_{n+1} \leq f$.
- **Convergence :** Si $f(x) < +\infty$, pour $n > f(x)$, $x \in A_{n,k}$ pour un certain $k$, donc $0 \leq f(x) - s_n(x) < 2^{-n}$. Ainsi $\lim_{n \to \infty} s_n(x) = f(x)$. Si $f(x) = +\infty$, alors $s_n(x) = n \to +\infty$.

## 5. Applications en probabilités

La construction de l'intégrale de Lebesgue pour les fonctions positives est le socle de la théorie moderne des probabilités. Dans un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$, une variable aléatoire positive $X : \Omega \to [0, +\infty[$ n'est rien d'autre qu'une fonction mesurable positive.
L'espérance mathématique est alors définie comme l'intégrale de Lebesgue :
$$ \mathbb{E}[X] = \int_{\Omega} X(\omega) \, d\mathbb{P}(\omega) $$
Cette définition, reposant sur le découpage de l'espace d'arrivée (les valeurs que peut prendre $X$), permet d'unifier le traitement des variables discrètes et continues sous un formalisme unique. Les théorèmes de convergence qui découleront de cette construction (Convergence Monotone, Lemme de Fatou) seront essentiels pour démontrer les lois des grands nombres et d'autres résultats asymptotiques.


## 6. Applications en Intelligence Artificielle et Logique

La théorie de la mesure et l'intégrale de Lebesgue ne sont pas de simples artefacts d'analyse abstraite ; elles constituent le socle de l'apprentissage statistique moderne.

### Théorie PAC (Probably Approximately Correct)
L'intégration de Lebesgue permet de définir rigoureusement le risque espéré d'un modèle d'IA : $R(h) = \int_{X \times Y} L(h(x), y) \, d\mathbb{P}(x, y)$. Sans la théorie de Lebesgue, les mesures de probabilité complexes (qui ne sont ni purement discrètes ni admettant des densités riemanniennes) sur des espaces de grande dimension ne pourraient pas être intégrées, ce qui rendrait impossible l'analyse de généralisation des réseaux de neurones.

### Descente de Gradient Stochastique (SGD)
La preuve de la convergence presque sûre de l'algorithme SGD, formalisée par l'algorithme de Robbins-Monro, s'appuie massivement sur les théorèmes de convergence de Lebesgue (notamment le théorème de convergence dominée et les lemmes de Fatou), garantissant que l'espérance de la perte diminue asymptotiquement malgré le bruit inhérent à l'échantillonnage par mini-batch.
