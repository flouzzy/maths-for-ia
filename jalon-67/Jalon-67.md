---
uuid: "jalon-67"
title: "Démonstration du théorème de convergence monotone"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon-66.md]]"
next: "[[Jalon-68.md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo-Levi)

## 1. Naissance d'un outil de passage à la limite

Historiquement, l'intégration au sens de Riemann a révélé des failles critiques lorsqu'il s'agissait de manipuler des suites de fonctions. En particulier, la question de l'interversion de la limite et de l'intégrale, c'est-à-dire savoir sous quelles conditions $\lim_{n \to \infty} \int f_n = \int \lim_{n \to \infty} f_n$, était un problème ardu nécessitant la convergence uniforme, une hypothèse très forte.

Henri Lebesgue, dans sa construction novatrice au début du XXe siècle, a déplacé le problème. En s'appuyant sur la théorie de la mesure, il a construit une intégrale robuste vis-à-vis des passages à la limite. Le mathématicien italien Beppo Levi a formalisé en 1906 le résultat fondamental de cette théorie : le Théorème de Convergence Monotone.

Le concept géométrique sous-jacent est constructiviste et profondément ancré dans l'intuition de la mesure. Si l'on considère une suite de fonctions mesurables positives qui croît point par point vers une fonction limite, on peut voir cela comme l'accumulation de "couches" successives d'aires sous la courbe. Puisque la suite est croissante, aucune aire n'est "perdue" en cours de route par annulation ou oscillation. L'aire sous la courbe limite est donc naturellement la limite (éventuellement infinie) des aires successives. C'est le pilier qui permet, par la suite, de démontrer le Lemme de Fatou et le célèbre Théorème de Convergence Dominée.

\begin{center}
\begin{tikzpicture}[scale=1]
  \draw[->] (-0.5, 0) -- (6, 0) node[right] {$x$};
  \draw[->] (0, -0.5) -- (0, 4) node[above] {$f(x)$};

  \draw[blue, thick, dashed] (0,0.5) to[out=20,in=180] (3,3.5) to[out=0,in=160] (5.5,3.8) node[right] {$f$};
  \draw[red, thick] (0,0.4) to[out=20,in=180] (3,2.8) to[out=0,in=160] (5.5,3.0) node[right] {$f_4$};
  \draw[orange, thick] (0,0.3) to[out=20,in=180] (3,2.2) to[out=0,in=160] (5.5,2.4) node[right] {$f_3$};
  \draw[green!70!black, thick] (0,0.2) to[out=20,in=180] (3,1.5) to[out=0,in=160] (5.5,1.7) node[right] {$f_2$};
  \draw[gray, thick] (0,0.1) to[out=20,in=180] (3,0.8) to[out=0,in=160] (5.5,1.0) node[right] {$f_1$};

  \node at (2.5, -0.8) {Suite de fonctions mesurables positives croissantes $f_1 \le f_2 \le \dots \le f$};
\end{tikzpicture}
\end{center}


## 2. Le Théorème de Convergence Monotone et ses corollaires

### Théorème de Convergence Monotone (Beppo-Levi)

Soit $(X, \mathcal{M}, \mu)$ un espace mesuré.
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables définies sur $X$ à valeurs dans $[0, +\infty]$.
On suppose que la suite $(f_n)_{n \in \mathbb{N}}$ est croissante $\mu$-presque partout, c'est-à-dire :
$$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \quad \mu\text{-presque partout sur } X.$$

Alors, la fonction limite $f$ définie par $f(x) = \lim_{n \to \infty} f_n(x)$ existe $\mu$-presque partout dans $[0, +\infty]$, $f$ est mesurable, et on a l'égalité :
$$\int_X f \, d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu.$$


