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

L'élaboration de la théorie de la mesure et de l'intégration de Lebesgue visait originellement à s'affranchir des limitations pathologiques de l'intégrale de Riemann, en particulier concernant le passage à la limite sous le signe intégral. Historiquement, le passage à la limite pour des suites de fonctions non uniformément convergentes constituait une faille béante de la théorie classique. Le théorème de convergence monotone, démontré par Beppo Levi au début du XXe siècle, offre une résolution magistrale à ce problème : il stipule que pour toute suite croissante de fonctions mesurables positives, l'intégrale de la limite est invariablement égale à la limite des intégrales.

Géométriquement, si l'on considère une suite de courbes mesurables positives dont l'ordonnée en chaque point croît avec l'indice de la suite, l'aire sous la courbe limite est exactement la limite des aires sous chaque courbe de la suite. Ce résultat de stabilité structurelle de l'intégrale de Lebesgue est le premier grand théorème d'interversion, ouvrant la voie à l'intégrabilité des séries de fonctions et préparant le terrain pour le théorème de convergence dominée.

## Définitions, Théorèmes et Exemples Concrets

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré formel.

### Énoncé du Théorème de Convergence Monotone

> **Théorème de Convergence Monotone (Beppo Levi) :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $\overline{\mathbb{R}}^+ = [0, +\infty]$.
> On suppose que la suite est **croissante presque partout** par rapport à la mesure $\mu$, c'est-à-dire :
> $$\forall n \in \mathbb{N}, \quad f_n(x) \le f_{n+1}(x) \text{ pour } \mu\text{-presque tout } x \in X$$
> Alors, la fonction limite $f(x) = \lim_{n \to \infty} f_n(x)$ (qui existe dans $\overline{\mathbb{R}}^+$) est mesurable, et on a l'égalité fondamentale :
> $$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

