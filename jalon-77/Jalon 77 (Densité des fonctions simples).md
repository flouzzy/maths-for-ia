---
uuid: "jalon-77"
title: "Densité dans Lp"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]]"
next: "[[Jalon 78 (Séries de Fourier).md]]"
---

# Jalon 77 : Densité dans $L^p$

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous vouliez reproduire une photo haute résolution (une fonction de $L^p$) avec des outils limités.
    - **Les fonctions simples**, c'est comme utiliser des pixels : vous avez des petits carrés de couleur uniforme. Si vos pixels sont assez petits, vous pouvez reproduire n'importe quelle image.
    - **Les fonctions continues**, c'est comme utiliser un pinceau : vous faites des dégradés lisses.
    Le concept de **Densité** dit que, même si les fonctions de $L^p$ peuvent être incroyablement compliquées et "sauvages" (comme de la neige à la télé), vous pouvez toujours les imiter à la perfection (avec une erreur aussi petite que vous voulez) en utilisant uniquement des fonctions "gentilles" (pixels ou dégradés).
- **Le "Pourquoi on a inventé ça" :** Il est très difficile de prouver une propriété sur TOUTES les fonctions de $L^p$. Grâce à la densité, on prouve la propriété uniquement sur les fonctions simples ou continues (qui sont faciles à manipuler), puis on dit : "par passage à la limite, c'est vrai pour tout le monde". C'est l'outil de simplification par excellence.
- **Visualisation :** Une courbe très découpée que l'on approche par une ligne brisée (continue) ou par un escalier (simple). Plus on ajoute de segments, plus l'écart (la norme $L^p$) devient invisible.

## 2. Formalisation & Rigueur Académique

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré. On s'intéresse à $L^p(\mu)$ avec $1 \le p < +\infty$.
*Note :* Pour $p = \infty$, les résultats de densité ci-dessous sont généralement faux.

### A. Densité des fonctions simples

> **Théorème 1 :**
> L'ensemble des fonctions simples intégrables est **dense** dans $L^p(\mu)$.
> $$\forall f \in L^p(\mu), \forall \epsilon > 0, \exists s \in \mathcal{S} \cap L^p, \quad \|f - s\|_p < \epsilon$$

### B. Densité des fonctions continues (Cas de Lebesgue)

Soit $X = \mathbb{R}^n$ muni de la mesure de Lebesgue $\lambda$. On note $\mathcal{C}_c(\mathbb{R}^n)$ l'espace des fonctions continues à support compact.

> **Théorème 2 :**
> $\mathcal{C}_c(\mathbb{R}^n)$ est **dense** dans $L^p(\lambda)$.
> Autrement dit, toute fonction de $L^p$ peut être approchée par une fonction "lisse" qui s'annule en dehors d'une grande boîte.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Densité des fonctions simples

1. **Cas des fonctions positives :** Soit $f \in L^p$ telle que $f \ge 0$.
   D'après le Jalon 65, il existe une suite croissante de fonctions simples $(s_n)$ telle que $s_n \to f$ partout.
2. **Domination :** Comme $0 \le s_n \le f$, on a $|f - s_n|^p \le (2f)^p = 2^p f^p$.
   Comme $f \in L^p$, la fonction $f^p$ est intégrable.
3. **Application du TCD :** Par le **Théorème de Convergence Dominée** (Jalon 69), l'intégrale $\int |f - s_n|^p d\mu$ tend vers 0.
   Donc $\|f - s_n\|_p \to 0$.
4. **Cas général :** On décompose $f = (f^+ - f^-) + i(f_{im}^+ - f_{im}^-)$ et on applique le résultat à chaque partie.

### Approche par les fonctions continues (Idée)

Pour approcher une fonction indicatrice $\mathbf{1}_{[a, b]}$ par une fonction continue, on utilise une fonction "trapèze" qui vaut 1 sur $[a, b]$ et qui descend linéairement vers 0 sur $[a-\epsilon, a]$ et $[b, b+\epsilon]$. Quand $\epsilon \to 0$, la norme $L^p$ de la différence tend vers 0. Comme les fonctions simples sont des sommes d'indicatrices, on en déduit la densité de $\mathcal{C}_c$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Approximation d'un signal créneau
**Énoncé :** Soit $f = \mathbf{1}_{[0, 1]}$. Trouver une fonction continue $g$ telle que $\|f - g\|_1 < 0.1$.
**Correction Détaillée :**
On définit $g$ par : $g(x) = 1$ sur $[0, 1]$, $g(x) = 1 - \frac{x-1}{\epsilon}$ sur $[1, 1+\epsilon]$, $g(x) = 1 + \frac{x}{\epsilon}$ sur $[-\epsilon, 0]$, et 0 ailleurs.
L'écart est l'aire des deux petits triangles de base $\epsilon$ et de hauteur 1.
$\|f - g\|_1 = 2 \cdot (\frac{1}{2} \cdot \epsilon \cdot 1) = \epsilon$.
En choisissant $\epsilon = 0.05$, on a bien $\|f - g\|_1 = 0.05 < 0.1$.

### Exercice 2 : Niveau Avancé (Invariance par translation dans $L^p$)
**Énoncé :** Montrer que pour $f \in L^p(\mathbb{R})$, $\lim_{h \to 0} \|f(\cdot + h) - f(\cdot)\|_p = 0$.
**Correction Détaillée :**
1. Si $f$ est continue à support compact, c'est vrai par continuité uniforme (Théorème de Heine).
2. Si $f \in L^p$ quelconque, on utilise la densité : pour tout $\epsilon$, il existe $g \in \mathcal{C}_c$ telle que $\|f-g\|_p < \epsilon$.
3. On utilise l'inégalité triangulaire : $\|f_h - f\| \le \|f_h - g_h\| + \|g_h - g\| + \|g - f\| = 2\|f-g\| + \|g_h - g\|$.
4. On conclut par passage à la limite. C'est un exemple type de l'utilisation de la densité pour prouver une propriété générale.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le Théorème d'Approximation Universelle (Jalon 60) est un cas particulier de théorème de densité. Il dit que les réseaux de neurones sont denses dans l'espace des fonctions continues, qui lui-même est dense dans $L^p$.
- **Example Concret :**
    - **Traitement du Signal :** On remplace un signal complexe (dans $L^2$) par sa série de Fourier (Jalon 78). Cela n'est possible que parce que les fonctions trigonométriques sont denses dans $L^2$.
    - **Robustesse au bruit :** Si les fonctions "lisses" sont denses, cela signifie que tout modèle complexe peut être approché par un modèle stable. La régularisation (Weight Decay) pousse le modèle vers ces fonctions lisses sans perdre de capacité d'expression.
    - **Finis Elements Methods (FEM) :** En simulation physique (météo, crash-test), on approche les solutions d'équations (dans des espaces de Sobolev, Jalon 83) par des fonctions simples (polynomiales par morceaux). La densité garantit que la simulation converge vers la réalité.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 75 (Preuve de la complétude des espaces Lp).md]], [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]
- **Concepts Futurs dépendants :** [[Jalon 78 (Séries de Fourier).md]], [[Jalon 82 (Introduction à la théorie des distributions de Schwartz).md]]
