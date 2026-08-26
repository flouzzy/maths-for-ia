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

## 1. Présentation du concept clé

Historiquement, la construction de l'intégrale de Lebesgue est descendante : on définit d'abord l'intégrale pour des fonctions en escalier très simples (les fonctions étagées), puis on généralise cette notion à toutes les fonctions mesurables positives par un passage à la borne supérieure (supremum). Cette approche permet de s'affranchir des limitations de l'intégrale de Riemann, en intégrant des fonctions hautement discontinues (telle la fonction indicatrice de $\mathbb{Q}$).

## 2. Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### A. Intégrale des Fonctions Simples

Soit $\mathcal{S}_+$ l'ensemble des fonctions simples (étagées) positives sur $X$.
Une fonction $s \in \mathcal{S}_+$ s'écrit $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ avec $a_i \ge 0$.

> **Définition 1 :** L'intégrale de la fonction simple $s$ par rapport à $\mu$ est :
> $$\int_X s d\mu = \sum_{i=1}^n a_i \mu(A_i)$$
> (On utilise la convention $0 \cdot \infty = 0$).


### Exemples Concrets Immédiats

**Exemple 1 : Fonction indicatrice simple.**
Soit $X = \mathbb{R}$ muni de la mesure de Lebesgue $\lambda$. Soit $s = 5 \mathbf{1}_{[0, 2]}$.
L'ensemble $A_1 = [0, 2]$ a pour mesure $\lambda([0, 2]) = 2$.
L'intégrale est : $\int_\mathbb{R} s d\lambda = 5 \times 2 = 10$.

**Exemple 2 : Combinaison linéaire d'indicatrices disjointes.**
Soit $s = 2 \mathbf{1}_{[0, 1]} + 7 \mathbf{1}_{[3, 4]}$. Les intervalles sont disjoints.
$\int_\mathbb{R} s d\lambda = 2 \times \lambda([0, 1]) + 7 \times \lambda([3, 4]) = 2 \times 1 + 7 \times 1 = 9$.

**Exemple 3 : Combinaison linéaire d'indicatrices non disjointes.**
Soit $s = 3 \mathbf{1}_{[0, 3]} + 4 \mathbf{1}_{[2, 5]}$. On réécrit $s$ sous forme canonique (ensembles disjoints) :
Sur $[0, 2[$, $s(x) = 3$.
Sur $[2, 3]$, $s(x) = 3 + 4 = 7$.
Sur $]3, 5]$, $s(x) = 4$.
Ailleurs, $s(x) = 0$.
Ainsi, $\int_\mathbb{R} s d\lambda = 3 \times \lambda([0, 2[) + 7 \times \lambda([2, 3]) + 4 \times \lambda(]3, 5]) = 3 \times 2 + 7 \times 1 + 4 \times 2 = 6 + 7 + 8 = 21$.
Vérifions par linéarité (qui sera démontrée plus tard) : $3 \times 3 + 4 \times 3 = 9 + 12 = 21$.

**Exemple 4 : Mesure de Dirac.**
Soit $X = \mathbb{R}$ muni de la mesure de Dirac en zéro, notée $\delta_0$.
Soit $s = 8 \mathbf{1}_{[-1, 1]} + 2 \mathbf{1}_{[2, 3]}$.
On a $\delta_0([-1, 1]) = 1$ car $0 \in [-1, 1]$, et $\delta_0([2, 3]) = 0$ car $0 \notin [2, 3]$.
L'intégrale est $\int_\mathbb{R} s d\delta_0 = 8 \times 1 + 2 \times 0 = 8$. Ceci correspond bien à $s(0) = 8$.

