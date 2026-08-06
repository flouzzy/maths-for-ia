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

# Jalon 48 : Livrable IA T4 : Formalisation mathématique de la Rétropropagation

## Introduction

L'optimisation des architectures neuronales profondes a longtemps été entravée par le problème de l'assignation de crédit : comment déterminer l'influence précise d'un paramètre isolé, enfoui dans de multiples couches de transformations non-linéaires, sur l'erreur globale de prédiction ? L'invention de la rétropropagation (backpropagation), popularisée dans les années 1980 par Rumelhart, Hinton et Williams (et anticipée par des travaux en théorie du contrôle comme ceux de Linnainmaa), résout ce problème de manière élégante par une application systématique de la règle de composition des différentielles. Ce procédé transforme un problème d'optimisation apparemment inextricable en un calcul itératif, couche par couche, tirant parti de la structure modulaire des réseaux de neurones. L'essence géométrique réside dans la propagation à rebours du vecteur gradient de la fonction de coût, modulé par les matrices jacobiennes des transformations locales successives.

## Définitions, Théorèmes et Exemples

### Modèle du Perceptron Multicouche (MLP)

Définissons rigoureusement l'architecture d'un réseau de neurones feedforward à $L$ couches.
Pour chaque couche $l \in \{1, \dots, L\}$, soient $n_{l-1}$ la dimension de l'entrée et $n_l$ la dimension de la sortie :
- $a^{(0)} \in \mathbb{R}^{n_0}$ : le vecteur d'entrée initial (les caractéristiques ou "features").
- $W^{(l)} \in \mathcal{M}_{n_l, n_{l-1}}(\mathbb{R})$ : la matrice des poids synaptiques de la couche $l$.
- $b^{(l)} \in \mathbb{R}^{n_l}$ : le vecteur de biais de la couche $l$.
- $z^{(l)} \in \mathbb{R}^{n_l}$ : le vecteur de pré-activation, défini par $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$.
- $a^{(l)} \in \mathbb{R}^{n_l}$ : le vecteur d'activation, défini par $a^{(l)} = \sigma(z^{(l)})$, où $\sigma : \mathbb{R} \to \mathbb{R}$ est une fonction d'activation non-linéaire (ex: Sigmoïde, ReLU) appliquée composante par composante.

**Exemple :**
Considérons un réseau simple avec $n_0 = 2$, $n_1 = 2$, et $\sigma(x) = \max(0, x)$ (ReLU).
Soit $a^{(0)} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
Pour la couche 1, soit $W^{(1)} = \begin{pmatrix} 0.5 & -0.5 \\ 1 & 0 \end{pmatrix}$ et $b^{(1)} = \begin{pmatrix} 0.2 \\ -1 \end{pmatrix}$.
Le calcul de la pré-activation donne :
$z^{(1)} = \begin{pmatrix} 0.5 & -0.5 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \end{pmatrix} + \begin{pmatrix} 0.2 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} + \begin{pmatrix} 0.2 \\ -1 \end{pmatrix} = \begin{pmatrix} 1.2 \\ 0 \end{pmatrix}$.
Le vecteur d'activation est :
$a^{(1)} = \begin{pmatrix} \max(0, 1.2) \\ \max(0, 0) \end{pmatrix} = \begin{pmatrix} 1.2 \\ 0 \end{pmatrix}$.

### Fonction de Coût et Jacobiennes

La performance du réseau est évaluée par une fonction de perte $\mathcal{L} : \mathbb{R}^{n_L} \times \mathbb{R}^{n_L} \to \mathbb{R}$, mesurant l'écart entre la sortie du réseau $a^{(L)}$ et la cible $y$.
L'objectif est de calculer le gradient de $\mathcal{L}$ par rapport à chaque paramètre $W^{(l)}$ et $b^{(l)}$.
D'après le théorème de dérivation des fonctions composées (Jalon 46), la différentielle de la perte se factorise. Si nous posons $\delta^{(l)} = \nabla_{z^{(l)}} \mathcal{L} \in \mathbb{R}^{n_l}$ (le vecteur d'erreur au niveau de la pré-activation de la couche $l$), on obtient les relations fondamentales de la rétropropagation.

### Théorème de la Rétropropagation

Les vecteurs d'erreur et les gradients satisfont les équations de récurrence arrière suivantes :
1. **Initialisation (couche de sortie) :** $\delta^{(L)} = \nabla_{a^{(L)}} \mathcal{L} \odot \sigma'(z^{(L)})$, où $\odot$ désigne le produit de Hadamard.
2. **Propagation (couches cachées) :** Pour $l = L-1, \dots, 1$, on a $\delta^{(l)} = \left( (W^{(l+1)})^T \delta^{(l+1)} \right) \odot \sigma'(z^{(l)})$.
3. **Gradients des paramètres :**
   - $\nabla_{W^{(l)}} \mathcal{L} = \delta^{(l)} (a^{(l-1)})^T$ (produit extérieur).
   - $\nabla_{b^{(l)}} \mathcal{L} = \delta^{(l)}$.

