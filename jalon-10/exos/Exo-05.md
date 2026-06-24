```yaml
title: "Exercice 05 : Changements de Base et Représentation Matricielle d'Applications Linéaires"
subtitle: "Jalon 10 - Changements de base, matrices de passage et matrices par blocs"
date: 2023-10-27
authors:
  - Pr. Intelligence Artificielle
keywords:
  - Algèbre Linéaire
  - Espaces Vectoriels
  - Bases
  - Coordonnées
  - Matrices de Passage
  - Applications Linéaires
  - Matrices d'Applications Linéaires
  - Changement de Base
tags:
  - Mathématiques
  - Intelligence Artificielle
  - L1
  - L2
  - L3
  - Master
  - Exercice
level: 3/5
subject: Mathématiques pour l'Intelligence Artificielle
chapter: Jalon 10
exercise_number: 05
```

# Exercice 05 : Changements de Base et Représentation Matricielle d'Applications Linéaires

## Préambule

Soit $\mathbb{K} = \mathbb{R}$ le corps des nombres réels.
Soit $E = \mathbb{R}^2$ l'espace vectoriel réel de dimension 2 sur le corps $\mathbb{R}$.

Nous considérons deux bases de $E$:
*   La base canonique $\mathcal{B}_0 = (e_1, e_2)$, où $e_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ et $e_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.
*   Une autre base $\mathcal{B}_1 = (u_1, u_2)$, où $u_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ et $u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.

Soit un vecteur $v \in E$ défini par $v = \begin{pmatrix} 3 \\ -1 \end{pmatrix}$.
Soit une application linéaire $f: E \to E$ définie pour tout vecteur $x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \in E$ par $f(x) = \begin{pmatrix} x_1 + 2x_2 \\ -x_1 + x_2 \end{pmatrix}$.

## Partie 1 : Coordonnées d'un vecteur

1.  Déterminer les coordonnées du vecteur $v$ dans la base $\mathcal{B}_0$. Nous noterons ce vecteur colonne $[v]_{\mathcal{B}_0}$.
2.  Déterminer les coordonnées du vecteur $v$ dans la base $\mathcal{B}_1$. Nous noterons ce vecteur colonne $[v]_{\mathcal{B}_1}$.

## Partie 2 : Matrices de passage

1.  Déterminer la matrice de passage $P_{\mathcal{B}_0 \to \mathcal{B}_1}$ de la base $\mathcal{B}_0$ à la base $\mathcal{B}_1$.
2.  Déterminer la matrice de passage $P_{\mathcal{B}_1 \to \mathcal{B}_0}$ de la base $\mathcal{B}_1$ à la base $\mathcal{B}_0$. Vérifier que $P_{\mathcal{B}_1 \to \mathcal{B}_0} = (P_{\mathcal{B}_0 \to \mathcal{B}_1})^{-1}$.

## Partie 3 : Représentation matricielle d'une application linéaire

1.  Déterminer la matrice $A = \text{Mat}_{\mathcal{B}_0}(f)$ de l'application linéaire $f$ dans la base $\mathcal{B}_0$.
2.  En utilisant la relation de changement de base pour les matrices d'applications linéaires, déterminer la matrice $A' = \text{Mat}_{\mathcal{B}_1}(f)$ de l'application linéaire $f$ dans la base $\mathcal{B}_1$.
    La relation à utiliser est $A' = (P_{\mathcal{B}_0 \to \mathcal{B}_1})^{-1} A P_{\mathcal{B}_0 \to \mathcal{B}_1}$.
3.  Vérifier le résultat de la question précédente en calculant directement la matrice $A' = \text{Mat}_{\mathcal{B}_1}(f)$ en exprimant $f(u_1)$ et $f(u_2)$ dans la base $\mathcal{B}_1$.

---

## Corrigé de l'Exercice 05

### Partie 1 : Coordonnées d'un vecteur