**Exemple 5 : Fonction constante sur un ensemble de mesure infinie.**
Soit $s = 3 \mathbf{1}_{[0, +\infty[}$ pour la mesure de Lebesgue.
$\lambda([0, +\infty[) = +\infty$.
L'intégrale est $\int_\mathbb{R} s d\lambda = 3 \times (+\infty) = +\infty$.

**Exemple 6 : Zéro sur un ensemble de mesure infinie.**
Soit $s = 0 \mathbf{1}_\mathbb{R}$. Par convention dans la théorie de la mesure, $0 \times \infty = 0$.
Donc $\int_\mathbb{R} s d\lambda = 0 \times \lambda(\mathbb{R}) = 0$.

### B. Intégrale des Fonctions Mesurables Positives

Soit $\mathcal{M}_+$ l'ensemble des fonctions mesurables de $X$ dans $[0, +\infty]$.

> **Définition 2 (Intégrale de Lebesgue) :**
> Pour tout $f \in \mathcal{M}_+$, on définit :
> $$\int_X f d\mu = \sup \left\lbrace \int_X s d\mu \mid s \in \mathcal{S}_+, 0 \le s \le f \right\rbrace$$
> Cette valeur appartient à $[0, +\infty]$. Si elle est finie, on dit que $f$ est **intégrable**.

\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Axes
  \draw[->] (-0.5, 0) -- (4, 0) node[right] {$x$};
  \draw[->] (0, -0.5) -- (0, 3) node[above] {$f(x)$};

  % Courbe
  \draw[thick, blue] (0, 0) .. controls (1, 2) and (2, 0.5) .. (3, 2.5);
  \node[blue, right] at (3, 2.5) {$f \in \mathcal{M}_+$};

  % Fonction simple s <= f
  \draw[thick, red] (0, 0) -- (0.8, 0) -- (0.8, 0.5) -- (1.5, 0.5) -- (1.5, 1) -- (2.2, 1) -- (2.2, 0.8) -- (2.8, 0.8) -- (2.8, 1.8) -- (3, 1.8) -- (3, 0);

  % Remplissage
  \fill[red, opacity=0.2] (0, 0) rectangle (0.8, 0);
  \fill[red, opacity=0.2] (0.8, 0) rectangle (1.5, 0.5);
  \fill[red, opacity=0.2] (1.5, 0) rectangle (2.2, 1);
  \fill[red, opacity=0.2] (2.2, 0) rectangle (2.8, 0.8);
  \fill[red, opacity=0.2] (2.8, 0) rectangle (3, 1.8);

  \node[red] at (1.5, 0.25) {$s \le f$};
\end{tikzpicture}
\end{center}


### C. Propriétés Immédiates

> **Théorème :**
> 1. **Positivité :** $\int f d\mu \ge 0$.
> 2. **Croissance :** Si $f \le g$, alors $\int f \le \int g$.
> 3. **Homogénéité :** $\int \alpha f d\mu = \alpha \int f d\mu$ pour $\alpha \ge 0$.

## 3. Démonstrations

### Démonstration : Relation entre intégrale et ensembles de mesure nulle

Montrons rigoureusement que si $f \in \mathcal{M}_+$ et $\int f d\mu = 0$, alors $f = 0$ presque partout (c'est-à-dire que $\mu(\{x \in X \mid f(x) > 0\}) = 0$).

**Étape 1 : Cadre et définition des ensembles de niveau.**
Soit $A = \{x \in X \mid f(x) > 0\}$. Nous voulons prouver que $\mu(A) = 0$.
Remarquons que si $f(x) > 0$, alors il existe nécessairement un entier $n \ge 1$ tel que $f(x) \ge \frac{1}{n}$.
Posons, pour tout $n \in \mathbb{N}^*$, l'ensemble de niveau :
$$A_n = \left\{x \in X \mid f(x) \ge \frac{1}{n}\right\}$$
Puisque $f$ est une fonction mesurable, chaque ensemble $A_n$ appartient à la tribu $\mathcal{F}$.

**Étape 2 : Décomposition de l'ensemble strict de positivité.**
L'ensemble $A$ s'écrit comme la réunion dénombrable (croissante) des ensembles $A_n$ :
$$A = \bigcup_{n=1}^\infty A_n$$

**Étape 3 : Minoration par des fonctions simples.**
Sur chaque sous-ensemble $A_n$, nous avons par définition $f(x) \ge \frac{1}{n}$.
Par conséquent, nous pouvons minorer globalement la fonction $f$ par une fonction simple impliquant l'indicatrice de $A_n$ :
$$f \ge \frac{1}{n} \mathbf{1}_{A_n}$$
Cette inégalité est vraie pour tout $x \in X$. Si $x \notin A_n$, alors $f(x) \ge 0$, ce qui est satisfait puisque $f \in \mathcal{M}_+$.

**Étape 4 : Utilisation de la croissance de l'intégrale.**
Par la propriété de croissance de l'intégrale de Lebesgue, si $g \le f$, alors $\int g d\mu \le \int f d\mu$.
En prenant $g = \frac{1}{n} \mathbf{1}_{A_n}$, qui est une fonction simple, nous obtenons :
$$\int_X \left(\frac{1}{n} \mathbf{1}_{A_n}\right) d\mu \le \int_X f d\mu$$
Par définition de l'intégrale d'une fonction simple, le terme de gauche vaut exactement $\frac{1}{n} \mu(A_n)$.
Donc :
$$\frac{1}{n} \mu(A_n) \le \int_X f d\mu$$

**Étape 5 : Exploitation de l'hypothèse principale.**
Par hypothèse, l'intégrale de $f$ est nulle : $\int_X f d\mu = 0$.
Il s'ensuit que pour tout entier $n \ge 1$ :
$$\frac{1}{n} \mu(A_n) \le 0$$
Puisque la mesure $\mu(A_n)$ est par définition positive ou nulle, et que $\frac{1}{n} > 0$, la seule solution possible est :
$$\mu(A_n) = 0 \quad \text{pour tout } n \ge 1$$

**Étape 6 : Conclusion par sous-additivité dénombrable.**
Nous savons que $\mu$ est une mesure (donc $\sigma$-sous-additive). La mesure de l'union dénombrable est majorée par la somme des mesures :
$$\mu(A) = \mu\left( \bigcup_{n=1}^\infty A_n \right) \le \sum_{n=1}^\infty \mu(A_n)$$
Puisque chaque terme de la somme est nul, nous concluons que :
$$\mu(A) \le \sum_{n=1}^\infty 0 = 0$$
Comme une mesure est toujours positive, $\mu(A) = 0$. Ainsi, $f = 0$ presque partout.

## 4. Application en Intelligence Artificielle

- **Le Pont Théorique :** L'intégrale de Lebesgue permet de définir l'**Espérance mathématique** de manière universelle, que la variable soit discrète, continue ou mixte. $\mathbb{E}[X] = \int_\Omega X(\omega) dP(\omega)$.
- **Example Concret :**
    - **Calcul de la Perte Attendue (Expected Loss) :** En IA, on minimise $L(\theta) = \int \ell(x, y, \theta) d\mathbb{P}(x, y)$. La mesure $\mathbb{P}$ représente nos données. Lebesgue nous permet de calculer cette intégrale même si nos données sont un mélange de catégories (discret) et de mesures physiques (continu).
    - **Mesures de similarité entre distributions :** La divergence de Jensen-Shannon ou la divergence KL sont définies par des intégrales de Lebesgue. Ces mesures sont le cœur des modèles génératifs et du clustering.
    - **Filtrage de Kalman :** La mise à jour des croyances dans un système dynamique repose sur l'intégration de fonctions de vraisemblance, souvent sur des espaces de grande dimension.

## 5. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 65 (Fonctions mesurables).md]], [[Jalon 63 (Définition axiomatique d'une mesure).md]]
- **Concepts Futurs dépendants :** [[Jalon 67 (Démonstration du théorème de convergence monotone).md]], [[Jalon 73 (Définition des espaces Lp).md]]
