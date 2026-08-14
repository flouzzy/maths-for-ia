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

# Jalon 60 : Livrable IA T5 : Preuve du théorème d'approximation universelle

# Présentation du concept clé

### Intuition Fondamentale
 Imaginez que vous ayez une boîte de LEGO. Chaque pièce de LEGO est très simple (une bosse, un creux). Le **Théorème d'Approximation Universelle** dit que, si vous avez assez de pièces, vous pouvez construire n'importe quelle forme complexe (une voiture, un château, un visage) avec une précision infinie. En IA, les LEGO sont les "neurones" et la forme complexe est la "fonction" que l'on veut apprendre. Tant que la fonction est continue (pas de sauts brusques), un réseau de neurones avec une seule couche cachée très large peut l'imiter parfaitement.
### Genèse Conceptuelle
 Au début de l'IA, on se demandait si les réseaux de neurones étaient juste des gadgets ou s'ils pouvaient vraiment tout calculer. Cette preuve mathématique a confirmé que les réseaux de neurones sont des **estimateurs universels** : ils ont la capacité théorique de représenter n'importe quelle logique ou n'importe quel phénomène physique.
### Représentation Géométrique
 On prend une courbe compliquée. On essaie de la reproduire en additionnant des fonctions "marches d'escalier" ou des "sigmoïdes". Plus on ajoute de fonctions simples, plus la somme ressemble à la courbe compliquée.

# Formalisation

### Énoncé du Théorème (Cybenko, 1989)

Soit $I_n = [0, 1]^n$ le cube unité de $\mathbb{R}^n$. Soit $\mathcal{C}(I_n)$ l'espace des fonctions continues sur $I_n$ muni de la norme uniforme $\|f\|_\infty = \sup |f(x)|$.

> **Théorème d'Approximation Universelle :**
> Soit $\sigma : \mathbb{R} \to \mathbb{R}$ une fonction d'activation continue, non constante et bornée (ex: une sigmoïde). L'ensemble des fonctions de la forme :
> $$G(x) = \sum_{i=1}^N \alpha_i \sigma(w_i^T x + b_i)$$
> est **dense** dans $\mathcal{C}(I_n)$.
> En d'autres termes, pour tout $f \in \mathcal{C}(I_n)$ et pour tout $\epsilon > 0$, il existe un entier $N$ et des paramètres $(\alpha_i, w_i, b_i)$ tels que :
> $$\|f - G\|_\infty < \epsilon$$


### Représentation Schématique (TikZ)

\begin{tikzpicture}[scale=1.5]
    \draw[->] (-0.5, 0) -- (3.5, 0) node[right] {$x$};
    \draw[->] (0, -0.5) -- (0, 1.5) node[above] {$y$};
    \draw[domain=0:3, smooth, variable=\x, blue, thick] plot ({\x}, {1/(1+exp(-2*(\x-1.5)))});
    \node[blue, right] at (3, 1) {$\sigma(w^T x + b)$};
    \draw[dashed] (0, 1) -- (3.5, 1);
    \node[left] at (0, 1) {$1$};
    \node[left] at (0, 0.5) {$0.5$};
    \draw[dashed] (1.5, 0) -- (1.5, 0.5) -- (0, 0.5);
    \node[below] at (1.5, 0) {$-b/w$};
\end{tikzpicture}



### Exemples Concrets Immédiats