1.  **Détermination des coordonnées du vecteur $v$ dans la base $\mathcal{B}_0$ :**

    Soit le vecteur $v \in E$ donné par $v = \begin{pmatrix} 3 \\ -1 \end{pmatrix}$.
    La base $\mathcal{B}_0 = (e_1, e_2)$ est la base canonique de $E = \mathbb{R}^2$, où $e_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ et $e_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.
    Par définition, les coordonnées d'un vecteur $v$ dans la base canonique sont les composantes du vecteur lui-même.
    Nous cherchons des scalaires $\alpha_1, \alpha_2 \in \mathbb{R}$ tels que $v = \alpha_1 e_1 + \alpha_2 e_2$.
    Ainsi, nous avons :
    $$ \begin{pmatrix} 3 \\ -1 \end{pmatrix} = \alpha_1 \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \alpha_2 \begin{pmatrix} 0 \\ 1 \end{pmatrix} $$
    $$ \begin{pmatrix} 3 \\ -1 \end{pmatrix} = \begin{pmatrix} \alpha_1 \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ \alpha_2 \end{pmatrix} $$
    $$ \begin{pmatrix} 3 \\ -1 \end{pmatrix} = \begin{pmatrix} \alpha_1 \\ \alpha_2 \end{pmatrix} $$
    Par identification des composantes, nous obtenons $\alpha_1 = 3$ et $\alpha_2 = -1$.
    Les coordonnées du vecteur $v$ dans la base $\mathcal{B}_0$ sont donc :
    $$ [v]_{\mathcal{B}_0} = \begin{pmatrix} 3 \\ -1 \end{pmatrix} $$

2.  **Détermination des coordonnées du vecteur $v$ dans la base $\mathcal{B}_1$ :**

    La base $\mathcal{B}_1 = (u_1, u_2)$ est donnée par $u_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ et $u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.
    Nous cherchons des scalaires $\beta_1, \beta_2 \in \mathbb{R}$ tels que $v = \beta_1 u_1 + \beta_2 u_2$.
    Nous avons :
    $$ \begin{pmatrix} 3 \\ -1 \end{pmatrix} = \beta_1 \begin{pmatrix} 1 \\ 1 \end{pmatrix} + \beta_2 \begin{pmatrix} -1 \\ 1 \end{pmatrix} $$
    $$ \begin{pmatrix} 3 \\ -1 \end{pmatrix} = \begin{pmatrix} \beta_1 \\ \beta_1 \end{pmatrix} + \begin{pmatrix} -\beta_2 \\ \beta_2 \end{pmatrix} $$
    $$ \begin{pmatrix} 3 \\ -1 \end{pmatrix} = \begin{pmatrix} \beta_1 - \beta_2 \\ \beta_1 + \beta_2 \end{pmatrix} $$
    Ceci nous conduit au système d'équations linéaires suivant :
    $$ \begin{cases} \beta_1 - \beta_2 = 3 & (L_1) \\ \beta_1 + \beta_2 = -1 & (L_2) \end{cases} $$
    Additionnons l'équation $(L_1)$ et l'équation $(L_2)$ :
    $$ (\beta_1 - \beta_2) + (\beta_1 + \beta_2) = 3 + (-1) $$
    $$ 2\beta_1 = 2 $$
    $$ \beta_1 = 1 $$
    Substituons la valeur de $\beta_1$ dans l'équation $(L_2)$ :
    $$ 1 + \beta_2 = -1 $$
    $$ \beta_2 = -1 - 1 $$
    $$ \beta_2 = -2 $$
    Les coordonnées du vecteur $v$ dans la base $\mathcal{B}_1$ sont donc :
    $$ [v]_{\mathcal{B}_1} = \begin{pmatrix} 1 \\ -2 \end{pmatrix} $$

### Partie 2 : Matrices de passage

1.  **Détermination de la matrice de passage $P_{\mathcal{B}_0 \to \mathcal{B}_1}$ de la base $\mathcal{B}_0$ à la base $\mathcal{B}_1$ :**

    La matrice de passage $P_{\mathcal{B}_0 \to \mathcal{B}_1}$ est la matrice dont les colonnes sont les vecteurs de la base $\mathcal{B}_1$ exprimés dans la base $\mathcal{B}_0$.
    Les vecteurs de la base $\mathcal{B}_1$ sont $u_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ et $u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.
    Les vecteurs de la base $\mathcal{B}_0$ sont $e_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ et $e_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.
    Exprimons $u_1$ et $u_2$ en fonction de $e_1$ et $e_2$:
    $$ u_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} = 1 \cdot \begin{pmatrix} 1 \\ 0 \end{pmatrix} + 1 \cdot \begin{pmatrix} 0 \\ 1 \end{pmatrix} = 1 \cdot e_1 + 1 \cdot e_2 $$
    $$ u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix} = -1 \cdot \begin{pmatrix} 1 \\ 0 \end{pmatrix} + 1 \cdot \begin{pmatrix} 0 \\ 1 \end{pmatrix} = -1 \cdot e_1 + 1 \cdot e_2 $$
    La matrice $P_{\mathcal{B}_0 \to \mathcal{B}_1}$ est donc :
    $$ P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} $$

