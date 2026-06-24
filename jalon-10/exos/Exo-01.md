```yaml
title: Exercice 1
subtitle: Changements de base et matrices de passage
course: Mathématiques pour l'Intelligence Artificielle
level: L1-Master
jalon: 10
exercise: 1
difficulty: 1/5
tags:
  - algèbre linéaire
  - espace vectoriel
  - base
  - coordonnées
  - matrice de passage
  - changement de base
```

# Exercice 1 : Introduction aux changements de base dans $\mathbb{R}^2$

Cet exercice introductif vise à consolider la compréhension des concepts fondamentaux de bases, de coordonnées de vecteurs et de matrices de passage dans un espace vectoriel de dimension finie. Nous travaillerons dans l'espace vectoriel réel $\mathbb{R}^2$.

---

## Énoncé de l'exercice

Soit $E$ un espace vectoriel sur le corps des nombres réels $\mathbb{R}$. On considère spécifiquement l'espace vectoriel $E = \mathbb{R}^2$.

Nous définissons deux bases pour cet espace vectoriel :

1.  La base canonique $\mathcal{B} = (\vec{e_1}, \vec{e_2})$, où les vecteurs sont donnés par :
    $$ \vec{e_1} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}_{\mathcal{B}} \quad \text{et} \quad \vec{e_2} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}_{\mathcal{B}} $$
    Ces coordonnées sont exprimées dans la base $\mathcal{B}$ elle-même, ce qui est la définition des vecteurs de la base canonique.

2.  Une nouvelle base $\mathcal{B}' = (\vec{u_1}, \vec{u_2})$, où les vecteurs sont donnés par leurs coordonnées dans la base canonique $\mathcal{B}$ :
    $$ \vec{u_1} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}_{\mathcal{B}} \quad \text{et} \quad \vec{u_2} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}_{\mathcal{B}} $$
    Ceci signifie que $\vec{u_1} = 2\vec{e_1} + 1\vec{e_2}$ et $\vec{u_2} = -1\vec{e_1} + 1\vec{e_2}$.

Soit un vecteur $\vec{v} \in E$ dont les coordonnées dans la base canonique $\mathcal{B}$ sont données par :
$$ [\vec{v}]_{\mathcal{B}} = \begin{pmatrix} 3 \\ 4 \end{pmatrix} $$

---

## Questions

1.  **Expression des vecteurs de la nouvelle base :**
    Exprimez explicitement les vecteurs de la base $\mathcal{B}'$ en fonction des vecteurs de la base canonique $\mathcal{B}$.