1. **Exemple Numérique (1D) :** Pour approcher $f(x) = x^2$ sur $[0,1]$, un réseau avec $\sigma(x) = \max(0,x)$ (ReLU) construit une approximation affine par morceaux. Si $N=3$, la somme $\sum_{i=1}^3 \alpha_i \max(0, w_i x + b_i)$ trace un polygone à 3 segments.
2. **Exemple Analytique :** La fonction porte (fonction indicatrice de l'intervalle $[a,b]$) s'approxime avec deux sigmoïdes: $\sigma(k(x-a)) - \sigma(k(x-b))$. Pour un très grand $k=1000$, l'erreur uniforme sur $\mathbb{R} \setminus ([a-\epsilon, a+\epsilon] \cup [b-\epsilon, b+\epsilon])$ tend vers $0$.
3. **Exemple Matriciel :** En dimension $n=2$, le terme $w_i^T x + b_i$ représente une droite de séparation $w_{i,1} x_1 + w_{i,2} x_2 + b_i = 0$. La combinaison affine pondère l'activation de ces demi-plans.
4. **Cas Pathologique (Absence de Non-linéarité) :** Si $\sigma(x) = cx$, le réseau s'écrit $\sum \alpha_i c(w_i^T x + b_i) = (\sum \alpha_i c w_i^T) x + (\sum \alpha_i c b_i)$, ce qui est purement affine. Il est impossible d'approcher $x^2$ sur $[-1, 1]$.
5. **Cas Pathologique (Constante) :** Si $\sigma(x) = 1$, le réseau ne produit qu'une fonction constante.
6. **Exemple Numérique de Densité :** Soit $f(x) = \sin(2\pi x)$ sur $[0,1]$ et $\epsilon = 0.01$. Le théorème stipule qu'il existe un jeu de poids explicite $(\alpha_i, w_i, b_i)$ pour $N$ grand tel que la différence maximale absolue entre la courbe du sinus et la sortie du réseau soit inférieure à $0.01$ en tout point $x$.
7. **Exemple d'Application de Hahn-Banach :** Dans la preuve, si l'espace engendré n'est pas tout $\mathcal{C}(I_n)$, Hahn-Banach garantit qu'on peut "séparer" cet espace d'une fonction hors de l'espace par un hyperplan fonctionnel (mesure $\mu$).
8. **Exemple Géométrique :** La boule unité de l'espace des fonctions continues est couverte de manière arbitrairement proche par la variété engendrée par les paramètres du réseau.


### Cadre Topologique

La densité s'entend au sens de la topologie de la convergence uniforme sur les compacts (Jalon 59). Cela signifie que le réseau peut s'approcher de $f$ partout sur le domaine de manière uniforme.

# Démonstrations

### Esquisse de la preuve via l'Analyse Fonctionnelle

La preuve originale de Cybenko utilise le **Théorème de Hahn-Banach** et le **Théorème de Riesz**.

1. **Stratégie par l'absurde :** Supposons que l'ensemble des réseaux $S$ n'est pas dense dans $\mathcal{C}(I_n)$.
2. **Utilisation de Hahn-Banach :** S'il n'est pas dense, alors son adhérence $\bar{S}$ est un sous-espace fermé strict. Il existe donc une forme linéaire continue non nulle $L$ sur $\mathcal{C}(I_n)$ telle que $L(g) = 0$ pour tout $g \in S$.
3. **Représentation de Riesz :** Toute forme linéaire continue sur $\mathcal{C}(I_n)$ est représentée par une mesure de Borel signée $\mu$ sur $I_n$. L'hypothèse $L(g)=0$ devient :
   $$\int_{I_n} \sigma(w^T x + b) d\mu(x) = 0 \quad \text{pour tous } w, b$$
4. **Propriété Discriminatoire :** Cybenko a prouvé que si $\sigma$ est une sigmoïdale continue, alors elle est "discriminatoire". Cela signifie que si l'intégrale ci-dessus est nulle pour tous $w, b$, alors la mesure $\mu$ est nécessairement nulle.
5. **Conclusion :** Comme $\mu = 0$, la forme linéaire $L$ est nulle. Contradiction. Donc $S$ est dense dans $\mathcal{C}(I_n)$.

# Exercices d'Application

### Exercice 1 : Approximation d'une porte par des sigmoïdes
**Énoncé :** Comment obtenir une fonction "marche" (qui vaut 0 pour $x < 0$ et 1 pour $x > 0$) en utilisant une sigmoïde $\sigma(z) = \frac{1}{1+e^{-z}}$ ?
**Correction Détaillée :**
On considère $g_k(x) = \sigma(kx)$.
- Si $x > 0$, $kx \to +\infty$ quand $k \to \infty$, donc $\sigma(kx) \to 1$.
- Si $x < 0$, $kx \to -\infty$, donc $\sigma(kx) \to 0$.
- Si $x = 0$, $\sigma(0) = 0.5$.
En augmentant le "poids" $k$, on rend la transition de la sigmoïde de plus en plus raide, tendant vers une fonction de Heaviside. On peut ensuite décaler et sommer ces marches pour approcher n'importe quelle fonction en escalier.

### Exercice 2 : Niveau Avancé (Cas de la ReLU)
**Énoncé :** Le théorème est-il vrai pour $\sigma(x) = \max(0, x)$ (ReLU) ?
**Correction Détaillée :**
Oui, bien que ReLU ne soit pas bornée. On peut construire une fonction "chapeau" (triangulaire) en combinant deux ou trois ReLUs. Comme toute fonction continue sur un compact est limite uniforme de fonctions affines par morceaux (triangulations), l'ensemble des réseaux ReLU est dense.

# Application en Intelligence Artificielle

- **Le Pont Théorique :** Ce théorème est la justification existentielle de l'IA. Il dit : "La solution existe dans votre espace de recherche". Cependant, il ne dit pas comment la trouver, ni si $N$ sera raisonnablement petit.
- **Example Concret :**
    - **Largeur vs Profondeur :** Le théorème original parle d'une seule couche cachée très large ($N \to \infty$). En pratique, on préfère des réseaux profonds (plusieurs couches) car ils sont beaucoup plus efficaces pour représenter certaines fonctions complexes avec beaucoup moins de neurones (compacité de la représentation).
    - **Le rôle de la non-linéarité :** Si $\sigma$ était linéaire, alors toute somme de $\sigma$ resterait linéaire. On ne pourrait approcher que des droites. C'est le passage par la non-linéarité (la "cassure" de la droite) qui donne au réseau sa puissance d'approximation universelle.
    - **Inductive Bias :** Puisque le réseau peut tout apprendre, pourquoi apprend-il souvent la "bonne" fonction ? C'est grâce à la régularisation et à l'architecture (CNN, Transformers) qui restreignent l'espace de recherche vers des fonctions physiquement plausibles.

# Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 59 (Topologie des espaces de fonctions).md]], [[Jalon 98 (Théorème de Hahn-Banach).md]] (anticipé)
- **Concepts Futurs dépendants :** [[Jalon 134 (Complexite des classes de fonctions).md]], [[Jalon 144 (Le phénomène de double descente).md]]
