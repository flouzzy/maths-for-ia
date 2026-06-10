---
uuid: "jalon-57"
title: "Théorème du point fixe de Banach"
year: 2
trimester: 5
tags:
  - math/analyse
  - ia/convergence
prev: "[[Jalon 56 (Espaces métriques complets).md]]"
next: "[[Jalon 58 (Théorème de Baire).md]]"
---

# Jalon 57 : Théorème du point fixe de Banach

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous ayez une carte de votre ville et que vous la froissiez un peu, puis que vous la jetiez par terre, n'importe où dans la ville. Le **Théorème de Banach** dit que, si la carte est restée dans les limites de la ville, il y aura toujours **exactement un point** de la carte qui se trouve pile-poil au-dessus de l'endroit réel qu'il représente. Un autre exemple : si vous mélangez une tasse de café, après que le mouvement s'est calmé, il y a au moins une molécule de café qui est revenue exactement à sa position initiale.
- **Le "Pourquoi on a inventé ça" :** Parfois, on ne sait pas résoudre une équation $f(x) = L$. Mais on peut la réécrire sous la forme $x = g(x)$. Si on applique $g$ encore et encore ($x, g(x), g(g(x)), \dots$), on espère se rapprocher de la solution. Le théorème de Banach donne les conditions pour que ce processus de "répétition" (itération) nous mène à coup sûr vers la solution unique.
- **Visualisation :** Un entonnoir. Peu importe où vous lancez une bille, si chaque rebond la rapproche du centre (contraction), elle finira par s'arrêter exactement au fond.

## 2. Formalisation

### A. Applications Contractantes

Soit $(X, d)$ un espace métrique.

> **Définition (Contraction) :**
> Une application $f : X \to X$ est dite **contractante** (ou $k$-lipschitzienne avec $k < 1$) s'il existe un réel $k \in [0, 1[$ tel que :
> $$\forall (x, y) \in X^2, \quad d(f(x), f(y)) \le k \cdot d(x, y)$$

### B. Le Théorème du Point Fixe de Banach

> **Théorème Fondamental :**
> Soit $(X, d)$ un espace métrique **complet** non vide. Toute application $f : X \to X$ **contractante** admet un **unique** point fixe $\alpha \in X$ (tel que $f(\alpha) = \alpha$).
> De plus, pour tout $x_0 \in X$, la suite définie par $x_{n+1} = f(x_n)$ converge vers $\alpha$, avec une vitesse de convergence géométrique :
> $$d(x_n, \alpha) \le \frac{k^n}{1-k} d(x_1, x_0)$$

## 3. Démonstrations

### Démonstration du Théorème

1. **Unicité :** Supposons $\alpha$ et $\beta$ deux points fixes.
   $d(\alpha, \beta) = d(f(\alpha), f(\beta)) \le k \cdot d(\alpha, \beta)$.
   Comme $k < 1$, cela implique $(1-k) d(\alpha, \beta) \le 0$, donc $d(\alpha, \beta) = 0$, soit $\alpha = \beta$.
2. **Existence (La suite est de Cauchy) :**
   Calculons l'écart entre deux termes consécutifs : $d(x_{n+1}, x_n) = d(f(x_n), f(x_{n-1})) \le k \cdot d(x_n, x_{n-1})$.
   Par récurrence : $d(x_{n+1}, x_n) \le k^n d(x_1, x_0)$.
   Pour $p > q$, par l'inégalité triangulaire :
   $d(x_p, x_q) \le \sum_{i=q}^{p-1} d(x_{i+1}, x_i) \le \sum_{i=q}^{p-1} k^i d(x_1, x_0)$.
   $d(x_p, x_q) \le k^q \frac{1-k^{p-q}}{1-k} d(x_1, x_0) \le \frac{k^q}{1-k} d(x_1, x_0)$.
   Comme $k < 1$, ce terme tend vers 0 quand $q \to \infty$. La suite est donc de Cauchy.
3. **Limite :** Comme $X$ est **complet**, la suite converge vers un point $\alpha \in X$.
4. **Point fixe :** Comme $f$ est contractante, elle est continue.
   $x_{n+1} = f(x_n) \implies \lim x_{n+1} = f(\lim x_n) \implies \alpha = f(\alpha)$.

## 4. Exercices d'Application

### Exercice 1 : Résolution de $\cos(x) = x$
**Énoncé :** Montrer que l'équation $\cos(x) = x$ admet une unique solution sur $[0, 1]$.
**Correction Détaillée :**
1. Soit $f(x) = \cos(x)$. $f$ envoie $[0, 1]$ dans $[0, 1]$.
2. Par l'inégalité des accroissements finis, $|f'(x)| = |-\sin(x)|$. Sur $[0, 1]$, $\sin(x) \le \sin(1) \approx 0.84 < 1$.
3. $f$ est donc une contraction sur le fermé $[0, 1]$ qui est complet.
4. Par le théorème de Banach, il existe un unique point fixe. On le trouve en tapant `cos` répétitivement sur une calculatrice.

### Exercice 2 : Niveau Avancé (Théorème de Picard)
**Énoncé :** Soit l'EDO $y' = f(t, y)$. Montrer que résoudre cette équation revient à chercher le point fixe d'un opérateur intégral.
**Correction Détaillée :**
L'équation équivaut à $y(t) = y_0 + \int_{t_0}^t f(s, y(s)) ds$.
On définit l'opérateur $T(y) = y_0 + \int f(s, y)$. Si $f$ est lipschitzienne, on montre que pour un intervalle de temps assez petit, $T$ est une contraction sur l'espace des fonctions continues (qui est complet, Jalon 56). C'est la base de l'existence des solutions d'équations différentielles.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Le théorème de Banach est au cœur des algorithmes de **Reinforcement Learning** (Apprentissage par renforcement) et des modèles d'équilibre.
- **Example Concret :**
    - **Équations de Bellman :** En RL, on cherche la fonction de valeur optimale $V^*$. Elle est définie comme le point fixe de l'**Opérateur de Bellman**. On prouve que cet opérateur est une contraction (grâce au facteur de remise $\gamma < 1$). L'algorithme "Value Iteration" n'est rien d'autre que l'application répétée de cet opérateur pour atteindre le point fixe.
    - **Deep Equilibrium Models (DEQ) :** Au lieu d'avoir un réseau avec $L$ couches différentes, on définit une seule couche $x = \sigma(Wx + b + u)$. On itère cette couche jusqu'à convergence. Le théorème de Banach garantit que si les poids $W$ sont assez petits (contraction), le réseau convergera toujours vers la même représentation, peu importe le nombre d'itérations.
    - **PageRank (Google) :** Le score d'une page Web est le point fixe d'une transformation matricielle (le vecteur propre associé à la valeur propre 1). C'est une application directe des méthodes itératives de point fixe.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 56 (Espaces métriques complets).md]], [[Jalon 19 (Dérivabilité).md]]
- **Concepts Futurs dépendants :** [[Jalon 101 (Théorème de l'application ouverte et théorème du graphe fermé.).md]], [[Jalon-142.md]]
