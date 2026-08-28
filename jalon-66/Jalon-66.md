---
uuid: "jalon-66"
title: "Intégrale de Lebesgue pour les fonctions positives"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 65 (Fonctions mesurables).md]]"
next: "[[Jalon 67 (Démonstration du théorème de convergence monotone).md]]"
---

# Intégrale de Lebesgue pour les fonctions positives

## Introduction

Imaginez que vous vouliez calculer l'aire totale de confiture étalée sur une table.
La confiture n'est pas étalée de manière régulière : il y a des endroits où elle est épaisse et d'autres où elle est très fine.
Au lieu de découper la table en carrés (méthode de Riemann), vous décidez d'utiliser des tampons de différentes tailles. Chaque tampon a une épaisseur de confiture précise (une valeur $a_i$).
Vous cherchez tous les endroits où l'épaisseur est exactement $a_i$ (l'ensemble $A_i$), vous mesurez la surface de ces endroits ($\mu(A_i)$), et vous multipliez par l'épaisseur.
En faisant cela pour toutes les épaisseurs possibles et en additionnant, vous obtenez le volume total de confiture.

Pour pouvoir intégrer des fonctions qui présentent de fortes irrégularités (comme la fonction indicatrice des rationnels, dite de Dirichlet). La construction de Lebesgue procède par approximations ascendantes : on définit l'intégrale pour des fonctions dites "simples" en premier lieu, puis on généralise aux fonctions mesurables positives par un passage au supremum.

On remplit l'espace sous la courbe par des "rectangles horizontaux" qui capturent l'ensemble des points du domaine où la fonction dépasse une certaine valeur, au lieu des rectangles verticaux de Riemann.

## Définitions, Théorèmes et Exemples Concrets

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré, où $X$ est un ensemble, $\mathcal{F}$ une tribu sur $X$, et $\mu$ une mesure positive.

### Intégrale des Fonctions Simples

Soit $\mathcal{S}_+$ l'ensemble des fonctions simples (ou étagées) positives sur $X$.
Une fonction $s \in \mathcal{S}_+$ s'écrit de manière unique (forme canonique) :
$$s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$$
avec $a_i \ge 0$ des réels distincts, et les $A_i = s^{-1}(\{a_i\}) \in \mathcal{F}$ formant une partition de $X$.

