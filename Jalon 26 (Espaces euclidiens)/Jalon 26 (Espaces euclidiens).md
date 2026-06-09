---
uuid: "jalon-26"
title: "Espaces euclidiens, orthogonalité, théorème de la projection orthogonale et algorithme de Gram-Schmidt"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/projection-donnees
prev: "[[Jalon 25 (Formes bilinéaires).md]]"
next: "[[Jalon 27 (Endomorphismes symétriques).md]]"
---

# Jalon 26 : Espaces euclidiens, orthogonalité, théorème de la projection orthogonale et algorithme de Gram-Schmidt

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** 
  - **Espace Euclidien :** C'est le monde de la géométrie parfaite, comme l'écran de votre smartphone où l'on peut mesurer des distances et des angles.
  - **Orthogonalité :** C'est l'équerre. Deux vecteurs sont orthogonaux s'ils forment un angle droit parfait. Ils sont "indépendants" au sens où bouger dans une direction ne fait pas avancer dans l'autre.
  - **Projection Orthogonale :** Imaginez que vous soyez sous un lampadaire à midi. Votre ombre sur le sol est votre projection. C'est le point du sol le plus proche de vous. 
  - **Gram-Schmidt :** C'est une machine à redresser. Vous lui donnez des bâtons tout tordus (une base quelconque), et elle les retaille et les oriente pour en faire une structure d'échafaudage parfaite avec des angles droits (une base orthonormée).
- **Le "Pourquoi on a inventé ça" :** Travailler avec des angles droits simplifie énormément les calculs. Au lieu d'avoir des équations croisées, chaque dimension devient indépendante. La projection est l'outil ultime pour simplifier des données : on garde l'essentiel (l'ombre) et on ignore le reste.
- **Visualisation :** Imaginez un plan incliné dans l'espace. Projeter un point sur ce plan, c'est trouver la "perpendiculaire" qui tombe pile sur le plan. C'est la distance la plus courte.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $E$ un espace vectoriel réel de dimension finie $n$.
1. **Espace Euclidien :** Un espace vectoriel réel muni d'un produit scalaire $\langle \cdot, \cdot \rangle$.
2. **Orthogonalité :** $x \perp y \iff \langle x, y \rangle = 0$.
3. **Famille Orthonormée :** Une famille $(e_1, ..., e_k)$ telle que $\langle e_i, e_j \rangle = \delta_{i,j}$ (orthogonaux et de norme 1).
4. **Sous-espace Orthogonal :** Soit $F$ un sous-espace de $E$. $F^\perp = \{ x \in E \mid \forall y \in F, \langle x, y \rangle = 0 \}$.
5. **Projection Orthogonale :** Soit $E = F \oplus F^\perp$. L'application $p_F$ qui à $x = y + z$ (avec $y \in F, z \in F^\perp$) associe $y$.

### B. Théorèmes, Propositions & Lemmes
> **Théorème de la Projection Orthogonale :**
> Soit $F$ un sous-espace vectoriel de $E$. Pour tout $x \in E$, $p_F(x)$ est l'unique élément de $F$ qui minimise la distance à $x$ :
> $$\|x - p_F(x)\| = \min_{y \in F} \|x - y\|$$

> **Existence de bases orthonormées :**
> Tout espace euclidien non nul admet au moins une base orthonormée.

> **Théorème de Pythagore :**
> $x \perp y \implies \|x+y\|^2 = \|x\|^2 + \|y\|^2$.

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Formule de la projection orthogonale
Soit $F$ un sous-espace de $E$ et $(e_1, ..., e_k)$ une base **orthonormée** de $F$. Montrons que pour tout $x \in E$, $p_F(x) = \sum_{i=1}^k \langle x, e_i \rangle e_i$.

1. **Initialisation / Cadre :** Posons $y = \sum_{i=1}^k \langle x, e_i \rangle e_i$. 
   - Par construction, $y$ est une combinaison linéaire des vecteurs de la base de $F$, donc $y \in F$.
   - Pour montrer que $y = p_F(x)$, il suffit de prouver que $(x - y) \in F^\perp$.
   - Un vecteur est dans $F^\perp$ s'il est orthogonal à tous les vecteurs d'une base de $F$. Montrons donc que $\forall j \in \{1, ..., k\}, \langle x - y, e_j \rangle = 0$.

2. **Étape 1 : Développement du produit scalaire**
   $\langle x - y, e_j \rangle = \langle x, e_j \rangle - \langle y, e_j \rangle$ (par linéarité à gauche).
   Substituons l'expression de $y$ :
   $\langle y, e_j \rangle = \langle \sum_{i=1}^k \langle x, e_i \rangle e_i, e_j \rangle$.

3. **Étape 2 : Utilisation de la linéarité et de l'orthonormalité**
   Par linéarité à gauche :
   $\langle y, e_j \rangle = \sum_{i=1}^k \langle x, e_i \rangle \langle e_i, e_j \rangle$.
   Or, la famille $(e_i)$ est orthonormée, donc $\langle e_i, e_j \rangle = 0$ si $i \neq j$ et $\langle e_i, e_j \rangle = 1$ si $i = j$.
   Dans la somme, il ne reste que le terme $i = j$ :
   $$\langle y, e_j \rangle = \langle x, e_j \rangle \cdot 1 = \langle x, e_j \rangle$$