2.  **Matrice de passage de $\mathcal{B}'$ vers $\mathcal{B}$ :**
    Déterminez la matrice de passage $P_{\mathcal{B}' \to \mathcal{B}}$ qui permet de transformer les coordonnées d'un vecteur de la base $\mathcal{B}'$ vers la base $\mathcal{B}$.

3.  **Matrice de passage de $\mathcal{B}$ vers $\mathcal{B}'$ :**
    Déterminez la matrice de passage $P_{\mathcal{B} \to \mathcal{B}'}$ qui permet de transformer les coordonnées d'un vecteur de la base $\mathcal{B}$ vers la base $\mathcal{B}'$.

4.  **Coordonnées du vecteur $\vec{v}$ dans la nouvelle base :**
    En utilisant la matrice de passage appropriée, calculez les coordonnées du vecteur $\vec{v}$ dans la base $\mathcal{B}'$.

5.  **Vérification :**
    Vérifiez le résultat obtenu à la question 4 en exprimant directement le vecteur $\vec{v}$ à partir de ses coordonnées dans la base $\mathcal{B}'$ et des vecteurs de cette base, puis en comparant avec ses coordonnées initiales dans la base $\mathcal{B}$.

---

## Solution

### Question 1 : Expression des vecteurs de la nouvelle base

Les vecteurs de la base $\mathcal{B}' = (\vec{u_1}, \vec{u_2})$ sont donnés par leurs coordonnées dans la base canonique $\mathcal{B} = (\vec{e_1}, \vec{e_2})$.
Par définition, si $[\vec{u_1}]_{\mathcal{B}} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, cela signifie que :
$$ \vec{u_1} = 2 \cdot \vec{e_1} + 1 \cdot \vec{e_2} $$
De même, si $[\vec{u_2}]_{\mathcal{B}} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$, cela signifie que :
$$ \vec{u_2} = -1 \cdot \vec{e_1} + 1 \cdot \vec{e_2} $$

### Question 2 : Matrice de passage $P_{\mathcal{B}' \to \mathcal{B}}$

La matrice de passage $P_{\mathcal{B}' \to \mathcal{B}}$ est la matrice dont les colonnes sont les coordonnées des vecteurs de la nouvelle base $\mathcal{B}'$ exprimées dans l'ancienne base $\mathcal{B}$.
Soit $[\vec{v}]_{\mathcal{B}}$ les coordonnées d'un vecteur $\vec{v}$ dans la base $\mathcal{B}$ et $[\vec{v}]_{\mathcal{B}'}$ ses coordonnées dans la base $\mathcal{B}'$. La relation est donnée par :
$$ [\vec{v}]_{\mathcal{B}} = P_{\mathcal{B}' \to \mathcal{B}} [\vec{v}]_{\mathcal{B}'} $$
Les colonnes de $P_{\mathcal{B}' \to \mathcal{B}}$ sont $[\vec{u_1}]_{\mathcal{B}}$ et $[\vec{u_2}]_{\mathcal{B}}$.
Par conséquent, la matrice $P_{\mathcal{B}' \to \mathcal{B}}$ est :
$$ P_{\mathcal{B}' \to \mathcal{B}} = \begin{pmatrix} [\vec{u_1}]_{\mathcal{B}} & [\vec{u_2}]_{\mathcal{B}} \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix} $$

### Question 3 : Matrice de passage $P_{\mathcal{B} \to \mathcal{B}'}$

La matrice de passage $P_{\mathcal{B} \to \mathcal{B}'}$ est l'inverse de la matrice $P_{\mathcal{B}' \to \mathcal{B}}$.
La relation est donnée par :
$$ [\vec{v}]_{\mathcal{B}'} = P_{\mathcal{B} \to \mathcal{B}'} [\vec{v}]_{\mathcal{B}} $$
Nous devons donc calculer l'inverse de la matrice $P_{\mathcal{B}' \to \mathcal{B}}$.
Soit $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Son inverse $M^{-1}$ est donnée par la formule :
$$ M^{-1} = \frac{1}{\det(M)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} $$
où $\det(M) = ad - bc$.

Pour notre matrice $P_{\mathcal{B}' \to \mathcal{B}} = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix}$ :
1.  Calcul du déterminant :
    $$ \det(P_{\mathcal{B}' \to \mathcal{B}}) = (2)(1) - (-1)(1) = 2 - (-1) = 2 + 1 = 3 $$
    Puisque le déterminant est non nul ($\det(P_{\mathcal{B}' \to \mathcal{B}}) = 3 \neq 0$), la matrice est inversible.

2.  Calcul de l'inverse :
    $$ P_{\mathcal{B} \to \mathcal{B}'} = (P_{\mathcal{B}' \to \mathcal{B}})^{-1} = \frac{1}{3} \begin{pmatrix} 1 & -(-1) \\ -1 & 2 \end{pmatrix} $$
    $$ P_{\mathcal{B} \to \mathcal{B}'} = \frac{1}{3} \begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix} $$
    $$ P_{\mathcal{B} \to \mathcal{B}'} = \begin{pmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{pmatrix} $$

### Question 4 : Coordonnées du vecteur $\vec{v}$ dans la nouvelle base

Nous avons les coordonnées de $\vec{v}$ dans la base $\mathcal{B}$ :
$$ [\vec{v}]_{\mathcal{B}} = \begin{pmatrix} 3 \\ 4 \end{pmatrix} $$
Et la matrice de passage de $\mathcal{B}$ vers $\mathcal{B}'$ :
$$ P_{\mathcal{B} \to \mathcal{B}'} = \begin{pmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{pmatrix} $$
Pour trouver les coordonnées de $\vec{v}$ dans la base $\mathcal{B}'$, nous appliquons la formule :
$$ [\vec{v}]_{\mathcal{B}'} = P_{\mathcal{B} \to \mathcal{B}'} [\vec{v}]_{\mathcal{B}} $$
$$ [\vec{v}]_{\mathcal{B}'} = \begin{pmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{pmatrix} \begin{pmatrix} 3 \\ 4 \end{pmatrix} $$
Effectuons la multiplication matricielle :
$$ [\vec{v}]_{\mathcal{B}'} = \begin{pmatrix} (1/3) \cdot 3 + (1/3) \cdot 4 \\ (-1/3) \cdot 3 + (2/3) \cdot 4 \end{pmatrix} $$
$$ [\vec{v}]_{\mathcal{B}'} = \begin{pmatrix} 1 + 4/3 \\ -1 + 8/3 \end{pmatrix} $$
Pour simplifier les fractions :
$$ [\vec{v}]_{\mathcal{B}'} = \begin{pmatrix} 3/3 + 4/3 \\ -3/3 + 8/3 \end{pmatrix} $$
$$ [\vec{v}]_{\mathcal{B}'} = \begin{pmatrix} 7/3 \\ 5/3 \end{pmatrix} $$
Les coordonnées du vecteur $\vec{v}$ dans la base $\mathcal{B}'$ sont donc $[\vec{v}]_{\mathcal{B}'} = \begin{pmatrix} 7/3 \\ 5/3 \end{pmatrix}$.

### Question 5 : Vérification

Pour vérifier le résultat, nous allons exprimer le vecteur $\vec{v}$ en utilisant ses coordonnées dans la base $\mathcal{B}'$ et les vecteurs de cette base, puis comparer avec ses coordonnées initiales dans $\mathcal{B}$.
Nous avons $[\vec{v}]_{\mathcal{B}'} = \begin{pmatrix} 7/3 \\ 5/3 \end{pmatrix}$, ce qui signifie que :
$$ \vec{v} = (7/3) \cdot \vec{u_1} + (5/3) \cdot \vec{u_2} $$
Nous substituons les expressions de $\vec{u_1}$ et $\vec{u_2}$ en fonction de $\vec{e_1}$ et $\vec{e_2}$ (obtenues à la Question 1) :
$$ \vec{v} = (7/3) \cdot \begin{pmatrix} 2 \\ 1 \end{pmatrix}_{\mathcal{B}} + (5/3) \cdot \begin{pmatrix} -1 \\ 1 \end{pmatrix}_{\mathcal{B}} $$
Effectuons la multiplication scalaire et l'addition vectorielle :
$$ \vec{v} = \begin{pmatrix} (7/3) \cdot 2 \\ (7/3) \cdot 1 \end{pmatrix}_{\mathcal{B}} + \begin{pmatrix} (5/3) \cdot (-1) \\ (5/3) \cdot 1 \end{pmatrix}_{\mathcal{B}} $$
$$ \vec{v} = \begin{pmatrix} 14/3 \\ 7/3 \end{pmatrix}_{\mathcal{B}} + \begin{pmatrix} -5/3 \\ 5/3 \end{pmatrix}_{\mathcal{B}} $$
$$ \vec{v} = \begin{pmatrix} 14/3 + (-5/3) \\ 7/3 + 5/3 \end{pmatrix}_{\mathcal{B}} $$
$$ \vec{v} = \begin{pmatrix} (14 - 5)/3 \\ (7 + 5)/3 \end{pmatrix}_{\mathcal{B}} $$
$$ \vec{v} = \begin{pmatrix} 9/3 \\ 12/3 \end{pmatrix}_{\mathcal{B}} $$
$$ \vec{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}_{\mathcal{B}} $$
Les coordonnées obtenues pour $\vec{v}$ dans la base $\mathcal{B}$ sont $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$, ce qui correspond exactement aux coordonnées initiales données dans l'énoncé. La vérification est concluante.
