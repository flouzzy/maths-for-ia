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

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous jouez à "téléphone arabe" mais avec une règle spéciale : à la fin, on compare le message final avec le message original. S'il y a une erreur, on repart en arrière. Le dernier joueur dit à l'avant-dernier : "Tu as un peu trop transformé le son 'A' en 'O'". L'avant-dernier dit au précédent : "Puisqu'il me dit ça, c'est que toi, tu as trop insisté sur telle syllabe". On remonte ainsi jusqu'au premier joueur pour que tout le monde ajuste sa manière de parler. La **Rétropropagation**, c'est exactement ce voyage à rebours pour corriger les erreurs de chaque participant (chaque neurone).
- **Le "Pourquoi on a inventé ça" :** Un réseau de neurones peut avoir des millions de réglages (poids). Si le réseau se trompe, comment savoir quel poids précis il faut modifier ? On ne peut pas tous les tester un par un. La rétropropagation utilise le calcul différentiel pour calculer d'un seul coup l'influence de chaque poids sur l'erreur finale.
- **Visualisation :** Une cascade d'eau qui remonte la montagne. L'erreur "coule" de la sortie vers l'entrée, en se divisant à chaque embranchement selon la pente locale de chaque neurone.

## 2. Formalisation & Rigueur Académique

### A. Modèle du Réseau de Neurones (MLP)

Soit un réseau à $L$ couches. Pour chaque couche $l \in \{1, \dots, L\}$ :
- $a^{(l-1)}$ : vecteur d'entrée (activations de la couche précédente).
- $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$ : somme pondérée (pré-activation).
- $a^{(l)} = \sigma(z^{(l)})$ : vecteur de sortie (activation via une fonction non-linéaire $\sigma$).
- $W^{(l)}$ : matrice des poids de taille $n_l \times n_{l-1}$.
- $\mathcal{L}$ : fonction de perte (Loss) mesurant l'écart entre $a^{(L)}$ et la cible $y$.

### B. Le formalisme Jacobien

Le réseau est une fonction composée : $\mathcal{L} = \ell \circ f_L \circ f_{L-1} \circ \dots \circ f_1(x)$.
D'après la règle de la chaîne (Jalon 46), la différentielle de la perte par rapport à une entrée $x$ est :
$$d\mathcal{L}_x = d\ell_{a^{(L)}} \circ df_{L, a^{(L-1)}} \circ \dots \circ df_{1, x}$$

En termes de matrices jacobiennes, le gradient de la perte par rapport aux activations d'une couche intermédiaire est :
$$\frac{\partial \mathcal{L}}{\partial a^{(l-1)}} = \left( \frac{\partial a^{(l)}}{\partial a^{(l-1)}} \right)^T \frac{\partial \mathcal{L}}{\partial a^{(l)}}$$
où $\frac{\partial a^{(l)}}{\partial a^{(l-1)}}$ est la matrice jacobienne de la couche $l$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Dérivation des équations de base

Posons $\delta^{(l)} = \frac{\partial \mathcal{L}}{\partial z^{(l)}}$ (l'erreur au niveau de la pré-activation).

1. **Étape 1 : Erreur à la couche de sortie ($L$)**
   Par la règle de la chaîne : $\delta^{(L)} = \frac{\partial \mathcal{L}}{\partial a^{(L)}} \odot \sigma'(z^{(L)})$
   (où $\odot$ est le produit de Hadamard, terme à terme).
2. **Étape 2 : Rétropropagation de l'erreur ($\delta^{(l+1)} \to \delta^{(l)}$)**
   On veut $\frac{\partial \mathcal{L}}{\partial z^{(l)}}$. On sait que $z^{(l+1)} = W^{(l+1)} \sigma(z^{(l)}) + b^{(l+1)}$.
   $\frac{\partial z^{(l+1)}}{\partial z^{(l)}} = W^{(l+1)} \cdot \text{diag}(\sigma'(z^{(l)}))$.
   Donc : $\delta^{(l)} = (W^{(l+1)})^T \delta^{(l+1)} \odot \sigma'(z^{(l)})$.
3. **Étape 3 : Gradient par rapport aux poids $W^{(l)}$**
   Comme $z^{(l)}_i = \sum_j W^{(l)}_{ij} a^{(l-1)}_j + b^{(l)}_i$, on a $\frac{\partial z^{(l)}_i}{\partial W^{(l)}_{ij}} = a^{(l-1)}_j$.
   D'où : $\frac{\partial \mathcal{L}}{\partial W^{(l)}} = \delta^{(l)} (a^{(l-1)})^T$.
4. **Conclusion :** Le gradient par rapport à une matrice de poids est le produit extérieur du vecteur d'erreur de la couche actuelle par le vecteur d'activation de la couche précédente.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Un neurone unique
**Énoncé :** Soit un neurone unique $y = \sigma(wx+b)$ avec une perte $\mathcal{L} = \frac{1}{2}(y-t)^2$. Calculer $\frac{\partial \mathcal{L}}{\partial w}$.
**Correction Détaillée :**
1. $\frac{\partial \mathcal{L}}{\partial y} = (y-t)$.
2. $\frac{\partial y}{\partial z} = \sigma'(z)$ où $z=wx+b$.
3. $\frac{\partial z}{\partial w} = x$.
4. Produit : $\frac{\partial \mathcal{L}}{\partial w} = (y-t) \sigma'(z) x$.

### Exercice 2 : Niveau Avancé (Softmax et Cross-Entropy)
**Énoncé :** Montrer que si la sortie est une couche Softmax et la perte est la Cross-Entropy, alors $\delta^{(L)} = a^{(L)} - y$.
**Correction Détaillée :**
C'est un calcul classique montrant que le choix de la paire (Softmax, Cross-Entropy) simplifie radicalement les gradients (l'erreur est simplement la différence entre la prédiction et la cible).
$\mathcal{L} = -\sum y_i \ln(a_i)$ et $a_i = e^{z_i} / \sum e^{z_k}$.
Le calcul de $\frac{\partial \mathcal{L}}{\partial z_i}$ mène directement à $a_i - y_i$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Ce jalon est le pont final entre l'analyse vectorielle et l'IA. Sans la formalisation des Jacobiennes, on ne pourrait pas entraîner de modèles profonds de manière efficace.
- **Exemple Concret :**
    - **Autograd dans PyTorch :** Quand vous écrivez `loss.backward()`, PyTorch parcourt le graphe de calcul en sens inverse et applique exactement ces produits de matrices jacobiennes.
    - **Vanishing Gradient :** Si $\sigma'(z)$ est très petit (ex: zone plate d'une Sigmoïde), le produit de Hadamard va "écraser" le signal $\delta^{(l)}$. Comme on multiplie ces termes à chaque couche, l'erreur devient nulle avant d'atteindre les premières couches du réseau. C'est pourquoi on utilise aujourd'hui des fonctions comme **ReLU** ($\sigma'=1$ pour $z>0$) qui ne saturent pas.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 46 (Matrice jacobienne).md]], [[Jalon 9 (Calcul matriciel).md]]
- **Concepts Futurs dépendants :** [[Jalon 60 (Livrable IA).md]], [[Jalon 132 (Livrable IA).md]]
