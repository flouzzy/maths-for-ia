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

## Présentation du concept clé


## Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Énoncé du Théorème

**Théorème de Convergence Monotone (Beppo Levi) :**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
Si la suite est **croissante** presque partout :
$$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \text{ p.p.}$$
Alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable et :
$$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

### Corollaire (Sommation terme à terme)

**Théorème :** Pour toute suite de fonctions mesurables **positives** $(u_n)$ :
$$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$


**Exemple concret 1 : Suite géométrique**
Soit $u_n(x) = x^n$ sur $X = [0,1]$. Les $u_n$ sont positives et mesurables.
Le théorème permet d'écrire $\int_0^1 \sum_{n=0}^\infty x^n dx = \sum_{n=0}^\infty \int_0^1 x^n dx$.
$\int_0^1 x^n dx = \frac{1}{n+1}$. La somme de ces intégrales est la série harmonique $\sum \frac{1}{n+1} = +\infty$.
La somme de la série de fonctions est $\frac{1}{1-x}$, dont l'intégrale sur $[0,1]$ vaut aussi $+\infty$.

**Exemple concret 2 : Série à convergence très rapide**
Soit $u_n(x) = \frac{x^n}{n!}$ sur $X = [0,1]$.
$\int_0^1 \sum_{n=0}^\infty \frac{x^n}{n!} dx = \int_0^1 e^x dx = e - 1$.
Par le théorème, ceci est égal à $\sum_{n=0}^\infty \int_0^1 \frac{x^n}{n!} dx = \sum_{n=0}^\infty \frac{1}{n!(n+1)} = \sum_{n=0}^\infty \frac{1}{(n+1)!} = e - 1$.



## Démonstrations

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

## Exercices d'Application

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

## Application en Intelligence Artificielle

-  En IA, on manipule souvent des **Espérances de sommes infinies** ou des limites de processus. Le TCM est l'outil qui permet de passer à la limite sous l'espérance en toute sécurité.
-
    - **Processus de Poisson :** Pour calculer le nombre moyen d'événements (ex: clics sur une pub) sur un intervalle de temps, on somme les probabilités d'événements infinitésimaux. Le TCM garantit que la somme de ces moyennes locales donne bien la moyenne globale.
    - **Séries de Taylor de fonctions de perte :** Si on décompose une fonction de coût complexe en une série de fonctions positives, on peut intégrer cette série terme à terme pour obtenir une approximation de la perte attendue.
    - **Théorie des Noyaux (Kernels) :** De nombreux noyaux (comme le noyau RBF) peuvent être vus comme des sommes infinies de caractéristiques. Le TCM permet de manipuler ces représentations de dimension infinie comme si elles étaient finies lors des calculs d'intégrales de risque.

## Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]], [[Jalon 63 (Définition axiomatique d'une mesure).md]]
- **Concepts Futurs dépendants :** [[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]], [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]
