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

## 1. Introduction

L'élaboration de la théorie de l'intégration par Henri Lebesgue au début du XXe siècle répondait à une impasse conceptuelle majeure laissée par l'intégrale de Riemann. Dans le cadre riemannien, la limite d'une suite de fonctions intégrables n'est pas nécessairement intégrable, et l'interversion de la limite et de l'intégrale nécessite des hypothèses très fortes, telles que la convergence uniforme. Cette restriction est un obstacle géométrique et analytique considérable, particulièrement lorsque l'on manipule des espaces de fonctions ou des séries de Fourier.

Le mathématicien italien Beppo Levi a apporté une réponse fondamentale à ce problème en 1906, en formulant ce qui allait devenir l'un des piliers de l'analyse moderne : le théorème de convergence monotone. L'intuition physique et géométrique sous-jacente est d'une grande limpidité. Si l'on considère une grandeur (représentée par une fonction) qui s'accumule continuellement et sans jamais décroître, l'accumulation totale à la limite doit correspondre exactement à la limite des accumulations partielles. En d'autres termes, si une suite de profils géométriques grandit monotonement vers un profil limite, l'aire sous le profil limite est précisément la limite des aires sous les profils successifs. Ce théorème confère à l'intégrale de Lebesgue sa formidable robustesse analytique et justifie son adoption universelle en théorie de la mesure et en probabilités.

## 2. Théorèmes de Convergence Monotone et de Sommation

### Le Théorème de Beppo Levi

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

**Théorème de convergence monotone :**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables définies sur $X$ et à valeurs dans $[0, +\infty]$.
On suppose que la suite est croissante presque partout par rapport à la mesure $\mu$, c'est-à-dire :
$$ \forall n \in \mathbb{N}, \quad f_n(x) \le f_{n+1}(x) \quad \text{pour presque tout } x \in X $$
Alors, la fonction limite $f = \lim_{n \to \infty} f_n$ (qui existe dans $[0, +\infty]$) est mesurable et vérifie :
$$ \int_X f(x) \, d\mu(x) = \lim_{n \to \infty} \int_X f_n(x) \, d\mu(x) $$

#### Exemples concrets immédiats

