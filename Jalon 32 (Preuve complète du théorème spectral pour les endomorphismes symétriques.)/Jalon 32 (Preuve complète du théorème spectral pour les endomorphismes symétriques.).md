---
uuid: "jalon-32"
title: "Preuve complète du théorème spectral pour les endomorphismes symétriques"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/optimisation-stochastique
prev: "[[Jalon 31 (Introduction à la réduction de Jordan et structure des nilpotents.).md]]"
next: "[[Jalon 33 (Formes quadratiques).md]]"
---

# Jalon 32 : Preuve complète du théorème spectral pour les endomorphismes symétriques

## 1. L'Intuition Première (Niveau 12 ans)
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous ayez une forme complexe dans l'espace. Le théorème spectral dit que peu importe l'orientation initiale de cette forme, vous pouvez *toujours* trouver un angle de vue spécial (une base orthonormée) où cette forme devient un simple étirement sur des axes privilégiés (les axes principaux). C'est le résultat le plus puissant de l'algèbre linéaire.
- **Le "Pourquoi on a inventé ça" :** Pour simplifier radicalement les transformations linéaires "symétriques" qui préservent certaines structures géométriques.
- **Visualisation :** Un ellipsoïde (un ballon de rugby) peut toujours être orienté pour que ses axes principaux soient alignés avec les axes de coordonnées ($x, y, z$).

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Théorème Fondamental
> **Théorème Spectral :**
> Soit $f$ un endomorphisme symétrique d'un espace euclidien $E$. Alors $f$ est diagonalisable dans une base orthonormée.

### B. Lemme crucial
> $F$ stable par $f \implies F^\perp$ stable par $f$ (si $f$ est symétrique).

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
### Démonstration : Récurrence sur la dimension
1. **Base :** $n=1$, trivial.
2. **Hérédité :** Soit $f$ symétrique sur $E$.
3. **Valeur propre :** $f$ admet au moins une valeur propre réelle $\lambda$ (via le polynôme caractéristique). Soit $u$ un vecteur propre associé ($\|u\|=1$).
4. **Sous-espace :** Soit $F = 	ext{Vect}(u)$. $F$ est stable.
5. **Orthogonal :** $F^\perp$ est stable par $f$ (lemme). $\dim(F^\perp) = n-1$.
6. **Conclusion :** $f_{|F^\perp}$ est symétrique. Par récurrence, $F^\perp$ admet une base orthonormée de vecteurs propres. En ajoutant $u$, on a une base orthonormée de $E$.

## 4. Exercices d'Application
### Exercice 1 : Diagonalisation orthogonale
Soit $A = \begin{pmatrix} 1 & 2 \ 2 & 1 \end{pmatrix}$. $\chi_A = (X-3)(X+1)$. $\lambda_1=3, \lambda_2=-1$. $v_1=(1,1), v_2=(1,-1)$. Normalisés : $e_1 = \frac{1}{\sqrt{2}}(1,1), e_2 = \frac{1}{\sqrt{2}}(1,-1)$.

## 5. Ancrage & Application en IA
*   **PCA (Principal Component Analysis)** est une application directe : on diagonalise la matrice de covariance (qui est symétrique) pour trouver les directions de variance maximale.

## 6. Liens Obsidian
- [[Jalon 27 (Endomorphismes symétriques).md]], [[Jalon 31 (Introduction à la réduction de Jordan et structure des nilpotents.).md]], [[Jalon 33 (Formes quadratiques).md]]
