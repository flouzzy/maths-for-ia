---
uuid: "jalon-43"
title: "Systèmes différentiels linéaires et exponentielle de matrice"
year: 1
trimester: 4
tags:
  - math/algebre-lineaire
  - ia/systemes-dynamiques
prev: "[[Jalon 42 (Équations différentielles linéaires du second ordre à coefficients constants.).md]]"
next: "[[Jalon 44 (Fonctions de plusieurs variables).md]]"
---

# Jalon 43 : Systèmes différentiels linéaires et exponentielle de matrice

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez un groupe de personnes qui discutent. L'humeur de chaque personne change en fonction de sa propre humeur mais aussi de celle de ses voisins. Si la personne A est joyeuse, elle rend la personne B joyeuse, mais si la personne B devient trop joyeuse, elle finit par agacer la personne A. C'est un **système différentiel** : tout bouge en même temps, et chaque variable influence les autres. L'**exponentielle de matrice**, c'est l'outil qui permet de calculer d'un seul coup l'état de tout le groupe dans 10 minutes, sans avoir à calculer seconde par seconde.
- **Le "Pourquoi on a inventé ça" :** Dans la nature, rien n'est isolé. La température d'une pièce, la pression d'un gaz, le cours de la bourse... tout est lié. Au lieu de résoudre 100 équations séparées, on les regroupe dans une seule boîte (un vecteur) et on utilise une seule matrice pour décrire toutes les interactions.
- **Visualisation :** Imaginez un tourbillon d'eau. Chaque goutte suit une trajectoire complexe, mais le mouvement global est dicté par une structure simple (la matrice). L'exponentielle nous donne la "photo" du tourbillon après un certain temps.

## 2. Formalisation & Rigueur Académique

### A. Systèmes Différentiels Linéaires

Soit $A \in \mathcal{M}_n(\mathbb{R})$ une matrice constante et $B : I \to \mathbb{R}^n$ une fonction continue. On considère le système :
$$(S) : X'(t) = A X(t) + B(t)$$
où $X(t) = (x_1(t), \dots, x_n(t))^T$ est le vecteur des fonctions inconnues.

### B. L'Exponentielle de Matrice

> **Définition (Exponentielle de matrice) :**
> Pour toute matrice carrée $M \in \mathcal{M}_n(\mathbb{K})$, on définit l'exponentielle de $M$ par la série convergente :
> $$\exp(M) = e^M = \sum_{k=0}^{+\infty} \frac{M^k}{k!} = I_n + M + \frac{M^2}{2!} + \dots$$

> **Propriétés fondamentales :**
> 1. Si $A$ et $B$ commutent ($AB=BA$), alors $e^{A+B} = e^A e^B$.
> 2. $e^{P D P^{-1}} = P e^D P^{-1}$. (Très utile pour le calcul via diagonalisation).
> 3. $\frac{d}{dt}(e^{At}) = A e^{At} = e^{At} A$.

### C. Résolution du Système

> **Théorème (Solution du problème de Cauchy) :**
> L'unique solution du système homogène $X' = AX$ vérifiant $X(0) = X_0$ est :
> $$X(t) = e^{At} X_0$$
> Pour le système complet ($B \neq 0$), on utilise la formule de Duhamel :
> $$X(t) = e^{At} X_0 + \int_0^t e^{A(t-s)} B(s) ds$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Calcul de l'exponentielle par diagonalisation

Supposons que $A$ soit diagonalisable : $A = P D P^{-1}$ avec $D = \text{diag}(\lambda_1, \dots, \lambda_n)$.

1. **Étape 1 : Puissances de A**
   $A^k = (P D P^{-1})(P D P^{-1}) \dots (P D P^{-1}) = P D^k P^{-1}$.
2. **Étape 2 : Somme de la série**
   $$e^A = \sum_{k=0}^\infty \frac{P D^k P^{-1}}{k!} = P \left( \sum_{k=0}^\infty \frac{D^k}{k!} \right) P^{-1}$$
3. **Étape 3 : Exponentielle d'une matrice diagonale**
   Comme $D^k = \text{diag}(\lambda_1^k, \dots, \lambda_n^k)$, on a :
   $$e^D = \text{diag}(e^{\lambda_1}, \dots, e^{\lambda_n})$$
4. **Conclusion :**
   $e^A = P \begin{pmatrix} e^{\lambda_1} & & 0 \\ & \ddots & \\ 0 & & e^{\lambda_n} \end{pmatrix} P^{-1}$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Résolution d'un système 2x2
**Énoncé :** Résoudre le système $\begin{cases} x' = x + y \\ y' = x - y \end{cases}$ avec $x(0)=1, y(0)=0$.
**Correction Détaillée :**
1. **Matrice :** $A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
2. **Valeurs propres :** $\chi_A(\lambda) = \lambda^2 - 2$. $\lambda_1 = \sqrt{2}, \lambda_2 = -\sqrt{2}$.
3. **Vecteurs propres :** $v_1 = (1, \sqrt{2}-1), v_2 = (1, -\sqrt{2}-1)$.
4. **Exponentielle :** $e^{At} = P e^{Dt} P^{-1}$.
5. **Solution :** $X(t) = e^{At} \begin{pmatrix} 1 \\ 0 \end{pmatrix}$. Le calcul mène à des combinaisons de $\cosh(\sqrt{2}t)$ et $\sinh(\sqrt{2}t)$.

### Exercice 2 : Niveau Avancé (Matrice nilpotente)
**Énoncé :** Calculer $e^{At}$ pour $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$.
**Correction Détaillée :**
1. **Puissances :** $A^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$, $A^3 = 0$.
2. **Série finie :** $e^{At} = I + tA + \frac{t^2}{2} A^2$.
3. **Résultat :** $e^{At} = \begin{pmatrix} 1 & t & t^2/2 \\ 0 & 1 & t \\ 0 & 0 & 1 \end{pmatrix}$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Les réseaux de neurones récurrents (RNN) et les **Transformers** peuvent être modélisés comme des systèmes dynamiques. L'évolution de l'état caché $h$ est une version discrète de $h' = Ah$.
- **Exemple Concret :**
    - **Problème du Gradient qui disparait (Vanishing Gradient) :** Si les valeurs propres de $A$ ont une partie réelle très négative, $e^{At}$ tend vers 0 très vite : le réseau "oublie" le passé. Si elles sont très positives, l'état explose. Pour avoir une mémoire longue, on veut des valeurs propres proches de 0 (ou sur le cercle unité en discret).
    - **Linear Recurrent Units (LRU) :** Des modèles récents comme S4 ou Mamba utilisent directement des systèmes différentiels linéaires et le calcul de l'exponentielle de matrice (via des techniques de discrétisation sophistiquées comme la transformée bilinéaire) pour traiter des séquences de texte très longues avec une efficacité bien supérieure aux RNN classiques.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 29 (Éléments propres).md]], [[Jalon 30 (Trigonalisation d'endomorphismes et décomposition de Dunford.).md]]
- **Concepts Futurs dépendants :** [[Jalon 44 (Fonctions de plusieurs variables).md]], [[Jalon 128 (Flots de gradient).md]]