**Cas pathologiques et limites :**
L'algorithme suppose que $\sigma$ est différentiable. Pour des fonctions comme ReLU, non-différentiable en 0, on adopte la convention $\sigma'(0) = 0$ (sous-gradient usuel).
De plus, si la norme de $W^{(l)}$ ou $\sigma'(z^{(l)})$ est trop faible (ou trop grande), la récurrence $\delta^{(l)} = \left( (W^{(l+1)})^T \delta^{(l+1)} \right) \odot \sigma'(z^{(l)})$ engendre le problème de la disparition (ou de l'explosion) du gradient, empêchant l'apprentissage des couches profondes.

## Démonstrations

Démontrons rigoureusement les équations du théorème de la rétropropagation en employant le calcul différentiel matriciel.

**Démonstration de l'équation 3 (Gradients des poids) :**
La pré-activation est $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$.
Pour une composante $i \in \{1, \dots, n_l\}$, on a $z^{(l)}_i = \sum_{j=1}^{n_{l-1}} W^{(l)}_{ij} a^{(l-1)}_j + b^{(l)}_i$.
Par la règle de la chaîne, la dérivée partielle de la perte par rapport au poids $W^{(l)}_{ij}$ est :
$\frac{\partial \mathcal{L}}{\partial W^{(l)}_{ij}} = \sum_{k=1}^{n_l} \frac{\partial \mathcal{L}}{\partial z^{(l)}_k} \frac{\partial z^{(l)}_k}{\partial W^{(l)}_{ij}}$.
Or, $\frac{\partial z^{(l)}_k}{\partial W^{(l)}_{ij}} = 0$ si $k \neq i$. Pour $k = i$, $\frac{\partial z^{(l)}_i}{\partial W^{(l)}_{ij}} = a^{(l-1)}_j$.
Ainsi, $\frac{\partial \mathcal{L}}{\partial W^{(l)}_{ij}} = \frac{\partial \mathcal{L}}{\partial z^{(l)}_i} a^{(l-1)}_j = \delta^{(l)}_i a^{(l-1)}_j$.
Sous forme matricielle, cela correspond exactement au produit extérieur : $\nabla_{W^{(l)}} \mathcal{L} = \delta^{(l)} (a^{(l-1)})^T$.
De même, $\frac{\partial z^{(l)}_i}{\partial b^{(l)}_i} = 1$, d'où $\nabla_{b^{(l)}} \mathcal{L} = \delta^{(l)}$.

**Démonstration de l'équation 2 (Propagation de l'erreur) :**
Nous cherchons à exprimer $\delta^{(l)} = \nabla_{z^{(l)}} \mathcal{L}$ en fonction de $\delta^{(l+1)} = \nabla_{z^{(l+1)}} \mathcal{L}$.
On a $z^{(l+1)} = W^{(l+1)} a^{(l)} + b^{(l+1)} = W^{(l+1)} \sigma(z^{(l)}) + b^{(l+1)}$.
Pour la composante $k$, on obtient : $z^{(l+1)}_k = \sum_{p=1}^{n_l} W^{(l+1)}_{kp} \sigma(z^{(l)}_p) + b^{(l+1)}_k$.
Par la règle de la chaîne multicouche :
$\delta^{(l)}_j = \frac{\partial \mathcal{L}}{\partial z^{(l)}_j} = \sum_{k=1}^{n_{l+1}} \frac{\partial \mathcal{L}}{\partial z^{(l+1)}_k} \frac{\partial z^{(l+1)}_k}{\partial z^{(l)}_j} = \sum_{k=1}^{n_{l+1}} \delta^{(l+1)}_k W^{(l+1)}_{kj} \sigma'(z^{(l)}_j)$.
En factorisant, on obtient :
$\delta^{(l)}_j = \left( \sum_{k=1}^{n_{l+1}} (W^{(l+1)})^T_{jk} \delta^{(l+1)}_k \right) \sigma'(z^{(l)}_j)$.
Vectoriellement, cela donne bien l'équation 2 : $\delta^{(l)} = \left( (W^{(l+1)})^T \delta^{(l+1)} \right) \odot \sigma'(z^{(l)})$.

## Applications en Physique, Logique et Intelligence Artificielle

En intelligence artificielle, le théorème de rétropropagation constitue le moteur fondamental de l'apprentissage profond (Deep Learning). Les bibliothèques modernes de différenciation automatique, telles que PyTorch ou TensorFlow, construisent dynamiquement le graphe de calcul de la fonction de perte (la passe "forward") puis parcourent ce graphe en sens inverse pour évaluer les gradients via la récurrence démontrée.

En théorie du contrôle optimal (d'où la rétropropagation tire partiellement ses origines), ces équations sont l'équivalent des équations adjoignantes pour le calcul du gradient d'une fonctionnelle de coût dans le principe du maximum de Pontryagin.

Le choix des fonctions d'activation (et de leurs dérivées $\sigma'$) est dicté par ces équations : la fonction sigmoïde, où la dérivée $\sigma'(x) = \sigma(x)(1-\sigma(x))$ atteint un maximum de 0.25, atténue géométriquement l'erreur lors de la rétropropagation, expliquant l'impossibilité historique d'entraîner des réseaux très profonds (Vanishing Gradient) avant l'adoption de fonctions à dérivée unitaire (ReLU).