Considérons l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Prenons la suite de fonctions $f_n(x) = \mathbf{1}_{[0, 1 - \frac{1}{n}]}(x)$.
Pour tout $x$, $f_n(x)$ ne prend que des valeurs positives ou nulles.
La suite $(f_n)$ est croissante car les intervalles emboîtés $[0, 1 - \frac{1}{n}]$ s'élargissent lorsque $n$ augmente.
La fonction limite ponctuelle est $f(x) = \lim_{n \to \infty} \mathbf{1}_{[0, 1 - \frac{1}{n}]}(x) = \mathbf{1}_{[0, 1[}(x)$.
Calculons les intégrales des fonctions de la suite :
$$ \int_{\mathbb{R}} f_n(x) \, d\lambda(x) = \lambda\left(\left[0, 1 - \frac{1}{n}\right]\right) = 1 - \frac{1}{n} $$
La limite de ces intégrales est $\lim_{n \to \infty} \left(1 - \frac{1}{n}\right) = 1$.
Calculons l'intégrale de la fonction limite :
$$ \int_{\mathbb{R}} f(x) \, d\lambda(x) = \lambda([0, 1[) = 1 $$
Nous observons une parfaite égalité, illustrant concrètement le théorème.

\begin{center}
\begin{tikzpicture}[scale=1.5]
  \draw[->] (-0.5,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,2) node[above] {$f_n(x)$};

  \draw[thick, blue!30] (0, 1) -- (1, 1) -- (1, 0);
  \node[blue!50] at (1.2, 1.2) {$f_2(x)$};

  \draw[thick, blue!60] (0, 1) -- (1.5, 1) -- (1.5, 0);
  \node[blue!80] at (1.7, 1.2) {$f_3(x)$};

  \draw[thick, blue] (0, 1) -- (2, 1) -- (2, 0);
  \node[blue] at (2.2, 1.2) {$f(x)$};

  \node[below] at (1, 0) {$1-1/2$};
  \node[below] at (1.5, 0) {$1-1/3$};
  \node[below] at (2, 0) {$1$};
\end{tikzpicture}
\end{center}

#### Cas limites et configurations pathologiques

Il est crucial d'observer que l'hypothèse de positivité (ou du moins qu'il existe une fonction intégrable minorant toutes les $f_n$) est indispensable.
Considérons la suite $f_n(x) = -\frac{1}{n} \mathbf{1}_{[0, n]}(x)$.
La suite est croissante (elle tend vers $0$ par valeurs négatives).
Cependant, l'intégrale de $f_n$ sur $\mathbb{R}$ est $\int_{\mathbb{R}} f_n(x) \, d\lambda(x) = -\frac{1}{n} \times n = -1$.
La limite de l'intégrale est $-1$.
Mais la fonction limite est $f(x) = 0$, dont l'intégrale est $0$.
Ici, la convergence monotone en l'absence de minorant intégrable ne permet pas de préserver l'égalité des limites, mettant en évidence le rôle de la contrainte de positivité de l'énoncé fondamental.

### Théorème d'intégration terme à terme (Séries de fonctions)

Une conséquence directe et d'une importance capitale du théorème de convergence monotone est l'intégration des séries de fonctions positives.

**Théorème :**
Soit $(u_k)_{k \in \mathbb{N}}$ une suite de fonctions mesurables positives sur $(X, \mathcal{F}, \mu)$. Alors :
$$ \int_X \left( \sum_{k=0}^{\infty} u_k(x) \right) \, d\mu(x) = \sum_{k=0}^{\infty} \int_X u_k(x) \, d\mu(x) $$

#### Exemples concrets immédiats

Soit à évaluer l'intégrale sur $]0, 1[$ de la fonction $-\ln(1-x)$.
On sait que pour $x \in ]0, 1[$, on a le développement en série entière : $-\ln(1-x) = \sum_{k=1}^{\infty} \frac{x^k}{k}$.
Posons $u_k(x) = \frac{x^k}{k} \mathbf{1}_{]0, 1[}(x)$. Chaque fonction $u_k$ est mesurable et positive.
En appliquant le corollaire du théorème de Beppo Levi :
$$ \int_0^1 (-\ln(1-x)) \, dx = \sum_{k=1}^{\infty} \int_0^1 \frac{x^k}{k} \, dx $$
On calcule l'intégrale de $u_k$ :
$$ \int_0^1 \frac{x^k}{k} \, dx = \left[ \frac{x^{k+1}}{k(k+1)} \right]_0^1 = \frac{1}{k(k+1)} $$
La somme se télescope :
$$ \sum_{k=1}^{\infty} \frac{1}{k(k+1)} = \sum_{k=1}^{\infty} \left(\frac{1}{k} - \frac{1}{k+1}\right) = 1 $$
Ainsi, l'intégrale vaut exactement $1$. Le calcul est non seulement rigoureux, mais s'affranchit de toute notion de convergence uniforme (qui est d'ailleurs fausse au voisinage de $1$).

## 3. Démonstrations

### Preuve du Théorème de Convergence Monotone

Soit $(f_n)$ une suite croissante de fonctions mesurables positives convergeant ponctuellement vers $f$.
La mesurabilité de la limite $f$ découle du fait que la limite d'une suite de fonctions mesurables est mesurable.

**Étape 1 : Majoration immédiate**
Puisque $f_n \le f$ pour tout $n$, la croissance de l'intégrale de Lebesgue assure que pour tout $n \in \mathbb{N}$ :
$$ \int_X f_n \, d\mu \le \int_X f \, d\mu $$
La suite des intégrales $\left(\int_X f_n \, d\mu\right)$ étant croissante dans $[0, +\infty]$, elle admet une limite. En passant à la limite dans l'inégalité précédente, nous obtenons :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \le \int_X f \, d\mu $$

**Étape 2 : Minoration par des fonctions étagées**
Pour établir l'inégalité inverse, nous allons utiliser la définition de l'intégrale des fonctions positives par supremum sur les fonctions étagées.
Soit $\varphi$ une fonction étagée mesurable telle que $0 \le \varphi \le f$.
Fixons un paramètre $\alpha \in ]0, 1[$.
Pour chaque $n \in \mathbb{N}$, définissons l'ensemble mesurable :
$$ A_n = \{x \in X \mid f_n(x) \ge \alpha \varphi(x)\} $$
Comme $(f_n)$ est une suite croissante, la suite d'ensembles $(A_n)$ est croissante ($A_n \subset A_{n+1}$).
Montrons que $\bigcup_{n \in \mathbb{N}} A_n = X$.
Pour un point $x \in X$, si $f(x) = 0$, alors $\varphi(x) = 0$ et $f_n(x) \ge 0 = \alpha \varphi(x)$ pour tout $n$, donc $x \in A_0 \subset \bigcup A_n$.
Si $f(x) > 0$, puisque $\alpha < 1$, on a $\alpha \varphi(x) < f(x)$. Comme $\lim_{n \to \infty} f_n(x) = f(x)$, il existe un rang $N$ tel que pour $n \ge N$, $f_n(x) \ge \alpha \varphi(x)$. Ainsi $x \in A_N \subset \bigcup A_n$.
Dans tous les cas, $X = \bigcup_{n \in \mathbb{N}} A_n$.

Sur l'ensemble $A_n$, nous avons l'inégalité $f_n \ge \alpha \varphi \mathbf{1}_{A_n}$.
Par conséquent :
$$ \int_X f_n \, d\mu \ge \int_{A_n} f_n \, d\mu \ge \alpha \int_{A_n} \varphi \, d\mu $$
La fonction étagée $\varphi$ s'écrit $\varphi = \sum_{i=1}^m c_i \mathbf{1}_{E_i}$.
L'intégrale sur $A_n$ donne $\int_{A_n} \varphi \, d\mu = \sum_{i=1}^m c_i \mu(E_i \cap A_n)$.
Par continuité croissante de la mesure $\mu$, puisque $E_i \cap A_n$ croît vers $E_i \cap X = E_i$, nous avons :
$$ \lim_{n \to \infty} \mu(E_i \cap A_n) = \mu(E_i) $$
Il s'ensuit que :
$$ \lim_{n \to \infty} \int_{A_n} \varphi \, d\mu = \sum_{i=1}^m c_i \mu(E_i) = \int_X \varphi \, d\mu $$
En reprenant notre minoration et en passant à la limite sur $n$ :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \ge \alpha \int_X \varphi \, d\mu $$
Puisque ce résultat est valable pour tout $\alpha \in ]0, 1[$, on peut faire tendre $\alpha$ vers $1$ :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \ge \int_X \varphi \, d\mu $$

**Étape 3 : Conclusion par passage au supremum**
L'inégalité précédente étant vraie pour toute fonction étagée $\varphi \le f$, on passe au supremum sur l'ensemble de ces fonctions $\varphi$ :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \ge \sup_{\varphi \le f} \int_X \varphi \, d\mu = \int_X f \, d\mu $$
Les deux inégalités (étapes 1 et 3) forcent l'égalité :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu = \int_X f \, d\mu $$
Le théorème est ainsi intégralement prouvé.

### Preuve du Théorème d'intégration terme à terme

Considérons la suite des sommes partielles $S_n(x) = \sum_{k=0}^n u_k(x)$.
Puisque les $u_k$ sont mesurables et positives, $(S_n)$ est une suite de fonctions mesurables positives.
De plus, la suite $(S_n)$ est croissante car $S_{n+1}(x) = S_n(x) + u_{n+1}(x) \ge S_n(x)$.
Par le théorème de convergence monotone appliqué à $(S_n)$ :
$$ \int_X \left( \lim_{n \to \infty} S_n(x) \right) \, d\mu = \lim_{n \to \infty} \int_X S_n(x) \, d\mu $$
Par linéarité de l'intégrale pour les sommes finies :
$$ \lim_{n \to \infty} \int_X \sum_{k=0}^n u_k(x) \, d\mu = \lim_{n \to \infty} \sum_{k=0}^n \int_X u_k(x) \, d\mu = \sum_{k=0}^{\infty} \int_X u_k(x) \, d\mu $$
L'égalité est ainsi démontrée.

## 4. Applications en Physique, Logique & Intelligence Artificielle

### Probabilités et Espérances
En théorie des probabilités (qui repose entièrement sur la théorie de la mesure, suivant l'axiomatisation de Kolmogorov), l'intégrale par rapport à une mesure de probabilité $\mathbb{P}$ est précisément l'espérance mathématique $\mathbb{E}$. Le théorème de convergence monotone assure que pour une suite croissante de variables aléatoires positives $X_n$, on a $\mathbb{E}[\lim_{n \to \infty} X_n] = \lim_{n \to \infty} \mathbb{E}[X_n]$. Cela permet de définir proprement l'espérance de temps d'arrêt ou de sommes infinies de variables aléatoires (comme dans l'étude des processus de Poisson).

### Optimisation et Machine Learning (Fonctions de risque empirique)
Dans le contexte de l'Intelligence Artificielle, et plus particulièrement en théorie de l'apprentissage statistique (Statistical Learning Theory), on cherche à minimiser une fonction de risque définie par une espérance : $\mathcal{R}(h) = \mathbb{E}_{(x,y) \sim P}[L(h(x), y)]$.
Souvent, ce risque est approché par une suite de limites. Si nous entraînons une architecture de type perceptron multicouche, où le modèle gagne en complexité via une série d'approximations successives monotones (par exemple, dans les méthodes de boosting où les classifieurs faibles s'ajoutent positivement pour former un estimateur robuste), la convergence du risque attendu est directement garantie par les théorèmes d'interversion de Beppo Levi.
La garantie que le risque limite correspond à la limite des risques des architectures successives permet de valider formellement la convergence de l'algorithme d'apprentissage vers une solution généralisable.

### Physique Théorique : Mécanique Statistique et Thermodynamique
Dans l'étude des gaz parfaits ou de la mécanique quantique statistique, la fonction de partition $\mathcal{Z}$ s'exprime comme une somme ou une intégrale infinie sur tous les états possibles du système (les états d'énergie). La manipulation de ces objets macroscopiques à partir d'états microscopiques requiert l'intégration de séries exponentielles. Le théorème d'intégration terme à terme, fruit direct de Beppo Levi, fournit l'armature logique autorisant les physiciens à intervertir sommes discrètes sur les niveaux d'énergie et intégrales de phase.