2.  **Détermination de la matrice de passage $P_{\mathcal{B}_1 \to \mathcal{B}_0}$ de la base $\mathcal{B}_1$ à la base $\mathcal{B}_0$ et vérification :**

    La matrice de passage $P_{\mathcal{B}_1 \to \mathcal{B}_0}$ est la matrice dont les colonnes sont les vecteurs de la base $\mathcal{B}_0$ exprimés dans la base $\mathcal{B}_1$.
    Nous cherchons des scalaires $\alpha, \beta, \gamma, \delta \in \mathbb{R}$ tels que :
    $$ e_1 = \alpha u_1 + \beta u_2 $$
    $$ e_2 = \gamma u_1 + \delta u_2 $$

    Pour $e_1$:
    $$ \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \alpha \begin{pmatrix} 1 \\ 1 \end{pmatrix} + \beta \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} \alpha - \beta \\ \alpha + \beta \end{pmatrix} $$
    Ceci donne le système :
    $$ \begin{cases} \alpha - \beta = 1 & (L_3) \\ \alpha + \beta = 0 & (L_4) \end{cases} $$
    Additionnons $(L_3)$ et $(L_4)$ :
    $$ (\alpha - \beta) + (\alpha + \beta) = 1 + 0 $$
    $$ 2\alpha = 1 $$
    $$ \alpha = \frac{1}{2} $$
    Substituons $\alpha$ dans $(L_4)$ :
    $$ \frac{1}{2} + \beta = 0 $$
    $$ \beta = -\frac{1}{2} $$
    Donc, $e_1 = \frac{1}{2} u_1 - \frac{1}{2} u_2$.

    Pour $e_2$:
    $$ \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \gamma \begin{pmatrix} 1 \\ 1 \end{pmatrix} + \delta \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} \gamma - \delta \\ \gamma + \delta \end{pmatrix} $$
    Ceci donne le système :
    $$ \begin{cases} \gamma - \delta = 0 & (L_5) \\ \gamma + \delta = 1 & (L_6) \end{cases} $$
    Additionnons $(L_5)$ et $(L_6)$ :
    $$ (\gamma - \delta) + (\gamma + \delta) = 0 + 1 $$
    $$ 2\gamma = 1 $$
    $$ \gamma = \frac{1}{2} $$
    Substituons $\gamma$ dans $(L_5)$ :
    $$ \frac{1}{2} - \delta = 0 $$
    $$ \delta = \frac{1}{2} $$
    Donc, $e_2 = \frac{1}{2} u_1 + \frac{1}{2} u_2$.

    La matrice $P_{\mathcal{B}_1 \to \mathcal{B}_0}$ est donc :
    $$ P_{\mathcal{B}_1 \to \mathcal{B}_0} = \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix} $$

    **Vérification :**
    Nous devons vérifier que $P_{\mathcal{B}_1 \to \mathcal{B}_0} = (P_{\mathcal{B}_0 \to \mathcal{B}_1})^{-1}$.
    Calculons l'inverse de $P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$.
    Le déterminant de $P_{\mathcal{B}_0 \to \mathcal{B}_1}$ est $\text{det}(P_{\mathcal{B}_0 \to \mathcal{B}_1}) = (1)(1) - (-1)(1) = 1 - (-1) = 1 + 1 = 2$.
    L'inverse d'une matrice $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ est $M^{-1} = \frac{1}{\text{det}(M)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
    Donc, $(P_{\mathcal{B}_0 \to \mathcal{B}_1})^{-1} = \frac{1}{2} \begin{pmatrix} 1 & -(-1) \\ -1 & 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix}$.
    Nous constatons que $P_{\mathcal{B}_1 \to \mathcal{B}_0} = (P_{\mathcal{B}_0 \to \mathcal{B}_1})^{-1}$, la vérification est réussie.

