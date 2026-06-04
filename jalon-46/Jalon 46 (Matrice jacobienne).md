---
uuid: "jalon-46"
title: "Matrice jacobienne et Règle de la chaîne"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/backpropagation
prev: "[[Jalon 45 (Différentiabilité).md]]"
next: "[[Jalon 47 (Dérivées partielles d'ordre deux).md]]"
---

# Jalon 46 : Matrice jacobienne et Règle de la chaîne

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez une chaîne de montage dans une usine.
    - La première machine transforme du métal en vis.
    - La deuxième machine assemble les vis pour faire un moteur.
    - La troisième machine installe le moteur dans une voiture.
    Si vous changez un tout petit peu la taille du métal au début, cela va changer la taille de la vis, ce qui changera la puissance du moteur, ce qui changera la vitesse de la voiture. La **Règle de la chaîne**, c'est la formule mathématique qui permet de calculer l'impact final en multipliant les impacts de chaque machine entre elles. La **Matrice Jacobienne**, c'est le "tableau de bord" de chaque machine qui résume comment chaque entrée influence chaque sortie.
- **Le "Pourquoi on a inventé ça" :** Dans les systèmes complexes, les fonctions sont imbriquées. Pour calculer la dérivée d'une fonction composée, on ne peut pas simplement dériver "l'extérieur" ou "l'intérieur". Il faut combiner les deux de manière structurée. C'est la base absolue du fonctionnement des réseaux de neurones profonds.
- **Visualisation :** Une cascade de transformations. Chaque transformation déforme l'espace, et la Jacobienne est la matrice qui décrit localement cette déformation (étirement, rotation).

## 2. Formalisation & Rigueur Académique

### A. La Matrice Jacobienne

Soit $f : U \subset \mathbb{R}^n \to \mathbb{R}^m$ une application différentiable en $a \in U$.
On note $f(x) = (f_1(x), \dots, f_m(x))^T$.

> **Définition (Matrice Jacobienne) :**
> La **matrice jacobienne** de $f$ en $a$, notée $J_f(a)$ ou $Mat(df_a)$, est la matrice de taille $m \times n$ dont les coefficients sont les dérivées partielles des composantes de $f$ :
> $$J_f(a) = \begin{pmatrix} \frac{\partial f_1}{\partial x_1}(a) & \dots & \frac{\partial f_1}{\partial x_n}(a) \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1}(a) & \dots & \frac{\partial f_m}{\partial x_n}(a) \end{pmatrix}$$

### B. Le Théorème de Composition (Chain Rule)

Soient $f : U \subset \mathbb{R}^n \to V \subset \mathbb{R}^p$ et $g : V \to \mathbb{R}^m$.

> **Théorème (Règle de la chaîne généralisée) :**
> Si $f$ est différentiable en $a$ et $g$ est différentiable en $f(a)$, alors $g \circ f$ est différentiable en $a$ et sa différentielle est la composée des différentielles :
> $$d(g \circ f)_a = dg_{f(a)} \circ df_a$$
> En termes de matrices jacobiennes, cela se traduit par un **produit matriciel** :
> $$J_{g \circ f}(a) = J_g(f(a)) \times J_f(a)$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration de la Règle de la Chaîne (Esquisse)

1. **Développements limités :**
   $f(a+h) = f(a) + df_a(h) + \|h\|\epsilon_1(h)$. Posons $k = f(a+h) - f(a)$.
   $g(f(a)+k) = g(f(a)) + dg_{f(a)}(k) + \|k\|\epsilon_2(k)$.
2. **Substitution :**
   $g(f(a+h)) = g(f(a)) + dg_{f(a)}(df_a(h) + \|h\|\epsilon_1(h)) + \|k\|\epsilon_2(k)$.
3. **Linéarité :**
   $g(f(a+h)) = g(f(a)) + dg_{f(a)}(df_a(h)) + dg_{f(a)}(\|h\|\epsilon_1(h)) + \|k\|\epsilon_2(k)$.
4. **Analyse des restes :**
   - $dg_{f(a)}(df_a(h))$ est une application linéaire de $h$ (composée de deux linéaires).
   - Les autres termes sont des $o(\|h\|)$ car $k$ est d'ordre $\|h\|$.
5. **Conclusion :**
   La partie linéaire du développement de $g \circ f$ est $dg_{f(a)} \circ df_a$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Jacobienne d'un passage en polaires
**Énoncé :** Soit $f : \mathbb{R}^2 \to \mathbb{R}^2$ définie par $f(r, \theta) = (r \cos \theta, r \sin \theta)$. Calculer sa matrice jacobienne et son déterminant (le Jacobien).
**Correction Détaillée :**
1. **Composantes :** $x(r, \theta) = r \cos \theta$, $y(r, \theta) = r \sin \theta$.
2. **Dérivées partielles :**
   - $\frac{\partial x}{\partial r} = \cos \theta$, $\frac{\partial x}{\partial \theta} = -r \sin \theta$.
   - $\frac{\partial y}{\partial r} = \sin \theta$, $\frac{\partial y}{\partial \theta} = r \cos \theta$.
3. **Matrice :** $J_f(r, \theta) = \begin{pmatrix} \cos \theta & -r \sin \theta \\ \sin \theta & r \cos \theta \end{pmatrix}$.
4. **Déterminant :** $\det(J_f) = r \cos^2 \theta - (-r \sin^2 \theta) = r(\cos^2 \theta + \sin^2 \theta) = r$.

### Exercice 2 : Application de la Chain Rule
**Énoncé :** Soit $z = f(x, y)$ et $x = u+v, y = u-v$. Exprimer $\frac{\partial z}{\partial u}$ en fonction des dérivées de $f$.
**Correction Détaillée :**
En utilisant la règle de la chaîne :
$\frac{\partial z}{\partial u} = \frac{\partial z}{\partial x} \frac{\partial x}{\partial u} + \frac{\partial z}{\partial y} \frac{\partial y}{\partial u}$.
Comme $\frac{\partial x}{\partial u} = 1$ et $\frac{\partial y}{\partial u} = 1$, on a :
$\frac{\partial z}{\partial u} = \frac{\partial f}{\partial x} + \frac{\partial f}{\partial y}$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** La règle de la chaîne est le moteur de l'algorithme de **Backpropagation** (Rétropropagation du gradient). Un réseau de neurones est une composition massive de fonctions : $Loss = \ell \circ \sigma_k \circ W_k \circ \dots \circ \sigma_1 \circ W_1(input)$.
- **Exemple Concret :**
    - **Calcul du gradient des poids :** Pour mettre à jour la première couche $W_1$, on doit calculer $\frac{\partial Loss}{\partial W_1}$. En utilisant la règle de la chaîne, cela devient un produit de matrices jacobiennes en remontant de la sortie vers l'entrée.
    - **Vecteur-Jacobian Product (VJP) :** Dans les bibliothèques comme PyTorch ou TensorFlow, on ne calcule jamais la matrice jacobienne entière (elle serait trop grosse). On calcule directement le produit d'un vecteur (le gradient de la couche suivante) par la jacobienne de la couche actuelle. C'est l'implémentation efficace de la règle de la chaîne.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 45 (Différentiabilité).md]], [[Jalon 9 (Calcul matriciel).md]]
- **Concepts Futurs dépendants :** [[Jalon 48 (Livrable IA).md]], [[Jalon 111 (Applications différentiables entre variétés).md]]
