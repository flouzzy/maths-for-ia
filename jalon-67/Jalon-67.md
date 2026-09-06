---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon-66.md]]"
next: "[[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo Levi)

## 1. Genèse du concept et intuition géométrique

L'intégration au sens de Riemann a révélé de profondes limites, en particulier son incapacité à intervertir systématiquement limites et intégrales pour des suites de fonctions pourtant régulières. Le **Théorème de convergence monotone**, formulé par le mathématicien italien Beppo Levi au début du XXe siècle, constitue la clé de voûte de la théorie de la mesure de Lebesgue. Ce théorème montre que si l'on accumule des couches de valeurs positives croissantes, l'intégrale de la limite est exactement la limite des intégrales. Cela permet une manipulation robuste et algébriquement sûre des limites infinies, qui est essentielle dans la théorie des probabilités et l'analyse fonctionnelle.

Imaginons une suite de fonctions $f_n$ qui approximent une fonction cible $f$ par le bas. Chaque fonction $f_{n+1}$ englobe l'aire sous $f_n$ et y ajoute une petite contribution positive. Géométriquement, l'aire totale finit par tendre vers l'aire sous la courbe limite.

## 2. Définitions et Théorème Fondamental

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré. Rappelons qu'une fonction mesurable positive est la limite croissante de fonctions étagées.

### Le Théorème de Convergence Monotone (Beppo Levi)

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ dans $[0, +\infty]$.
Si la suite est mesurable et croissante presque partout, c'est-à-dire :
$$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \quad \mu\text{-p.p.}$$

Alors, la fonction limite $f(x) = \lim_{n \to \infty} f_n(x)$ est mesurable, et on a l'égalité suivante :
$$\int_X f \, d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu$$

