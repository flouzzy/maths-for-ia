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

- **Introduction Intuitive :** Imaginez que vous construisiez une tour de blocs de glace qui fondent très lentement, mais que chaque jour vous ajoutiez une petite couche de glace supplémentaire par-dessus ($f_n \le f_{n+1}$). Vous voulez savoir quel sera le volume final de la tour ($f = \lim f_n$). Le **Théorème de Convergence Monotone** dit quelque chose de très simple et rassurant : le volume de la tour finale est exactement égal à la limite des volumes que vous avez mesurés jour après jour. En d'autres termes, pour des objets qui ne font que grandir, l'ordre dans lequel on fait les opérations (calculer le volume puis faire la limite, ou faire la limite puis calculer le volume) ne change pas le résultat.
- **Genèse Historique et Limites de Riemann :** C'est la grande force de l'intégrale de Lebesgue par rapport à celle de Riemann. Avec Riemann, on ne pouvait pas garantir que la limite d'une suite de fonctions intégrables soit encore intégrable. Avec Lebesgue et Beppo Levi, on a un outil ultra-robuste pour manipuler les limites et les sommes infinies.
- **Interprétation Géométrique :** Une suite de courbes qui "montent" vers une courbe plafond. L'aire sous les courbes monte elle aussi vers l'aire sous le plafond.

## 2. Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### A. Énoncé du Théorème

> **Théorème de Convergence Monotone (Beppo Levi) :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
> Si la suite est croissante presque partout :
> $$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \text{ p.p.}$$
> Alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable et :
> $$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

### Exemples de Validation

**Exemple 1 : La série géométrique**
Prenons l'espace $[0,1[$ muni de la mesure de Lebesgue $\lambda$. Soit $f_n(x) = \sum_{k=0}^n x^k$.
Les fonctions $f_n$ sont mesurables, positives. La suite $(f_n)$ est croissante car $f_{n+1}(x) - f_n(x) = x^{n+1} \ge 0$.
La limite simple est $f(x) = \lim_{n \to \infty} f_n(x) = \sum_{k=0}^\infty x^k = \frac{1}{1-x}$.
Calculons l'intégrale de chaque $f_n$ :
$$\int_0^1 f_n(x) dx = \sum_{k=0}^n \int_0^1 x^k dx = \sum_{k=0}^n \frac{1}{k+1}$$
Par le TCM, on a :
$$\int_0^1 \frac{1}{1-x} dx = \lim_{n \to \infty} \sum_{k=0}^n \frac{1}{k+1} = +\infty$$
Le TCM fonctionne même si la limite est infinie.

**Exemple 2 : Une suite d'indicatrices**
Soit $f_n = \mathbf{1}_{[0, 1 - \frac{1}{n}]}$.
Pour $x \in \mathbb{R}$, on a bien $f_n(x) \le f_{n+1}(x)$.
La limite simple est $f = \mathbf{1}_{[0, 1[}$.
On a $\int f_n = 1 - \frac{1}{n}$.
La limite des intégrales est $\lim (1 - \frac{1}{n}) = 1$.
Et l'intégrale de la limite est $\int \mathbf{1}_{[0, 1[} = 1$.
C'est bien égal.

**Exemple 3 : Échec de la croissance**
Prenons $f_n = n \mathbf{1}_{]0, 1/n]}$.
On a $\int f_n = 1$ pour tout $n$.
La limite simple de $f_n$ est $f(x) = 0$ pour tout $x$.
L'intégrale de la limite est $0$.
$1 \neq 0$. Le théorème de convergence monotone ne s'applique pas car la suite $f_n$ **n'est pas** croissante. En effet $f_1(x) = \mathbf{1}_{]0, 1]}$, alors que $f_2(x) = 2 \mathbf{1}_{]0, 1/2]}$. Si $x = 0.8$, $f_1(x) = 1$ et $f_2(x) = 0$. Donc $f_1 \not\le f_2$.


Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### B. Corollaire (Sommation terme à terme)

> **Théorème :** Pour toute suite de fonctions mesurables **positives** $(u_n)$ :
> $$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$


\begin{tikzpicture}[scale=1.2]
  \draw[->] (-0.5, 0) -- (4, 0) node[right] {$x$};
  \draw[->] (0, -0.5) -- (0, 3) node[above] {$y$};

  \draw[thick, blue, domain=0:3.5, samples=100] plot (\x, {2.5 - 2*exp(-0.5*\x)}) node[right] {$f(x)$};

  \draw[red, domain=0:3.5, samples=100] plot (\x, {1.5 - 1.5*exp(-0.5*\x)}) node[right] {$f_1(x)$};
  \draw[red, domain=0:3.5, samples=100] plot (\x, {2.0 - 1.8*exp(-0.5*\x)}) node[right] {$f_2(x)$};
  \draw[red, domain=0:3.5, samples=100] plot (\x, {2.3 - 1.9*exp(-0.5*\x)}) node[right] {$f_3(x)$};

  \node at (2, -1) {Illustration du Théorème de Convergence Monotone : Les courbes $f_n$ (en rouge) montent vers la courbe limite $f$ (en bleu).};
\end{tikzpicture}

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
