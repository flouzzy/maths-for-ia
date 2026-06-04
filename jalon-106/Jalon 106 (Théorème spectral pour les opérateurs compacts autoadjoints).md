---
uuid: "jalon-106"
title: "Théorème spectral pour les opérateurs compacts"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 105 (Opérateurs adjoints).md]]"
next: "[[Jalon 107 (Introduction à la théorie des opérateurs non bornés et résolvante.).md]]"
---

# Jalon 106 : Théorème spectral pour les opérateurs compacts

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous fassiez briller une lumière à travers un cristal de roche (l'opérateur $T$).
    - Normalement, la lumière ressort dans tous les sens de manière confuse.
    - Mais si le cristal est **Auto-adjoint** (parfaitement symétrique) et **Compact** (il concentre la lumière au lieu de l'éparpiller à l'infini), alors un miracle se produit.
    - La lumière ressort décomposée en une infinité de rayons de couleurs pures (les **vecteurs propres**).
    - Chaque rayon a une intensité précise (la **valeur propre**).
    - Plus les rayons sont "complexes", plus ils deviennent faibles, jusqu'à devenir invisibles (les valeurs propres tendent vers 0).
    - Ce théorème dit que vous pouvez reconstruire n'importe quelle image complexe simplement en additionnant ces rayons de couleur pure.
- **Le "Pourquoi on a inventé ça" :** C'est la généralisation finale de la diagonalisation des matrices (Jalon 32). En dimension infinie, la plupart des opérateurs sont trop compliqués pour être diagonalisés. Les opérateurs compacts sont les seuls qui se comportent "presque" comme des matrices finies. C'est l'outil qui permet de résoudre les équations de la physique et de l'IA (comme la compression de données).
- **Visualisation :** Une machine qui transforme une sphère géante en une ellipse dont les axes deviennent de plus en plus petits. On peut décrire la machine simplement en donnant la direction et la longueur de chaque axe.

## 2. Formalisation & Rigueur Académique

Soit $H$ un espace de Hilbert de dimension infinie.

### A. Opérateurs Compacts

> **Définition 1 :** Un opérateur $T \in \mathcal{L}(H)$ est dit **compact** si l'image de la boule unité fermée de $H$ par $T$ est une partie relativement compacte de $H$ (son adhérence est compacte).
> *Intuition :* $T$ transforme des suites bornées en suites dont on peut extraire une sous-suite convergente.

### B. Spectre d'un opérateur compact auto-adjoint

> **Théorème 1 :** Si $T$ est compact et auto-adjoint ($T^* = T$), alors :
> 1. Ses valeurs propres sont réelles.
> 2. Ses sous-espaces propres associés à des valeurs propres non nulles sont de dimension **finie**.
> 3. L'ensemble des valeurs propres est soit fini, soit forme une suite tendant vers 0.

### C. Le Théorème Spectral

> **Théorème 2 (Spectral) :**
> Soit $T$ un opérateur compact auto-adjoint sur $H$. Il existe une base hilbertienne $(e_n)_{n \in \mathbb{N}}$ de $H$ composée de vecteurs propres de $T$. On a la décomposition :
> $$\forall x \in H, \quad Tx = \sum_{n=0}^\infty \lambda_n \langle x, e_n \rangle e_n$$
> où $\lambda_n$ est la valeur propre associée à $e_n$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Existence de la plus grande valeur propre

1. **La Forme Quadratique :** On considère $q(x) = \langle Tx, x \rangle$ sur la sphère unité $S = \{ \|x\|=1 \}$. Comme $T$ est auto-adjoint, $q(x)$ est réel.
2. **Supremum :** Posons $M = \sup_{x \in S} |q(x)|$. On montre que $M = \|T\|$.
3. **Compacité et Convergence :** Soit $(x_n)$ une suite telle que $q(x_n) \to \lambda$ avec $|\lambda| = M$. Comme $H$ est un Hilbert, on peut extraire une sous-suite $(x_{\phi(n)})$ qui converge **faiblement** vers $x$.
4. **Utilisation de la compacité de T :** Comme $T$ est compact, la convergence faible $x_n \rightharpoonup x$ implique la convergence **forte** $Tx_n \to Tx$.
5. **Conclusion :** Par continuité du produit scalaire (fort $\times$ faible), on montre que $q(x_n) \to q(x)$. Donc $q(x) = \lambda$. Le maximum est atteint en $x$, et on prouve par un calcul de différentielle que $Tx = \lambda x$. $x$ est donc un vecteur propre.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Opérateur intégral
**Énoncé :** Soit $T : L^2([0, 1]) \to L^2([0, 1])$ défini par $Tf(x) = \int_0^1 K(x, y) f(y) dy$ avec $K(x, y) = \min(x, y)$. Montrer que $T$ est compact auto-adjoint.
**Correction Détaillée :**
1. **Auto-adjoint :** $K(x, y) = K(y, x)$, donc par Fubini, $\langle Tf, g \rangle = \langle f, Tg \rangle$.
2. **Compact :** L'intégrale de $|K|^2$ est finie ($1/3$). C'est un opérateur de Hilbert-Schmidt, donc il est compact.
3. **Valeurs propres :** L'équation $Tf = \lambda f$ se transforme en une équation différentielle $f'' + \frac{1}{\lambda} f = 0$ avec conditions $f(0)=0, f'(1)=0$. On trouve des solutions en $\sin( (n+1/2)\pi x )$.

### Exercice 2 : Niveau Avancé (Approximation par rang fini)
**Énoncé :** Montrer que tout opérateur compact est la limite en norme d'opérateurs de rang fini.
**Correction Détaillée :**
C'est une conséquence directe du théorème spectral : les sommes partielles $T_N = \sum_{n=0}^N \lambda_n \langle \cdot, e_n \rangle e_n$ sont de rang $N$ et $\|T - T_N\| = \sup_{n > N} |\lambda_n|$, qui tend vers 0 car les valeurs propres tendent vers 0.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le théorème spectral est le fondement mathématique de l'**Analyse en Composantes Principales (PCA)** et des **Méthodes à Noyaux**.
- **Example Concret :**
    - **Kernel PCA :** En IA, on ne peut pas souvent manipuler les fonctions directement. On travaille sur une matrice de noyau $K_{ij} = k(x_i, x_j)$. Le théorème spectral garantit que lorsque le nombre de données $N \to \infty$, les vecteurs propres de cette matrice convergent vers les fonctions propres de l'opérateur intégral associé. C'est ce qui permet d'apprendre des représentations non-linéaires puissantes.
    - **Compression de Modèles (SVD/Pruning) :** Dans un Transformer, on décompose les matrices de poids par SVD (qui est la version non-carrée du théorème spectral). On remarque que les valeurs propres décroissent très vite : on peut donc supprimer 90% des petites valeurs propres sans changer la sortie du réseau.
    - **Diffusion Models :** L'évolution de la distribution des données pendant le débruitage est régie par un opérateur (le générateur du semi-groupe) dont on étudie le spectre pour garantir la vitesse de convergence.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 105 (Opérateurs adjoints).md]], [[Jalon 104 (Bases hilbertiennes).md]], [[Jalon 32 (Preuve complète du théorème spectral pour les endomorphismes symétriques.).md]]
- **Concepts Futurs dépendants :** [[Jalon 107 (Introduction à la théorie des opérateurs non bornés et résolvante.).md]], [[Jalon 143 (Théorie spectrale des graphes).md]]
