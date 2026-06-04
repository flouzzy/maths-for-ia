---
uuid: "jalon-47"
title: "Dérivées partielles d'ordre deux et Hessienne"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 46 (Matrice jacobienne).md]]"
next: "[[Jalon 48 (Livrable IA).md]]"
---

# Jalon 47 : Dérivées partielles d'ordre deux et Hessienne

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous roulez à vélo sur un terrain vallonné.
    - Le **gradient** (dérivée première) vous dit si vous montez ou si vous descendez à cet instant précis.
    - Les **dérivées secondes** vous disent si le terrain est en train de "se courber" sous vos roues. Est-ce que la montée devient de plus en plus raide (un creux) ou est-ce qu'elle commence à s'aplatir (un sommet) ?
    - La **Matrice Hessienne**, c'est la carte complète de toutes ces courbures dans toutes les directions. Elle permet de savoir si vous êtes dans un vrai trou (minimum), sur un vrai sommet (maximum), ou sur une "selle de cheval" (ça monte dans un sens et ça descend dans l'autre).
- **Le "Pourquoi on a inventé ça" :** Pour ne pas s'arrêter n'importe où. Le gradient s'annule aussi bien au sommet d'une montagne qu'au fond d'un ravin. Les dérivées secondes permettent de faire la différence entre les deux et de garantir qu'on a bien trouvé la solution la plus basse possible.
- **Visualisation :** La forme locale de la surface. Une Hessienne positive correspond à un bol (convexe), une Hessienne négative à une cloche (concave).

## 2. Formalisation & Rigueur Académique

### A. Dérivées d'ordre deux

Soit $f : U \subset \mathbb{R}^n \to \mathbb{R}$ une fonction.

> **Définition 1 (Dérivée seconde partielle) :**
> Si la dérivée partielle $\frac{\partial f}{\partial x_j}$ est elle-même différentiable, on définit la dérivée partielle seconde par rapport à $x_i$ et $x_j$ :
> $$\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial}{\partial x_i} \left( \frac{\partial f}{\partial x_j} \right)$$

> **Théorème (Lemme de Schwarz) :**
> Si $f$ est de classe $\mathcal{C}^2$ sur $U$ (c'est-à-dire que toutes les dérivées secondes existent et sont continues), alors l'ordre des dérivations n'importe pas :
> $$\forall i, j \in \{1, \dots, n\}, \quad \frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i}$$

### B. La Matrice Hessienne

> **Définition 2 (Matrice Hessienne) :**
> Soit $f$ une fonction de classe $\mathcal{C}^2$ en $a \in U$. La **matrice hessienne** de $f$ en $a$ est la matrice symétrique $H_f(a)$ de taille $n \times n$ définie par :
> $$H_f(a) = \begin{pmatrix} \frac{\partial^2 f}{\partial x_1^2}(a) & \dots & \frac{\partial^2 f}{\partial x_1 \partial x_n}(a) \\ \vdots & \ddots & \vdots \\ \frac{\partial^2 f}{\partial x_n \partial x_1}(a) & \dots & \frac{\partial^2 f}{\partial x_n^2}(a) \end{pmatrix}$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Utilisation de la Hessienne pour l'étude des points critiques

Soit $a$ un point critique de $f$ (c'est-à-dire $\nabla f(a) = 0$).

1. **Développement de Taylor à l'ordre 2 :**
   $f(a+h) = f(a) + \frac{1}{2} h^T H_f(a) h + o(\|h\|^2)$.
2. **Analyse de la forme quadratique :**
   La nature du point $a$ dépend de la signature de la forme quadratique associée à $H_f(a)$ (voir Jalon 33).
3. **Cas de $\mathbb{R}^2$ (Déterminant Hessien) :**
   Soit $r = \frac{\partial^2 f}{\partial x^2}$, $s = \frac{\partial^2 f}{\partial x \partial y}$, $t = \frac{\partial^2 f}{\partial y^2}$.
   Le déterminant est $\Delta = rt - s^2$.
   - **Si $\Delta > 0$ :** Extremum local. Un minimum si $r > 0$, un maximum si $r < 0$.
   - **Si $\Delta < 0$ :** Point selle (col).
   - **Si $\Delta = 0$ :** On ne peut pas conclure (cas dégénéré).

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Calcul de Hessienne et nature d'un point
**Énoncé :** Soit $f(x, y) = x^3 + y^3 - 3xy$.
1. Trouver les points critiques.
2. Déterminer leur nature.
**Correction Détaillée :**
1. **Gradient :** $\nabla f = (3x^2 - 3y, 3y^2 - 3x)^T$.
   Points critiques : $x^2 = y$ et $y^2 = x \implies x^4 = x \implies x(x^3-1) = 0$.
   Points : $(0, 0)$ et $(1, 1)$.
2. **Hessienne :** $H_f(x, y) = \begin{pmatrix} 6x & -3 \\ -3 & 6y \end{pmatrix}$.
   - **En $(0, 0)$ :** $H_f = \begin{pmatrix} 0 & -3 \\ -3 & 0 \end{pmatrix}$. $\Delta = -9 < 0$. **Point selle**.
   - **En $(1, 1)$ :** $H_f = \begin{pmatrix} 6 & -3 \\ -3 & 6 \end{pmatrix}$. $\Delta = 36 - 9 = 27 > 0$ et $r=6 > 0$. **Minimum local**.

### Exercice 2 : Niveau Avancé (Laplacien)
**Énoncé :** On appelle Laplacien de $f$ la trace de sa matrice Hessienne : $\Delta f = \sum \frac{\partial^2 f}{\partial x_i^2}$. Montrer que si $f(x, y) = \ln(x^2 + y^2)$, alors $\Delta f = 0$ pour $(x, y) \neq (0, 0)$.
**Correction Détaillée :**
1. $\frac{\partial f}{\partial x} = \frac{2x}{x^2+y^2}$.
2. $\frac{\partial^2 f}{\partial x^2} = \frac{2(x^2+y^2) - 2x(2x)}{(x^2+y^2)^2} = \frac{2y^2 - 2x^2}{(x^2+y^2)^2}$.
3. Par symétrie, $\frac{\partial^2 f}{\partial y^2} = \frac{2x^2 - 2y^2}{(x^2+y^2)^2}$.
4. Somme : $\Delta f = 0$. (On dit que $f$ est une fonction harmonique).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** La courbure de la fonction de perte dictée par la Hessienne est ce qui rend l'entraînement des réseaux de neurones difficile. C'est le problème du **conditionnement**.
- **Exemple Concret :**
    - **Algorithmes de second ordre (Newton) :** On met à jour les poids par $\theta \leftarrow \theta - H_f^{-1} \nabla f$. Cela permet d'aller directement au minimum si la fonction est quadratique. En Deep Learning, $H$ a des milliards de paramètres, on utilise donc des approximations (L-BFGS).
    - **Adam et RMSProp :** Ces algorithmes populaires utilisent une estimation de la courbure (via les moments d'ordre 2 du gradient) pour ajuster le pas d'apprentissage direction par direction. C'est une manière "pauvre" d'utiliser l'information contenue dans la Hessienne sans la calculer.
    - **Stabilité de l'entraînement :** Si la plus grande valeur propre de la Hessienne est très grande, le gradient change très brusquement, ce qui force à utiliser un learning rate minuscule pour ne pas faire exploser le modèle.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 45 (Différentiabilité).md]], [[Jalon 33 (Formes quadratiques).md]]
- **Concepts Futurs dépendants :** [[Jalon 48 (Livrable IA).md]], [[Jalon 117 (Calcul des variations).md]]
