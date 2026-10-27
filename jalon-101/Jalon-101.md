---
uuid: "jalon-101"
title: "Théorème de l'application ouverte et théorème du graphe fermé"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/fondations
prev: "[[jalon-100/Jalon-100.md|Jalon 100]]"
next: "[[jalon-102/Jalon-102.md|Jalon 102]]"
---

# Jalon 101 : Théorème de l'application ouverte et théorème du graphe fermé

## Origines physiques et géométriques

Dans l'étude des systèmes physiques et des équations aux dérivées partielles, une question fondamentale se pose : si un système (représenté par un opérateur $T$) admet une solution unique pour chaque donnée initiale (bijection), cette solution varie-t-elle continûment en fonction de la donnée initiale ? Autrement dit, une petite perturbation des conditions initiales entraîne-t-elle seulement une petite variation de la solution ?
Hadamard a formalisé cela sous la notion de "problème bien posé". En dimension finie, toute bijection linéaire est un isomorphisme topologique (son inverse est automatiquement continu). Cependant, en dimension infinie, ce n'est plus vrai en général.
Les théorèmes de l'application ouverte et du graphe fermé, établis indépendamment par Stefan Banach, Juliusz Schauder et d'autres dans les années 1920-1930, apportent une réponse magistrale. Ils affirment que dans le cadre des espaces de Banach (espaces vectoriels normés complets, qui capturent l'idée de "solidité" géométrique où aucune limite de suite de Cauchy ne "fuit" de l'espace), la structure algébrique d'une bijection continue impose automatiquement la continuité de son inverse. L'axiome de complétude agit comme un verrou qui empêche les "déchirures" topologiques.

## Espaces de Banach et Applications Ouvertes

Commençons par définir le cœur de cette théorie.

### Théorème de l'Application Ouverte (Banach-Schauder)

Soient $(E, \|\cdot\|_E)$ et $(F, \|\cdot\|_F)$ deux espaces de Banach.
Soit $T : E \to F$ un opérateur linéaire, continu et **surjectif**.
Alors, l'application $T$ est ouverte. Autrement dit, pour tout ouvert $U \subset E$, l'image $T(U)$ est un ouvert de $F$.

De manière équivalente et plus quantitative, il existe une constante $c > 0$ telle que pour tout $y \in F$, il existe $x \in E$ vérifiant :
$$ T(x) = y \quad \text{et} \quad \|x\|_E \le c \|y\|_F $$
Ceci implique géométriquement que l'image de la boule unité ouverte de $E$, notée $B_E(0, 1)$, contient une boule ouverte centrée en $0$ de $F$, c'est-à-dire qu'il existe $r > 0$ tel que $B_F(0, r) \subset T(B_E(0, 1))$.

### Corollaire immédiat : Théorème de l'Isomorphisme de Banach

Soient $(E, \|\cdot\|_E)$ et $(F, \|\cdot\|_F)$ deux espaces de Banach.
Soit $T : E \to F$ une bijection linéaire et continue.
Alors $T^{-1} : F \to E$ est une application continue. $T$ est donc un isomorphisme topologique.

**Exemple concret calculatoire : Équivalence de normes**
Considérons l'espace vectoriel $E = \mathcal{C}([0, 1], \mathbb{R})$ des fonctions continues de $[0, 1]$ dans $\mathbb{R}$.
Munissons-le de deux normes classiques :
1. La norme de la convergence uniforme : $\|f\|_\infty = \sup_{x \in [0, 1]} |f(x)|$. L'espace $(E, \|\cdot\|_\infty)$ est un espace de Banach.
2. La norme intégrale $L^1$ : $\|f\|_1 = \int_0^1 |f(x)| \, dx$. L'espace $(E, \|\cdot\|_1)$ n'est *pas* complet.

