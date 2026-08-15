---
uuid: "jalon-60"
title: "Livrable IA T5 : Preuve du théorème d'approximation universelle"
year: 2
trimester: 5
tags:
  - math/analyse
  - ia/theorie
prev: "[[Jalon 59 (Topologie des espaces de fonctions).md]]"
next: "[[Jalon 61 (Insuffisances de l'intégrale de Riemann).md]]"
---

# Preuve du théorème d'approximation universelle

## Genèse et Intuition Géométrique

Le théorème d'approximation universelle, formalisé initialement par George Cybenko en 1989 puis étendu par Kurt Hornik en 1991, constitue le fondement mathématique justifiant la capacité des réseaux de neurones artificiels à modéliser n'importe quelle fonction continue.

L'intuition fondamentale repose sur la densité : de manière analogue au théorème d'approximation de Weierstrass qui affirme que les polynômes sont denses dans l'espace des fonctions continues sur un compact, ce théorème énonce qu'une somme pondérée de fonctions d'activation (par exemple des sigmoïdes) peut approcher uniformément toute fonction continue sur un hypercube compact de $\mathbb{R}^n$.

Géométriquement, chaque neurone d'une couche cachée agit comme un demi-plan séparateur de l'espace d'entrée. En combinant un nombre suffisant de ces demi-plans, on peut construire des "bosses" locales ou des "hyper-cylindres" qui, additionnés, permettent d'épouser n'importe quelle surface continue avec une erreur arbitrairement petite, sans nécessiter plus d'une seule couche cachée.

\begin{tikzpicture}
  \draw[->] (-0.5, 0) -- (6, 0) node[right] {$x$};
  \draw[->] (0, -0.5) -- (0, 3) node[above] {$f(x)$};

  \draw[thick, blue, domain=0:5.5, samples=100] plot (\x, {sin(\x*50) + 1.5});
  \node[blue] at (5.5, 2.5) {$f(x)$ continue};

  \draw[red, dashed, thick] (0, 1.5) -- (1, 1.5) -- (1, 2.3) -- (2, 2.3) -- (2, 0.7) -- (3, 0.7) -- (3, 1.9) -- (4, 1.9) -- (4, 1.2) -- (5, 1.2) -- (5, 0.5);
  \node[red] at (4, 2.5) {Approximation $G(x)$};
\end{tikzpicture}

## Définitions, Théorèmes et Exemples Concrets

Soit $I_n = [0, 1]^n$ le cube unité de $\mathbb{R}^n$. Considérons l'espace de Banach $\mathcal{C}(I_n)$ des fonctions continues de $I_n$ dans $\mathbb{R}$, muni de la norme de la convergence uniforme :
$$ \|f\|_\infty = \sup_{x \in I_n} |f(x)| $$

\textbf{Définition (Fonction sigmoïdale)}
Une fonction $\sigma : \mathbb{R} \to \mathbb{R}$ est dite sigmoïdale si elle est mesurable et vérifie :
$$ \lim_{t \to -\infty} \sigma(t) = 0 \quad \text{et} \quad \lim_{t \to +\infty} \sigma(t) = 1 $$

\textbf{Théorème (Approximation Universelle - Cybenko 1989)}
Soit $\sigma$ une fonction d'activation continue sigmoïdale. L'ensemble $S$ des fonctions de la forme :
$$ G(x) = \sum_{j=1}^N \alpha_j \sigma(w_j^T x + b_j) $$
avec $N \in \mathbb{N}^*$, $\alpha_j, b_j \in \mathbb{R}$ et $w_j \in \mathbb{R}^n$, est dense dans $\mathcal{C}(I_n)$.
Autrement dit, pour toute $f \in \mathcal{C}(I_n)$ et tout $\epsilon > 0$, il existe $G \in S$ telle que $\|f - G\|_\infty < \epsilon$.

