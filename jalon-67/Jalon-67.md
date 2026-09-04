---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon-66.md]]"
next: "[[Jalon-68.md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo Levi)

## 1. Émergence du Théorème de Beppo Levi

La théorie de l'intégration au sens de Riemann se heurte à des difficultés majeures concernant le passage à la limite sous le signe intégral. Si l'on dispose d'une suite de fonctions intégrables $(f_n)_{n \in \mathbb{N}}$ convergeant simplement vers une fonction $f$, rien ne garantit en général que $f$ soit intégrable, ni que la suite des intégrales converge vers l'intégrale de la limite, sans requérir la condition restrictive de convergence uniforme.

Historiquement, cette impasse a motivé Henri Lebesgue puis le mathématicien italien Beppo Levi à formuler une nouvelle théorie de l'intégration où les opérations de limite et d'intégration commutent de manière bien plus souple, pourvu que la suite de fonctions croisse. Le théorème de convergence monotone garantit ainsi la conservation de la masse lors d'accumulations progressives, un résultat indispensable dans le traitement des séries de fonctions et en théorie des probabilités.

## 2. Théorème de Convergence Monotone et Exemples Immédiats

### Théorème de Beppo Levi

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
Si la suite est croissante presque partout, c'est-à-dire :
$$ \forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \quad \text{presque partout} $$
Alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable et :
$$ \int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu $$

**Corollaire (Sommation terme à terme) :**
Pour toute suite de fonctions mesurables positives $(u_n)_{n \in \mathbb{N}}$ :
$$ \int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu $$

### Exemples Calculatoires Immédiats

**Exemple 1 : L'intégrale de la série géométrique**
Considérons l'espace mesuré $([0,1[, \mathcal{B}([0,1[), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Soit $f_n(x) = \sum_{k=0}^n x^k$. Les fonctions $f_n$ sont mesurables et positives. La suite $(f_n)_{n \in \mathbb{N}}$ est manifestement croissante puisque $x^k \ge 0$. La limite simple est $f(x) = \sum_{k=0}^\infty x^k = \frac{1}{1-x}$.
D'après le théorème de Beppo Levi :
$$ \int_0^1 \frac{1}{1-x} dx = \int_0^1 \lim_{n \to \infty} \sum_{k=0}^n x^k dx = \lim_{n \to \infty} \sum_{k=0}^n \int_0^1 x^k dx $$
Le calcul donne :
$$ \int_0^1 x^k dx = \frac{1}{k+1} $$
Ainsi, on retrouve rigoureusement :
$$ \int_0^1 \frac{1}{1-x} dx = \lim_{n \to \infty} \sum_{k=0}^n \frac{1}{k+1} = +\infty $$

**Cas pathologique : Perte de la monotonie**
Prenons $f_n(x) = n \cdot \mathbf{1}_{]0, \frac{1}{n}]}(x)$ sur $]0, 1]$. On a $\lim_{n \to \infty} f_n(x) = 0$ pour tout $x \in ]0, 1]$.
$$ \lim_{n \to \infty} \int_0^1 f_n(x) dx = \lim_{n \to \infty} 1 = 1 $$
Mais :
$$ \int_0^1 \lim_{n \to \infty} f_n(x) dx = \int_0^1 0 dx = 0 $$
Le théorème de Beppo Levi ne s'applique pas car la suite $(f_n)$ n'est pas croissante. Ce contre-exemple illustre le rôle crucial de l'hypothèse de croissance.

## 3. Démonstration Rigoureuse du Théorème de Convergence Monotone

1. **Existence et mesurabilité de la limite :**
Comme $(f_n(x))$ est une suite croissante à valeurs dans $[0, +\infty]$, elle admet toujours une limite dans $[0, +\infty]$ pour chaque $x \in X$. La fonction limite $f = \sup_{n} f_n$ est mesurable en tant que supremum dénombrable de fonctions mesurables.

2. **Majoration évidente :**
Par hypothèse, $f_n \le f$ pour tout $n$. Par croissance de l'intégrale des fonctions mesurables positives :
$$ \int_X f_n d\mu \le \int_X f d\mu $$
En passant à la limite (la suite des intégrales étant croissante, elle admet une limite dans $[0, +\infty]$) :
$$ \lim_{n \to \infty} \int_X f_n d\mu \le \int_X f d\mu $$

3. **Minoration fondamentale :**
Pour établir l'inégalité réciproque, soit $s$ une fonction étagée mesurable telle que $0 \le s \le f$. Soit $\alpha \in ]0, 1[$.
Définissons les ensembles mesurables :
$$ A_n = \{x \in X \mid f_n(x) \ge \alpha s(x)\} $$
Puisque $(f_n)$ est croissante, la suite d'ensembles $(A_n)$ est emboîtée croissante : $A_n \subset A_{n+1}$.
De plus, puisque $\lim f_n(x) = f(x)$ et que pour tout $x$ où $s(x) > 0$, on a $\alpha s(x) < f(x)$, il vient $\bigcup_{n \ge 0} A_n = X$.
Sur $A_n$, nous avons $f_n \ge \alpha s$, ce qui implique :
$$ \int_X f_n d\mu \ge \int_{A_n} f_n d\mu \ge \alpha \int_{A_n} s d\mu $$
L'application $\nu : A \mapsto \int_A s d\mu$ est une mesure sur $\mathcal{F}$. Par le théorème de continuité séquentielle monotone croissante des mesures :
$$ \lim_{n \to \infty} \int_{A_n} s d\mu = \int_X s d\mu $$
Ainsi, en passant à la limite quand $n \to \infty$ dans notre inégalité :
$$ \lim_{n \to \infty} \int_X f_n d\mu \ge \alpha \int_X s d\mu $$
Cette relation étant vraie pour tout $\alpha \in ]0, 1[$, on peut faire tendre $\alpha$ vers $1$ pour obtenir :
$$ \lim_{n \to \infty} \int_X f_n d\mu \ge \int_X s d\mu $$

4. **Conclusion par la définition de l'intégrale :**
Par définition de l'intégrale de $f$, qui est le supremum des intégrales des fonctions étagées positives majorées par $f$, on a :
$$ \sup_{0 \le s \le f, \, s \text{ étagée}} \int_X s d\mu = \int_X f d\mu $$
D'où l'on déduit la seconde inégalité :
$$ \lim_{n \to \infty} \int_X f_n d\mu \ge \int_X f d\mu $$
Les deux inégalités établissent le théorème de convergence monotone.

## 4. Applications en Processus Stochastiques et Modèles d'Apprentissage

Le théorème de Beppo Levi garantit la sécurité des opérations d'interversion entre séries et intégrales.

En **théorie des probabilités**, il est l'outil fondamental pour prouver le lemme de Borel-Cantelli, qui permet d'étudier la survenue d'une infinité d'événements. Il permet d'intervertir espérance et sommation infinie pour des variables aléatoires positives, fondamental pour le calcul de l'espérance des processus de comptage, comme le processus de Poisson.

En **intelligence artificielle et apprentissage statistique**, l'analyse des risques (Risk Bounds) repose souvent sur l'intégration par rapport à la distribution de probabilité inconnue des données. Lorsque l'on étudie la limite d'une suite de fonctions de perte empirique croissante (ou la minimisation d'une suite décroissante, corollaire duel), le passage à la limite sous l'espérance est justifié par Beppo Levi. De même, en théorie des noyaux (Kernel Methods), l'évaluation d'un produit scalaire dans un RKHS par la somme de ses caractéristiques propres requiert l'inversion rigoureuse d'une somme infinie et de l'intégration, scellée par ce théorème.