Considérons l'application identité :
$$ \text{Id} : (E, \|\cdot\|_\infty) \to (E, \|\cdot\|_1) $$
définie par $\text{Id}(f) = f$.
Cette application est linéaire, bijective. Elle est aussi continue car pour toute fonction $f$, on a :
$$ \|\text{Id}(f)\|_1 = \int_0^1 |f(x)| \, dx \le \int_0^1 \|f\|_\infty \, dx = \|f\|_\infty $$
L'inverse est l'identité $\text{Id}^{-1} : (E, \|\cdot\|_1) \to (E, \|\cdot\|_\infty)$.
Est-elle continue ? Si elle l'était, il existerait une constante $C > 0$ telle que pour tout $f$, $\|f\|_\infty \le C \|f\|_1$.
Prenons les fonctions $f_n(x) = (n+1) x^n$ pour $n \in \mathbb{N}^*$.
Calculons leurs normes :
$\|f_n\|_\infty = n+1$ (atteint en $x=1$).
$\|f_n\|_1 = \int_0^1 (n+1) x^n \, dx = \left[ x^{n+1} \right]_0^1 = 1$.
Nous avons donc $n+1 \le C \times 1$ pour tout $n$, ce qui est absurde.
Ainsi, l'inverse n'est pas continue.
Pourquoi le théorème de l'isomorphisme de Banach ne s'applique-t-il pas ici ? L'application est bijective et continue de $(E, \|\cdot\|_\infty)$ vers $(E, \|\cdot\|_1)$, mais $(E, \|\cdot\|_1)$ **n'est pas un espace de Banach** ! Le théorème montre l'importance cruciale de la complétude de l'espace d'arrivée.

## Le Théorème du Graphe Fermé

La continuité d'une application linéaire implique la vérification d'une majoration $\|Tx\|_F \le C \|x\|_E$. Parfois, il est plus facile de vérifier une condition topologique sur le graphe de la fonction.

### Définition du Graphe

Soit $T : E \to F$ une application linéaire entre deux espaces vectoriels normés $(E, \|\cdot\|_E)$ et $(F, \|\cdot\|_F)$.
Le graphe de $T$, noté $\text{Gr}(T)$ ou $\Gamma(T)$, est le sous-ensemble de l'espace produit $E \times F$ défini par :
$$ \text{Gr}(T) = \{ (x, T(x)) \mid x \in E \} $$
L'espace produit $E \times F$ est muni de la norme $\|(x, y)\|_{E \times F} = \|x\|_E + \|y\|_F$.
Dire que le graphe est fermé signifie que pour toute suite $(x_n)_{n \in \mathbb{N}}$ dans $E$ telle que $x_n \to x$ dans $E$ et $T(x_n) \to y$ dans $F$, on a $y = T(x)$.

### Énoncé formel du Théorème du Graphe Fermé

Soient $(E, \|\cdot\|_E)$ et $(F, \|\cdot\|_F)$ deux espaces de Banach.
Soit $T : E \to F$ une application linéaire.
Alors $T$ est continue si et seulement si son graphe $\text{Gr}(T)$ est fermé dans $E \times F$.

## Démonstration exhaustive

Nous allons démontrer l'équivalence.

**Étape 1 : Si $T$ est continue, alors $\text{Gr}(T)$ est fermé.**
Ceci est une propriété topologique générale, vraie dans tout espace vectoriel normé (sans même supposer la complétude).
Soit $(x_n)_{n \in \mathbb{N}}$ une suite d'éléments de $E$ telle que la suite des couples $(x_n, T(x_n))$ converge vers $(x, y)$ dans $E \times F$.
La convergence dans l'espace produit signifie que $x_n \xrightarrow{\|\cdot\|_E} x$ et $T(x_n) \xrightarrow{\|\cdot\|_F} y$.
Puisque $T$ est continue en $x$, la convergence de $x_n$ vers $x$ implique que $T(x_n)$ converge vers $T(x)$ dans $F$.
Par unicité de la limite dans un espace séparé (comme $F$), on a nécessairement $y = T(x)$.
Ainsi, le couple limite $(x, y)$ est égal à $(x, T(x))$, qui appartient par définition à $\text{Gr}(T)$.
Le graphe contient toutes ses limites de suites, il est donc fermé.

