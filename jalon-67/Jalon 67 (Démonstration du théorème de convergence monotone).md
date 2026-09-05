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

## 1. Introduction Théorique au Passage à la Limite

L'un des problèmes fondamentaux de l'analyse est de déterminer les conditions sous lesquelles la limite d'une suite d'intégrales est égale à l'intégrale de la limite. Dans le cadre de l'intégration de Riemann, cette interversion nécessite des hypothèses restrictives telles que la convergence uniforme. La théorie de la mesure de Lebesgue apporte une réponse élégante et minimale à ce problème avec le théorème de convergence monotone (ou théorème de Beppo Levi), qui stipule que la croissance de la suite suffit pour garantir l'interversion.

### Exemples Concrets Immédiats

1. **Suite stationnaire :** Soit $f_n(x) = x^2$ pour tout $n$. La suite est trivialement croissante ($f_n \le f_{n+1}$). La limite est $f(x) = x^2$. L'intégrale sur $[0, 1]$ est constante à $1/3$, et sa limite est bien $1/3$.
2. **Suite croissante sur un ensemble de mesure nulle :** Soit $f_n = \mathbf{1}_{\{0, 1/n, 2/n, \dots, 1\}}$. L'intégrale de chaque $f_n$ est $0$ car il s'agit d'un nombre fini de points. La limite $f$ vaut $1$ sur les rationnels, dont la mesure de Lebesgue est $0$. L'intégrale de la limite est $0$.
3. **Masse s'échappant à l'infini (Contre-exemple sans croissance) :** Soit $f_n(x) = n \mathbf{1}_{]0, 1/n[}$. $f_n \ge 0$, $\int f_n = 1$. $\lim f_n = 0$. $\int \lim f_n = 0$. Le théorème ne s'applique pas car $f_n$ n'est pas croissante ($f_2(1/3) = 0 \le f_1(1/3) = 1$).
4. **Bosses glissantes (Contre-exemple sans croissance) :** Soit $f_n(x) = \mathbf{1}_{[n, n+1]}$. $\int f_n = 1$, $\lim f_n = 0$. Encore une fois, la perte de la masse est due à l'absence de monotonie.
5. **Polynômes de Bernstein :** La suite des approximations de Bernstein pour une fonction convexe continue croît de manière monotone, illustrant l'utilité du théorème pour établir des limites sans avoir recours à la convergence uniforme sur des non-compacts.



## 2. Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Énoncé du Théorème

> **Théorème de Convergence Monotone (Beppo Levi) :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
> Si la suite est **croissante** presque partout :
> $$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \text{ p.p.}$$
> Alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable et :
> $$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

### Corollaire (Sommation terme à terme)

> **Théorème :** Pour toute suite de fonctions mesurables **positives** $(u_n)$ :
> $$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$

## 3. Démonstrations

### Démonstration du Théorème de Beppo Levi

1. **Existence de la limite :** Comme $(f_n(x))$ est une suite croissante de $[0, +\infty]$, elle admet toujours une limite dans $[0, +\infty]$ pour chaque $x$. On a vu (Jalon 65) que le sup (ou la limite ici) de fonctions mesurables est mesurable.
2. **Inégalité facile ($\ge$) :** Comme $f_n \le f$ pour tout $n$, par croissance de l'intégrale (Jalon 66) :
   $\int f_n \le \int f$. En prenant la limite : $\lim \int f_n \le \int f$.
3. **Inégalité difficile ($\le$) :** Soit $s$ une fonction simple telle que $0 \le s \le f$. Soit $\alpha \in ]0, 1[$.
   On définit $A_n = \{x \in X \mid f_n(x) \ge \alpha s(x) \}$.
   - Comme $f_n$ croît vers $f$ et $\alpha s < f$ (là où $s>0$), la suite d'ensembles $(A_n)$ est croissante et son union est $X$.
   - On a $\int f_n \ge \int_{A_n} f_n \ge \int_{A_n} \alpha s = \alpha \int_{A_n} s$.
   - Par continuité monotone de la mesure (Jalon 63), $\lim \int_{A_n} s = \int_X s$.
   - Donc $\lim \int f_n \ge \alpha \int_X s$.
   - En faisant tendre $\alpha \to 1$, on a $\lim \int f_n \ge \int s$.
4. **Conclusion :** Comme c'est vrai pour tout $s \le f$, alors $\lim \int f_n \ge \sup \int s = \int f$.
   Les deux inégalités prouvent l'égalité.

## 4. Application en Intelligence Artificielle

    - **Processus de Poisson :** Pour calculer le nombre moyen d'événements (ex: clics sur une pub) sur un intervalle de temps, on somme les probabilités d'événements infinitésimaux. Le TCM garantit que la somme de ces moyennes locales donne bien la moyenne globale.
    - **Séries de Taylor de fonctions de perte :** Si on décompose une fonction de coût complexe en une série de fonctions positives, on peut intégrer cette série terme à terme pour obtenir une approximation de la perte attendue.
    - **Théorie des Noyaux (Kernels) :** De nombreux noyaux (comme le noyau RBF) peuvent être vus comme des sommes infinies de caractéristiques. Le TCM permet de manipuler ces représentations de dimension infinie comme si elles étaient finies lors des calculs d'intégrales de risque.

## 5. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]], [[Jalon 63 (Définition axiomatique d'une mesure).md]]
- **Concepts Futurs dépendants :** [[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]], [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]
