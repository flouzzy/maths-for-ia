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

## Introduction Historique et Intuition

Le développement de l'intégrale de Lebesgue a été largement motivé par le besoin de disposer de théorèmes de passage à la limite plus robustes que ceux offerts par la théorie de Riemann. Le Théorème de Convergence Monotone, souvent appelé théorème de Beppo Levi, répond à cette exigence pour les suites croissantes de fonctions mesurables positives. L'idée géométrique fondamentale est qu'une limite croissante de fonctions voit l'aire sous sa courbe approchée arbitrairement près par les aires des fonctions de la suite, sans hypothèse de majoration globale (contrairement au théorème de convergence dominée).

## Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Énoncé du Théorème de Convergence Monotone (Beppo Levi)

> **Théorème :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
> Si la suite est croissante presque partout, c'est-à-dire :
> $$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \text{ p.p.}$$
> Alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable et :
> $$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

### Exemples Concrets Immédiats

**Exemple 1 : Limite infinie et aire non bornée.**
Soit $X = \mathbb{R}$ muni de la mesure de Lebesgue $\lambda$.
Posons $f_n = \chi_{[0, n]}$. La suite $(f_n)$ est croissante car $[0, n] \subset [0, n+1]$.
Pour tout $x$, $\lim_{n \to \infty} f_n(x) = \chi_{[0, +\infty[}(x) = f(x)$.
Calculons les intégrales :
$\int_\mathbb{R} f_n d\lambda = \lambda([0, n]) = n$.
Ainsi, $\lim_{n \to \infty} \int_\mathbb{R} f_n d\lambda = \lim_{n \to \infty} n = +\infty$.
Et d'autre part, $\int_\mathbb{R} f d\lambda = \lambda([0, +\infty[) = +\infty$.
L'égalité est bien vérifiée dans $[0, +\infty]$.

**Exemple 2 : Fonctions exponentielles tronquées.**
Soit $X = [0, 1]$ muni de la mesure de Lebesgue.
Posons $f_n(x) = x^n$. Pour $x \in [0, 1[$, la suite $(f_n(x))$ n'est *pas* croissante, elle est décroissante. Attention ! Le théorème ne s'applique pas directement à $(f_n)$ si on veut la limite. Pour appliquer Beppo Levi à des puissances, il faut inverser ou considérer les sommes partielles de séries.

Considérons plutôt la série géométrique : $S_n(x) = \sum_{k=0}^n x^k$.
Pour $x \in [0, 1[$, la suite de fonctions $S_n$ est croissante et positive.
$\lim_{n \to \infty} S_n(x) = \frac{1}{1-x}$.
Par le théorème de Beppo Levi, $\int_0^1 \frac{1}{1-x} dx = \lim_{n \to \infty} \int_0^1 \sum_{k=0}^n x^k dx = \lim_{n \to \infty} \sum_{k=0}^n \frac{1}{k+1} = +\infty$.

**Exemple 3 : Échec en cas d'absence de positivité ou croissance.**
Si on lâche l'hypothèse de croissance : $f_n = n \chi_{]0, 1/n]}$.
On a $f_n(x) \to 0$ pour tout $x > 0$, donc $f \equiv 0$ p.p.
$\int_\mathbb{R} f_n = 1$ pour tout $n$, donc $\lim \int f_n = 1$.
Cependant, $\int \lim f_n = \int 0 = 0$. Le théorème échoue. La croissance était cruciale.

### Corollaire (Sommation terme à terme)

> **Théorème :** Pour toute suite de fonctions mesurables positives $(u_n)_{n \in \mathbb{N}}$ de $X$ dans $[0, +\infty]$ :
> $$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$

*Preuve :* Il suffit d'appliquer le théorème de Beppo Levi à la suite des sommes partielles $S_N = \sum_{n=0}^N u_n$, qui est une suite croissante de fonctions mesurables positives.

**Exemple d'application du corollaire :**
Calculons l'intégrale $I = \int_0^1 \frac{-\ln(1-x)}{x} dx$.
On sait que pour $x \in [0, 1[$, $-\ln(1-x) = \sum_{n=1}^\infty \frac{x^n}{n}$.
Donc $\frac{-\ln(1-x)}{x} = \sum_{n=1}^\infty \frac{x^{n-1}}{n}$.
Les fonctions $u_n(x) = \frac{x^{n-1}}{n}$ sont mesurables et positives. Par le corollaire :
$I = \sum_{n=1}^\infty \int_0^1 \frac{x^{n-1}}{n} dx = \sum_{n=1}^\infty \left[ \frac{x^n}{n^2} \right]_0^1 = \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.

## Démonstration Complète du Théorème de Beppo Levi

1. **Existence de la limite et inégalité évidente :**
Comme $(f_n(x))$ est une suite croissante de $[0, +\infty]$, elle admet toujours une limite dans $[0, +\infty]$ pour chaque $x \in X$, notée $f(x)$. La fonction $f$ est mesurable en tant que limite (supremum dénombrable) de fonctions mesurables.
Par croissance de l'intégrale, puisque $f_n \le f$ pour tout $n \in \mathbb{N}$, on a :
$$\int_X f_n d\mu \le \int_X f d\mu$$
La suite numérique $(\int_X f_n d\mu)$ est croissante dans $[0, +\infty]$, elle admet donc une limite, et on déduit :
$$\lim_{n \to \infty} \int_X f_n d\mu \le \int_X f d\mu$$

2. **Inégalité inverse (minoration par des fonctions simples) :**
Pour prouver l'inégalité inverse, il suffit, par définition de l'intégrale de Lebesgue pour les fonctions positives, de montrer que pour toute fonction étagée (simple) positive $s$ telle que $0 \le s \le f$, on a :
$$\int_X s d\mu \le \lim_{n \to \infty} \int_X f_n d\mu$$
Fixons un tel $s$ et choisissons une constante $\alpha \in ]0, 1[$.
Définissons les ensembles $A_n = \{x \in X \mid f_n(x) \ge \alpha s(x) \}$.
Puisque $(f_n)$ est croissante, la suite d'ensembles $(A_n)$ est emboîtée croissante : $A_n \subset A_{n+1}$.
De plus, si $s(x) = 0$, $x \in A_n$ de façon triviale. Si $s(x) > 0$, alors $\alpha s(x) < s(x) \le f(x) = \lim f_n(x)$. Ainsi, il existe un certain rang à partir duquel $f_n(x) > \alpha s(x)$, ce qui implique $x \in A_n$.
Par conséquent, $\bigcup_{n \in \mathbb{N}} A_n = X$.

3. **Passage à la limite sur la mesure :**
On peut écrire la minoration suivante :
$$\int_X f_n d\mu \ge \int_{A_n} f_n d\mu \ge \int_{A_n} \alpha s d\mu = \alpha \int_{A_n} s d\mu$$
La fonction $s$ étant étagée, on peut l'écrire $s = \sum_{i=1}^k c_i \chi_{E_i}$.
L'intégrale sur $A_n$ s'écrit $\int_{A_n} s d\mu = \sum_{i=1}^k c_i \mu(E_i \cap A_n)$.
Puisque $(A_n)$ est une suite croissante d'ensembles de limite $X$, la continuité croissante de la mesure $\mu$ donne $\lim_{n \to \infty} \mu(E_i \cap A_n) = \mu(E_i \cap X) = \mu(E_i)$.
Ainsi, $\lim_{n \to \infty} \int_{A_n} s d\mu = \int_X s d\mu$.
En passant à la limite dans notre minoration, on obtient :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \alpha \int_X s d\mu$$

4. **Conclusion de la preuve :**
Cette inégalité étant vraie pour tout $\alpha \in ]0, 1[$, en faisant tendre $\alpha$ vers 1, il vient :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \int_X s d\mu$$
Cette minoration étant valide pour toute fonction étagée $s$ inférieure ou égale à $f$, on obtient par passage au supremum :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \sup_{0 \le s \le f} \int_X s d\mu = \int_X f d\mu$$
Les deux inégalités établissent le théorème. $\blacksquare$

## Applications en Intelligence Artificielle et Optimisation

En apprentissage statistique, on manipule couramment des espérances mathématiques, qui sont des intégrales de Lebesgue par rapport à une mesure de probabilité $\mathbb{P}$.
Le théorème de convergence monotone est particulièrement utile pour démontrer la convergence des processus de minimisation du risque empirique, ou lors de l'étude asymptotique des bornes de généralisation.
Par exemple, lors de la construction de noyaux (kernels) reproduisants définis par des séries entières $k(x, y) = \sum_{n=0}^\infty a_n (x \cdot y)^n$ avec $a_n \ge 0$, le théorème de Beppo Levi garantit que l'intégration du noyau par rapport à n'importe quelle mesure (pour évaluer le risque) commute de manière inconditionnelle avec la sommation infinie, permettant l'analyse dimensionnelle infinie des machines à vecteurs de support (SVM).

## Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]], [[Jalon 63 (Définition axiomatique d'une mesure).md]]
- **Concepts Futurs dépendants :** [[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]], [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]
