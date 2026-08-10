---
uuid: "jalon-52"
title: "Applications continues et Homéomorphismes"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/abstraction
prev: "[[Jalon 51 (Espaces métriques).md]]"
next: "[[Jalon 53 (Axiomes de séparation).md]]"
---

# Applications continues entre espaces topologiques et définition fine des homéomorphismes

## Introduction à la déformation spatiale

La naissance de la notion générale de continuité et d'homéomorphisme puise ses racines dans l'incapacité de l'analyse classique à classifier les espaces géométriques indépendamment de leur métrique. Au XIXe siècle, alors que Riemann et Betti exploraient les fondements de la géométrie intrinsèque et que Poincaré fondait l'Analysis Situs (l'ancêtre de la topologie algébrique), une impasse fondamentale émergea : comment formaliser rigoureusement l'intuition de déformer un objet de manière élastique, sans déchirure ni recollement, au-delà de la simple notion de distance ?

Dans un espace métrique, la continuité repose sur les boules et la notion de proximité mesurable par la fonction distance $\epsilon - \delta$ de Cauchy et Weierstrass. Cependant, Kolmogorov et Alexandroff, poursuivant les idées de Hausdorff, ont imposé une formalisation où la topologie elle-même dicte la structure. Une déformation continue ne préserve pas les distances, mais l'appartenance aux voisinages : ce qui était localement attaché le reste. L'homéomorphisme devient la manifestation ultime de cette déformation : une équivalence structurelle parfaite entre deux espaces apparemment distincts, posant les jalons essentiels pour l'étude des variétés et, ultérieurement, la théorie des modèles génératifs en intelligence artificielle.

## Formalisation de la continuité topologique

Soient $(X, \mathcal{T}_X)$ et $(Y, \mathcal{T}_Y)$ deux espaces topologiques. La continuité abstraite substitue l'image réciproque d'ouverts à l'utilisation des boules métriques.

### Continuité globale et locale

**Définition 1 (Continuité en un point) :**
Une application $f : X \to Y$ est continue en un point $x_0 \in X$ si, pour tout voisinage $V$ de $f(x_0)$ dans $Y$, son image réciproque $f^{-1}(V)$ est un voisinage de $x_0$ dans $X$.

Symboliquement :
$$ \forall V \in \mathcal{V}_{Y}(f(x_0)), \quad f^{-1}(V) \in \mathcal{V}_{X}(x_0) $$
où $\mathcal{V}_{Z}(z)$ désigne l'ensemble des voisinages du point $z$ dans l'espace topologique $Z$.

**Définition 2 (Continuité globale) :**
Une application $f : X \to Y$ est dite continue sur $X$ si l'image réciproque de tout ouvert de $Y$ est un ouvert de $X$.
$$ \forall O \in \mathcal{T}_Y, \quad f^{-1}(O) \in \mathcal{T}_X $$

**Exemple concret immédiat :**
Soit $X = \mathbb{R}$ muni de la topologie usuelle (générée par les intervalles ouverts) et $Y = \{0, 1\}$ muni de la topologie discrète $\mathcal{T}_Y = \{\emptyset, \{0\}, \{1\}, \{0, 1\}\}$. Considérons la fonction d'Heaviside $H : X \to Y$ définie par :
$$ H(x) = \begin{cases} 0 & \text{si } x < 0 \\ 1 & \text{si } x \ge 0 \end{cases} $$
Prenons l'ouvert $O = \{1\} \in \mathcal{T}_Y$. L'image réciproque est $H^{-1}(\{1\}) = [0, +\infty[$. Cet intervalle n'est pas un ouvert dans $\mathbb{R}$ avec la topologie usuelle (il contient son bord gauche sans contenir un intervalle ouvert autour de $0$). Par conséquent, la fonction d'Heaviside n'est pas continue.

**Cas pathologique :**
Si $X$ est muni de la topologie discrète (tout sous-ensemble est ouvert), *toute* application $f : X \to Y$ vers un espace topologique $Y$ quelconque est continue, car pour tout $O \in \mathcal{T}_Y$, l'ensemble $f^{-1}(O)$ est nécessairement ouvert dans $X$. À l'inverse, si $Y$ est muni de la topologie grossière $\mathcal{T}_Y = \{\emptyset, Y\}$, toute application $f : X \to Y$ est également continue, car $f^{-1}(\emptyset) = \emptyset$ et $f^{-1}(Y) = X$, qui sont toujours ouverts dans $X$.

## Homéomorphismes : L'isomorphisme topologique

L'isomorphisme dans la catégorie des espaces topologiques (Top) est appelé un homéomorphisme.

**Définition 3 (Homéomorphisme) :**
Une application $f : X \to Y$ est un homéomorphisme si les trois propriétés suivantes sont simultanément vérifiées :
1. $f$ est une bijection.
2. $f$ est continue.
3. Son application réciproque $f^{-1} : Y \to X$ est continue.

Deux espaces $X$ et $Y$ entre lesquels il existe un homéomorphisme sont dits **homéomorphes** (noté $X \simeq Y$). D'un point de vue topologique, ils sont indiscernables ; ils partagent toutes leurs propriétés topologiques (compacité, connexité, séparabilité, etc.).

**Exemple concret immédiat (Projection stéréographique) :**
Considérons la sphère unité épointée $S^2 \setminus \{N\} \subset \mathbb{R}^3$, où $N = (0, 0, 1)$ est le pôle Nord, et le plan équatorial identifié à $\mathbb{R}^2$. L'application de projection stéréographique $P : S^2 \setminus \{N\} \to \mathbb{R}^2$ associe à un point $M(x, y, z)$ sur la sphère le point d'intersection de la droite $(NM)$ avec le plan $z=0$.
L'expression analytique est donnée par :
$$ P(x, y, z) = \left( \frac{x}{1-z}, \frac{y}{1-z} \right) $$
Son application réciproque $P^{-1} : \mathbb{R}^2 \to S^2 \setminus \{N\}$ pour un point $(u, v)$ est :
$$ P^{-1}(u, v) = \left( \frac{2u}{u^2+v^2+1}, \frac{2v}{u^2+v^2+1}, \frac{u^2+v^2-1}{u^2+v^2+1} \right) $$
Ces deux fonctions, étant composées de fonctions polynomiales et rationnelles dont les dénominateurs ne s'annulent pas sur les domaines respectifs, sont continues. Ainsi, la sphère privée d'un point est homéomorphe au plan réel tout entier, $S^2 \setminus \{N\} \simeq \mathbb{R}^2$.

**Cas pathologique (Bijection continue mais non homéomorphisme) :**
Considérons l'application $f : [0, 2\pi[ \to S^1$ (le cercle unité dans $\mathbb{C}$) définie par $f(t) = e^{it}$.
Cette application est une bijection évidente, et elle est continue sur $[0, 2\pi[$. Cependant, $f$ n'est pas un homéomorphisme, car son inverse $f^{-1} : S^1 \to [0, 2\pi[$ n'est pas continue au point $(1,0)$ (ou $1$ en complexe). Si nous considérons une suite de points sur le cercle s'approchant de $1$ par des ordonnées négatives (ex: $z_n = e^{i(2\pi - 1/n)}$), $f^{-1}(z_n) = 2\pi - 1/n$ tend vers $2\pi$, tandis que $f^{-1}(1) = 0$. La réciproque n'est pas continue, les espaces ne sont donc pas homéomorphes (l'un est compact, l'autre non).

## Démonstrations Fondamentales

**Théorème : Équivalence de la continuité globale par les ouverts et les fermés.**
Une application $f : X \to Y$ est continue si et seulement si pour tout fermé $F$ de $Y$, son image réciproque $f^{-1}(F)$ est un fermé de $X$.

*Démonstration ligne par ligne :*
1. Supposons d'abord que $f$ est continue (l'image réciproque de tout ouvert est un ouvert).
2. Soit $F$ un sous-ensemble fermé de l'espace topologique $Y$.
3. Par définition de la topologie, le complémentaire de $F$ dans $Y$, noté $Y \setminus F$, est un ouvert de $Y$.
4. Par l'hypothèse de continuité de $f$, l'image réciproque de cet ouvert, $f^{-1}(Y \setminus F)$, est un ouvert dans $X$.
5. Or, l'opérateur d'image réciproque commute avec le passage au complémentaire : $f^{-1}(Y \setminus F) = X \setminus f^{-1}(F)$.
6. Ainsi, $X \setminus f^{-1}(F)$ est un ouvert de $X$.
7. Par conséquent, son complémentaire dans $X$, qui est exactement $f^{-1}(F)$, est par définition un fermé de $X$.
8. Inversement, supposons que l'image réciproque de tout fermé est un fermé.
9. Soit $O$ un ouvert arbitraire de $Y$. Son complémentaire $Y \setminus O$ est fermé.
10. Par hypothèse, $f^{-1}(Y \setminus O) = X \setminus f^{-1}(O)$ est un fermé de $X$.
11. Donc, le complémentaire de ce fermé, qui est $f^{-1}(O)$, est nécessairement un ouvert de $X$.
12. La fonction $f$ est donc continue, ce qui achève la démonstration. $\blacksquare$

## Applications en Mathématiques et Intelligence Artificielle

En apprentissage profond et géométrie différentielle, l'homéomorphisme permet de formaliser la théorie des **Normalizing Flows** (flux normalisateurs). Ces architectures génératives (comme RealNVP ou GLOW) reposent sur la construction d'une bijection $f : \mathbb{R}^d \to \mathbb{R}^d$ paramétrée par des réseaux de neurones. L'objectif est d'apprendre un difféomorphisme (un homéomorphisme qui est également différentiable, avec un inverse différentiable) qui transporte une distribution de probabilité complexe (comme la distribution des pixels d'une image) vers une distribution latente simple, souvent gaussienne.

Le calcul de l'évidence et la génération de nouvelles données reposent sur la continuité et la bijectivité stricte de cette transformation, rendues calculables par la matrice Jacobienne et la formule de changement de variables. Si la transformation n'était pas un homéomorphisme, la topologie intrinsèque de l'espace latent serait brisée (apparitions de "trous" ou croisements), interdisant toute interpolation géométrique cohérente dans les modèles génératifs.