**Étape 2 : Si $\text{Gr}(T)$ est fermé, alors $T$ est continue (Preuve via l'isomorphisme de Banach).**
Supposons que $\text{Gr}(T)$ est un sous-ensemble fermé de l'espace de Banach $E \times F$.
Un sous-espace fermé d'un espace complet est lui-même un espace complet pour la distance induite.
Donc, $(\text{Gr}(T), \|\cdot\|_{E \times F})$ est un espace de Banach.

Considérons l'application de projection sur la première coordonnée :
$$ \Pi_1 : \text{Gr}(T) \to E $$
définie par $\Pi_1(x, T(x)) = x$.
Cette application est clairement linéaire.
Vérifions sa continuité : pour tout élément $(x, T(x)) \in \text{Gr}(T)$, nous avons
$$ \|\Pi_1(x, T(x))\|_E = \|x\|_E \le \|x\|_E + \|T(x)\|_F = \|(x, T(x))\|_{E \times F} $$
L'application $\Pi_1$ est donc continue (et de norme inférieure ou égale à $1$).

L'application $\Pi_1$ est injective : si $\Pi_1(x, T(x)) = 0_E$, alors $x = 0_E$. Comme $T$ est linéaire, $T(0_E) = 0_F$, d'où $(x, T(x)) = (0_E, 0_F) = 0_{\text{Gr}(T)}$.
L'application $\Pi_1$ est surjective : pour tout $x \in E$, l'élément $(x, T(x))$ appartient à $\text{Gr}(T)$ et $\Pi_1(x, T(x)) = x$.

L'application $\Pi_1$ est donc une bijection linéaire et continue entre l'espace de Banach $\text{Gr}(T)$ et l'espace de Banach $E$.
D'après le théorème de l'isomorphisme de Banach, son inverse $\Pi_1^{-1} : E \to \text{Gr}(T)$ est une application linéaire continue.
La définition de cet inverse est simplement $\Pi_1^{-1}(x) = (x, T(x))$.
Puisque $\Pi_1^{-1}$ est continue, il existe une constante $C > 0$ telle que pour tout $x \in E$, on ait :
$$ \|\Pi_1^{-1}(x)\|_{E \times F} \le C \|x\|_E $$
Ce qui se traduit par :
$$ \|x\|_E + \|T(x)\|_F \le C \|x\|_E $$
Soit :
$$ \|T(x)\|_F \le (C - 1) \|x\|_E $$
Cette inégalité prouve formellement que l'opérateur $T$ est borné, et donc continu.
La démonstration est ainsi complète.

## Applications en Intelligence Artificielle et Mécanique Quantique

**1. Problèmes Inverses et Régularisation**
En apprentissage automatique, de nombreuses tâches (débruitage, super-résolution d'images) se formulent comme la résolution de $T(x) = y$, où $T$ est un opérateur de dégradation (flou, sous-échantillonnage) continu. Souvent, $T$ n'est pas surjectif sur un espace complet ou son image n'est pas fermée. Le théorème de l'isomorphisme de Banach nous alerte : si l'espace image n'est pas "parfait" (complet), l'opérateur inverse $T^{-1}$ sera instable (discontinu). Le bruit de mesure $\epsilon$ sur $y$ sera dramatiquement amplifié : $\|T^{-1}(y+\epsilon) - T^{-1}(y)\|$ peut être immense. Ceci justifie mathématiquement la nécessité absolue d'utiliser des techniques de régularisation (comme la régularisation de Tikhonov, la "Ridge Regression") pour stabiliser l'inversion en modifiant l'opérateur ou l'espace de travail.

**2. Opérateurs non bornés en Mécanique Quantique**
En physique quantique, l'opérateur impulsion (dérivée) n'est pas continu (borné) sur l'espace de Hilbert $L^2(\mathbb{R})$.
Le théorème du graphe fermé montre que l'opérateur dérivation $D : f \mapsto f'$ ne peut pas être défini sur *tout* l'espace $L^2$ tout en conservant un graphe fermé. On est forcé de le définir sur un domaine restreint dense dans $L^2$ (comme l'espace de Sobolev $H^1(\mathbb{R})$). L'étude des opérateurs non bornés fermés est le langage fondamental de l'équation de Schrödinger, qui régit les systèmes quantiques sous-jacents aux futures architectures d'informatique quantique pour l'IA.

**3. Normalizing Flows (Réseaux de neurones inversibles)**
Les Normalizing Flows sont des modèles génératifs qui reposent sur des réseaux de neurones conçus par architecture pour être des bijections exactes $f_\theta : \mathcal{X} \to \mathcal{Z}$. Les théorèmes présentés ici assurent que, si l'espace latent et l'espace des données peuvent être assimilés à des espaces de Banach (souvent $\mathbb{R}^d$), la construction d'un réseau continu (ce qui est toujours le cas avec les couches classiques) garantit que le flux inverse $f_\theta^{-1}$ sera lui-même continu. Cela assure une génération d'échantillons stable : des points proches dans l'espace latent généreront des images perceptuellement proches dans l'espace de données, évitant un comportement chaotique du générateur.