**Exemple calculatoire immédiat :**
Considérons l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Soit la suite de fonctions $f_n : \mathbb{R} \to [0, +\infty]$ définie par $f_n(x) = \mathbf{1}_{[0, 1]}(x) \cdot \left(1 - \frac{x}{n}\right)^n$.
Pour $x \in [0, 1]$, la suite $u_n = \left(1 - \frac{x}{n}\right)^n$ est croissante (on peut le vérifier en étudiant le logarithme).
De plus, $\lim_{n \to \infty} f_n(x) = \mathbf{1}_{[0, 1]}(x) \cdot e^{-x}$.
Par le Théorème de Convergence Monotone :
$$\lim_{n \to \infty} \int_{[0,1]} \left(1 - \frac{x}{n}\right)^n d\lambda(x) = \int_{[0,1]} e^{-x} d\lambda(x) = \left[ -e^{-x} \right]_0^1 = 1 - \frac{1}{e}.$$

### Corollaire des séries à termes positifs

Si $(u_n)_{n \in \mathbb{N}}$ est une suite de fonctions mesurables positives, on peut intervertir la série et l'intégrale :
$$\int_X \left( \sum_{n=0}^{+\infty} u_n \right) d\mu = \sum_{n=0}^{+\infty} \int_X u_n \, d\mu.$$

**Cas limite et pathologie :**
Le théorème requiert fondamentalement que les fonctions soient de signe constant (positives). Si la suite $f_n$ oscille entre valeurs positives et négatives, ou si elle "fuit à l'infini" en masse de Dirac mobile, la convergence monotone n'est pas applicable.
Considérons $f_n(x) = n \cdot \mathbf{1}_{(0, 1/n)}(x)$.
On a $\lim_{n \to \infty} f_n(x) = 0$ pour tout $x > 0$.
Or, $\int f_n d\lambda = n \cdot \frac{1}{n} = 1$, ce qui ne tend pas vers l'intégrale de la limite (qui est 0).
Ici, la suite $(f_n)$ **n'est pas croissante**, l'hypothèse principale du TCM est violée.

## 3. Démonstration ligne par ligne

La démonstration est un joyau de l'analyse réelle moderne, car elle relie intimement l'intégrale des fonctions étagées (via la définition par le supremum) à la continuité par valeurs croissantes de la mesure.

**Étape 1 : Croissance des intégrales et majoration triviale.**
Quitte à redéfinir la suite sur un ensemble de mesure nulle, on peut supposer que la suite est croissante partout.
Pour tout $x \in X$, la suite $(f_n(x))_{n \in \mathbb{N}}$ est croissante à valeurs dans $[0, +\infty]$. Par propriété de $\overline{\mathbb{R}}$, la limite $f(x) = \lim_{n \to \infty} f_n(x) = \sup_{n} f_n(x)$ existe.
Comme les $f_n$ sont mesurables, la limite supérieure $f$ est également mesurable.
De plus, pour tout $n$, $f_n \le f_{n+1} \le f$.
Par monotonie de l'intégrale de Lebesgue pour les fonctions positives :
$$\int_X f_n \, d\mu \le \int_X f_{n+1} \, d\mu \le \int_X f \, d\mu.$$
La suite $\left(\int_X f_n \, d\mu\right)$ est donc croissante dans $[0, +\infty]$. Elle admet une limite $\alpha \le \int_X f \, d\mu$.
Il nous reste à démontrer l'inégalité inverse : $\int_X f \, d\mu \le \alpha$.

**Étape 2 : Minoration par les fonctions étagées.**
Rappelons la définition de l'intégrale de Lebesgue pour une fonction mesurable positive $f$ :
$$\int_X f \, d\mu = \sup \left\{ \int_X \varphi \, d\mu \;\middle|\; \varphi \text{ est une fonction étagée positive et } 0 \le \varphi \le f \right\}.$$
Soit donc une fonction étagée $\varphi$ telle que $0 \le \varphi \le f$. Fixons un réel $c$ tel que $0 < c < 1$.
Considérons les ensembles mesurables :
$$E_n = \{ x \in X \mid f_n(x) \ge c \, \varphi(x) \}.$$
Puisque $(f_n)$ est croissante, on a immédiatement $E_n \subset E_{n+1}$.
De plus, comme $\lim_{n \to \infty} f_n(x) = f(x)$ et que pour tout $x$ tel que $f(x) > 0$, on a $c \, \varphi(x) < f(x)$, il vient nécessairement qu'à partir d'un certain rang, $f_n(x)$ dépasse $c \, \varphi(x)$.
(Si $f(x) = 0$, alors $\varphi(x) = 0$, et donc $f_n(x) \ge 0 = c \, \varphi(x)$ est vrai pour tout $n$).
Ainsi, $\bigcup_{n \in \mathbb{N}} E_n = X$.

