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

Imaginez que vous construisiez une tour de blocs de glace qui fondent très lentement, mais que chaque jour vous ajoutiez une petite couche de glace supplémentaire par-dessus ($f_n \le f_{n+1}$). Vous voulez savoir quel sera le volume final de la tour ($f = \lim f_n$). Le **Théorème de Convergence Monotone** dit quelque chose de très simple et rassurant : le volume de la tour finale est exactement égal à la limite des volumes que vous avez mesurés jour après jour. En d'autres termes, pour des objets qui ne font que grandir, l'ordre dans lequel on fait les opérations (calculer le volume puis faire la limite, ou faire la limite puis calculer le volume) ne change pas le résultat.
C'est la grande force de l'intégrale de Lebesgue par rapport à celle de Riemann. Avec Riemann, on ne pouvait pas garantir que la limite d'une suite de fonctions intégrables soit encore intégrable. Avec Lebesgue et Beppo Levi, on a un outil ultra-robuste pour manipuler les limites et les sommes infinies.
Une suite de courbes qui "montent" vers une courbe plafond. L'aire sous les courbes monte elle aussi vers l'aire sous le plafond.

## 2. Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Énoncé du Théorème

> **Théorème de Convergence Monotone (Beppo Levi) :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
> Si la suite est **croissante** presque partout :
> $$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \text{ p.p.}$$
> Alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable et :
> $$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$


### C. Exemples Concrets Immédiats

**Exemple 1 (Suite constante) :**
Soit $f_n(x) = c \ge 0$ pour tout $n$. La suite est croissante (large) et converge vers $f(x) = c$. On a bien $\int c d\mu = \lim \int c d\mu$.

**Exemple 2 (Suite de fonctions étagées sur $[0,1]$) :**
Soit $f_n(x) = 1 - \frac{1}{n}$. La suite est positive et croissante.
La limite est $f(x) = 1$. L'intégrale de Lebesgue de $f_n$ sur $[0,1]$ est $\int_0^1 (1 - 1/n) dx = 1 - 1/n$.
La limite des intégrales est $\lim (1 - 1/n) = 1$. L'intégrale de la limite est $\int_0^1 1 dx = 1$. L'égalité est vérifiée.

**Exemple 3 (Fonction tendant vers $+\infty$) :**
Soit $f_n(x) = n \cdot \chi_{[0,1]}(x)$. La suite est positive, croissante et diverge vers $+\infty$ sur $[0,1]$.
L'intégrale de $f_n$ est $n$. La limite est $+\infty$. L'intégrale de la limite (la fonction $+\infty \cdot \chi_{[0,1]}$) est $+\infty$.

**Exemple 4 (Série géométrique) :**
Soit $X = \mathbb{N}$ avec la mesure de comptage. Soit $u_n(k) = (\frac{1}{2})^n \chi_{\{0\}}(k)$.
La somme $\sum_n u_n(0) = \sum (1/2)^n = 2$.
L'intégrale de la somme est 2. La somme des intégrales est $\sum 1/2^n = 2$.

**Exemple 5 (Croissance stricte) :**
Soit $f_n(x) = x^2 - \frac{1}{n}$ pour $x \in [1,2]$. $f_n$ est croissante et $f_n(x) > 0$ sur l'intervalle.
La limite est $f(x) = x^2$. L'intégrale de $f_n$ est $[x^3/3 - x/n]_1^2 = (8/3 - 2/n) - (1/3 - 1/n) = 7/3 - 1/n$.
La limite est $7/3$, ce qui est bien $\int_1^2 x^2 dx$.

**Exemple 6 (Fonctions indicatrices emboîtées) :**
Soit $A_n = [0, 1 - 1/n]$. Les ensembles sont emboîtés $A_n \subset A_{n+1}$.
Soit $f_n = \chi_{A_n}$. La suite de fonctions croît vers $f = \chi_{[0,1[}$.
$\int f_n d\mu = \mu(A_n) = 1 - 1/n$. La limite est $1$. $\int f d\mu = \mu([0,1[) = 1$.

**Exemple 7 (Gaussienne qui s'élargit) :**
Soit $f_n(x) = e^{-x^2} \cdot \chi_{[-n,n]}(x)$. La suite est croissante.
La limite est $e^{-x^2}$ sur tout $\mathbb{R}$.
$\int f_n = \int_{-n}^n e^{-x^2} dx \to \sqrt{\pi}$, qui est bien l'intégrale sur $\mathbb{R}$ de la gaussienne.

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
