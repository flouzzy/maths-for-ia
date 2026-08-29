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

## 1. Présentation du concept clé

Le passage à la limite sous le signe intégral est l'un des problèmes centraux de l'analyse mathématique. La théorie de Riemann offre des théorèmes de convergence très restrictifs (nécessitant souvent la convergence uniforme, une condition extrêmement forte). L'intégrale de Lebesgue, quant à elle, brille par sa robustesse face aux processus limites. Le Théorème de Convergence Monotone de Beppo Levi en est la première et plus éclatante démonstration. Il affirme que pour des fonctions positives mesurables, si la suite est croissante, on peut toujours intervertir limite et intégrale, y compris lorsque ces grandeurs tendent vers l'infini.



## 2. Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### A. Énoncé du Théorème

> **Théorème de Convergence Monotone (Beppo Levi) :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
> Si la suite est **croissante** presque partout :
> $$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \text{ p.p.}$$
> Alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable et :
> $$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

### B. Corollaire (Sommation terme à terme)

> **Théorème :** Pour toute suite de fonctions mesurables **positives** $(u_n)$ :
> $$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$



### Exemples d'application immédiats

1. **Exemple 1 : Suites constantes**
   Soit $X = \mathbb{R}$ avec la mesure de Lebesgue. Si $f_n(x) = c \ge 0$ pour tout $x \in [0, 1]$ et tout $n$, la suite est croissante au sens large. La limite est $f(x) = c$. L'intégrale de la limite est $\int_0^1 c dx = c$. La limite des intégrales est $\lim_{n \to \infty} c = c$.

2. **Exemple 2 : Suite géométrique croissante**
   Sur $X = [0, 1]$, soit $f_n(x) = 1 - (x/2)^n$. Pour tout $x \in [0, 1]$, $x/2 \le 1/2$, donc $(x/2)^n$ décroît vers $0$. La suite $f_n(x)$ croît vers $f(x) = 1$.
   L'intégrale de $f_n$ est $\int_0^1 (1 - (x/2)^n) dx = 1 - \frac{1}{2^n(n+1)}$.
   La limite est $1$. L'intégrale de la limite est $\int_0^1 1 dx = 1$.

3. **Exemple 3 : Convergence ponctuelle vers l'infini**
   Soit $f_n(x) = n \cdot \mathbf{1}_{[0, 1]}(x)$. $f_n$ est croissante. La limite est $f(x) = +\infty$ sur $[0, 1]$ et $0$ ailleurs.
   $\int f_n d\lambda = n \to +\infty$.
   $\int f d\lambda = +\infty$.

4. **Exemple 4 : La bosse glissante (contre-exemple si non croissant)**
   $g_n(x) = n \cdot \mathbf{1}_{[0, 1/n]}(x)$. La limite est $g(x) = 0$ pour $x > 0$. La suite n'est pas croissante.
   $\int g_n = 1$, mais $\int g = 0$. Le TCM ne s'applique pas.

5. **Exemple 5 : La bosse croissante**
   $f_n(x) = \mathbf{1}_{[n, n+1]}(x)$ n'est pas croissante, mais si on prend $S_n(x) = \sum_{k=1}^n \mathbf{1}_{[k, k+1]}(x) = \mathbf{1}_{[1, n+1]}(x)$, $S_n$ est croissante vers $\mathbf{1}_{[1, +\infty)}$.
   $\int S_n = n \to +\infty$. $\int \mathbf{1}_{[1, +\infty)} = +\infty$.

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

## 4. Exercices d'Application

### Exercice 1 : Intégrale d'une série
**Énoncé :** Calculer $\int_0^1 \sum_{n=1}^\infty x^n dx$.
**Correction Détaillée :**
1. Les fonctions $u_n(x) = x^n$ sont mesurables et positives sur $[0, 1]$.
2. Par le corollaire du TCM, on peut intervertir somme et intégrale.
3. $I = \sum_{n=1}^\infty \int_0^1 x^n dx = \sum_{n=1}^\infty \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \sum_{n=1}^\infty \frac{1}{n+1}$.
4. Cette série est la série harmonique (moins son premier terme), elle diverge vers $+\infty$.
5. L'intégrale de la somme est donc $+\infty$.

### Exercice 2 : Niveau Avancé (Utilisation de la mesure de comptage)
**Énoncé :** Retrouver le théorème de sommation des séries à termes positifs doubles : $\sum_{i} \sum_{j} a_{i,j} = \sum_{j} \sum_{i} a_{i,j}$.
**Correction Détaillée :**
On considère l'espace $\mathbb{N}$ muni de la mesure de comptage $\mu$. Soit $f_n(i) = \sum_{j=0}^n a_{i,j}$. La suite de fonctions $(f_n)$ est croissante car $a_{i,j} \ge 0$. Par Beppo Levi, l'intégrale de la limite est la limite des intégrales, ce qui correspond exactement à l'interversion des sommes.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, on manipule souvent des **Espérances de sommes infinies** ou des limites de processus. Le TCM est l'outil qui permet de passer à la limite sous l'espérance en toute sécurité.
- **Example Concret :**
    - **Processus de Poisson :** Pour calculer le nombre moyen d'événements (ex: clics sur une pub) sur un intervalle de temps, on somme les probabilités d'événements infinitésimaux. Le TCM garantit que la somme de ces moyennes locales donne bien la moyenne globale.
    - **Séries de Taylor de fonctions de perte :** Si on décompose une fonction de coût complexe en une série de fonctions positives, on peut intégrer cette série terme à terme pour obtenir une approximation de la perte attendue.
    - **Théorie des Noyaux (Kernels) :** De nombreux noyaux (comme le noyau RBF) peuvent être vus comme des sommes infinies de caractéristiques. Le TCM permet de manipuler ces représentations de dimension infinie comme si elles étaient finies lors des calculs d'intégrales de risque.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]], [[Jalon 63 (Définition axiomatique d'une mesure).md]]
- **Concepts Futurs dépendants :** [[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]], [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]