### Partie 3 : Représentation matricielle d'une application linéaire

1.  **Détermination de la matrice $A = \text{Mat}_{\mathcal{B}_0}(f)$ de l'application linéaire $f$ dans la base $\mathcal{B}_0$ :**

    La matrice $A$ de l'application linéaire $f$ dans la base $\mathcal{B}_0$ est obtenue en appliquant $f$ aux vecteurs de la base $\mathcal{B}_0$ et en exprimant les résultats dans cette même base $\mathcal{B}_0$. Les colonnes de $A$ sont les vecteurs $[f(e_1)]_{\mathcal{B}_0}$ et $[f(e_2)]_{\mathcal{B}_0}$.
    L'application linéaire $f: E \to E$ est définie par $f(x) = \begin{pmatrix} x_1 + 2x_2 \\ -x_1 + x_2 \end{pmatrix}$ pour $x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$.

    Calculons $f(e_1)$:
    $$ f(e_1) = f\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 + 2(0) \\ -1 + 0 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix} $$
    En exprimant $f(e_1)$ dans la base $\mathcal{B}_0$:
    $$ f(e_1) = 1 \cdot e_1 - 1 \cdot e_2 $$
    Donc, $[f(e_1)]_{\mathcal{B}_0} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.

    Calculons $f(e_2)$:
    $$ f(e_2) = f\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 0 + 2(1) \\ -0 + 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} $$
    En exprimant $f(e_2)$ dans la base $\mathcal{B}_0$:
    $$ f(e_2) = 2 \cdot e_1 + 1 \cdot e_2 $$
    Donc, $[f(e_2)]_{\mathcal{B}_0} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.

    La matrice $A = \text{Mat}_{\mathcal{B}_0}(f)$ est donc :
    $$ A = \begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix} $$

2.  **Détermination de la matrice $A' = \text{Mat}_{\mathcal{B}_1}(f)$ en utilisant la relation de changement de base :**

    La relation de changement de base pour les matrices d'applications linéaires est $A' = (P_{\mathcal{B}_0 \to \mathcal{B}_1})^{-1} A P_{\mathcal{B}_0 \to \mathcal{B}_1}$.
    Nous avons déjà calculé :
    $$ P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} $$
    $$ (P_{\mathcal{B}_0 \to \mathcal{B}_1})^{-1} = \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix} $$
    $$ A = \begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix} $$
    Effectuons le produit matriciel $A' = (P_{\mathcal{B}_0 \to \mathcal{B}_1})^{-1} A P_{\mathcal{B}_0 \to \mathcal{B}_1}$ étape par étape.

    Premièrement, calculons le produit $A P_{\mathcal{B}_0 \to \mathcal{B}_1}$:
    $$ A P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} $$
    $$ A P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix} (1)(1) + (2)(1) & (1)(-1) + (2)(1) \\ (-1)(1) + (1)(1) & (-1)(-1) + (1)(1) \end{pmatrix} $$
    $$ A P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix} 1 + 2 & -1 + 2 \\ -1 + 1 & 1 + 1 \end{pmatrix} $$
    $$ A P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix} $$

    Deuxièmement, calculons le produit $(P_{\mathcal{B}_0 \to \mathcal{B}_1})^{-1} (A P_{\mathcal{B}_0 \to \mathcal{B}_1})$ :
    $$ A' = \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix} \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix} $$
    $$ A' = \begin{pmatrix} (1/2)(3) + (1/2)(0) & (1/2)(1) + (1/2)(2) \\ (-1/2)(3) + (1/2)(0) & (-1/2)(1) + (1/2)(2) \end{pmatrix} $$
    $$ A' = \begin{pmatrix} 3/2 + 0 & 1/2 + 1 \\ -3/2 + 0 & -1/2 + 1 \end{pmatrix} $$
    $$ A' = \begin{pmatrix} 3/2 & 3/2 \\ -3/2 & 1/2 \end{pmatrix} $$
    La matrice $A' = \text{Mat}_{\mathcal{B}_1}(f)$ est donc :
    $$ A' = \begin{pmatrix} 3/2 & 3/2 \\ -3/2 & 1/2 \end{pmatrix} $$