### Anatomie des variables et conditions
*   $X$ : Un ensemble fondamental abstrait constituant l'espace de base.
*   $\mathcal{F}$ : Une tribu (ou $\sigma$-algèbre) sur $X$, garantissant que les sous-ensembles mesurés sont bien formés vis-à-vis des opérations de limite infinie.
*   $\mu$ : Une mesure positive définie sur $\mathcal{F}$, permettant d'évaluer la taille des ensembles.
*   $f_n : X \to [0, +\infty]$ : Une suite de fonctions mesurables positives (l'image peut inclure $+\infty$).
*   Croissance p.p. : La condition $f_n(x) \le f_{n+1}(x)$ peut être violée sur un ensemble de mesure $\mu$ nulle sans altérer le résultat intégral.

### Exemples d'application immédiats et cas limites

**Exemple 1 : Suite de fonctions puissances sur $[0,1]$**
Soit l'espace mesuré $([0,1], \mathcal{B}([0,1]), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Considérons la suite $f_n(x) = 1 - x^n$.
Pour tout $x \in [0,1]$, on a $x^{n+1} \le x^n$, donc $-x^{n+1} \ge -x^n$, ce qui implique $f_n(x) \le f_{n+1}(x)$.
La suite est mesurable, positive et croissante. Sa limite ponctuelle est $f(x) = 1$ si $x \in [0,1[$ et $f(1) = 0$.
Calculons les intégrales de la suite :
$$\int_0^1 f_n(x) d\lambda(x) = \int_0^1 (1 - x^n) dx = \left[ x - \frac{x^{n+1}}{n+1} \right]_0^1 = 1 - \frac{1}{n+1}$$
La limite des intégrales est $\lim_{n \to \infty} \left( 1 - \frac{1}{n+1} \right) = 1$.
L'intégrale de la limite $f$ (qui vaut $1$ presque partout, car le singleton $\{1\}$ est de mesure nulle) est :
$$\int_0^1 f(x) d\lambda(x) = \int_0^1 1 \, dx = 1$$
Les deux valeurs coïncident, illustrant la validité du théorème.

**Exemple 2 : Fonctions indicatrices de segments concentriques**
Considérons $f_n = \chi_{[-n, n]}$ sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$.
Clairement, $[-n, n] \subset [-(n+1), n+1]$, donc $f_n \le f_{n+1}$.
La limite est $f(x) = \lim_{n \to \infty} \chi_{[-n, n]}(x) = \chi_{\mathbb{R}}(x) = 1$.
On a $\int_\mathbb{R} f_n d\lambda = \lambda([-n, n]) = 2n$.
La limite de ces intégrales est $\lim_{n \to \infty} 2n = +\infty$.
L'intégrale de la limite est $\int_\mathbb{R} 1 d\lambda = +\infty$.
L'égalité est vérifiée dans $\overline{\mathbb{R}}^+$.

**Exemple 3 : Échec sans la condition de positivité (translation de la bosse glissante vers le bas)**
Si l'on retire la condition $f_n \ge 0$, le théorème peut échouer.
Soit $f_n(x) = - \frac{1}{n} \chi_{[0, n]}(x)$.
La suite croît vers la fonction nulle $f(x) = 0$, d'intégrale $0$.
Pourtant, $\int_\mathbb{R} f_n d\lambda = - \frac{1}{n} \times n = -1$.
La limite des intégrales est $-1$, qui n'est pas égale à $0$. La positivité (au moins à partir d'un certain rang ou par minoration par une fonction intégrable, menant à Fatou) est cruciale.

**Exemple 4 : Échec sans la condition de croissance (bosse glissante)**
Considérons $f_n = n \chi_{]0, 1/n[}$. Ces fonctions sont positives mais non croissantes en $n$.
La limite ponctuelle est $f(x) = 0$ pour tout $x \in \mathbb{R}$, d'intégrale $0$.
Cependant, l'intégrale de $f_n$ est $n \times \frac{1}{n} = 1$ pour tout $n$.
La limite des intégrales est $1$, différente de l'intégrale de la limite $0$. Le manque de croissance viole les hypothèses de Beppo Levi.

**Exemple 5 : La mesure de comptage et les séries**
Soit $X = \mathbb{N}$ muni de la tribu discrète $\mathcal{P}(\mathbb{N})$ et de la mesure de comptage $\mu$.
Toute fonction positive $u: \mathbb{N} \to \mathbb{R}^+$ correspond à une suite $(u_k)$. Son intégrale par rapport à $\mu$ est exactement la somme de la série $\sum_{k=0}^\infty u_k$.
Si l'on définit la suite de fonctions croissantes $f_n(k) = \sum_{j=0}^n v_j(k)$ avec $v_j \ge 0$, l'application de Beppo Levi fournit directement l'autorisation de permuter une limite et une série, ouvrant le domaine de la sommation terme à terme de séries à termes positifs.

### Corollaire de sommation terme à terme

> **Théorème (Sommation à termes positifs) :**
> Pour toute suite de fonctions mesurables **positives** $(u_n)_{n \in \mathbb{N}}$ :
> $$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$

## Démonstrations

### Démonstration du Théorème de Beppo Levi

**1. Continuité monotone des limites mesurables :**
La suite $(f_n(x))$ étant à valeurs dans $[0, +\infty]$ et croissante, elle admet nécessairement une limite dans $[0, +\infty]$ en tout point $x$ (le suprémum de ses valeurs). Le passage à la limite supérieure d'une suite de fonctions mesurables engendre une fonction limite mesurable, validant la définition formelle de l'intégrale $\int_X f d\mu$.

**2. Obtention de l'inégalité de majoration par croissance de l'intégrale :**
Par hypothèse, $\forall n \in \mathbb{N}$, pour $\mu$-presque tout $x$, $f_n(x) \le f_{n+1}(x) \le f(x)$.
La linéarité et la croissance de l'intégrale de Lebesgue garantissent que :
$$\int_X f_n d\mu \le \int_X f_{n+1} d\mu \le \int_X f d\mu$$
La suite de nombres réels étendus $\left( \int_X f_n d\mu \right)$ est donc croissante et majorée par $\int_X f d\mu$. Elle admet par conséquent une limite, et on obtient l'inégalité évidente :
$$\lim_{n \to \infty} \int_X f_n d\mu \le \int_X f d\mu$$

**3. Obtention de l'inégalité inverse (le cœur de la preuve) :**
Pour établir l'inégalité inverse, nous devons manipuler des fonctions étagées. Par définition de l'intégrale de Lebesgue pour les fonctions positives :
$$\int_X f d\mu = \sup \left\{ \int_X s d\mu \mid s \text{ étagée mesurable }, 0 \le s \le f \right\}$$
Soit $s$ une telle fonction étagée vérifiant $0 \le s \le f$.
Introduisons un coefficient d'atténuation $\alpha \in ]0, 1[$.
Définissons la suite d'ensembles mesurables :
$$A_n = \{x \in X \mid f_n(x) \ge \alpha s(x) \}$$
Puisque la suite $(f_n)$ est croissante, il s'ensuit que la suite d'ensembles $(A_n)$ est une suite croissante d'ensembles ($A_n \subset A_{n+1}$).
De plus, pour tout $x \in X$ tel que $f(x) > 0$, comme $f_n(x) \to f(x)$ et $\alpha < 1$, il existera nécessairement un rang $N$ tel que $f_n(x) \ge \alpha f(x) \ge \alpha s(x)$ pour tout $n \ge N$. Ainsi, l'union des ensembles $A_n$ recouvre l'espace entier (à un ensemble de mesure nulle près si $s=0$, ce qui est trivial), soit $\bigcup_{n \in \mathbb{N}} A_n = X$.

En se restreignant à $A_n$, on exploite la positivité des fonctions :
$$\int_X f_n d\mu \ge \int_{A_n} f_n d\mu \ge \int_{A_n} \alpha s d\mu = \alpha \int_X s \chi_{A_n} d\mu$$
Soit la fonction étagée $s = \sum_{i=1}^k c_i \chi_{E_i}$.
L'intégrale devient :
$$\int_X s \chi_{A_n} d\mu = \sum_{i=1}^k c_i \mu(E_i \cap A_n)$$
Par la propriété de continuité croissante de la mesure $\mu$, puisque $E_i \cap A_n$ croît vers $E_i \cap X = E_i$, nous avons :
$$\lim_{n \to \infty} \mu(E_i \cap A_n) = \mu(E_i)$$
Par conséquent, en passant à la limite lorsque $n \to \infty$ dans l'inégalité de l'intégrale :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \alpha \sum_{i=1}^k c_i \mu(E_i) = \alpha \int_X s d\mu$$

**4. Conclusion et passage au supremum :**
L'inégalité précédente, $\lim_{n \to \infty} \int_X f_n d\mu \ge \alpha \int_X s d\mu$, est valide pour tout $\alpha \in ]0, 1[$.
En faisant tendre le paramètre $\alpha$ vers $1$, il vient :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \int_X s d\mu$$
Cette minoration étant vérifiée pour toute fonction étagée $s$ telle que $0 \le s \le f$, on obtient en passant au suprémum sur l'ensemble de ces fonctions étagées :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \sup_{0 \le s \le f} \int_X s d\mu = \int_X f d\mu$$
L'obtention des deux inégalités contradictoires prouve l'égalité absolue :
$$\lim_{n \to \infty} \int_X f_n d\mu = \int_X f d\mu$$

### Démonstration du Corollaire de Sommation

Définissons les sommes partielles de la série par $f_N = \sum_{n=0}^N u_n$.
Chaque fonction $u_n$ étant positive et mesurable, les sommes partielles $f_N$ sont mesurables et positives.
De plus, $f_{N+1} - f_N = u_{N+1} \ge 0$, ce qui prouve que la suite $(f_N)_{N \in \mathbb{N}}$ est croissante.
On peut lui appliquer directement le théorème de Beppo Levi :
$$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \int_X \left( \lim_{N \to \infty} f_N \right) d\mu = \lim_{N \to \infty} \int_X f_N d\mu$$
Par linéarité finie de l'intégrale, on a :
$$\lim_{N \to \infty} \int_X \left( \sum_{n=0}^N u_n \right) d\mu = \lim_{N \to \infty} \sum_{n=0}^N \int_X u_n d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$
Ce qui démontre la légitimité de l'inversion intégrale-série pour des termes positifs.

## Applications en Physique, Logique et Intelligence Artificielle

Dans la théorie moderne de l'apprentissage statistique et du Machine Learning, les processus stochastiques sous-jacents se formalisent par des espérances mathématiques, qui ne sont rien d'autre que des intégrales de Lebesgue relativement à une mesure de probabilité $\mathbb{P}$.

L'optimisation des fonctions de perte (loss functions) implique souvent d'étudier la convergence de risques empiriques vers un risque d'espérance lorsque le nombre de données tend vers l'infini, ou d'exprimer ces coûts via des décompositions en séries (ex. développements de Taylor de l'entropie croisée, ou expansions de noyaux en dimension infinie, RKHS).

Le théorème de Beppo Levi, et son corollaire pour les séries à termes positifs, permet aux algorithmes de garantir théoriquement que la sommation infinie de coûts d'erreurs locaux est strictement équivalente à l'espérance de l'erreur globale. Par exemple, dans les processus de Poisson modélisant des flux d'arrivées asynchrones de données, la sommation des probabilités d'événements infinitésimaux positifs peut être légitimement intervertie avec l'intégrale temporelle, garantissant que les estimateurs stochastiques d'intensité convergent de manière mathématiquement solide sans exiger une convergence uniforme, souvent introuvable en pratique à cause du bruit stochastique résiduel dans la modélisation.
