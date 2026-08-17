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

# Livrable IA T5 : Preuve du théorème d'approximation universelle

## Introduction et contexte historique

Le théorème d'approximation universelle, formulé initialement par George Cybenko en 1989 pour les fonctions d'activation sigmoïdales, puis généralisé par Kurt Hornik, établit qu'un réseau de neurones artificiels à propagation avant (feedforward) avec une seule couche cachée finie peut approximer n'importe quelle fonction continue sur un sous-ensemble compact de $\mathbb{R}^n$, sous des hypothèses très faibles sur la fonction d'activation.

L'émergence de ce théorème a marqué une étape fondamentale en théorie de l'apprentissage automatique. Avant sa démonstration, la capacité de représentation des réseaux de neurones était souvent considérée empiriquement. Cette preuve a cimenté les réseaux de neurones comme des approximateurs universels, garantissant que tout phénomène modélisable par une fonction continue peut, en théorie, être appris avec une précision arbitraire, pourvu que l'architecture soit suffisamment large. Le problème se déplace alors de l'expressivité de l'architecture vers les difficultés de l'optimisation (entraînement) et de la généralisation.

La démonstration repose sur des outils profonds d'analyse fonctionnelle, en particulier le théorème de Hahn-Banach et le théorème de représentation de Riesz-Markov-Kakutani, reliant la densité dans les espaces de fonctions continues aux mesures de Radon.

## Définitions, théorèmes et exemples concrets

### Espace des fonctions continues et topologie

Soit $I_n = [0, 1]^n$ le cube unité de $\mathbb{R}^n$, qui est un espace compact. On considère $\mathcal{C}(I_n)$, l'espace vectoriel des fonctions réelles continues définies sur $I_n$. Cet espace est muni de la norme uniforme, définie par :
$$\|f\|_\infty = \sup_{x \in I_n} |f(x)|$$

La convergence par rapport à cette norme correspond à la convergence uniforme sur le compact $I_n$.

### Fonctions discriminatoires

**Définition (Fonction discriminatoire) :** Une fonction $\sigma : \mathbb{R} \to \mathbb{R}$ est dite discriminatoire si, pour toute mesure de Borel signée finie $\mu$ sur $I_n$, la condition :
$$\int_{I_n} \sigma(w^T x + b) d\mu(x) = 0 \quad \text{pour tous } w \in \mathbb{R}^n, b \in \mathbb{R}$$
implique que la mesure $\mu$ est identiquement nulle ($\mu = 0$).

### Énoncé du Théorème d'Approximation Universelle (Cybenko, 1989)

**Théorème :** Soit $\sigma : \mathbb{R} \to \mathbb{R}$ une fonction continue, non constante et bornée. Alors $\sigma$ est discriminatoire. De plus, l'ensemble des fonctions de la forme :
$$G(x) = \sum_{i=1}^N \alpha_i \sigma(w_i^T x + b_i)$$
avec $N \in \mathbb{N}^*$, $\alpha_i \in \mathbb{R}$, $w_i \in \mathbb{R}^n$ et $b_i \in \mathbb{R}$, est dense dans $\mathcal{C}(I_n)$.

Autrement dit, pour toute fonction $f \in \mathcal{C}(I_n)$ et pour tout $\epsilon > 0$, il existe un entier $N$ et des paramètres $(\alpha_i, w_i, b_i)_{1 \le i \le N}$ tels que :
$$\|f - G\|_\infty = \sup_{x \in I_n} |f(x) - G(x)| < \epsilon$$

### Exemples d'application du théorème

**Exemple 1 : Approximation de la fonction cosinus**
Considérons $f(x) = \cos(x)$ sur $I_1 = [0, 1]$. On utilise la fonction d'activation sigmoïde standard $\sigma(x) = \frac{1}{1 + e^{-x}}$. Le théorème assure l'existence de paramètres tels que $\sup_{x \in [0, 1]} |\cos(x) - \sum_{i=1}^N \alpha_i \sigma(w_i x + b_i)| < 0.01$.

**Exemple 2 : Approximation d'une surface parabolique**
Soit $f(x_1, x_2) = x_1^2 + x_2^2$ sur $[0, 1]^2$. Bien que $f$ soit une fonction polynomiale de degré 2, un réseau avec une seule couche cachée utilisant une activation $\tanh(x)$ (qui est continue et bornée) peut approximer $f$ à toute précision $\epsilon > 0$ près.

**Exemple 3 : Fonction en escalier lissée**
Considérons une fonction continue $f$ approchant une fonction indicatrice de l'intervalle $[0.4, 0.6]$. En utilisant des combinaisons linéaires de sigmoïdes, on peut créer une fonction "chapeau" très précise, ce qui démontre la capacité du réseau à localiser ses approximations.

**Exemple 4 : Limites avec des activations non bornées (ReLU)**
Bien que le théorème original de Cybenko requière une fonction d'activation bornée, le résultat a été étendu à d'autres fonctions non bornées, comme la ReLU (Rectified Linear Unit), $\sigma(x) = \max(0, x)$. Une combinaison de ReLU peut former des fonctions affines par morceaux qui sont denses dans $\mathcal{C}(I_n)$.

**Exemple 5 : L'importance de la continuité**
Si l'on cherche à approximer une fonction discontinue, comme $f(x) = 1$ pour $x \ge 0.5$ et $0$ sinon, sur $[0,1]$, la norme $\|\cdot\|_\infty$ ne permet pas de converger uniformément. La convergence n'est garantie que presque partout vis-à-vis d'une mesure de probabilité (norme $L^p$).