\textbf{Exemple 1 : Approximation d'une constante}
Si $f(x) = C$, on choisit $N=1$, $w_1 = 0$, $b_1 \to \infty$ tel que $\sigma(b_1) \approx 1$. Alors $G(x) = \alpha_1 \sigma(b_1)$. En posant $\alpha_1 = C / \sigma(b_1)$, on a $G(x) = C$.
Si $C = 5$, $\alpha_1 = 5$, $\sigma(w^T x + b) \to 1$, $G(x) \to 5$.

\textbf{Exemple 2 : Fonction porte en 1D}
Approximation de $f(x) = 1$ si $x \in [0.4, 0.6]$, $0$ sinon.
On utilise $G(x) = \sigma(k(x - 0.4)) - \sigma(k(x - 0.6))$ avec $k \gg 1$.
Pour $x = 0.5$, $k(0.1) \to +\infty \implies \sigma \to 1$, $k(-0.1) \to -\infty \implies \sigma \to 0$. $G(0.5) \approx 1 - 0 = 1$.
Pour $x = 0.2$, $k(-0.2) \to -\infty \implies \sigma \to 0$, $k(-0.4) \to -\infty \implies \sigma \to 0$. $G(0.2) \approx 0$.
Pour $x = 0.8$, $k(0.4) \to +\infty \implies 1$, $k(0.2) \to +\infty \implies 1$. $G(0.8) \approx 1 - 1 = 0$.

\textbf{Exemple 3 : Évaluation numérique de la porte}
Avec $\sigma(t) = \frac{1}{1+e^{-t}}$, pour $k=100$ et $x=0.5$:
$G(0.5) = \sigma(10) - \sigma(-10) = \frac{1}{1+e^{-10}} - \frac{1}{1+e^{10}} \approx 0.99995 - 0.00005 = 0.9999$.

\textbf{Exemple 4 : La bosse 2D}
Soit $x = (x_1, x_2) \in [0,1]^2$. Pour approcher un pic autour de $(0.5, 0.5)$, on somme plusieurs "hyper-cylindres" orientés le long de différents vecteurs $w$.
Si on veut localiser l'activation, on prend $\sigma(w_1 x_1 - b_1) - \sigma(w_1 x_1 - b_2)$ et similairement pour $x_2$.

\textbf{Exemple 5 : Fonction d'activation ReLU}
Le théorème se généralise pour $\sigma(t) = \max(0, t)$. Une fonction "chapeau" s'écrit: $T(x) = \sigma(x+1) - 2\sigma(x) + \sigma(x-1)$.
Pour $x=0$, $T(0) = \sigma(1) - 2\sigma(0) + \sigma(-1) = 1 - 0 + 0 = 1$.
Pour $x=1$, $T(1) = \sigma(2) - 2\sigma(1) + \sigma(0) = 2 - 2 + 0 = 0$.
Pour $x=-1$, $T(-1) = \sigma(0) - 2\sigma(-1) + \sigma(-2) = 0 - 0 + 0 = 0$.

\textbf{Exemple 6 : Limites pathologiques}
Si $f(x) = \sin(1/x)$ sur $(0, 1]$ prolongée par 0 en 0. $f$ n'est pas continue en 0. Le théorème ne s'applique pas sur le compact $[0,1]$ au sens de la norme uniforme.

\begin{tikzpicture}
  \draw[->] (-2, 0) -- (2, 0) node[right] {$x$};
  \draw[->] (0, -0.5) -- (0, 2) node[above] {$\sigma(x)$};

  \draw[thick, blue, domain=-2:2, samples=100] plot (\x, {max(0, \x)});
  \node[blue] at (1.5, 1.8) {ReLU};

  \draw[thick, red, domain=-2:2, samples=100] plot (\x, {1 / (1 + exp(-4*\x))});
  \node[red] at (-1, 0.5) {Sigmoïde};
\end{tikzpicture}


## Démonstrations

La preuve originale exploite la dualité topologique et le théorème de Riesz-Markov, démontrant la densité par l'absurde via le théorème de Hahn-Banach.

\textbf{Étape 1 : Hypothèse par l'absurde}
Soit $S$ le sous-espace vectoriel engendré par les fonctions $x \mapsto \sigma(w^T x + b)$.
Supposons que $S$ ne soit pas dense dans $\mathcal{C}(I_n)$.
L'adhérence $\bar{S}$ est donc un sous-espace fermé strict de $\mathcal{C}(I_n)$.

\textbf{Étape 2 : Intervention du Théorème de Hahn-Banach}
D'après un corollaire du théorème de Hahn-Banach (forme analytique), il existe une forme linéaire continue non nulle $L$ sur $\mathcal{C}(I_n)$ telle que $L(g) = 0$ pour toute fonction $g \in \bar{S}$.

\textbf{Étape 3 : Théorème de Représentation de Riesz}
Le dual de $\mathcal{C}(I_n)$ est isomorphe à l'espace des mesures de Borel régulières signées finies sur $I_n$.
Il existe donc une mesure $\mu \neq 0$ sur $I_n$ telle que pour toute $f \in \mathcal{C}(I_n)$, $L(f) = \int_{I_n} f(x) d\mu(x)$.
Puisque $L$ s'annule sur $S$, on a :
$$ \int_{I_n} \sigma(w^T x + b) d\mu(x) = 0 \quad \forall w \in \mathbb{R}^n, \forall b \in \mathbb{R} $$

\textbf{Étape 4 : Propriété discriminatoire}
Une fonction $\sigma$ est dite discriminatoire si la condition ci-dessus implique $\mu = 0$.
Cybenko démontre que toute fonction sigmoïdale continue est discriminatoire. En fixant $w \neq 0$, et en considérant $h(x) = w^T x$, on projette la mesure $\mu$ sur la droite engendrée par $w$.
Par des arguments d'analyse de Fourier (ou par transformation de Laplace pour des mesures à support compact), l'annulation de l'intégrale pour toutes translations $b$ et dilatations des sigmoïdes implique que la mesure projetée est nulle pour toute direction $w$.

\textbf{Étape 5 : Conclusion}
Puisque les projections monodimensionnelles de la mesure $\mu$ sont toutes nulles, la transformée de Fourier de $\mu$ s'annule partout. Cela entraîne que $\mu$ est la mesure nulle.
Or, on avait supposé $L \neq 0$, donc $\mu \neq 0$, ce qui est une contradiction.
Par conséquent, $S$ est nécessairement dense dans $\mathcal{C}(I_n)$.

## Applications en Physique, Logique et IA

Le théorème d'approximation universelle justifie théoriquement la capacité de l'apprentissage profond à modéliser des systèmes physiques complexes non linéaires, tels que la dynamique des fluides (via les Physics-Informed Neural Networks - PINNs) ou la résolution d'équations aux dérivées partielles à haute dimension (comme l'équation de Schrödinger).

En logique, ce théorème établit que les réseaux de neurones constituent un système formel complet pour l'approximation de fonctions continues réelles, surpassant les limites expressives du perceptron simple, qui ne pouvait pas représenter la fonction logique XOR non linéairement séparable.