**Exemple concret immédiat :**
Considérons l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$, où $\lambda$ est la mesure de Lebesgue.
Prenons $f_n(x) = \mathbf{1}_{[0, 1 - \frac{1}{n}]}(x)$.
La suite $(f_n)$ est croissante en $n$. Pour tout $x$, $\lim_{n \to \infty} f_n(x) = \mathbf{1}_{[0, 1[}(x) = f(x)$.
Calculons l'intégrale de $f_n$ :
$$\int_{\mathbb{R}} f_n \, d\lambda = \lambda\left(\left[0, 1 - \frac{1}{n}\right]\right) = 1 - \frac{1}{n}$$
La limite de ces intégrales est $\lim_{n \to \infty} \left( 1 - \frac{1}{n} \right) = 1$.
D'autre part, l'intégrale de la limite $f$ est :
$$\int_{\mathbb{R}} \mathbf{1}_{[0, 1[} \, d\lambda = \lambda([0, 1[) = 1$$
Les deux valeurs sont bien égales, illustrant l'interversion de la limite et de l'intégrale.

### Corollaire : Sommation terme à terme des séries de fonctions positives

Soit $(u_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables positives sur $X$.
Alors, on a :
$$\int_X \left( \sum_{n=0}^{\infty} u_n \right) d\mu = \sum_{n=0}^{\infty} \int_X u_n \, d\mu$$
Ce résultat fondamental découle directement de l'application du théorème de Beppo Levi à la suite des sommes partielles $S_N = \sum_{n=0}^N u_n$, qui est croissante puisque les $u_n$ sont positives.

**Exemple concret immédiat :**
Calculons l'intégrale $\int_0^1 \frac{1}{1-x} \, dx$ de deux manières.
On sait que pour $x \in [0, 1[$, $\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n$. Les fonctions $u_n(x) = x^n$ sont positives et mesurables.
Par le corollaire, on a :
$$\int_0^1 \left( \sum_{n=0}^{\infty} x^n \right) dx = \sum_{n=0}^{\infty} \int_0^1 x^n \, dx$$
Or, $\int_0^1 x^n \, dx = \left[\frac{x^{n+1}}{n+1}\right]_0^1 = \frac{1}{n+1}$.
Donc, la somme devient la série harmonique $\sum_{n=0}^{\infty} \frac{1}{n+1} = \sum_{k=1}^{\infty} \frac{1}{k}$, qui diverge vers $+\infty$. L'intégrale de départ vaut donc $+\infty$.

## 3. Démonstration Rigoureuse du Théorème de Beppo Levi

Démontrons que $\int_X f \, d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu$.

**Étape 1 : Existence de la limite et de l'inégalité de monotonie**
Comme la suite $(f_n)$ est croissante et à valeurs dans $[0, +\infty]$, elle admet en tout point $x$ une limite $f(x) \in [0, +\infty]$. La mesurabilité de la limite de fonctions mesurables garantit que $f$ est mesurable.
Puisque $f_n \le f$ pour tout $n$, la monotonie de l'intégrale implique que $\int_X f_n \, d\mu \le \int_X f \, d\mu$.
En passant à la limite (qui existe car la suite des intégrales est croissante), on obtient :
$$\lim_{n \to \infty} \int_X f_n \, d\mu \le \int_X f \, d\mu \quad \text{(*)}$$

**Étape 2 : L'inégalité réciproque**
C'est le cœur de la preuve. Soit $s$ une fonction étagée mesurable telle que $0 \le s \le f$.
Choisissons une constante $\alpha \in ]0, 1[$.
Pour chaque $n \in \mathbb{N}$, définissons l'ensemble mesurable $A_n$ tel que :
$$A_n = \{ x \in X \mid f_n(x) \ge \alpha s(x) \}$$
Comme $(f_n)$ est croissante, la suite d'ensembles $(A_n)$ est croissante ($A_n \subset A_{n+1}$).
De plus, si $s(x) = 0$, $x \in A_n$ pour tout $n$. Si $s(x) > 0$, alors $\alpha s(x) < s(x) \le f(x) = \lim f_n(x)$, donc pour $n$ assez grand, $f_n(x) > \alpha s(x)$ par définition de la limite, et donc $x \in A_n$.
Ainsi, $\bigcup_{n=0}^{\infty} A_n = X$.

Sur $A_n$, on a $f_n \ge \alpha s$, donc :
$$\int_X f_n \, d\mu \ge \int_{A_n} f_n \, d\mu \ge \alpha \int_{A_n} s \, d\mu$$
L'intégrale $\int_{A_n} s \, d\mu$ est une mesure (la mesure de densité $s$). Par le théorème de continuité séquentielle croissante de la mesure, puisque $A_n \uparrow X$ :
$$\lim_{n \to \infty} \int_{A_n} s \, d\mu = \int_X s \, d\mu$$
En prenant la limite sur $n$ dans notre inégalité, on obtient :
$$\lim_{n \to \infty} \int_X f_n \, d\mu \ge \alpha \int_X s \, d\mu$$
Cette relation est vraie pour tout $\alpha \in ]0, 1[$. En faisant tendre $\alpha \to 1$, il vient :
$$\lim_{n \to \infty} \int_X f_n \, d\mu \ge \int_X s \, d\mu$$
Enfin, par définition de l'intégrale d'une fonction positive, $\int_X f \, d\mu = \sup \{ \int_X s \, d\mu \mid 0 \le s \le f, s \text{ étagée} \}$.
En prenant le suprémum sur toutes ces fonctions étagées $s$, on conclut :
$$\lim_{n \to \infty} \int_X f_n \, d\mu \ge \int_X f \, d\mu \quad \text{(**)}$$

**Conclusion**
Les inégalités (*) et (**) permettent de conclure l'égalité stricte :
$$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu$$

## 4. Pathologies et Cas Limites

**Suite non croissante**
Considérons l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$.
Soit $f_n(x) = \mathbf{1}_{[n, n+1]}(x)$. Pour tout $x \in \mathbb{R}$, pour $n$ assez grand, $x \notin [n, n+1]$, donc $\lim_{n \to \infty} f_n(x) = 0$.
L'intégrale de la limite est $\int 0 \, d\lambda = 0$.
Cependant, pour tout $n$, $\int f_n \, d\lambda = 1$, donc $\lim_{n \to \infty} \int f_n = 1 \neq 0$.
Ici, la suite n'est pas croissante, le théorème de convergence monotone ne s'applique pas (c'est un cas typique du Lemme de Fatou).

**Suite non positive**
Considérons $f_n(x) = -\frac{1}{n} \mathbf{1}_{]0, \infty[}(x)$ avec la mesure de Lebesgue.
La suite est croissante, $\lim_{n \to \infty} f_n(x) = 0$, donc $\int \lim f_n = 0$.
Mais $\int f_n \, d\lambda = -\infty$ pour tout $n$. La limite des intégrales est $-\infty \neq 0$.
Le théorème exige des fonctions à valeurs dans $[0, +\infty]$.

## 5. Applications en Intelligence Artificielle et Optimisation

Le théorème de convergence monotone est une clé d'accès pour démontrer rigoureusement la convergence des espérances.
Dans l'apprentissage statistique et les processus stochastiques :
- **Optimisation Stochastique :** Pour un risque empirique décomposé comme une somme d'erreurs (positives) sur des données, le théorème permet de s'assurer que si on accroît le nombre de termes, on peut manipuler les limites d'espérance en toute légalité pour prouver la convergence vers le risque théorique.
- **Processus de Markov et Reinforcement Learning :** L'évaluation d'une politique via la fonction de valeur de Bellman s'écrit souvent comme une série infinie de récompenses pondérées. Si les récompenses sont positives, le théorème de Beppo Levi justifie le calcul de l'espérance de ce retour infini et permet l'itération des opérateurs de Bellman.

---

\begin{tikzpicture}
  \draw[->, thick] (-0.5, 0) -- (6, 0) node[right] {$x$};
  \draw[->, thick] (0, -0.5) -- (0, 4) node[above] {$y$};

  \draw[domain=0.2:5, smooth, variable=\x, blue, thick] plot ({\x}, {3 - 2/\x}) node[right] {$f(x)$};
  \draw[domain=0.3:5, smooth, variable=\x, red, dashed, thick] plot ({\x}, {3 - 2.5/\x}) node[right] {$f_{n+1}(x)$};
  \draw[domain=0.5:5, smooth, variable=\x, orange, dashed, thick] plot ({\x}, {3 - 3.5/\x}) node[right] {$f_n(x)$};

  \node at (2.5, -0.5) {Convergence Monotone : $f_n \le f_{n+1} \le f$};
\end{tikzpicture}