\begin{center}
\begin{tikzpicture}
    % Axes
    \draw[->, thick] (-3, 0) -- (3, 0) node[right] {$x$};
    \draw[->, thick] (0, -0.5) -- (0, 2.5) node[above] {$y$};

    % The target function (e.g., a Gaussian-like pulse)
    \draw[thick, blue, domain=-2.5:2.5, samples=100] plot (\x, {2*exp(-\x*\x)});
    \node[blue, above right] at (1, 1) {$f(x)$ cible};

    % Approximation with 3 sigmoids
    \draw[thick, red, dashed, domain=-2.5:2.5, samples=100] plot (\x, {2*exp(-\x*\x) + 0.1*sin(\x*180/3.14*10)});
    \node[red, above right] at (-2, 1.5) {$G(x)$ réseau};
\end{tikzpicture}
\end{center}

\begin{center}
\begin{tikzpicture}
    % 2D Domain
    \draw[thick] (0,0) rectangle (4,4);
    \node at (2, -0.5) {$I_n = [0,1]^n$};

    % Function representation
    \draw[->, thick, shorten >= 2pt] (4.2, 2) -- (5.8, 2);
    \node[above] at (5, 2) {$G(x) \approx f(x)$};

    % Error bounds
    \draw[thick, blue] (7, 0) -- (7, 4);
    \draw[thick, red, dashed] (6.8, 0) to[out=90,in=270] (7.2, 2) to[out=90,in=270] (6.8, 4);
    \node at (8, 2) {$\|f - G\|_\infty < \epsilon$};
\end{tikzpicture}
\end{center}


## Démonstrations

La démonstration complète, telle que donnée par Cybenko, s'appuie sur la contraposée d'une conséquence du théorème de Hahn-Banach.

**Preuve :**
Soit $S \subset \mathcal{C}(I_n)$ le sous-espace vectoriel défini par :
$$S = \text{Vect} \left\lbrace x \mapsto \sigma(w^T x + b) \mid w \in \mathbb{R}^n, b \in \mathbb{R} \right\rbrace$$
Nous voulons montrer que $S$ est dense dans $\mathcal{C}(I_n)$, c'est-à-dire que son adhérence $\overline{S}$ est égale à $\mathcal{C}(I_n)$.

Supposons par l'absurde que $\overline{S} \neq \mathcal{C}(I_n)$. Comme $\overline{S}$ est un sous-espace vectoriel fermé propre de l'espace de Banach $\mathcal{C}(I_n)$, le théorème de Hahn-Banach garantit l'existence d'une forme linéaire continue non nulle $L : \mathcal{C}(I_n) \to \mathbb{R}$ telle que $L_{|\overline{S}} = 0$.

Le théorème de représentation de Riesz-Markov-Kakutani affirme que toute forme linéaire continue sur $\mathcal{C}(I_n)$ peut être représentée par l'intégrale par rapport à une unique mesure de Radon (Borel signée régulière) finie $\mu$ sur $I_n$. Ainsi :
$$L(f) = \int_{I_n} f(x) d\mu(x) \quad \text{pour toute } f \in \mathcal{C}(I_n)$$
Puisque $L$ s'annule sur $S$, on a pour tous $w \in \mathbb{R}^n$ et $b \in \mathbb{R}$ :
$$\int_{I_n} \sigma(w^T x + b) d\mu(x) = 0$$

Par hypothèse du théorème, la fonction $\sigma$ est continue, bornée et non constante. Un lemme technique (Lemme de Cybenko) stipule que toute fonction continue sigmoïdale (ou simplement bornée non constante, selon les formulations étendues de Hornik) est discriminatoire.

La propriété discriminatoire de $\sigma$ implique alors que la mesure $\mu$ est identiquement nulle.
Si $\mu = 0$, alors la forme linéaire $L$ est identiquement nulle.
Ceci contredit le fait que $L$ est non nulle.
L'hypothèse initiale est donc fausse, et on conclut que $\overline{S} = \mathcal{C}(I_n)$, ce qui achève la démonstration. \qed

## Applications en physique, logique et intelligence artificielle

### Expressivité des réseaux de neurones

En intelligence artificielle, le théorème garantit qu'un réseau de neurones multicouches classique (Perceptron Multicouche ou MLP) possède la puissance de représentation nécessaire pour modéliser toute relation continue déterministe entre des entrées (par exemple, les pixels d'une image, un vecteur d'état physique) et des sorties (probabilités de classe, énergies, coordonnées).

Cependant, ce théorème est un résultat d'existence. Il n'indique pas :
1. Le nombre de neurones $N$ requis (qui peut croître exponentiellement avec la dimension $n$, souffrant du "fléau de la dimension").
2. Si un algorithme d'optimisation par descente de gradient (comme la rétropropagation) convergera vers ce minimum global.

### Mécanique quantique et physique statistique

Dans la modélisation de systèmes physiques complexes, les réseaux de neurones sont utilisés pour approximer les fonctions d'onde en mécanique quantique (Neural Network Quantum States). La compacité du domaine $I_n$ peut être adaptée via des homéomorphismes pour couvrir des espaces de configuration physiques, et la densité garantie par le théorème justifie la recherche d'énergies fondamentales par des méthodes variationnelles utilisant des architectures neuronales.

### Modélisation en dynamique des fluides

Pour les équations aux dérivées partielles non linéaires (comme l'équation de Navier-Stokes), les réseaux de neurones informés par la physique (PINNs) exploitent l'approximation universelle pour représenter le champ de vitesse ou de pression. La capacité à représenter n'importe quelle fonction lisse garantit que la solution physique exacte appartient à l'adhérence de l'espace des fonctions générées par le réseau.