**Définition (Intégrale d'une fonction simple) :** L'intégrale de la fonction simple $s$ par rapport à $\mu$ est définie par :
$$\int_X s \, d\mu = \sum_{i=1}^n a_i \mu(A_i)$$
*(On utilise la convention $0 \cdot \infty = 0$ pour traiter le cas où une valeur nulle est prise sur un ensemble de mesure infinie).*

**Exemples de calcul pour des fonctions simples :**
1. **Mesure de Lebesgue sur $[0,1]$ :** Si $s(x) = 3 \cdot \mathbf{1}_{[0, 1/2]}(x) + 5 \cdot \mathbf{1}_{]1/2, 1]}(x)$, alors $\int s \, d\lambda = 3 \cdot \lambda([0, 1/2]) + 5 \cdot \lambda(]1/2, 1]) = 3 \cdot \frac{1}{2} + 5 \cdot \frac{1}{2} = 4$.
2. **Mesure de Dirac en 0 :** Soit $\delta_0$ sur $\mathbb{R}$. Si $s(x) = 7 \cdot \mathbf{1}_{[-1, 1]}(x) + 2 \cdot \mathbf{1}_{]1, 3]}(x)$, on a $\int s \, d\delta_0 = 7 \cdot \delta_0([-1, 1]) + 2 \cdot \delta_0(]1, 3]) = 7 \cdot 1 + 2 \cdot 0 = 7$.
3. **Mesure de comptage sur $\mathbb{N}$ :** Si $s(n) = 4 \cdot \mathbf{1}_{\{2, 4, 6\}}(n)$, alors $\int s \, d\mu = 4 \cdot \mu(\{2, 4, 6\}) = 4 \cdot 3 = 12$.
4. **Fonction simple sur un espace fini :** Soit $X = \{a, b, c\}$ avec $\mu(\{a\})=2, \mu(\{b\})=3, \mu(\{c\})=1$. Pour $s(a)=1, s(b)=1, s(c)=4$, la forme canonique est $1 \cdot \mathbf{1}_{\{a,b\}} + 4 \cdot \mathbf{1}_{\{c\}}$. Son intégrale est $1 \cdot (2+3) + 4 \cdot 1 = 9$.
5. **Ensemble de mesure infinie :** Sur $\mathbb{R}$ muni de Lebesgue $\lambda$, si $s = 2 \cdot \mathbf{1}_{[0, +\infty[}$, alors $\int s \, d\lambda = 2 \cdot \lambda([0, +\infty[) = 2 \cdot \infty = \infty$.
6. **Convention $0 \cdot \infty = 0$ :** Si $s = 0 \cdot \mathbf{1}_{\mathbb{R}}$, alors $\int s \, d\lambda = 0 \cdot \lambda(\mathbb{R}) = 0 \cdot \infty = 0$.

\begin{tikzpicture}[scale=1.5]
  % Axes
  \draw[->] (-0.5,0) -- (4,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,3) node[above] {$y$};

  % Graphe fonction simple
  \draw[thick, blue] (0, 1) -- (1, 1);
  \draw[thick, blue] (1, 2.5) -- (2.5, 2.5);
  \draw[thick, blue] (2.5, 1.5) -- (3.5, 1.5);

  % Lignes pointillees
  \draw[dashed] (1,0) -- (1,2.5);
  \draw[dashed] (2.5,0) -- (2.5,2.5);
  \draw[dashed] (3.5,0) -- (3.5,1.5);
  \draw[dashed] (0,1) -- (1,1);
  \draw[dashed] (0,2.5) -- (1,2.5);
  \draw[dashed] (0,1.5) -- (2.5,1.5);

  % Valeurs
  \node[below] at (0.5, 0) {$A_1$};
  \node[below] at (1.75, 0) {$A_2$};
  \node[below] at (3, 0) {$A_3$};

  \node[left] at (0, 1) {$a_1$};
  \node[left] at (0, 2.5) {$a_2$};
  \node[left] at (0, 1.5) {$a_3$};

  % Rectangles
  \fill[blue, opacity=0.1] (0,0) rectangle (1,1);
  \fill[blue, opacity=0.1] (1,0) rectangle (2.5,2.5);
  \fill[blue, opacity=0.1] (2.5,0) rectangle (3.5,1.5);

  \node at (2, -0.7) {L'intégrale est la somme des aires : $a_1\mu(A_1) + a_2\mu(A_2) + a_3\mu(A_3)$};
\end{tikzpicture}

### Intégrale des Fonctions Mesurables Positives

Soit $\mathcal{M}_+$ l'ensemble des fonctions mesurables de $X$ dans $[0, +\infty]$.

**Définition (Intégrale de Lebesgue) :** Pour tout $f \in \mathcal{M}_+$, on définit :
$$\int_X f \, d\mu = \sup \left\lbrace \int_X s \, d\mu \mid s \in \mathcal{S}_+, \ 0 \le s \le f \right\rbrace$$
Cette valeur appartient à $[0, +\infty]$. Si elle est finie, on dit que $f$ est **intégrable**.

**Théorème (Propriétés de l'intégrale) :** Soient $f, g \in \mathcal{M}_+$ et $\alpha \ge 0$.
1. **Positivité :** $\int_X f \, d\mu \ge 0$.
2. **Croissance :** Si $f \le g$ presque partout, alors $\int_X f \, d\mu \le \int_X g \, d\mu$.
3. **Homogénéité positive :** $\int_X \alpha f \, d\mu = \alpha \int_X f \, d\mu$.
*(La linéarité complète nécessite le théorème de convergence monotone, abordé au prochain jalon).*

**Exemples concrets d'intégrales de fonctions mesurables :**
1. **Fonction indicatrice de Dirichlet :** $f = \mathbf{1}_{\mathbb{Q}}$ sur $[0,1]$ avec la mesure de Lebesgue $\lambda$. Puisque $f$ est une fonction simple (valant 1 sur $\mathbb{Q} \cap [0,1]$ de mesure nulle, et 0 ailleurs), $\int f \, d\lambda = 1 \cdot \lambda(\mathbb{Q} \cap [0,1]) = 1 \cdot 0 = 0$.
2. **Fonction continue positive sur un segment :** Soit $f(x) = x^2$ sur $[0, 1]$. L'intégrale de Lebesgue coïncide avec l'intégrale de Riemann : $\int_{[0,1]} x^2 \, d\lambda = \left[ \frac{x^3}{3} \right]_0^1 = \frac{1}{3}$.
3. **Série comme intégrale de Lebesgue :** Sur $\mathbb{N}$ avec la mesure de comptage $\mu_c$, si $f(n) = \frac{1}{2^n}$, l'intégrale est la somme de la série : $\int_{\mathbb{N}} f \, d\mu_c = \sum_{n=0}^\infty \frac{1}{2^n} = 2$.
4. **Fonction tendant vers l'infini :** Soit $f(x) = \frac{1}{\sqrt{x}}$ sur $]0, 1]$. Bien que $f$ ne soit pas bornée, elle est mesurable positive et $\int_{]0,1]} \frac{1}{\sqrt{x}} \, d\lambda = [2\sqrt{x}]_0^1 = 2$. Elle est donc intégrable.
5. **Intégrale divergente :** Soit $f(x) = \frac{1}{x}$ sur $]0, 1]$. L'intégrale vaut $\int_{]0,1]} \frac{1}{x} \, d\lambda = [\ln(x)]_0^1 = +\infty$. Elle n'est pas intégrable.
6. **Modification sur un ensemble de mesure nulle :** Soit $g(x) = x^2$ si $x \notin \mathbb{Q}$ et $g(x) = 17$ si $x \in \mathbb{Q}$, sur $[0,1]$. Puisque $g = f$ (où $f(x)=x^2$) presque partout, $\int_{[0,1]} g \, d\lambda = \int_{[0,1]} f \, d\lambda = \frac{1}{3}$.

\begin{tikzpicture}[scale=1.5]
  % Axes
  \draw[->] (-0.5,0) -- (4,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,3.5) node[above] {$y$};

  % Courbe
  \draw[thick, red, domain=0:3.5, samples=100] plot (\x, {0.2*\x*\x + 0.5});
  \node[red, right] at (3.5, 2.95) {$f(x)$};

  % Approximation par des fonctions simples (s_n <= f)
  \fill[blue, opacity=0.1] (0,0) rectangle (1, 0.5);
  \fill[blue, opacity=0.2] (1,0) rectangle (2, 0.7);
  \fill[blue, opacity=0.3] (2,0) rectangle (2.8, 1.3);
  \fill[blue, opacity=0.4] (2.8,0) rectangle (3.5, 2.06);

  \draw[blue, thick] (0, 0.5) -- (1, 0.5);
  \draw[blue, thick] (1, 0.7) -- (2, 0.7);
  \draw[blue, thick] (2, 1.3) -- (2.8, 1.3);
  \draw[blue, thick] (2.8, 2.06) -- (3.5, 2.06);

  \draw[dashed, blue] (1, 0) -- (1, 0.5);
  \draw[dashed, blue] (2, 0) -- (2, 1.3);
  \draw[dashed, blue] (2.8, 0) -- (2.8, 2.06);
  \draw[dashed, blue] (3.5, 0) -- (3.5, 2.06);

  \node at (1.75, -0.5) {L'intégrale de $f$ est le supremum des intégrales de fonctions simples $s \le f$};
\end{tikzpicture}


## Démonstrations

### Démonstration : Relation entre intégrale nulle et nullité presque partout

Soit $f \in \mathcal{M}_+$. Montrons que $\int_X f \, d\mu = 0 \iff f = 0$ $\mu$-presque partout.

**Sens direct ($\implies$) :** Supposons $\int_X f \, d\mu = 0$.
Soit $A = \{x \in X \mid f(x) > 0\}$. Nous devons prouver que $\mu(A) = 0$.
Pour tout entier $n \ge 1$, définissons $A_n = \left\{x \in X \mid f(x) \ge \frac{1}{n}\right\}$.
On observe que $A = \bigcup_{n=1}^\infty A_n$.
Sur l'ensemble $A_n$, nous avons $f(x) \ge \frac{1}{n}$. Ainsi, la fonction simple $s_n = \frac{1}{n} \mathbf{1}_{A_n}$ vérifie $0 \le s_n \le f$ sur $X$.
Par croissance de l'intégrale :
$$\int_X f \, d\mu \ge \int_X s_n \, d\mu = \frac{1}{n} \mu(A_n)$$
Puisque $\int_X f \, d\mu = 0$, nous avons $0 \ge \frac{1}{n} \mu(A_n)$. La mesure étant positive, cela implique $\mu(A_n) = 0$ pour tout $n \ge 1$.
Par $\sigma$-sous-additivité de la mesure, nous concluons :
$$\mu(A) = \mu\left( \bigcup_{n=1}^\infty A_n \right) \le \sum_{n=1}^\infty \mu(A_n) = \sum_{n=1}^\infty 0 = 0$$
Donc $\mu(A) = 0$, ce qui signifie que $f = 0$ presque partout.

**Sens réciproque ($\impliedby$) :** Supposons que $f = 0$ $\mu$-presque partout.
Soit $s \in \mathcal{S}_+$ telle que $0 \le s \le f$. Écrivons $s = \sum_{i=1}^k a_i \mathbf{1}_{B_i}$ dans sa forme canonique.
Puisque $s \le f$ et $f = 0$ p.p., pour tout $x \in B_i$ où $a_i > 0$, on doit avoir $f(x) \ge a_i > 0$. L'ensemble des tels $x$ est inclus dans l'ensemble des points où $f(x) > 0$, qui est de mesure nulle. Ainsi, pour chaque $i$ tel que $a_i > 0$, $\mu(B_i) = 0$.
L'intégrale de $s$ est :
$$\int_X s \, d\mu = \sum_{i=1}^k a_i \mu(B_i) = \sum_{a_i > 0} a_i \cdot 0 + \sum_{a_i = 0} 0 \cdot \mu(B_i) = 0$$
Le supremum sur toutes ces fonctions simples $s$ est donc 0, d'où $\int_X f \, d\mu = 0$.


## Applications en Intelligence Artificielle

- **Calcul de la Perte Attendue (Expected Loss) :** En apprentissage automatique, le risque statistique est formulé comme l'espérance mathématique de la fonction de perte : $L(\theta) = \int \ell(x, y, \theta) \, d\mathbb{P}(x, y)$. La théorie de Lebesgue offre le cadre adéquat pour calculer cette intégrale de manière unifiée, que la loi de probabilité sous-jacente $\mathbb{P}$ soit discrète, absolument continue par rapport à la mesure de Lebesgue, ou une mixture complexe des deux.
- **Divergences en Modélisation Générative :** Les méthodes avancées comme les réseaux antagonistes génératifs (GANs) ou les modèles de diffusion cherchent à minimiser une divergence entre la distribution des données réelles et celle du modèle (ex: Divergence de Kullback-Leibler). La formulation de ces divergences repose intrinsèquement sur des intégrales de Lebesgue par rapport à des mesures de probabilité sur des espaces de grande dimension (images, textes).
- **Processus Stochastiques et Filtrage :** Le filtrage de Kalman et ses variantes non linéaires nécessitent l'intégration de densités de transition. Le cadre de Lebesgue garantit la stabilité et l'existence des espérances conditionnelles calculées à chaque étape du filtre.
