---
uuid: "jalon-48"
title: "Livrable IA T4 : Formalisation mathématique de la Rétropropagation"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/backpropagation
prev: "[[Jalon 47 (Dérivées partielles d'ordre deux).md]]"
next: "[[Jalon 49 (Espaces topologiques généraux).md]]"
---

# Jalon 48 : Formalisation mathématique de la Rétropropagation

## Introduction Historique et Genèse Conceptuelle

L'entraînement des réseaux de neurones profonds repose sur l'optimisation de fonctions de perte hautement dimensionnelles. Dans les années 1970 et 1980, l'impossibilité de calculer efficacement le gradient d'un réseau multicouche constituait une impasse majeure, connue sous le nom de problème de l'affectation du crédit (credit assignment problem). Comment déterminer l'influence infinitésimale d'un paramètre enfoui dans les premières couches sur l'erreur globale du système ?

La réponse algébrique et géométrique à ce problème fut formalisée sous le nom de rétropropagation du gradient (backpropagation). Loin d'être un simple algorithme informatique, la rétropropagation est l'application récursive et élégante du théorème de dérivation des fonctions composées, exprimé à travers le formalisme des matrices jacobiennes. Ce jalon unifie le calcul différentiel, l'algèbre linéaire et la théorie de l'optimisation.

\begin{tikzpicture}[
    node distance=2cm,
    every node/.style={circle, draw, minimum size=1cm, text centered},
    arrow/.style={thick, ->, >=stealth}
]
    \node (x) at (0,0) {$x$};
    \node (z1) at (2,0) {$z^{(1)}$};
    \node (a1) at (4,0) {$a^{(1)}$};
    \node (z2) at (6,0) {$z^{(2)}$};
    \node (L) at (8,0) {$\mathcal{L}$};

    \draw[arrow] (x) -- node[above, draw=none] {$W^{(1)}$} (z1);
    \draw[arrow] (z1) -- node[above, draw=none] {$\sigma$} (a1);
    \draw[arrow] (a1) -- node[above, draw=none] {$W^{(2)}$} (z2);
    \draw[arrow] (z2) -- node[above, draw=none] {loss} (L);

    \draw[thick, <-, dashed, red, >=stealth, bend left=30] (z1) to node[below, draw=none, text=red] {$\delta^{(1)}$} (a1);
    \draw[thick, <-, dashed, red, >=stealth, bend left=30] (a1) to node[below, draw=none, text=red] {$\partial a^{(1)}$} (z2);
    \draw[thick, <-, dashed, red, >=stealth, bend left=30] (z2) to node[below, draw=none, text=red] {$\delta^{(2)}$} (L);
\end{tikzpicture}

## Formalisation du Modèle Multicouche

### Définitions Fondamentales

Considérons un perceptron multicouche (MLP) constitué de $L$ couches. Soit $x \in \mathbb{R}^{n_0}$ l'entrée du réseau.
Pour chaque couche $l \in \{1, \dots, L\}$, nous définissons la matrice des poids $W^{(l)} \in \mathcal{M}_{n_l, n_{l-1}}(\mathbb{R})$ et le vecteur de biais $b^{(l)} \in \mathbb{R}^{n_l}$.

La dynamique de propagation avant (forward pass) est régie par les relations de récurrence suivantes :
- $a^{(0)} = x$
- $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$ (vecteur des pré-activations, $z^{(l)} \in \mathbb{R}^{n_l}$)
- $a^{(l)} = \sigma(z^{(l)})$ (vecteur des activations, $a^{(l)} \in \mathbb{R}^{n_l}$, où $\sigma$ est appliquée composante par composante)

La fonction de perte scalaire (par exemple l'erreur quadratique moyenne ou l'entropie croisée) est notée $\mathcal{L} : \mathbb{R}^{n_L} \to \mathbb{R}$, telle que $\text{Perte} = \mathcal{L}(a^{(L)}, y)$, où $y$ est la cible.

### Théorème de Rétropropagation des Erreurs

Soit $\delta^{(l)} = \nabla_{z^{(l)}} \mathcal{L} \in \mathbb{R}^{n_l}$ le vecteur d'erreur associé aux pré-activations de la couche $l$.
La rétropropagation fournit un système d'équations récursif permettant de calculer tous les gradients du réseau de la couche $L$ jusqu'à la couche 1 :

1. **Erreur de sortie :**
   $\delta^{(L)} = \nabla_{a^{(L)}} \mathcal{L} \odot \sigma'(z^{(L)})$
   où $\odot$ dénote le produit de Hadamard (multiplication terme à terme).