4. **Étape 3 : Calcul final**
   $\langle x - y, e_j \rangle = \langle x, e_j \rangle - \langle x, e_j \rangle = 0$.
   Ceci est vrai pour tout $j \in \{1, ..., k\}$.

5. **Conclusion :**
   Le vecteur $(x - y)$ est orthogonal à tous les vecteurs de la base de $F$, donc $(x - y) \in F^\perp$.
   Comme $x = y + (x-y)$ avec $y \in F$ et $(x-y) \in F^\perp$, alors par définition de la projection orthogonale, $y = p_F(x)$.
   La formule est démontrée.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Algorithme de Gram-Schmidt
**Énoncé :** Dans $\mathbb{R}^3$, transformer la base $\mathcal{B} = (v_1, v_2, v_3)$ avec $v_1=(1,1,0), v_2=(1,0,1), v_3=(0,1,1)$ en une base orthonormée $(e_1, e_2, e_3)$.
**Correction Détaillée :**
1. **Calcul de $e_1$ :**
   - $u_1 = v_1 = (1, 1, 0)$.
   - $\|u_1\| = \sqrt{1^2 + 1^2} = \sqrt{2}$.
   - $e_1 = \frac{u_1}{\|u_1\|} = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0)$.
2. **Calcul de $e_2$ :**
   - $u_2 = v_2 - \langle v_2, e_1 \rangle e_1$.
   - $\langle v_2, e_1 \rangle = 1 \cdot \frac{1}{\sqrt{2}} + 0 \cdot \frac{1}{\sqrt{2}} + 1 \cdot 0 = \frac{1}{\sqrt{2}}$.
   - $u_2 = (1, 0, 1) - \frac{1}{\sqrt{2}} (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0) = (1, 0, 1) - (1/2, 1/2, 0) = (1/2, -1/2, 1)$.
   - $\|u_2\| = \sqrt{1/4 + 1/4 + 1} = \sqrt{3/2}$.
   - $e_2 = \frac{u_2}{\|u_2\|} = (\frac{1}{\sqrt{6}}, -\frac{1}{\sqrt{6}}, \frac{2}{\sqrt{6}})$.
3. **Calcul de $e_3$ :** (Même principe, orthogonalisation par rapport à $e_1$ et $e_2$).
**Conclusion :** On obtient une base où tous les vecteurs sont de norme 1 et deux à deux orthogonaux.

### Exercice 2 : Niveau Avancé (Meilleure approximation)
**Énoncé :** Déterminer la distance du point $A(1, 2, 3)$ au plan $P$ d'équation $x + y + z = 0$.
**Correction Détaillée :**
1. La distance est donnée par $\| \vec{OA} - p_P(\vec{OA}) \| = \| p_{P^\perp}(\vec{OA}) \|$.
2. Le vecteur normal au plan est $n = (1, 1, 1)$. La droite $P^\perp$ est $\text{Vect}(n)$.
3. Une base orthonormée de $P^\perp$ est $e = \frac{n}{\|n\|} = (\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}})$.
4. La projection sur $P^\perp$ est : $p_{P^\perp}(v) = \langle v, e \rangle e$.
5. $\langle \vec{OA}, e \rangle = 1 \cdot \frac{1}{\sqrt{3}} + 2 \cdot \frac{1}{\sqrt{3}} + 3 \cdot \frac{1}{\sqrt{3}} = \frac{6}{\sqrt{3}} = 2\sqrt{3}$.
6. $\| p_{P^\perp}(\vec{OA}) \| = | \langle \vec{OA}, e \rangle | \cdot \|e\| = 2\sqrt{3} \cdot 1 = 2\sqrt{3}$.
**Conclusion :** La distance est $2\sqrt{3}$.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** La projection orthogonale est le fondement de la **Réduction de Bruit** et de la **Compression**.
- **Exemple Concret :** Dans l'**ACP (Analyse en Composantes Principales)**, on cherche un sous-espace $F$ (de dimension $k < n$) qui préserve le plus d'information possible des données. Mathématiquement, on projette orthogonalement tous les vecteurs de données sur ce sous-espace. L'algorithme de **Gram-Schmidt** est utilisé numériquement (sous la forme de la **Décomposition QR**) pour stabiliser les calculs de matrices de poids dans les réseaux de neurones profonds, garantissant que les filtres d'une même couche restent orthogonaux et ne capturent pas des informations redondantes.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 25 (Formes bilinéaires)]]
- **Concepts Futurs dépendants :** [[Jalon 27 (Endomorphismes symétriques)]], [[Jalon 32 (Preuve complète du théorème spectral pour les endomorphismes symétriques.)]], [[Jalon 36 (Livrable IA)]], [[Jalon 103 (Espaces de Hilbert généraux)]]
