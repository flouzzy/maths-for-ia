---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[jalon-66/Jalon-66.md]]"
next: "[[jalon-68/Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo Levi)

## 1. Genèse et intuition de l'intégration des limites

L'intégration au sens de Riemann (XIXe siècle) souffrait d'une lacune fondamentale : le passage à la limite sous le signe intégral n'était garanti que sous l'hypothèse très forte de la convergence uniforme. Les physiciens et les probabilistes avaient besoin d'une théorie plus souple pour manipuler des séries de fonctions ou des suites de variables aléatoires où la convergence uniforme fait souvent défaut.

En 1902, Henri Lebesgue introduit sa théorie de la mesure et de l'intégration, qui déplace l'attention de l'axe des abscisses (partitionnement du domaine de Riemann) vers l'axe des ordonnées (fonctions étagées mesurables). Dans ce nouveau paradigme, le mathématicien italien Beppo Levi formule en 1906 ce qui deviendra l'un des piliers de l'analyse fonctionnelle : le Théorème de Convergence Monotone. Ce théorème stipule que pour une suite croissante de fonctions positives, l'intégrale de la limite est toujours égale à la limite des intégrales. L'intégration de Lebesgue permet à l'aire sous une courbe de s'accumuler de manière monotone sans exiger des propriétés topologiques globales contraignantes, validant l'interversion dans les calculs de probabilités et d'analyse harmonique.

## 2. Définitions, Théorèmes et Exemples

### Théorème de Convergence Monotone (Beppo Levi)

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.

**Énoncé formel :**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables définies sur $X$ et à valeurs dans $\overline{\mathbb{R}}^+ = [0, +\infty]$.
On suppose que la suite est croissante presque partout :
$$\forall n \in \mathbb{N}, \quad 0 \le f_n(x) \le f_{n+1}(x) \quad \text{pour } \mu\text{-presque tout } x \in X$$
Alors, la fonction limite $f(x) = \lim_{n \to \infty} f_n(x)$ (qui existe dans $[0, +\infty]$) est mesurable et vérifie :
$$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

**Exemple concret immédiat :**
Plaçons-nous sur $X = [0, 1)$ muni de la mesure de Lebesgue $\lambda$.
Considérons la suite de fonctions $f_n(x) = \sum_{k=1}^n x^{k-1}$.
Pour tout $x \in [0, 1)$, $f_n(x) \ge 0$ et $f_{n+1}(x) - f_n(x) = x^n \ge 0$. La suite $(f_n)$ est donc bien positive et croissante.
La limite simple est la somme de la série géométrique : $f(x) = \lim_{n \to \infty} f_n(x) = \frac{1}{1-x}$.
Calculons l'intégrale de chaque terme de la suite :
$$\int_0^1 f_n(x) d\lambda(x) = \int_0^1 \sum_{k=1}^n x^{k-1} dx = \sum_{k=1}^n \int_0^1 x^{k-1} dx = \sum_{k=1}^n \left[ \frac{x^k}{k} \right]_0^1 = \sum_{k=1}^n \frac{1}{k}$$
D'après le théorème de convergence monotone, nous pouvons affirmer :
$$\int_0^1 \frac{1}{1-x} dx = \lim_{n \to \infty} \sum_{k=1}^n \frac{1}{k} = +\infty$$
Ce résultat relie l'intégrale de la fonction pôle à la divergence de la série harmonique.

### Corollaire de l'intégration terme à terme

