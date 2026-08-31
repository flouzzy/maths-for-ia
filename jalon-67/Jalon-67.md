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

# Théorème de convergence monotone (Beppo Levi)

## Introduction

Imaginez la construction d'une tour constituée de strates successives de matériaux, où chaque jour une nouvelle couche est ajoutée de sorte que le volume global de la structure soit strictement croissant ($f_n \le f_{n+1}$). Le problème central consiste à déterminer si le volume final de la tour ($f = \lim f_n$) peut être directement déduit par la limite des mesures intermédiaires. Le Théorème de Convergence Monotone stipule que pour des grandeurs positives et croissantes, la mesure de la limite coïncide exactement avec la limite des mesures.

L'intégrale de Riemann ne garantit pas que la limite simple d'une suite de fonctions intégrables soit elle-même intégrable, ni que l'intégrale de la limite soit égale à la limite des intégrales. Le cadre de Lebesgue pallie cette déficience structurelle, offrant un outil robuste pour l'interversion des symboles de limite et d'intégrale.

## Définitions, Théorèmes et Exemples

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Théorème de Convergence Monotone (Beppo Levi)

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
Si la suite est croissante presque partout :
$$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \text{ p.p.}$$
Alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable et :
$$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

**Exemple concret immédiat :**
Considérons l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ avec la mesure de Lebesgue.
Soit la suite de fonctions indicatrices $f_n = \chi_{[-n, n]}$.
- Chaque fonction $f_n$ est positive et mesurable.
- Pour tout $x \in \mathbb{R}$, si on augmente $n$, l'intervalle $[-n, n]$ s'élargit. Donc $f_n(x) \le f_{n+1}(x)$.
- L'intégrale de chaque fonction est la longueur de l'intervalle : $\int_{\mathbb{R}} f_n d\lambda = 2n$.
- La limite ponctuelle de la suite est $f(x) = \lim_{n \to \infty} f_n(x) = 1$ (la fonction constante égale à 1).
D'après le théorème de convergence monotone, l'intégrale de la fonction limite est la limite des intégrales :
$$\int_{\mathbb{R}} 1 d\lambda = \lim_{n \to \infty} 2n = +\infty$$
Ce qui correspond bien à la mesure de Lebesgue de $\mathbb{R}$.

