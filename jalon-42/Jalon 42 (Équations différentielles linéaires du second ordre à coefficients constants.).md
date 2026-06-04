---
uuid: "jalon-42"
title: "Équations différentielles linéaires du second ordre"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 41 (Équations différentielles linéaires du premier ordre et méthode de variation de la constante.).md]]"
next: "[[Jalon 43 (Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.).md]]"
---

# Jalon 42 : Équations différentielles linéaires du second ordre à coefficients constants

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez un poids attaché à un ressort et plongé dans un bocal d'huile. Si vous tirez sur le poids et que vous le lâchez :
    1. Le ressort veut le ramener (force proportionnelle à la position $y$).
    2. L'huile freine le mouvement (force proportionnelle à la vitesse $y'$).
    3. Le poids a une inertie (liée à l'accélération $y''$).
    L'équation du second ordre décrit exactement ce ballet. Selon la viscosité de l'huile, le poids peut soit osciller longtemps, soit revenir lentement à sa place sans jamais dépasser le centre.
- **Le "Pourquoi on a inventé ça" :** Les lois fondamentales de la physique (Newton : $F = ma$) font intervenir l'accélération, qui est la dérivée seconde de la position. Presque tous les systèmes physiques réels (ponts, circuits électriques, robots) sont régis par des équations du second ordre. En IA, cela nous aide à modéliser des optimisateurs "nerveux" ou "calmes".
- **Visualisation :** Une courbe qui oscille de moins en moins fort (amortissement) ou une courbe qui s'envole (instabilité).

## 2. Formalisation & Rigueur Académique

Soient $a, b, c \in \mathbb{R}$ avec $a \neq 0$, et $d$ une fonction continue sur $I \subset \mathbb{R}$.
L'équation différentielle est $(E) : a y''(t) + b y'(t) + c y(t) = d(t)$.

### A. L'Équation Homogène

L'équation homogène associée est $(H) : a y'' + b y' + c y = 0$.
On considère l'équation caractéristique : $a r^2 + b r + c = 0$, de discriminant $\Delta = b^2 - 4ac$.

> **Théorème (Solutions de l'équation homogène) :**
> 1. **Si $\Delta > 0$ :** Deux racines réelles distinctes $r_1, r_2$.
>    $y_H(t) = \lambda e^{r_1 t} + \mu e^{r_2 t}$.
> 2. **Si $\Delta = 0$ :** Une racine réelle double $r_0 = -b/2a$.
>    $y_H(t) = (\lambda + \mu t) e^{r_0 t}$.
> 3. **Si $\Delta < 0$ :** Deux racines complexes conjuguées $r = \alpha \pm i \beta$.
>    $y_H(t) = e^{\alpha t} (A \cos(\beta t) + B \sin(\beta t))$.

### B. L'Équation Complète

> **Théorème (Structure des solutions) :**
> La solution générale de $(E)$ est $y = y_H + y_P$, où $y_P$ est une solution particulière de $(E)$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Pourquoi l'exponentielle ?

1. **Hypothèse :** Cherchons une solution de la forme $y(t) = e^{rt}$.
2. **Dérivation :** $y'(t) = r e^{rt}$ et $y''(t) = r^2 e^{rt}$.
3. **Injection :** $a(r^2 e^{rt}) + b(r e^{rt}) + c(e^{rt}) = 0$.
4. **Simplification :** Comme $e^{rt} \neq 0$, on peut diviser : $a r^2 + b r + c = 0$.
5. **Conclusion :** $y(t) = e^{rt}$ est solution si et seulement si $r$ est racine de l'équation caractéristique. La linéarité de l'équation garantit que toute combinaison linéaire de solutions est encore une solution.

### Recherche d'une solution particulière par la méthode des coefficients indéterminés

Si $d(t) = P(t) e^{mt}$ où $P$ est un polynôme :
1. Si $m$ n'est pas racine caractéristique : $y_P(t) = Q(t) e^{mt}$ avec $\deg Q = \deg P$.
2. Si $m$ est racine simple : $y_P(t) = t Q(t) e^{mt}$.
3. Si $m$ est racine double : $y_P(t) = t^2 Q(t) e^{mt}$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Résolution avec second membre
**Énoncé :** Résoudre $y'' - 3y' + 2y = 2e^{3t}$.
**Correction Détaillée :**
1. **Homogène :** $r^2 - 3r + 2 = 0 \implies (r-1)(r-2) = 0$.
   $y_H(t) = A e^t + B e^{2t}$.
2. **Particulière :** $m=3$ n'est pas racine. On cherche $y_P(t) = k e^{3t}$.
   $y_P' = 3k e^{3t}, y_P'' = 9k e^{3t}$.
   $9k - 3(3k) + 2k = 2 \implies 2k = 2 \implies k = 1$.
   $y_P(t) = e^{3t}$.
3. **Générale :** $y(t) = A e^t + B e^{2t} + e^{3t}$.

### Exercice 2 : Niveau Avancé (Amortissement critique)
**Énoncé :** Résoudre $y'' + 2y' + y = 0$ avec $y(0)=1$ et $y'(0)=0$.
**Correction Détaillée :**
1. **Caractéristique :** $r^2 + 2r + 1 = 0 \implies (r+1)^2 = 0$. Racine double $r=-1$.
2. **Générale :** $y(t) = (A + Bt) e^{-t}$.
3. **Conditions initiales :**
   $y(0) = A = 1$.
   $y'(t) = B e^{-t} - (A + Bt) e^{-t} = (B - A - Bt) e^{-t}$.
   $y'(0) = B - A = 0 \implies B = A = 1$.
4. **Résultat :** $y(t) = (1+t) e^{-t}$. C'est le régime critique (le plus rapide pour revenir à l'équilibre sans osciller).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Les optimisateurs de second ordre (comme le Momentum ou le Nesterov Momentum) sont basés sur une discrétisation d'une équation du second ordre.
- **Exemple Concret :**
    - **Momentum et Oscillations :** La descente de gradient avec momentum est régie par l'équation :
      $$y'' + \gamma y' + \nabla L(y) = 0$$
      Si le coefficient de friction $\gamma$ est trop faible ($\Delta < 0$ dans l'analogue linéaire), l'optimiseur va **osciller** autour du minimum avant de s'arrêter. Si $\gamma$ est bien choisi (régime critique), il plonge au fond du minimum sans perdre de temps.
    - **EDO pour les réseaux de neurones :** Comprendre le régime oscillatoire permet d'expliquer pourquoi certains modèles "divergent" si le pas d'apprentissage est trop grand : l'analogie physique est celle d'un ressort qui devient instable.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 41 (Équations différentielles linéaires du premier ordre et méthode de variation de la constante.).md]], [[Jalon 28 (Polynômes d'endomorphismes).md]]
- **Concepts Futurs dépendants :** [[Jalon 43 (Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.).md]], [[Jalon 117 (Calcul des variations).md]]