2. **Rétropropagation de l'erreur :**
   Pour tout $l \in \{L-1, \dots, 1\}$, l'erreur se propage selon l'équation :
   $\delta^{(l)} = \left( (W^{(l+1)})^T \delta^{(l+1)} \right) \odot \sigma'(z^{(l)})$

3. **Gradients des paramètres :**
   Les dérivées partielles de la perte par rapport aux matrices de poids et aux biais sont données par :
   $\nabla_{W^{(l)}} \mathcal{L} = \delta^{(l)} (a^{(l-1)})^T \in \mathcal{M}_{n_l, n_{l-1}}(\mathbb{R})$
   $\nabla_{b^{(l)}} \mathcal{L} = \delta^{(l)} \in \mathbb{R}^{n_l}$

## Démonstrations Pas à Pas

Nous allons démontrer rigoureusement ces équations en utilisant le formalisme matriciel.

**Démonstration de l'équation des erreurs récursives (2) :**
Appliquons la règle de dérivation des fonctions composées pour exprimer la dérivée de $\mathcal{L}$ par rapport à la $j$-ème composante de $z^{(l)}$ :
$$ \frac{\partial \mathcal{L}}{\partial z^{(l)}_j} = \sum_{k=1}^{n_{l+1}} \frac{\partial \mathcal{L}}{\partial z^{(l+1)}_k} \frac{\partial z^{(l+1)}_k}{\partial z^{(l)}_j} $$
Par définition, le premier terme est $\delta^{(l+1)}_k$.
Explicitons la dépendance de $z^{(l+1)}$ vis-à-vis de $z^{(l)}$ :
$$ z^{(l+1)}_k = \sum_{i=1}^{n_l} W^{(l+1)}_{ki} a^{(l)}_i + b^{(l+1)}_k = \sum_{i=1}^{n_l} W^{(l+1)}_{ki} \sigma(z^{(l)}_i) + b^{(l+1)}_k $$
En dérivant par rapport à $z^{(l)}_j$, tous les termes de la somme s'annulent sauf pour $i=j$ :
$$ \frac{\partial z^{(l+1)}_k}{\partial z^{(l)}_j} = W^{(l+1)}_{kj} \sigma'(z^{(l)}_j) $$
Substituons ce résultat dans la première équation :
$$ \delta^{(l)}_j = \sum_{k=1}^{n_{l+1}} \delta^{(l+1)}_k W^{(l+1)}_{kj} \sigma'(z^{(l)}_j) = \left( \sum_{k=1}^{n_{l+1}} (W^{(l+1)})^T_{jk} \delta^{(l+1)}_k \right) \sigma'(z^{(l)}_j) $$
Ce qui se réécrit matriciellement de manière élégante :
$$ \delta^{(l)} = \left( (W^{(l+1)})^T \delta^{(l+1)} \right) \odot \sigma'(z^{(l)}) $$
La démonstration est ainsi achevée.

## Exemples Concrets et Géométrie des Gradients

Considérons l'équation du gradient des poids : $\nabla_{W^{(l)}} \mathcal{L} = \delta^{(l)} (a^{(l-1)})^T$.
Cette expression correspond à un produit tensoriel (ou produit extérieur) entre deux vecteurs.
- Le vecteur $\delta^{(l)}$ encode le signal d'erreur de correction (la direction vers laquelle pousser la sortie).
- Le vecteur $a^{(l-1)}$ encode l'intensité de l'activation en entrée.
- Le produit extérieur garantit que l'on ajuste fortement les poids reliant les neurones très actifs de la couche $l-1$ vers les neurones de la couche $l$ qui nécessitent une forte correction.

Géométriquement, l'opération $(W^{(l+1)})^T$ transpose l'opérateur linéaire forward. L'erreur est projetée en arrière dans l'espace dual en traversant la matrice transposée, effectuant l'exacte opération adjointe de la propagation avant.

### Problème de l'évanouissement du gradient (Vanishing Gradient)
Si l'on utilise la fonction sigmoïde $\sigma(x) = \frac{1}{1+e^{-x}}$, sa dérivée maximale est $0.25$.
Lors de la propagation d'erreurs profondes sur un réseau de 50 couches, le terme $\sigma'(z^{(l)})$ multiplie itérativement l'erreur par des facteurs inférieurs à $0.25$. Le gradient tend exponentiellement vers zéro, gelant l'apprentissage des premières couches. Ce constat analytique direct justifie l'invention d'activations linéaires par morceaux comme ReLU, où $\sigma'(x) = 1$ pour $x > 0$.
