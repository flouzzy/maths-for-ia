---
uuid: "jalon-10"
title: "Changements de base, matrices de passage et matrices par blocs"
year: 1
trimester: 1
tags:
  - math/algebre-lineaire
  - ia/changement-repere
prev: "[[Jalon-9.md]]"
next: "[[Jalon 11 (Formes linéaires).md]]"
---
# Jalon 10 : Changements de base, matrices de passage et matrices par blocs

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** 
  - **Changement de base :** Imaginez que vous décriviez un chemin à un ami. Vous pouvez dire "Va 100m au Nord, puis 50m à l'Est" (base standard). Mais votre ami, qui regarde une carte tournée de 45 degrés, préférerait entendre "Va 120m tout droit, puis tourne à gauche". C'est le même chemin, mais décrit dans un **nouveau système de coordonnées**. La **matrice de passage**, c'est le dictionnaire de traduction entre votre Nord/Est et son "Tout droit/Gauche".
  - **Matrices par blocs :** C'est comme diviser une grande tâche complexe en petites sous-tâches. Au lieu de regarder un tableau de 1000 nombres, vous le voyez comme 4 petits tableaux. C'est la base de la modularité.
- **Le "Pourquoi on a inventé ça" :** Certaines transformations sont très difficiles à calculer dans la base "facile" (comme la grille des pixels d'une image), mais deviennent triviales si on change de point de vue (comme les fréquences ou les directions principales des données).
- **Visualisation :** Imaginez que vous inclinez votre tête. Le monde n'a pas changé, mais les axes "Haut/Bas" et "Gauche/Droite" de votre vision ont tourné par rapport au sol. Le changement de base recalcule les coordonnées des objets dans votre nouveau champ de vision.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension $n$.
1. **Matrice de passage ($P_{\mathcal{B} \to \mathcal{B}'}$) :** Soient $\mathcal{B} = (e_1, ..., e_n)$ et $\mathcal{B}' = (e'_1, ..., e'_n)$ deux bases de $E$. La matrice de passage de $\mathcal{B}$ à $\mathcal{B}'$ est la matrice de l'application identité $Id_E$ relativement aux bases $\mathcal{B}'$ (départ) et $\mathcal{B}$ (arrivée) :
   $$P_{\mathcal{B} \to \mathcal{B}'} = \text{Mat}_{\mathcal{B}', \mathcal{B}}(Id_E)$$
   Ses colonnes sont les coordonnées des vecteurs de la "nouvelle" base $\mathcal{B}'$ exprimées dans l' "ancienne" base $\mathcal{B}$.

2. **Matrices par blocs :** Une matrice $M$ peut être découpée en sous-matrices $A, B, C, D$ :
   $$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$$
   Les opérations (somme, produit) se font sur les blocs comme sur des scalaires, à condition que les dimensions des blocs soient compatibles.

### B. Théorèmes, Propositions & Lemmes
> **Formule du changement de base pour un vecteur :**
> Soit $X$ la colonne des coordonnées de $u \in E$ dans $\mathcal{B}$, et $X'$ dans $\mathcal{B}'$. Alors :
> $$X = P X'$$

> **Formule du changement de base pour un endomorphisme :**
> Soit $f \in \mathcal{L}(E)$. Soit $M = \text{Mat}_{\mathcal{B}}(f)$ et $M' = \text{Mat}_{\mathcal{B}'}(f)$. Alors :
> $$M' = P^{-1} M P$$
> On dit que $M$ et $M'$ sont des matrices **semblables**.

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Formule du changement de base pour un endomorphisme
Nous voulons établir $M' = P^{-1} M P$.

1. **Initialisation / Cadre :**
   - Soit $u \in E$ et $v = f(u)$.
   - Soient $X, Y$ les coordonnées de $u, v$ dans $\mathcal{B}$.
   - Soient $X', Y'$ les coordonnées de $u, v$ dans $\mathcal{B}'$.
   - Par définition de la matrice d'un endomorphisme : $Y = MX$ (dans $\mathcal{B}$) et $Y' = M'X'$ (dans $\mathcal{B}'$).
   - Par définition de la matrice de passage $P$ : $X = PX'$ (1) et $Y = PY'$ (2).

2. **Étape 1 : Substitution des vecteurs**
   Partons de l'égalité $Y = MX$.
   Remplaçons $Y$ par son expression en fonction de $Y'$ (en utilisant (2)) :
   $PY' = MX$.

3. **Étape 2 : Substitution de $X$**
   Remplaçons $X$ par son expression en fonction de $X'$ (en utilisant (1)) :
   $PY' = M(PX')$.
   $PY' = MPX'$.

4. **Étape 3 : Isolement de $Y'$**
   Puisque $P$ est une matrice de passage entre deux bases, elle est nécessairement inversible. Multiplions à gauche par $P^{-1}$ :
   $P^{-1} (PY') = P^{-1} (MPX')$
   $(P^{-1} P) Y' = P^{-1} M P X'$
   $I_n Y' = P^{-1} M P X'$
   $Y' = (P^{-1} M P) X'$.

5. **Conclusion :**
   Nous avons obtenu $Y' = (P^{-1} M P) X'$. Or, par définition de $M'$, on a $Y' = M'X'$.
   Ceci étant vrai pour tout vecteur $X'$, on en déduit par unicité de la matrice associée à une application linéaire :
   $M' = P^{-1} M P$.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe (Coordonnées dans une nouvelle base)
**Énoncé :** Dans $\mathbb{R}^2$ muni de la base canonique $\mathcal{B}$, on considère $\mathcal{B}' = (e'_1, e'_2)$ avec $e'_1 = (1, 1)$ et $e'_2 = (1, -1)$. Soit $u$ le vecteur de coordonnées $\begin{pmatrix} 4 \\ 2 \end{pmatrix}$ dans $\mathcal{B}$. Calculer ses coordonnées $X'$ dans $\mathcal{B}'$.
**Correction Détaillée :**
1. **Matrice de passage :** $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
2. **Formule :** $X = PX' \implies X' = P^{-1} X$.
3. **Calcul de $P^{-1}$ :** $\det P = -1 - 1 = -2$. $P^{-1} = \frac{1}{-2} \begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 0.5 & 0.5 \\ 0.5 & -0.5 \end{pmatrix}$.
4. **Calcul de $X'$ :** $X' = \begin{pmatrix} 0.5 & 0.5 \\ 0.5 & -0.5 \end{pmatrix} \begin{pmatrix} 4 \\ 2 \end{pmatrix} = \begin{pmatrix} 2+1 \\ 2-1 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$.
**Conclusion :** $u = 3e'_1 + 1e'_2$.

### Exercice 2 : Niveau Avancé (Matrice par blocs et Inverse)
**Énoncé :** Soit $M = \begin{pmatrix} A & B \\ 0 & D \end{pmatrix}$ une matrice triangulaire supérieure par blocs, où $A$ et $D$ sont carrées et inversibles. Démontrer que $M$ est inversible et exprimer $M^{-1}$ sous forme de blocs.
**Correction Détaillée :**
1. Cherchons $M^{-1} = \begin{pmatrix} X & Y \\ Z & W \end{pmatrix}$ tel que $M M^{-1} = I$.
2. $\begin{pmatrix} A & B \\ 0 & D \end{pmatrix} \begin{pmatrix} X & Y \\ Z & W \end{pmatrix} = \begin{pmatrix} AX+BZ & AY+BW \\ DZ & DW \end{pmatrix} = \begin{pmatrix} I & 0 \\ 0 & I \end{pmatrix}$.
3. Par identification :
   - $DZ = 0 \implies Z = D^{-1} \cdot 0 = 0$ (car $D$ inversible).
   - $DW = I \implies W = D^{-1}$.
   - $AX + BZ = I \implies AX + B(0) = I \implies AX = I \implies X = A^{-1}$.
   - $AY + BW = 0 \implies AY + B D^{-1} = 0 \implies AY = -B D^{-1} \implies Y = -A^{-1} B D^{-1}$.
**Conclusion :** $M$ est inversible et $M^{-1} = \begin{pmatrix} A^{-1} & -A^{-1} B D^{-1} \\ 0 & D^{-1} \end{pmatrix}$.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Le changement de base est l'essence même de l'**Extraction de Caractéristiques** (Feature Engineering). On passe d'un espace de données brutes à un espace où les motifs sont évidents.
- **Exemple Concret :** Dans la **Compression d'Images (JPEG)**, on effectue un changement de base vers la base des **Cosinus Discrets (DCT)**. Dans cette nouvelle base, les informations visuelles importantes se concentrent sur quelques coefficients (les basses fréquences), permettant de supprimer les autres (les hautes fréquences, invisibles à l'œil nu) sans perte de qualité perçue. C'est un changement de base massif appliqué par blocs de $8 \times 8$ pixels.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon-7.md|Jalon 7 (Espaces vectoriels abstraits)]], [[Jalon-9]]
- **Concepts Futurs dépendants :** [[Jalon 29 (Éléments propres)]], [[Jalon 30 (Trigonalisation d'endomorphismes et décomposition de Dunford.)]], [[Jalon 80 (Transformée de Fourier dans L^1)]]
