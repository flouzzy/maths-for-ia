---
uuid: "jalon-51"
title: "Espaces métriques"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/algorithmes
prev: "[[Jalon 50 (Opérateurs topologiques).md]]"
next: "[[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.).md]]"
---

# Jalon 51 : Espaces métriques

## 1. Genèse du concept et impasses historiques

Historiquement, la géométrie s'est construite sur les fondations euclidiennes, où la notion de distance semblait aller de soi, intimement liée à la règle et au compas, à la norme de vecteurs dans des espaces de dimension finie. Cependant, à l'aube du XXème siècle, avec les travaux de mathématiciens comme Maurice Fréchet (qui a introduit la notion d'espace métrique en 1906) et Felix Hausdorff, le besoin de généralisation est devenu impérieux.

L'impasse était double : d'une part, comment définir rigoureusement la proximité, la continuité et la convergence non plus pour des points dans l'espace physique, mais pour des objets beaucoup plus complexes, comme des suites infinies, des fonctions, ou même des courbes ? D'autre part, la topologie générale, bien que puissante, s'avérait souvent trop abstraite pour capturer les nuances quantitatives nécessaires en analyse.

L'invention des espaces métriques offre une réponse magistrale : extraire l'essence même de l'inégalité triangulaire et de la symétrie de la distance usuelle, et l'ériger en axiomes fondateurs sur des ensembles arbitraires. Cela permet de ramener la rigueur calculatoire au cœur des espaces abstraits, rendant possible l'étude quantitative des déformations, des approximations et de la compacité.

## 2. Définition et axiomatisation des espaces métriques

### A. La métrique comme application fondamentale

Soit $X$ un ensemble arbitraire, non vide.

> **Définition (Espace métrique) :**
> On appelle distance (ou métrique) sur l'ensemble $X$ toute application $d : X \times X \longrightarrow \mathbb{R}_{+}$ satisfaisant aux trois axiomes suivants pour tous éléments $x, y, z \in X$ :
>
> 1. **Séparation (Identité des indiscernables) :**
>    $$d(x, y) = 0 \iff x = y$$
> 2. **Symétrie :**
>    $$d(x, y) = d(y, x)$$
> 3. **Inégalité triangulaire (Sous-additivité géométrique) :**
>    $$d(x, z) \le d(x, y) + d(y, z)$$
>
> Le couple structuré $(X, d)$ est alors qualifié d'**espace métrique**.

**Conséquence immédiate (Positivité stricte) :** L'axiome de séparation et l'arrivée dans $\mathbb{R}_{+}$ impliquent que pour tout $x \neq y$, $d(x, y) > 0$. L'inégalité triangulaire, souvent appelée l'inégalité du plus court chemin, stipule qu'aucun détour par un point $y$ ne peut raccourcir le trajet direct de $x$ à $z$.

### B. Exemples immédiats et pathologiques

1. **La distance discrète : L'isolement absolu**
   Sur n'importe quel ensemble $X$, on peut définir la distance discrète :
   $$d(x, y) = \begin{cases} 0 & \text{si } x = y \\ 1 & \text{si } x \neq y \end{cases}$$
   *Vérification rapide de l'inégalité triangulaire :* Si $x=z$, $0 \le d(x,y) + d(y,z)$ est trivial. Si $x \neq z$, alors $d(x,z) = 1$. Puisque $x \neq z$, on ne peut avoir simultanément $x=y$ et $z=y$. Donc l'une des deux distances $d(x,y)$ ou $d(y,z)$ vaut nécessairement 1, garantissant $1 \le 1 + 0$ ou $1 \le 1+1$. Cette distance, bien que triviale, montre qu'absolument tout ensemble peut être métrisé.

2. **La métrique uniforme sur les espaces de fonctions**
   Considérons l'espace des fonctions continues réelles sur un segment, $E = \mathcal{C}([a, b], \mathbb{R})$. On définit la distance de la convergence uniforme :
   $$d_{\infty}(f, g) = \sup_{t \in [a, b]} |f(t) - g(t)|$$
   Ici, l'inégalité triangulaire se déduit directement de celle de la valeur absolue sur $\mathbb{R}$ en passant à la borne supérieure. La séparation est assurée par la continuité.

3. **Métrique induite par une norme**
   Si $(E, \| \cdot \|)$ est un espace vectoriel normé, la distance induite est naturellement définie par :
   $$d(x, y) = \|x - y\|$$
   Toute norme engendre une métrique (par invariance par translation et homogénéité). Attention : la réciproque est fausse (la distance discrète ne provient d'aucune norme car elle n'est pas homogène : $d(\lambda x, \lambda y) \neq |\lambda| d(x, y)$).

## 3. Topologie induite par la distance

L'outil principal d'investigation locale dans un espace métrique est la boule.

> **Définition (Boules) :**
> Soit $(X, d)$ un espace métrique, $a \in X$ un point (le centre) et $r > 0$ un réel strictement positif (le rayon).
> - **Boule ouverte :** $B(a, r) = \left\lbrace x \in X \mid d(a, x) < r \right\rbrace$
> - **Boule fermée :** $B_{f}(a, r) = \left\lbrace x \in X \mid d(a, x) \le r \right\rbrace$
> - **Sphère :** $S(a, r) = \left\lbrace x \in X \mid d(a, x) = r \right\rbrace$

> **Théorème fondamental de la topologie métrique :**
> L'ensemble de toutes les réunions quelconques de boules ouvertes constitue une topologie sur $X$.
> Autrement dit, un sous-ensemble $O \subset X$ est un **ouvert** si et seulement si, pour tout $x \in O$, il existe un rayon $\epsilon > 0$ tel que la boule ouverte $B(x, \epsilon)$ soit entièrement incluse dans $O$.

### Démonstration : L'ouverture des boules ouvertes

Il faut montrer que si on définit les ouverts comme ci-dessus, alors une boule ouverte est bien un ouvert au sens de cette topologie. C'est le socle de toute la théorie.

*Preuve détaillée :*
Soit $B(a, r)$ une boule ouverte. Soit $x$ un point arbitraire de cette boule, c'est-à-dire $x \in B(a, r)$. Par définition, nous savons que $d(a, x) < r$.
Nous cherchons un rayon $\epsilon > 0$ tel que $B(x, \epsilon) \subseteq B(a, r)$.

Posons précisément l'écart disponible : $\epsilon = r - d(a, x)$.
Puisque $d(a, x) < r$, nous avons bien $\epsilon > 0$.

Vérifions maintenant l'inclusion. Soit $y \in B(x, \epsilon)$, ce qui signifie que $d(x, y) < \epsilon$.
Évaluons la distance de $y$ au centre initial $a$ en utilisant l'inégalité triangulaire :
$$d(a, y) \le d(a, x) + d(x, y)$$
En substituant la stricte majoration pour $d(x, y)$ :
$$d(a, y) < d(a, x) + \epsilon$$
Substituons l'expression de $\epsilon$ :
$$d(a, y) < d(a, x) + (r - d(a, x)) = r$$
Ainsi, $d(a, y) < r$, ce qui démontre rigoureusement que $y \in B(a, r)$. L'inclusion $B(x, \epsilon) \subseteq B(a, r)$ est établie. La boule ouverte est bien un voisinage de chacun de ses points. $\blacksquare$

### Propriétés topologiques remarquables

> **Théorème de séparation (Espace de Hausdorff) :**
> Tout espace métrique $(X, d)$ est séparé (propriété $T_2$).
> *Démonstration immédiate :* Si $x \neq y$, posons $\delta = d(x, y) > 0$. Les boules ouvertes $B(x, \delta/3)$ et $B(y, \delta/3)$ sont disjointes par l'absurde (sinon, un point dans l'intersection violerait l'inégalité triangulaire $d(x, y) \le d(x, z) + d(z, y) < 2\delta/3$, contradiction).

## 4. Équivalence topologique des distances

Deux distances sur le même ensemble peuvent "voir" les mêmes voisinages, et donc induire la même topologie.

> **Définition (Distances topologiquement équivalentes) :**
> Deux métriques $d_1$ et $d_2$ sur $X$ sont topologiquement équivalentes si elles définissent la même topologie (les mêmes ouverts).
> Plus fortement, elles sont **uniformément équivalentes** (ou Lipschitz-équivalentes) s'il existe des constantes $c > 0$ et $C > 0$ telles que pour tout couple $(x, y) \in X^2$ :
> $$c \cdot d_1(x, y) \le d_2(x, y) \le C \cdot d_1(x, y)$$

*Exemple fondamental en $\mathbb{R}^n$ :* Les distances induites par les normes classiques $\| \cdot \|_1, \| \cdot \|_2, \| \cdot \|_{\infty}$ sont toutes uniformément équivalentes. L'équivalence forte implique l'équivalence topologique, mais la réciproque est fausse (ex: $d(x,y)=|x-y|$ et $\delta(x,y)=\min(1, |x-y|)$ sur $\mathbb{R}$ sont topologiquement équivalentes, mais pas uniformément car l'une est bornée et l'autre non).

## 5. Applications transversales

**En Apprentissage Statistique (Machine Learning) :**
L'espace des données, des "features" ou des embeddings lexicaux est par essence un espace métrique. Les algorithmes fondamentaux comme les k-Plus Proches Voisins (k-NN), le clustering par K-Means, ou les algorithmes basés sur la densité (DBSCAN) s'appuient exclusivement sur la définition d'une métrique rigoureuse.
Le choix de la distance ($L_1$ pour la robustesse aux valeurs aberrantes, $L_2$ pour la stricte convexité et la dérivation, ou la distance cosinus pour des espaces documentaires) détermine entièrement la topologie et donc l'apprentissage du modèle.

**En Théorie de l'Information et Optimal Transport :**
La distance de Wasserstein (Earth Mover's Distance), centrale dans l'entraînement des modèles génératifs de pointe (WGANs), dote l'espace des mesures de probabilité d'une structure métrique complète, corrigeant les défauts pathologiques de la divergence de Kullback-Leibler qui ne satisfait ni la symétrie ni l'inégalité triangulaire.
