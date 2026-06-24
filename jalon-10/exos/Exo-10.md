```yaml
---
title: "Exercice 10 : Changements de Base, Matrices de Passage et Matrices par Blocs"
subtitle: "Jalon 10 - Mathématiques pour l'Intelligence Artificielle"
author: "Votre Nom / Université"
date: "2023-10-27"
keywords:
  - Algèbre linéaire
  - Changement de base
  - Matrice de passage
  - Matrice par blocs
  - Endomorphisme
  - Espace vectoriel
  - Base
  - Coordonnées
  - Sous-espaces invariants
  - Diagonalisation par blocs
---

# Exercice 10 : Changements de Base, Matrices de Passage et Matrices par Blocs

Cet exercice est conçu pour approfondir la compréhension des concepts de changements de base, de matrices de passage et de matrices par blocs, des outils fondamentaux en algèbre linéaire avec des applications cruciales en Intelligence Artificielle (par exemple, pour la décomposition de matrices, l'analyse de systèmes dynamiques ou la compression de données). L'exercice est structuré en plusieurs parties de difficulté croissante, culminant avec une question de synthèse exigeante.

---

## Partie 1 : Fondamentaux des Changements de Base dans $\mathbb{R}^n$

**Objectifs :** Revoir les concepts de base, coordonnées, et matrices de passage dans un cadre familier.

Soit $E = \mathbb{R}^3$ un espace vectoriel sur le corps des nombres réels $\mathbb{R}$.

1.  **Définition des bases :**
    *   La base canonique de $E$ est $\mathcal{B}_c = (e_1, e_2, e_3)$, où $e_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$, $e_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$, $e_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$.
    *   Considérons une nouvelle base $\mathcal{B} = (v_1, v_2, v_3)$ de $E$, où les vecteurs sont définis par leurs coordonnées dans $\mathcal{B}_c$: $v_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$, $v_2 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$, $v_3 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$.

2.  **Question 1.1 : Matrice de passage de $\mathcal{B}_c$ à $\mathcal{B}$**
    Déterminer la matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}}$ de la base canonique $\mathcal{B}_c$ à la base $\mathcal{B}$.
    *Rappel :* La matrice de passage de $\mathcal{B}_c$ à $\mathcal{B}$ est la matrice dont les colonnes sont les vecteurs de la base $\mathcal{B}$ exprimés dans la base $\mathcal{B}_c$.

3.  **Question 1.2 : Matrice de passage de $\mathcal{B}$ à $\mathcal{B}_c$**
    Déterminer la matrice de passage $P_{\mathcal{B} \to \mathcal{B}_c}$ de la base $\mathcal{B}$ à la base canonique $\mathcal{B}_c$.
    *Rappel :* La matrice $P_{\mathcal{B} \to \mathcal{B}_c}$ est l'inverse de la matrice $P_{\mathcal{B}_c \to \mathcal{B}}$. Toutes les étapes du calcul de l'inverse doivent être explicitées.

4.  **Question 1.3 : Changement de coordonnées d'un vecteur**
    Soit un vecteur $x \in E$ dont les coordonnées dans la base $\mathcal{B}_c$ sont $[x]_{\mathcal{B}_c} = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$.
    Calculer les coordonnées de $x$ dans la base $\mathcal{B}$, notées $[x]_{\mathcal{B}}$. Toutes les étapes du calcul matriciel doivent être explicitées.

5.  **Question 1.4 : Changement de matrice d'un endomorphisme**
    Soit $f: E \to E$ un endomorphisme de $E$ dont la matrice dans la base $\mathcal{B}_c$ est $A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$.
    Calculer la matrice $A'$ de l'endomorphisme $f$ dans la base $\mathcal{B}$.
    *Rappel :* La relation entre $A$ et $A'$ est $A' = P_{\mathcal{B} \to \mathcal{B}_c} A P_{\mathcal{B}_c \to \mathcal{B}}$. Toutes les étapes des multiplications matricielles doivent être explicitées.

---

## Partie 2 : Changement de Base pour un Endomorphisme dans un Espace de Polynômes

**Objectifs :** Appliquer les concepts à un espace vectoriel abstrait et un endomorphisme plus complexe.

Soit $E = \mathbb{R}_2[X]$ l'espace vectoriel des polynômes de degré inférieur ou égal à 2 à coefficients réels, sur le corps $\mathbb{R}$.

1.  **Définition des bases :**
    *   La base canonique de $E$ est $\mathcal{B}_1 = (1, X, X^2)$.
    *   Considérons une nouvelle base $\mathcal{B}_2 = (1, X-1, (X-1)^2)$.

2.  **Définition de l'endomorphisme :**
    Soit $f: E \to E$ l'application définie pour tout polynôme $P(X) \in E$ par $f(P(X)) = P'(X) + P(X)$, où $P'(X)$ est la dérivée de $P(X)$ par rapport à $X$.

3.  **Question 2.1 : Vérification de l'endomorphisme**
    Vérifier que $f$ est un endomorphisme de $E$. Pour cela, il faut montrer que $f$ est linéaire et que l'image de tout polynôme de $E$ est un polynôme de $E$. Toutes les étapes de la démonstration doivent être détaillées.

4.  **Question 2.2 : Matrice de $f$ dans $\mathcal{B}_1$**
    Déterminer la matrice $A_1$ de l'endomorphisme $f$ dans la base $\mathcal{B}_1$. Pour chaque vecteur de base $P_i \in \mathcal{B}_1$, calculer $f(P_i)$ et exprimer le résultat comme combinaison linéaire des vecteurs de $\mathcal{B}_1$.

5.  **Question 2.3 : Matrice de passage de $\mathcal{B}_1$ à $\mathcal{B}_2$**
    Déterminer la matrice de passage $P_{\mathcal{B}_1 \to \mathcal{B}_2}$ de la base $\mathcal{B}_1$ à la base $\mathcal{B}_2$. Pour chaque vecteur de base $Q_j \in \mathcal{B}_2$, exprimer $Q_j$ comme combinaison linéaire des vecteurs de $\mathcal{B}_1$.

6.  **Question 2.4 : Matrice de passage de $\mathcal{B}_2$ à $\mathcal{B}_1$**
    Déterminer la matrice de passage $P_{\mathcal{B}_2 \to \mathcal{B}_1}$ de la base $\mathcal{B}_2$ à la base $\mathcal{B}_1$. Toutes les étapes du calcul de l'inverse doivent être explicitées.

7.  **Question 2.5 : Matrice de $f$ dans $\mathcal{B}_2$ par changement de base**
    Déterminer la matrice $A_2$ de l'endomorphisme $f$ dans la base $\mathcal{B}_2$ en utilisant la formule de changement de base $A_2 = P_{\mathcal{B}_2 \to \mathcal{B}_1} A_1 P_{\mathcal{B}_1 \to \mathcal{B}_2}$. Toutes les étapes des multiplications matricielles doivent être explicitées.

8.  **Question 2.6 : Vérification directe de $A_2$**
    Vérifier le résultat de $A_2$ obtenu à la question 2.5 en calculant directement les images des vecteurs de la base $\mathcal{B}_2$ par $f$ et en exprimant leurs coordonnées dans la base $\mathcal{B}_2$. Pour chaque vecteur de base $Q_j \in \mathcal{B}_2$, calculer $f(Q_j)$ et exprimer le résultat comme combinaison linéaire des vecteurs de $\mathcal{B}_2$.

---

## Partie 3 : Matrices par Blocs et Sous-Espaces Invariants

**Objectifs :** Introduire les matrices par blocs et leur lien avec la décomposition d'un espace en sous-espaces invariants.

Soit $E = \mathbb{R}^4$ un espace vectoriel sur le corps $\mathbb{R}$.
Considérons deux sous-espaces vectoriels de $E$:
*   $E_1 = \text{Vect}(e_1, e_2)$, où $e_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}$ et $e_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$.
*   $E_2 = \text{Vect}(e_3, e_4)$, où $e_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}$ et $e_4 = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}$.
La base canonique de $\mathbb{R}^4$ est $\mathcal{B}_c = (e_1, e_2, e_3, e_4)$.
On peut vérifier que $E = E_1 \oplus E_2$ (la démonstration n'est pas demandée ici).

Soit $f: E \to E$ un endomorphisme dont la matrice dans la base $\mathcal{B}_c$ est donnée par:
$A = \begin{pmatrix}
1 & 2 & 0 & 0 \\
3 & 4 & 0 & 0 \\
0 & 0 & 5 & 6 \\
0 & 0 & 7 & 8
\end{pmatrix}$

1.  **Question 3.1 : Invariance des sous-espaces**
    Montrer que $E_1$ et $E_2$ sont des sous-espaces vectoriels invariants par l'endomorphisme $f$.
    *Rappel :* Un sous-espace $F$ est invariant par $f$ si pour tout $x \in F$, $f(x) \in F$. Pour $E_1$, il suffit de montrer que $f(e_1) \in E_1$ et $f(e_2) \in E_1$. Pour $E_2$, il suffit de montrer que $f(e_3) \in E_2$ et $f(e_4) \in E_2$. Toutes les étapes des calculs vectoriels doivent être explicitées.

2.  **Question 3.2 : Forme par blocs de la matrice $A$**
    Écrire la matrice $A$ sous forme de blocs $A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}$ en identifiant chaque bloc comme une matrice de taille appropriée.

3.  **Question 3.3 : Lien entre forme par blocs et invariance**
    Expliquer pourquoi la forme par blocs de $A$ (avec des blocs nuls $A_{12}$ et $A_{21}$) est directement liée à l'invariance des sous-espaces $E_1$ et $E_2$.

4.  **Question 3.4 : Restriction de $f$ à $E_1$**
    Soit $f_1: E_1 \to E_1$ la restriction de $f$ à $E_1$. Déterminer la matrice de $f_1$ dans la base $\mathcal{B}_{E_1} = (e_1, e_2)$ de $E_1$.

5.  **Question 3.5 : Restriction de $f$ à $E_2$**
    Soit $f_2: E_2 \to E_2$ la restriction de $f$ à $E_2$. Déterminer la matrice de $f_2$ dans la base $\mathcal{B}_{E_2} = (e_3, e_4)$ de $E_2$.

---

## Partie 4 : Changement de Base et Diagonalisation par Blocs (Niveau 5/5)

**Objectifs :** Combiner changement de base et matrices par blocs pour analyser une transformation complexe, et trouver une base "adaptée" où la matrice prend une forme bloc-diagonale, révélant ainsi la structure de l'endomorphisme.

Soit $E = \mathbb{R}^4$ un espace vectoriel sur le corps $\mathbb{R}$.

1.  **Contexte initial :**
    Soit $f: E \to E$ un endomorphisme dont la matrice dans la base canonique $\mathcal{B}_c = (e_1, e_2, e_3, e_4)$ est:
    $M = \begin{pmatrix}
    1 & 1 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 2 & 1 \\
    0 & 0 & 0 & 2
    \end{pmatrix}$
    On observe que $M$ est déjà sous forme bloc-diagonale par rapport à la décomposition $E = F_1 \oplus F_2$, où $F_1 = \text{Vect}(e_1, e_2)$ et $F_2 = \text{Vect}(e_3, e_4)$.

2.  **Nouvelle base $\mathcal{B}'$ :**
    Considérons une nouvelle base $\mathcal{B}' = (v_1, v_2, v_3, v_4)$ de $E$ où les vecteurs sont définis par leurs coordonnées dans $\mathcal{B}_c$:
    $v_1 = e_1 + e_3 = \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix}$
    $v_2 = e_2 + e_4 = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 1 \end{pmatrix}$
    $v_3 = e_1 - e_3 = \begin{pmatrix} 1 \\ 0 \\ -1 \\ 0 \end{pmatrix}$
    $v_4 = e_2 - e_4 = \begin{pmatrix} 0 \\ 1 \\ 0 \\ -1 \end{pmatrix}$

3.  **Question 4.1 : Vérification de la base $\mathcal{B}'$**
    Vérifier que $\mathcal{B}'$ est bien une base de $E$. Pour cela, il faut montrer que les vecteurs $v_1, v_2, v_3, v_4$ sont linéairement indépendants. Toutes les étapes du calcul du déterminant de la matrice formée par ces vecteurs (ou de la résolution d'un système linéaire) doivent être explicitées.

4.  **Question 4.2 : Matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$**
    Déterminer la matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$ de la base $\mathcal{B}_c$ à la base $\mathcal{B}'$.

5.  **Question 4.3 : Matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$**
    Déterminer la matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ de la base $\mathcal{B}'$ à la base $\mathcal{B}_c$. Toutes les étapes du calcul de l'inverse doivent être explicitées.

6.  **Question 4.4 : Matrice de $f$ dans $\mathcal{B}'$**
    Calculer la matrice $M'$ de l'endomorphisme $f$ dans la base $\mathcal{B}'$. Utiliser la formule $M' = P_{\mathcal{B}' \to \mathcal{B}_c} M P_{\mathcal{B}_c \to \mathcal{B}'}$. Toutes les étapes des multiplications matricielles doivent être explicitées.

7.  **Question 4.5 : Analyse de la structure de $M'$**
    Analyser la structure de la matrice $M'$. Est-elle bloc-diagonale ? Si non, pourquoi ? Expliquer ce que cette forme révèle sur l'action de $f$ par rapport aux sous-espaces $V_1 = \text{Vect}(v_1, v_2)$ et $V_2 = \text{Vect}(v_3, v_4)$.

8.  **Question 4.6 : Question de synthèse - Diagonalisation par blocs d'un endomorphisme (Très difficile)**
    Soit $E = \mathbb{R}^4$ un espace vectoriel sur le corps $\mathbb{R}$.
    Soit $g: E \to E$ un endomorphisme dont la matrice dans la base canonique $\mathcal{B}_c = (e_1, e_2, e_3, e_4)$ est:
    $A = \begin{pmatrix}
    1 & 0 & 1 & 0 \\
    0 & 1 & 0 & 1 \\
    1 & 0 & 1 & 0 \\
    0 & 1 & 0 & 1
    \end{pmatrix}$
    On cherche à trouver une base $\mathcal{B}''$ de $E$ telle que la matrice de $g$ dans $\mathcal{B}''$ soit bloc-diagonale. Pour cela, on considère les sous-espaces vectoriels suivants:
    *   $W_1 = \text{Vect}(u_1, u_2)$, où $u_1 = e_1+e_3$ et $u_2 = e_2+e_4$.
    *   $W_2 = \text{Vect}(u_3, u_4)$, où $u_3 = e_1-e_3$ et $u_4 = e_2-e_4$.

    a.  **Invariance des sous-espaces :** Montrer que $W_1$ et $W_2$ sont des sous-espaces vectoriels invariants par l'endomorphisme $g$.
        *   Pour $W_1$: Calculer $g(u_1)$ et $g(u_2)$ en utilisant la matrice $A$ et les coordonnées des vecteurs $e_i$. Montrer que $g(u_1)$ et $g(u_2)$ peuvent être exprimés comme des combinaisons linéaires de $u_1$ et $u_2$. Toutes les étapes des calculs vectoriels doivent être explicitées.
        *   Pour $W_2$: Calculer $g(u_3)$ et $g(u_4)$ en utilisant la matrice $A$. Montrer que $g(u_3)$ et $g(u_4)$ peuvent être exprimés comme des combinaisons linéaires de $u_3$ et $u_4$. Toutes les étapes des calculs vectoriels doivent être explicitées.

    b.  **Construction de la base $\mathcal{B}''$ :** Déterminer une base $\mathcal{B}''$ de $E$ adaptée à la décomposition $E = W_1 \oplus W_2$. Cette base sera formée par la concaténation des bases de $W_1$ et $W_2$. Vérifier que $\mathcal{B}''$ est bien une base de $E$ (par exemple, en montrant l'indépendance linéaire des vecteurs).

    c.  **Calcul de la matrice $A''$ :** Calculer la matrice $A''$ de l'endomorphisme $g$ dans cette base $\mathcal{B}''$. Vous pouvez soit utiliser la formule de changement de base $A'' = P_{\mathcal{B}'' \to \mathcal{B}_c} A P_{\mathcal{B}_c \to \mathcal{B}''}$, soit calculer directement les images des vecteurs de $\mathcal{B}''$ par $g$ et exprimer leurs coordonnées dans $\mathcal{B}''$. Toutes les étapes des calculs doivent être explicitées.

    d.  **Interprétation :** Expliquer l'intérêt de cette forme bloc-diagonale pour l'étude de l'endomorphisme $g$. Quels sont les sous-espaces propres (ou généralisés) de $g$ que cette décomposition révèle ? Comment cette forme simplifie-t-elle la compréhension de l'action de $g$ sur l'espace $E$ ?

---
