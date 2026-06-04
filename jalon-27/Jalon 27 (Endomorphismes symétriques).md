---
uuid: "jalon-27"
title: "Endomorphismes symétriques, adjoint d'un opérateur et matrices orthogonales"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/matrices-symetriques
prev: "[[Jalon 26 (Espaces euclidiens).md]]"
next: "[[Jalon 28 (Polynômes d'endomorphismes).md]]"
---
# Jalon 27 : Endomorphismes symétriques, adjoint d'un opérateur et matrices orthogonales

## 1. L'Intuition Première (Niveau 12 ans)
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** 
  - **Adjoint d'un opérateur :** Imaginez une machine qui transforme des objets. L'adjoint, c'est comme regarder le fonctionnement de cette machine "à l'envers", ou plutôt voir comment elle se comporte avec le produit scalaire (la mesure de proximité). C'est le "compagnon" de l'opérateur.
  - **Endomorphisme symétrique :** C'est une machine dont l'effet est parfaitement équilibré. Dans un miroir, elle se comporte exactement de la même manière. Physiquement, cela correspond souvent à des systèmes qui conservent l'énergie.
  - **Matrice orthogonale :** C'est une machine qui ne change jamais la taille des objets, ni les angles entre eux : elle ne fait que tourner ou retourner l'espace. C'est une "isométrie", comme une rotation solide.
- **Le "Pourquoi on a inventé ça" :** Les opérateurs symétriques ont des propriétés magiques : ils sont toujours diagonalisables avec des bases orthogonales. Cela simplifie radicalement les calculs en physique et en IA.
- **Visualisation :** Une rotation 2D est une matrice orthogonale. Un étirement sur les axes est une matrice symétrique.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $E$ un espace euclidien.
1. **Adjoint d'un endomorphisme :** Pour $f \in \mathcal{L}(E)$, il existe un unique endomorphisme $f^* \in \mathcal{L}(E)$ tel que $\forall x, y \in E, \langle f(x), y \rangle = \langle x, f^*(y) \rangle$.
2. **Endomorphisme symétrique :** $f \in \mathcal{L}(E)$ est symétrique si $f^* = f$. (Matrice symétrique $A^T = A$).
3. **Matrice Orthogonale :** $P \in \mathcal{M}_n(\mathbb{R})$ est orthogonale si $P^T P = I_n$. Les colonnes de $P$ forment une base orthonormée de $\mathbb{R}^n$.

### B. Théorèmes, Propositions & Lemmes
> **Théorème Spectral (Version compacte) :**
> Si $f$ est symétrique, alors il existe une base orthonormée de vecteurs propres de $f$. $f$ est diagonalisable dans une base orthonormée.

> **Isométries et Matrices orthogonales :**
> $f$ est une isométrie $\iff \text{Mat}(f)$ est orthogonale.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
### Démonstration : $f$ symétrique $\implies$ sous-espaces propres orthogonaux
Soient $\lambda, \mu$ deux valeurs propres distinctes de $f$ symétrique, et $x, y$ des vecteurs propres associés.

1. **Initialisation :** $\langle f(x), y \rangle = \langle \lambda x, y \rangle = \lambda \langle x, y \rangle$.
2. **Utilisation de la symétrie :** $\langle f(x), y \rangle = \langle x, f(y) \rangle = \langle x, \mu y \rangle = \mu \langle x, y \rangle$.
3. **Égalité :** $\lambda \langle x, y \rangle = \mu \langle x, y \rangle \implies (\lambda - \mu) \langle x, y \rangle = 0$.
4. **Conclusion :** Comme $\lambda \neq \mu$, alors $\langle x, y \rangle = 0$. Les espaces propres sont orthogonaux.

## 4. Exercices d'Application
### Exercice 1 : Orthogonalité
Vérifier si $A = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -1 \ 1 & 1 \end{pmatrix}$ est orthogonale.
*   $A^T A = \frac{1}{2} \begin{pmatrix} 1 & 1 \ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \ 1 & 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 2 & 0 \ 0 & 2 \end{pmatrix} = I_2$. Oui.

## 5. Ancrage & Application en IA
*   **Les noyaux symétriques** dans les réseaux de neurones (ex: poids partagés) permettent de réduire drastiquement le nombre de paramètres.
*   **PCA** repose entièrement sur le théorème spectral appliqué à la matrice de covariance (qui est symétrique).

## 6. Liens Obsidian
- [[Jalon 26 (Espaces euclidiens).md]], [[Jalon 28 (Polynômes d'endomorphismes).md]]
