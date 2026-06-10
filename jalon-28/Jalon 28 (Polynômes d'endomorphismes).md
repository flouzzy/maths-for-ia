---
uuid: "jalon-28"
title: "Polynômes d'endomorphismes, idéaux annulateurs et théorème de Cayley-Hamilton"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/reduction-endomorphismes
prev: "[[Jalon 27 (Endomorphismes symétriques).md]]"
next: "[[Jalon 29 (Éléments propres).md]]"
---

# Jalon 28 : Polynômes d'endomorphismes, idéaux annulateurs et théorème de Cayley-Hamilton

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Un polynôme, c'est une formule mathématique comme $P(x) = x^2 - 3x + 2$. Si on remplace $x$ par un nombre, on obtient un résultat. La magie ici, c'est qu'on peut remplacer $x$ par une **matrice** (ou un endomorphisme). On obtient alors une nouvelle matrice. Le **théorème de Cayley-Hamilton**, c'est une propriété fascinante : chaque matrice, lorsqu'on la met dans sa propre formule caractéristique, donne la matrice nulle. Elle "s'annule" elle-même.
- **Le "Pourquoi on a inventé ça" :** Pour comprendre comment une transformation agit (rotation, étirement), il faut comprendre ses "polynômes". Cela permet de simplifier les calculs de puissances de matrices (ex: calculer $A^{1000}$ devient très facile avec le polynôme minimal).
- **Visualisation :** Si une matrice est une machine, son polynôme caractéristique est son "ADN". Si vous nourrissez la machine avec son propre ADN, elle s'éteint (elle devient la matrice zéro).

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
1. **Polynôme d'endomorphisme :** Pour $P = \sum_{k=0}^d a_k X^k$, on définit $P(f) = \sum_{k=0}^d a_k f^k$ où $f^k = f \circ ... \circ f$ ($k$ fois).
2. **Idéal annulateur :** L'ensemble $\{ P \in \mathbb{K}[X] \mid P(f) = 0_E \}$ est un idéal de $\mathbb{K}[X]$.
3. **Polynôme minimal :** Unique polynôme unitaire générateur de l'idéal annulateur.

### B. Théorèmes, Propositions & Lemmes
> **Théorème de Cayley-Hamilton :**
> Soit $\chi_f$ le polynôme caractéristique de $f$ ($\chi_f(X) = \det(X \cdot Id - f)$). Alors $\chi_f(f) = 0_E$.

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration : Cayley-Hamilton (pour les matrices diagonalisables)
1. **Initialisation :** Soit $A$ diagonalisable. Il existe $P$ inversible telle que $A = P D P^{-1}$ avec $D = \text{diag}(\lambda_1, ..., \lambda_n)$.
2. **Calcul :** $\chi_A(A) = \det(A \cdot I - A) = P \det(D \cdot I - D) P^{-1} = P \chi_D(D) P^{-1}$.
3. **Diagonal :** $\chi_D(X) = \prod (X - \lambda_i)$. $\chi_D(D) = \text{diag}(\prod (\lambda_j - \lambda_i), ..., \prod (\lambda_j - \lambda_n))$.
4. **Conclusion :** Chaque élément diagonal contient un facteur $(\lambda_i - \lambda_i) = 0$. Donc $\chi_D(D) = 0 \implies \chi_A(A) = 0$.

## 4. Exercices d'Application
### Exercice 1 : Calcul de puissance
$A = \begin{pmatrix} 0 & 1 \ 1 & 0 \end{pmatrix}$. $\chi_A = X^2 - 1$. $A^2 - I = 0 \implies A^2 = I$. $A^n = A$ si $n$ impair, $I$ si $n$ pair.

## 5. Ancrage & Application en IA
Cayley-Hamilton est utilisé pour stabiliser les calculs des réseaux de neurones : si on connaît le polynôme minimal de la matrice de poids, on peut calculer des inverses sans inversion matricielle explicite (très coûteuse).

## 6. Liens Obsidian
- [[Jalon 27 (Endomorphismes symétriques).md]], [[Jalon 29 (Éléments propres).md]]