**Énoncé formel :**
Soit $(u_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables positives (c'est-à-dire de $X$ dans $[0, +\infty]$).
Alors :
$$\int_X \left( \sum_{n=0}^{\infty} u_n \right) d\mu = \sum_{n=0}^{\infty} \int_X u_n d\mu$$

**Exemple concret immédiat :**
Soit $X = \mathbb{R}^+$ et $u_n(x) = e^{-x} \frac{x^n}{n!}$. Chaque $u_n$ est positive et mesurable.
La somme de la série est $\sum_{n=0}^{\infty} e^{-x} \frac{x^n}{n!} = e^{-x} e^x = 1$.
Intégrons la somme :
$$\int_0^{+\infty} \left( \sum_{n=0}^{\infty} e^{-x} \frac{x^n}{n!} \right) dx = \int_0^{+\infty} 1 dx = +\infty$$
D'après le corollaire, la somme des intégrales doit donner le même résultat. Effectivement, l'intégrale de $u_n(x)$ est liée à la fonction Gamma d'Euler :
$\int_0^{+\infty} x^n e^{-x} dx = \Gamma(n+1) = n!$.
Donc $\int_0^{+\infty} u_n(x) dx = \frac{n!}{n!} = 1$.
Et la somme de ces intégrales est $\sum_{n=0}^{\infty} 1 = +\infty$.

**Cas limites et contre-exemples :**
La positivité (ou l'existence d'une minoration intégrable) est strictement nécessaire.
Si on relâche cette hypothèse, le théorème s'effondre.
Considérons sur $X = \mathbb{R}$ muni de la mesure de Lebesgue, la suite $f_n(x) = \frac{1}{n} \mathbf{1}_{[0, n]}(x)$.
Les fonctions $f_n$ sont mesurables et positives. La suite converge simplement vers la fonction nulle : $\lim_{n \to \infty} f_n(x) = 0$.
L'intégrale de la limite est $\int_\mathbb{R} 0 dx = 0$.
Cependant, pour chaque $n$, $\int_\mathbb{R} f_n(x) dx = \frac{1}{n} \times n = 1$.
La limite des intégrales est $1$, ce qui est différent de $0$.
Pourquoi le théorème de Beppo Levi ne s'applique-t-il pas ? Parce que la suite n'est **pas croissante**. En effet, pour $x \in (0, 1)$, $f_1(x) = 1$ et $f_2(x) = 1/2$, donc $f_2(x) < f_1(x)$.

## 3. Démonstrations

### Preuve du Théorème de Convergence Monotone

1. **Existence et mesurabilité de la limite :**
Comme pour $\mu$-presque tout $x$, la suite numérique $(f_n(x))$ est croissante et à valeurs dans $[0, +\infty]$, elle admet une limite dans $\overline{\mathbb{R}}^+$. Posons $f(x) = \sup_{n \in \mathbb{N}} f_n(x) = \lim_{n \to \infty} f_n(x)$.
Étant la limite simple (supremum) d'une suite dénombrable de fonctions mesurables, $f$ est elle-même une fonction mesurable.

2. **Inégalité directe ($\ge$) :**
Puisque $f_n \le f_{n+1}$, par définition du supremum, nous avons $f_n(x) \le f(x)$ pour tout $n \in \mathbb{N}$ et $\mu$-presque tout $x$.
L'intégrale étant un opérateur croissant (propriété de base de l'intégrale de Lebesgue pour les fonctions positives), nous déduisons :
$$\int_X f_n d\mu \le \int_X f d\mu$$
La suite numérique $\left( \int_X f_n d\mu \right)$ est croissante et majorée par $\int_X f d\mu$. Elle admet donc une limite, et par passage à la limite :
$$\lim_{n \to \infty} \int_X f_n d\mu \le \int_X f d\mu$$

3. **Inégalité réciproque ($\le$) via l'approximation par des fonctions étagées :**
C'est le cœur de la preuve. Soit $s$ une fonction étagée mesurable telle que $0 \le s \le f$.
Par définition, $s = \sum_{i=1}^k c_i \mathbf{1}_{A_i}$ où les $c_i > 0$ et les $A_i$ forment une partition mesurable.
Fixons un réel arbitraire $c \in ]0, 1[$.
Pour chaque entier $n$, définissons l'ensemble :
$$E_n = \{x \in X \mid f_n(x) \ge c \cdot s(x)\}$$
- Les $E_n$ sont des ensembles mesurables car $f_n$ et $s$ sont mesurables.
- Puisque la suite $(f_n)$ est croissante, la suite d'ensembles $(E_n)$ est emboîtée croissante : $E_n \subseteq E_{n+1}$.
- Montrons que $\bigcup_{n \in \mathbb{N}} E_n = X$ (à un ensemble de mesure nulle près). Pour un point $x$ où $f(x) = \lim f_n(x)$, si $f(x) > 0$, alors $c \cdot s(x) < s(x) \le f(x)$. Par définition de la limite, il existe un rang $N$ à partir duquel $f_N(x) > c \cdot s(x)$, donc $x \in E_N$. Si $f(x) = 0$, alors $s(x) = 0$, et pour tout $n$, $f_n(x) \ge 0 = c \cdot s(x)$, donc $x \in E_0$. L'union couvre bien $X$ presque partout.

Sur l'ensemble $E_n$, nous avons $f_n \ge c \cdot s$. Par positivité de $f_n$, nous pouvons écrire :
$$\int_X f_n d\mu \ge \int_{E_n} f_n d\mu \ge \int_{E_n} c \cdot s d\mu = c \int_{E_n} s d\mu$$
Remplaçons $s$ par sa forme explicite :
$$\int_{E_n} s d\mu = \sum_{i=1}^k c_i \mu(A_i \cap E_n)$$
Or, la suite d'ensembles $(A_i \cap E_n)_{n \in \mathbb{N}}$ est croissante et tend vers $A_i \cap X = A_i$. Par le théorème de continuité séquentielle croissante de la mesure $\mu$, nous avons $\lim_{n \to \infty} \mu(A_i \cap E_n) = \mu(A_i)$.
En passant à la limite $n \to \infty$ dans l'inégalité, on obtient :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge c \sum_{i=1}^k c_i \lim_{n \to \infty} \mu(A_i \cap E_n) = c \sum_{i=1}^k c_i \mu(A_i) = c \int_X s d\mu$$
Cette inégalité est valable pour tout $c \in ]0, 1[$. En faisant tendre $c$ vers $1$ (les deux termes étant indépendants de $c$), il vient :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \int_X s d\mu$$
Enfin, cette dernière inégalité est vérifiée pour **toute** fonction étagée mesurable $s$ telle que $0 \le s \le f$. Par définition de l'intégrale de Lebesgue d'une fonction positive (qui est le supremum des intégrales de toutes les fonctions étagées minorant la fonction) :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \sup_{0 \le s \le f} \int_X s d\mu = \int_X f d\mu$$

4. **Conclusion :**
Les deux inégalités $\le$ et $\ge$ établissent l'égalité stricte :
$$\int_X f d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

## 4. Applications en Physique, Logique et Intelligence Artificielle

L'intégration au sens de Lebesgue et les théorèmes d'interversion trouvent des applications directes là où des structures mathématiques manipulent de la mesure, de la probabilité, ou des processus infinis.

1. **Réseaux de Neurones et processus d'apprentissage stochastique :**
Dans la théorie du PAC (Probably Approximately Correct) learning, le risque espéré (l'erreur généralisée) d'un modèle d'IA s'exprime comme une intégrale du risque sous une mesure de probabilité inconnue. Lorsque l'on construit un méta-algorithme (comme le Boosting) qui accumule itérativement des classifieurs faibles (ajout monotone de fonctions de coût positif sur l'ensemble d'entraînement), le théorème de convergence monotone assure de manière stricte que le risque de l'ensemble (la série infinie) converge formellement vers la somme des risques individuels mesurés. Le T.C.M permet de valider le passage de limites à l'infini lors de l'estimation de l'erreur empirique, sans exiger de propriétés topologiques fortes comme la compacité stricte.

2. **Thermodynamique Statistique et Processus de Markov :**
Dans les Modèles de Markov Cachés (HMM) utilisés en traitement automatique des langues, la probabilité totale d'une séquence d'observations s'obtient en marginalisant sur une infinité d'états latents. Ces probabilités sont modélisées par des sommes infinies d'intégrales positives. Le TCM permet d'inverser sans condition les sommes de probabilités et l'espérance, un procédé indispensable dans la preuve de convergence de l'algorithme d'Espérance-Maximisation (EM) qui maximise itérativement une borne inférieure (Evidence Lower Bound - ELBO) strictement croissante.