**Exemple avec croissance stricte sur un compact :**
Soit $f_n(x) = (1 - x/n)^n \chi_{[0, n]}(x)$.
- Sur $[0, n]$, $f_n(x)$ est positive. On peut montrer (via l'étude de la dérivée par rapport à $n$) que la suite $(f_n(x))$ est croissante et converge vers $e^{-x}$.
- Les intégrales valent : $\int_0^\infty f_n(x) dx = \int_0^n (1 - x/n)^n dx = \frac{n}{n+1}$.
- La limite de ces intégrales est $\lim \frac{n}{n+1} = 1$.
- D'autre part, la fonction limite est $f(x) = e^{-x}$. Son intégrale sur $[0, +\infty[$ vaut $\int_0^\infty e^{-x} dx = 1$.
Les deux quantités coïncident, validant le théorème.

### Corollaire sur les séries de fonctions (Sommation terme à terme)

Pour toute suite de fonctions mesurables positives $(u_n)$ sur $(X, \mathcal{F}, \mu)$ :
$$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$

**Exemple concret immédiat :**
Soit $X = [0, 1[$ avec la mesure de Lebesgue.
Considérons la série géométrique : $u_n(x) = x^n$.
- Les fonctions $u_n$ sont positives et mesurables.
- L'intégrale de $u_n$ est : $\int_0^1 x^n dx = \frac{1}{n+1}$.
- La limite de la somme est $\sum_{n=0}^\infty x^n = \frac{1}{1-x}$.
D'après le corollaire, on peut intervertir la somme et l'intégrale, on a alors :
$$\int_0^1 \frac{1}{1-x} dx = \sum_{n=0}^\infty \frac{1}{n+1} = +\infty$$
L'intégrale vaut bien $+\infty$ (divergence logarithmique en 1), confirmant l'égalité.

## Demonstrations

**Démonstration du Théorème de Beppo Levi**

1. Existence de la limite : Comme la suite $(f_n(x))$ est une suite croissante à valeurs dans $[0, +\infty]$, elle admet nécessairement une limite dans $[0, +\infty]$ pour chaque $x \in X$. Soit $f(x) = \lim_{n \to \infty} f_n(x) = \sup_{n} f_n(x)$. Le supremum dénombrable de fonctions mesurables est mesurable.

2. Majoration immédiate : Puisque pour tout $n$, $f_n \le f$, la monotonie de l'intégrale (établie pour les fonctions positives) implique que :
   $$\int_X f_n d\mu \le \int_X f d\mu$$
   En passant à la limite (qui existe dans $[0, +\infty]$ car la suite des intégrales est croissante) :
   $$\lim_{n \to \infty} \int_X f_n d\mu \le \int_X f d\mu$$

3. Minoration fondamentale : Soit $s$ une fonction étagée mesurable telle que $0 \le s \le f$. Soit un réel $\alpha \in ]0, 1[$.
   Pour chaque $n \in \mathbb{N}$, définissons l'ensemble mesurable :
   $$A_n = \{x \in X \mid f_n(x) \ge \alpha s(x) \}$$
   - Comme $(f_n)$ est une suite croissante, la suite d'ensembles $(A_n)$ est croissante : $A_n \subset A_{n+1}$.
   - De plus, pour tout $x$ où $s(x) > 0$, on a $\alpha s(x) < s(x) \le f(x) = \lim f_n(x)$. Donc il existe un rang à partir duquel $f_n(x) \ge \alpha s(x)$. Sur l'ensemble où $s(x) = 0$, $x \in A_1$. Par conséquent, $\bigcup_{n=1}^\infty A_n = X$.
   - Sur l'ensemble $A_n$, on a $f_n \ge \alpha s$. Donc, par positivité :
   $$\int_X f_n d\mu \ge \int_{A_n} f_n d\mu \ge \alpha \int_{A_n} s d\mu$$
   - Par propriété de continuité monotone ascendante de la mesure, puisque $A_n \uparrow X$ :
   $$\lim_{n \to \infty} \int_{A_n} s d\mu = \int_X s d\mu$$
   - On en déduit, en passant à la limite dans l'inégalité précédente :
   $$\lim_{n \to \infty} \int_X f_n d\mu \ge \alpha \int_X s d\mu$$
   - Cette inégalité est vraie pour tout $\alpha \in ]0, 1[$. En faisant tendre $\alpha$ vers $1$, on obtient :
   $$\lim_{n \to \infty} \int_X f_n d\mu \ge \int_X s d\mu$$

4. Conclusion de l'égalité : Cette dernière inégalité est vraie pour toute fonction étagée $s \le f$. Par définition de l'intégrale des fonctions mesurables positives comme le supremum des intégrales des fonctions étagées minorantes, on prend le supremum sur toutes les fonctions $s$ :
   $$\lim_{n \to \infty} \int_X f_n d\mu \ge \sup_{0 \le s \le f} \int_X s d\mu = \int_X f d\mu$$
   Les deux inégalités combinées prouvent formellement l'égalité.

## Applications en Physique, Logique et IA

En apprentissage statistique et en théorie de l'information, on calcule fréquemment des espérances d'une somme infinie de variables aléatoires positives, ou l'on étudie la limite de processus itératifs. Le théorème de convergence monotone est le pilier qui permet d'intervertir sans condition l'espérance mathématique (l'intégrale de Lebesgue) et la limite de ces processus monotones.

**Évaluation de fonctions de coût sous forme de séries :**
Dans le cadre de l'optimisation stochastique ou des développements en séries de Taylor de fonctions de perte (par exemple la cross-entropie évaluée sur des distributions), l'erreur attendue est souvent décomposable en une série de fonctions de risque partielles positives. Le TCM garantit que l'espérance de la perte globale est précisément la somme des espérances des pertes partielles, validant ainsi la convergence théorique de nombreux algorithmes d'apprentissage sur des espaces de grande dimension.