3.  **Vérification par calcul direct de la matrice $A' = \text{Mat}_{\mathcal{B}_1}(f)$ :**

    Pour vérifier, nous allons calculer directement la matrice $A'$ en appliquant $f$ aux vecteurs de la base $\mathcal{B}_1$ et en exprimant les résultats dans cette même base $\mathcal{B}_1$. Les colonnes de $A'$ seront $[f(u_1)]_{\mathcal{B}_1}$ et $[f(u_2)]_{\mathcal{B}_1}$.
    Les vecteurs de la base $\mathcal{B}_1$ sont $u_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ et $u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.

    Calculons $f(u_1)$:
    $$ f(u_1) = f\left(\begin{pmatrix} 1 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 1 + 2(1) \\ -1 + 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix} $$
    Exprimons $f(u_1)$ dans la base $\mathcal{B}_1$. Nous cherchons $\alpha', \beta' \in \mathbb{R}$ tels que $f(u_1) = \alpha' u_1 + \beta' u_2$:
    $$ \begin{pmatrix} 3 \\ 0 \end{pmatrix} = \alpha' \begin{pmatrix} 1 \\ 1 \end{pmatrix} + \beta' \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} \alpha' - \beta' \\ \alpha' + \beta' \end{pmatrix} $$
    Ceci donne le système :
    $$ \begin{cases} \alpha' - \beta' = 3 & (L_7) \\ \alpha' + \beta' = 0 & (L_8) \end{cases} $$
    Additionnons $(L_7)$ et $(L_8)$ :
    $$ (\alpha' - \beta') + (\alpha' + \beta') = 3 + 0 $$
    $$ 2\alpha' = 3 $$
    $$ \alpha' = \frac{3}{2} $$
    Substituons $\alpha'$ dans $(L_8)$ :
    $$ \frac{3}{2} + \beta' = 0 $$
    $$ \beta' = -\frac{3}{2} $$
    Donc, $[f(u_1)]_{\mathcal{B}_1} = \begin{pmatrix} 3/2 \\ -3/2 \end{pmatrix}$.

    Calculons $f(u_2)$:
    $$ f(u_2) = f\left(\begin{pmatrix} -1 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} -1 + 2(1) \\ -(-1) + 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} $$
    Exprimons $f(u_2)$ dans la base $\mathcal{B}_1$. Nous cherchons $\gamma', \delta' \in \mathbb{R}$ tels que $f(u_2) = \gamma' u_1 + \delta' u_2$:
    $$ \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \gamma' \begin{pmatrix} 1 \\ 1 \end{pmatrix} + \delta' \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} \gamma' - \delta' \\ \gamma' + \delta' \end{pmatrix} $$
    Ceci donne le système :
    $$ \begin{cases} \gamma' - \delta' = 1 & (L_9) \\ \gamma' + \delta' = 2 & (L_{10}) \end{cases} $$
    Additionnons $(L_9)$ et $(L_{10})$ :
    $$ (\gamma' - \delta') + (\gamma' + \delta') = 1 + 2 $$
    $$ 2\gamma' = 3 $$
    $$ \gamma' = \frac{3}{2} $$
    Substituons $\gamma'$ dans $(L_{10})$ :
    $$ \frac{3}{2} + \delta' = 2 $$
    $$ \delta' = 2 - \frac{3}{2} $$
    $$ \delta' = \frac{4}{2} - \frac{3}{2} $$
    $$ \delta' = \frac{1}{2} $$
    Donc, $[f(u_2)]_{\mathcal{B}_1} = \begin{pmatrix} 3/2 \\ 1/2 \end{pmatrix}$.

    La matrice $A' = \text{Mat}_{\mathcal{B}_1}(f)$ est donc :
    $$ A' = \begin{pmatrix} 3/2 & 3/2 \\ -3/2 & 1/2 \end{pmatrix} $$
    Ce résultat est identique à celui obtenu par la formule de changement de base, ce qui confirme l'exactitude des calculs.
