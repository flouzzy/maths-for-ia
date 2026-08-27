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

# Jalon 66 : Intégrale de Lebesgue pour les fonctions positives

## 1. Genèse et Intuition Géométrique

La construction de l'intégrale de Lebesgue repose sur une approche conceptuellement distincte de celle de Riemann. Alors que Riemann découpe le domaine de définition (l'axe des abscisses) en petits intervalles, Lebesgue choisit de partitionner l'espace d'arrivée (l'axe des ordonnées). Cette inversion de perspective permet d'intégrer des fonctions présentant un comportement très irrégulier, telles que la fonction caractéristique des rationnels (fonction de Dirichlet), qui n'est pas intégrable au sens de Riemann.

L'idée centrale est de construire l'intégrale progressivement : d'abord pour des fonctions très simples prenant un nombre fini de valeurs (les fonctions étagées), puis d'étendre cette définition à toute fonction mesurable positive par un processus de passage à la limite supérieure.

\begin{center}
\begin{tikzpicture}[scale=1]
  % Axes
  \draw[->] (-0.5, 0) -- (6, 0) node[right] {$x$};
  \draw[->] (0, -0.5) -- (0, 4) node[above] {$y$};

  % Courbe approximée
  \draw[thick, blue] (0,0.5) to[out=20,in=180] (2,3) to[out=0,in=150] (4,1.5) to[out=-30,in=180] (5.5,2.5);

  % Fonction étagée s(x)
  \fill[red, opacity=0.3] (0,0) rectangle (1,0.5);
  \draw[red, thick] (0,0.5) -- (1,0.5);

  \fill[red, opacity=0.3] (1,0) rectangle (1.8, 1.5);
  \draw[red, thick] (1,1.5) -- (1.8,1.5);
  \draw[red, dashed] (1,0.5) -- (1,1.5);

  \fill[red, opacity=0.3] (1.8,0) rectangle (3, 2.5);
  \draw[red, thick] (1.8,2.5) -- (3,2.5);
  \draw[red, dashed] (1.8,1.5) -- (1.8,2.5);

  \fill[red, opacity=0.3] (3,0) rectangle (4.5, 1.2);
  \draw[red, thick] (3,1.2) -- (4.5,1.2);
  \draw[red, dashed] (3,2.5) -- (3,1.2);

  \fill[red, opacity=0.3] (4.5,0) rectangle (5.5, 2.0);
  \draw[red, thick] (4.5,2.0) -- (5.5,2.0);
  \draw[red, dashed] (4.5,1.2) -- (4.5,2.0);

  \node[red] at (2.5, 1.2) {$s \le f$};
  \node[blue] at (5, 3.2) {$y = f(x)$};
\end{tikzpicture}
\end{center}

## 2. Définitions, Théorèmes et Exemples Numériques

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Intégrale des Fonctions Étages

On note $\mathcal{E}_+$ l'ensemble des fonctions étagées mesurables positives sur $X$. Une fonction $s \in \mathcal{E}_+$ peut s'écrire sous forme canonique :
$$s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$$
où les $A_i \in \mathcal{F}$ forment une partition de $X$, et $a_i \ge 0$ sont les valeurs distinctes prises par $s$.

> **Définition (Intégrale d'une fonction étagée) :** L'intégrale de la fonction étagée $s$ par rapport à la mesure $\mu$ est définie par :
> $$\int_X s \, d\mu = \sum_{i=1}^n a_i \mu(A_i)$$
> avec la convention stricte que $0 \cdot (+\infty) = 0$.

**Exemple Calculatoire Immédiat :**
Sur l'espace $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ où $\lambda$ est la mesure de Lebesgue, considérons la fonction :
$$s(x) = 3 \cdot \mathbf{1}_{[0, 2]}(x) + 5 \cdot \mathbf{1}_{[4, 5]}(x)$$
L'intégrale vaut :
$$\int_{\mathbb{R}} s \, d\lambda = 3 \cdot \lambda([0, 2]) + 5 \cdot \lambda([4, 5]) = 3 \cdot 2 + 5 \cdot 1 = 11$$

**Exemple sur une mesure de probabilité :**
Soit un dé équilibré. L'espace est $X = \{1, 2, 3, 4, 5, 6\}$ muni de la mesure $\mathbb{P}(A) = \frac{\text{Card}(A)}{6}$.
Soit la fonction gain $G(x) = 10 \cdot \mathbf{1}_{\{6\}}(x) + 2 \cdot \mathbf{1}_{\{1,2,3,4,5\}}(x)$.
$$\int_X G \, d\mathbb{P} = 10 \cdot \mathbb{P}(\{6\}) + 2 \cdot \mathbb{P}(\{1,2,3,4,5\}) = 10 \cdot \frac{1}{6} + 2 \cdot \frac{5}{6} = \frac{20}{6} = \frac{10}{3}$$
L'intégrale de Lebesgue correspond ici parfaitement à l'espérance mathématique.

### Intégrale des Fonctions Mesurables Positives

Soit $\mathcal{M}_+$ l'ensemble des fonctions mesurables de $X$ dans $[0, +\infty]$.

> **Définition (Intégrale de Lebesgue) :**
> Pour toute fonction $f \in \mathcal{M}_+$, on définit son intégrale par :
> $$\int_X f \, d\mu = \sup \left\lbrace \int_X s \, d\mu \ \mid \ s \in \mathcal{E}_+, \ s \le f \right\rbrace$$
> Cette valeur appartient à $[0, +\infty]$. Si cette valeur est finie, on dit que $f$ est intégrable sur $X$.

**Exemple de la fonction de Dirichlet :**
Soit $f = \mathbf{1}_{\mathbb{Q} \cap [0,1]}$. $f \in \mathcal{M}_+$.
$f$ ne prend que les valeurs 0 et 1, c'est donc elle-même une fonction étagée sur le segment $[0, 1]$.
$$\int_{[0,1]} f \, d\lambda = 1 \cdot \lambda(\mathbb{Q} \cap [0,1]) + 0 \cdot \lambda(([0,1] \setminus \mathbb{Q}))$$
Puisque les rationnels sont dénombrables, $\lambda(\mathbb{Q}) = 0$. Ainsi :
$$\int_{[0,1]} f \, d\lambda = 1 \cdot 0 + 0 = 0$$

## 3. Démonstrations Pas-à-Pas

### Théorème : Annulation de l'intégrale

> **Théorème :** Soit $f \in \mathcal{M}_+$.
> $\int_X f \, d\mu = 0 \iff f = 0$ presque partout ($\mu$-p.p).

**Démonstration Complète :**

\textbf{Sens Réciproque ($\impliedby$) :}
Supposons que $f = 0$ $\mu$-p.p. Cela signifie que l'ensemble $N = \{x \in X \mid f(x) > 0\}$ est de mesure nulle : $\mu(N) = 0$.
Soit $s \in \mathcal{E}_+$ telle que $0 \le s \le f$.
Puisque $s \le f$, alors $\{x \mid s(x) > 0\} \subset \{x \mid f(x) > 0\} = N$.
Ainsi, $s$ peut s'écrire $s = \sum_{i=1}^k a_i \mathbf{1}_{A_i}$, où $a_i > 0 \implies A_i \subset N$, ce qui impose $\mu(A_i) = 0$.
Par conséquent, $\int_X s \, d\mu = \sum a_i \mu(A_i) = 0$.
Par passage au supremum sur toutes ces fonctions étagées, on obtient bien $\int_X f \, d\mu = 0$.

\textbf{Sens Direct ($\implies$) :}
Supposons $\int_X f \, d\mu = 0$.
Considérons les ensembles $A_n = \left\lbrace x \in X \mid f(x) \ge \frac{1}{n} \right\rbrace$ pour tout $n \in \mathbb{N}^*$.
Définissons la fonction étagée $s_n = \frac{1}{n} \mathbf{1}_{A_n}$.
Par construction, pour tout $x \in A_n$, $f(x) \ge \frac{1}{n} = s_n(x)$. Pour $x \notin A_n$, $s_n(x) = 0 \le f(x)$.
Donc $0 \le s_n \le f$ partout sur $X$.
Par définition du supremum de l'intégrale de Lebesgue :
$$\int_X s_n \, d\mu \le \int_X f \, d\mu = 0$$
Or $\int_X s_n \, d\mu = \frac{1}{n} \mu(A_n)$.
On a donc $\frac{1}{n} \mu(A_n) \le 0$, ce qui, la mesure étant positive, impose $\mu(A_n) = 0$.
L'ensemble où $f$ est strictement positive s'écrit $A = \{x \in X \mid f(x) > 0\}$.
Remarquons que $A = \bigcup_{n=1}^\infty A_n$.
Par $\sigma$-sous-additivité de la mesure :
$$\mu(A) \le \sum_{n=1}^\infty \mu(A_n) = \sum_{n=1}^\infty 0 = 0$$
Puisque $\mu(A) \ge 0$, on conclut que $\mu(A) = 0$, soit $f = 0$ $\mu$-presque partout. $\blacksquare$

## 4. Applications en Intelligence Artificielle

### Fondations pour l'Apprentissage Statistique

En apprentissage automatique (Machine Learning), le risque réel d'un modèle (la Loss Function espérée) est défini par une intégrale de Lebesgue.
Étant donné un espace de données $\mathcal{Z} = \mathcal{X} \times \mathcal{Y}$ muni d'une mesure de probabilité inconnue $\mathbb{P}$, et une fonction de perte (loss) $\ell(z, \theta) \ge 0$ paramétrée par $\theta$, le risque est :
$$\mathcal{R}(\theta) = \int_{\mathcal{Z}} \ell(z, \theta) \, d\mathbb{P}(z)$$
Le fait de définir cette fonction via l'intégrale de Lebesgue permet au cadre de l'apprentissage statistique d'être universel : il couvre indifféremment les problèmes de classification (où $\mathbb{P}$ a des composantes discrètes, mesures de Dirac sur les classes) et de régression (où $\mathbb{P}$ a des densités continues par rapport à la mesure de Lebesgue).

### Théorie de l'Information (Divergence KL)

La similarité entre deux distributions de probabilités utilisées lors de la génération de texte (LLMs) est mesurée par la Divergence de Kullback-Leibler. Si $P$ et $Q$ sont deux mesures de probabilité, et si $P$ est absolument continue par rapport à $Q$ (noté $P \ll Q$), le théorème de Radon-Nikodym permet de définir une dérivée $f = \frac{dP}{dQ}$.
La divergence KL est alors définie rigoureusement par l'intégrale de Lebesgue de la fonction positive $f \log f$ :
$$D_{KL}(P || Q) = \int_{\Omega} \log\left(\frac{dP}{dQ}\right) dP$$
Sans la théorie de l'intégration de Lebesgue, ce concept central pour les auto-encodeurs variationnels (VAE) et l'apprentissage par renforcement (PPO) n'aurait aucune assise mathématique robuste.