**Étape 3 : Passage à la limite sur la mesure.**
Par définition des ensembles $E_n$, on a sur tout l'espace $X$ :
$$f_n \ge f_n \cdot \mathbf{1}_{E_n} \ge c \, \varphi \cdot \mathbf{1}_{E_n}.$$
En intégrant de part et d'autre :
$$\int_X f_n \, d\mu \ge \int_X c \, \varphi \cdot \mathbf{1}_{E_n} \, d\mu = c \int_{E_n} \varphi \, d\mu.$$
La fonction étagée $\varphi$ s'écrit $\varphi = \sum_{i=1}^k a_i \mathbf{1}_{A_i}$, où les $A_i$ forment une partition mesurable et $a_i \ge 0$.
L'intégrale sur $E_n$ vaut :
$$\int_{E_n} \varphi \, d\mu = \sum_{i=1}^k a_i \, \mu(A_i \cap E_n).$$
Or, la suite d'ensembles $(A_i \cap E_n)_{n \in \mathbb{N}}$ est une suite croissante de limite $A_i \cap X = A_i$.
Par la propriété de *continuité monotone croissante* d'une mesure, on a $\lim_{n \to \infty} \mu(A_i \cap E_n) = \mu(A_i)$.
Ainsi,
$$\lim_{n \to \infty} \int_{E_n} \varphi \, d\mu = \sum_{i=1}^k a_i \, \mu(A_i) = \int_X \varphi \, d\mu.$$
On obtient alors en passant à la limite dans l'inégalité :
$$\alpha = \lim_{n \to \infty} \int_X f_n \, d\mu \ge c \int_X \varphi \, d\mu.$$
Cette inégalité étant vraie pour tout $c \in (0, 1)$, on peut faire tendre $c \to 1$ par valeurs inférieures pour obtenir :
$$\alpha \ge \int_X \varphi \, d\mu.$$

**Étape 4 : Conclusion.**
On a montré que pour toute fonction étagée $\varphi$ telle que $0 \le \varphi \le f$, on a $\alpha \ge \int_X \varphi \, d\mu$.
En prenant le supremum sur l'ensemble de ces fonctions étagées $\varphi$, on trouve :
$$\alpha \ge \sup_{\varphi \le f} \int_X \varphi \, d\mu = \int_X f \, d\mu.$$
On avait déjà $\alpha \le \int_X f \, d\mu$, d'où l'égalité stricte :
$$\lim_{n \to \infty} \int_X f_n \, d\mu = \int_X f \, d\mu. \quad \blacksquare$$

## 4. Applications en apprentissage et physique théorique

En intelligence artificielle et probabilités continues, le TCM est le théorème de base pour manipuler des espérances mathématiques infinies.

**Processus de comptage et distributions de Poisson**
Dans la modélisation des processus d'arrivée d'événements (par exemple le nombre de connexions à un serveur), on somme une infinité de probabilités de variables indépendantes. L'espérance totale $\mathbb{E}\left[\sum X_n\right]$ est mathématiquement définie via le Corollaire de Beppo-Levi. C'est ce qui justifie que la moyenne de la somme est la somme des moyennes, même pour une infinité dénombrable de variables, tant que ces variables mesurent un décompte (positives).

**Calcul stochastique et méthodes de Monte-Carlo**
Si l'on cherche à approximer une fonction de perte globale complexe par une suite d'approximations monotones (par exemple, des relaxations convexes successives d'un problème NP-Hard), le TCM nous garantit que si notre approximation algorithmique approche l'énergie réelle de manière monotone, alors l'espérance de l'énergie (le risque moyen du modèle) convergera de manière stable vers le vrai risque, garantissant la sûreté théorique de l'apprentissage sur de longs cycles d'entraînement.
