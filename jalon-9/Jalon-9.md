---
uuid: "jalon-9"
title: "Calcul matriciel, opérations, inversibilité et représentations des applications linéaires"
year: 1
trimester: 1
tags:
  - math/algebre-lineaire
  - ia/poids-reseaux
prev: "[[Jalon-8.md]]"
next: "[[Jalon 10 (Changements de base).md]]"
---

# Jalon 9 : Calcul matriciel, opérations, inversibilité et représentations des applications linéaires

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*
- **La Métaphore :** Imaginez une série de machines dans une usine. Chaque machine prend des matières premières (des nombres, des "quantités") et les transforme en produits finis selon une recette fixe. Une **matrice** est cette "recette" ou ce "plan de transformation". C'est un tableau de nombres qui décrit comment les entrées sont mélangées et transformées pour produire les sorties.
  - Si vous avez une machine qui transforme des pigments en couleurs primaires, et une autre qui transforme ces couleurs primaires en teintes spécifiques de peinture, la **multiplication de matrices** est l'équivalent de brancher ces deux machines l'une après l'autre pour obtenir une seule "super-machine" qui va directement des pigments aux teintes de peinture.
  - L'**inversibilité** d'une matrice, c'est comme savoir si votre machine de transformation est réversible. Pouvez-vous, à partir du produit fini, retrouver exactement les matières premières d'origine, sans aucune perte d'information ? Si oui, la machine est inversible. Si elle écrase, mélange irréversiblement ou perd des informations, elle n'est pas inversible.
- **Le "Pourquoi on a inventé ça" :** Avant les matrices, décrire une transformation linéaire (comme une rotation, une mise à l'échelle, une projection) sur des vecteurs nécessitait d'écrire des systèmes d'équations complexes pour chaque composante. Pour des espaces de grande dimension, cela devenait ingérable. Les matrices ont été inventées pour compacter toute cette information en un seul objet rectangulaire. Elles permettent de représenter des transformations complexes de manière compacte et de calculer l'effet de transformations successives (composition) par une simple opération algébrique : le produit matriciel. C'est une révolution pour la concision et l'efficacité calculatoire.
- **Visualisation :** Une matrice $2 \times 2$ peut être visualisée comme une transformation géométrique du plan. Elle prend le carré unité (défini par les vecteurs $(1,0)$ et $(0,1)$) et le déforme en un parallélogramme. Les colonnes de la matrice sont les vecteurs où atterrissent $(1,0)$ et $(0,1)$ après la transformation.
  - Si la matrice est inversible, le parallélogramme a une aire non nulle : l'espace est étiré ou compressé, mais aucune dimension n'est perdue. Vous pouvez "défaire" la transformation.
  - Si la matrice n'est pas inversible, le parallélogramme est "écrasé" en une ligne ou même un point (son aire est nulle). Cela signifie que la transformation a réduit la dimension de l'espace, rendant impossible de retrouver l'état initial : l'information a été perdue.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soient $\mathbb{K}$ un corps commutatif (typiquement $\mathbb{R}$ ou $\mathbb{C}$), et $n, p, q \in \mathbb{N}^*$ des entiers naturels non nuls.

1.  **Matrice ($M \in \mathcal{M}_{n,p}(\mathbb{K})$) :** Un tableau rectangulaire de $n$ lignes et $p$ colonnes dont les éléments sont des scalaires du corps $\mathbb{K}$. Une matrice $A$ est notée $A = (a_{i,j})$ où $a_{i,j}$ est le coefficient situé à l'intersection de la $i$-ème ligne ($1 \le i \le n$) et de la $j$-ème colonne ($1 \le j \le p$). L'ensemble de toutes ces matrices est noté $\mathcal{M}_{n,p}(\mathbb{K})$. Si $n=p$, on parle de matrice carrée et on note $\mathcal{M}_n(\mathbb{K})$.

2.  **Matrice Nulle ($0_{n,p}$) :** La matrice dont tous les coefficients sont nuls. $0_{n,p} = (0)_{i,j}$.

3.  **Matrice Identité ($I_n$) :** La matrice carrée d'ordre $n$ dont les coefficients diagonaux sont égaux à 1 et tous les autres sont nuls. $I_n = (\delta_{i,j})$ où $\delta_{i,j}$ est le symbole de Kronecker ($\delta_{i,j}=1$ si $i=j$, et $\delta_{i,j}=0$ si $i \neq j$).

4.  **Somme Matricielle :** Soient $A = (a_{i,j}) \in \mathcal{M}_{n,p}(\mathbb{K})$ et $B = (b_{i,j}) \in \mathcal{M}_{n,p}(\mathbb{K})$. Leur somme $C = A+B \in \mathcal{M}_{n,p}(\mathbb{K})$ est définie par :
    $$c_{i,j} = a_{i,j} + b_{i,j}$$

5.  **Multiplication par un Scalaire :** Soit $A = (a_{i,j}) \in \mathcal{M}_{n,p}(\mathbb{K})$ et $\lambda \in \mathbb{K}$. Le produit $\lambda A \in \mathcal{M}_{n,p}(\mathbb{K})$ est défini par :
    $$(\lambda A)_{i,j} = \lambda a_{i,j}$$

6.  **Produit Matriciel :** Soit $A = (a_{i,k}) \in \mathcal{M}_{n,p}(\mathbb{K})$ et $B = (b_{k,j}) \in \mathcal{M}_{p,q}(\mathbb{K})$. Le produit $C = AB \in \mathcal{M}_{n,q}(\mathbb{K})$ est défini par :
    $$c_{i,j} = \sum_{k=1}^p a_{i,k} b_{k,j}$$
    Le nombre de colonnes de $A$ doit être égal au nombre de lignes de $B$.

7.  **Matrice Inversible :** Une matrice carrée $A \in \mathcal{M}_n(\mathbb{K})$ est dite inversible (ou régulière) s'il existe une matrice $B \in \mathcal{M}_n(\mathbb{K})$ telle que $AB = BA = I_n$. La matrice $B$, si elle existe, est unique et est appelée l'inverse de $A$, notée $A^{-1}$.

8.  **Représentation d'une application linéaire :** Soient $E$ et $F$ deux $\mathbb{K}$-espaces vectoriels de dimensions finies $p$ et $n$ respectivement. Soient $\mathcal{B}_E = (e_1, \dots, e_p)$ une base de $E$ et $\mathcal{B}_F = (f_1, \dots, f_n)$ une base de $F$. Pour toute application linéaire $f \in \mathcal{L}(E, F)$, la matrice de $f$ relativement aux bases $\mathcal{B}_E$ et $\mathcal{B}_F$, notée $\text{Mat}_{\mathcal{B}_E, \mathcal{B}_F}(f)$, est la matrice $A = (a_{i,j}) \in \mathcal{M}_{n,p}(\mathbb{K})$ dont la $j$-ème colonne est constituée des coordonnées du vecteur $f(e_j)$ dans la base $\mathcal{B}_F$. Autrement dit, pour chaque $j \in \{1, \dots, p\}$ :
    $$f(e_j) = \sum_{i=1}^n a_{i,j} f_i$$

9.  **Noyau d'une Matrice ($\ker A$) :** Pour une matrice $A \in \mathcal{M}_{n,p}(\mathbb{K})$, le noyau de $A$ est l'ensemble des vecteurs colonnes $X \in \mathcal{M}_{p,1}(\mathbb{K})$ tels que $AX = 0_{n,1}$. C'est un sous-espace vectoriel de $\mathbb{K}^p$.
    $$\ker A = \{X \in \mathbb{K}^p \mid AX = 0\}$$

10. **Image d'une Matrice ($\text{Im } A$) :** Pour une matrice $A \in \mathcal{M}_{n,p}(\mathbb{K})$, l'image de $A$ est l'ensemble des vecteurs colonnes $Y \in \mathcal{M}_{n,1}(\mathbb{K})$ qui peuvent être écrits comme $AX$ pour un certain $X \in \mathcal{M}_{p,1}(\mathbb{K})$. C'est un sous-espace vectoriel de $\mathbb{K}^n$, engendré par les colonnes de $A$.
    $$\text{Im } A = \{AX \mid X \in \mathbb{K}^p\}$$

11. **Rang d'une Matrice ($\text{rg } A$) :** Le rang d'une matrice $A$ est la dimension de son image, c'est-à-dire le nombre maximal de colonnes (ou de lignes) linéairement indépendantes.
    $$\text{rg } A = \dim(\text{Im } A)$$

### B. Théorèmes, Propositions & Lemmes

> **Proposition (Structure d'espace vectoriel de $\mathcal{M}_{n,p}(\mathbb{K})$) :**
> L'ensemble $\mathcal{M}_{n,p}(\mathbb{K})$ muni de l'addition matricielle et de la multiplication par un scalaire est un $\mathbb{K}$-espace vectoriel de dimension $np$.

> **Théorème (Propriétés du Produit Matriciel) :**
> Soient $A \in \mathcal{M}_{n,p}(\mathbb{K})$, $B \in \mathcal{M}_{p,q}(\mathbb{K})$, $C \in \mathcal{M}_{q,r}(\mathbb{K})$ et $D \in \mathcal{M}_{p,q}(\mathbb{K})$, $\lambda \in \mathbb{K}$.
> 1.  **Associativité :** $(AB)C = A(BC)$.
> 2.  **Distributivité :** $A(B+D) = AB + AD$ et $(A+B)C = AC + BC$ (si les dimensions sont compatibles).
> 3.  **Homogénéité :** $\lambda(AB) = (\lambda A)B = A(\lambda B)$.
> 4.  **Élément Neutre :** $I_n A = A I_p = A$.
> 5.  **Non-commutativité :** En général, $AB \neq BA$.

> **Théorème de l'Isomorphisme entre applications linéaires et matrices :**
> Soient $E$ et $F$ des $\mathbb{K}$-espaces vectoriels de dimensions $p$ et $n$ respectivement, munis de bases $\mathcal{B}_E$ et $\mathcal{B}_F$. L'application $\Phi : \mathcal{L}(E, F) \to \mathcal{M}_{n,p}(\mathbb{K})$ définie par $\Phi(f) = \text{Mat}_{\mathcal{B}_E, \mathcal{B}_F}(f)$ est un isomorphisme d'espaces vectoriels.

> **Théorème Pivot (Matrice d'une composée et produit matriciel) :**
> Soient $E, F, G$ des $\mathbb{K}$-espaces vectoriels de dimensions finies $q, p, n$ respectivement. Soient $\mathcal{B}_E, \mathcal{B}_F, \mathcal{B}_G$ des bases respectives de $E, F, G$.
> Soient $f \in \mathcal{L}(E, F)$ et $g \in \mathcal{L}(F, G)$. Alors la matrice de l'application linéaire composée $g \circ f \in \mathcal{L}(E, G)$ est le produit des matrices de $g$ et $f$ :
> $$\text{Mat}_{\mathcal{B}_E, \mathcal{B}_G}(g \circ f) = \text{Mat}_{\mathcal{B}_F, \mathcal{B}_G}(g) \times \text{Mat}_{\mathcal{B}_E, \mathcal{B}_F}(f)$$

> **Théorème du Rang (ou Théorème de la dimension) :**
> Soit $f \in \mathcal{L}(E, F)$ une application linéaire où $E$ est un espace vectoriel de dimension finie. Alors :
> $$\dim E = \dim(\ker f) + \dim(\text{Im } f)$$
> Pour une matrice $A \in \mathcal{M}_{n,p}(\mathbb{K})$, cela se traduit par :
> $$p = \dim(\ker A) + \text{rg } A$$

> **Théorème (Caractérisations de l'inversibilité) :**
> Soit $A \in \mathcal{M}_n(\mathbb{K})$ une matrice carrée d'ordre $n$. Les propriétés suivantes sont équivalentes :
> 1.  $A$ est inversible.
> 2.  L'application linéaire $f_A: \mathbb{K}^n \to \mathbb{K}^n$ associée à $A$ (dans la base canonique) est un isomorphisme (bijective).
> 3.  $\det(A) \neq 0$.
> 4.  $\text{rg}(A) = n$.
> 5.  $\ker A = \{0_{\mathbb{K}^n}\}$.
> 6.  Les colonnes de $A$ forment une base de $\mathbb{K}^n$.
> 7.  Les lignes de $A$ forment une base de $\mathbb{K}^n$.
> 8.  Il existe $B \in \mathcal{M}_n(\mathbb{K})$ telle que $AB = I_n$.
> 9.  Il existe $C \in \mathcal{M}_n(\mathbb{K})$ telle que $CA = I_n$.

> **Proposition (Propriétés de l'inverse) :**
> Soient $A, B \in \mathcal{M}_n(\mathbb{K})$ deux matrices inversibles. Alors :
> 1.  L'inverse $A^{-1}$ est unique.
> 2.  $A^{-1}$ est inversible et $(A^{-1})^{-1} = A$.
> 3.  Le produit $AB$ est inversible et $(AB)^{-1} = B^{-1}A^{-1}$.
> 4.  Pour tout $\lambda \in \mathbb{K}^*$, $\lambda A$ est inversible et $(\lambda A)^{-1} = \frac{1}{\lambda} A^{-1}$.
> 5.  La transposée $A^T$ est inversible et $(A^T)^{-1} = (A^{-1})^T$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Matrice d'une composée et produit matriciel
Soient $f : E \to F$ et $g : F \to G$ deux applications linéaires.
Soient $\mathcal{B}_E = (e_j)_{1 \le j \le q}$ une base de $E$ (de dimension $q$).
Soient $\mathcal{B}_F = (f_k)_{1 \le k \le p}$ une base de $F$ (de dimension $p$).
Soient $\mathcal{B}_G = (g_i)_{1 \le i \le n}$ une base de $G$ (de dimension $n$).

Montrons que $\text{Mat}_{\mathcal{B}_E, \mathcal{B}_G}(g \circ f) = \text{Mat}_{\mathcal{B}_F, \mathcal{B}_G}(g) \times \text{Mat}_{\mathcal{B}_E, \mathcal{B}_F}(f)$.

1.  **Initialisation / Cadre :**
    Nous allons calculer les coefficients de la matrice de l'application composée $g \circ f$ et montrer qu'ils correspondent à la définition du produit matriciel des matrices de $g$ et $f$.
    Soit $A = \text{Mat}_{\mathcal{B}_F, \mathcal{B}_G}(g) = (a_{i,k}) \in \mathcal{M}_{n,p}(\mathbb{K})$. Par définition, pour tout $k \in \{1, \dots, p\}$, le vecteur $g(f_k)$ s'écrit dans la base $\mathcal{B}_G$ comme :
    $$g(f_k) = \sum_{i=1}^n a_{i,k} g_i \quad (*)$$
    Soit $B = \text{Mat}_{\mathcal{B}_E, \mathcal{B}_F}(f) = (b_{k,j}) \in \mathcal{M}_{p,q}(\mathbb{K})$. Par définition, pour tout $j \in \{1, \dots, q\}$, le vecteur $f(e_j)$ s'écrit dans la base $\mathcal{B}_F$ comme :
    $$f(e_j) = \sum_{k=1}^p b_{k,j} f_k \quad (**)$$
    Nous cherchons à déterminer la matrice $C = \text{Mat}_{\mathcal{B}_E, \mathcal{B}_G}(g \circ f) = (c_{i,j}) \in \mathcal{M}_{n,q}(\mathbb{K})$. Par définition, pour tout $j \in \{1, \dots, q\}$, le vecteur $(g \circ f)(e_j)$ s'écrit dans la base $\mathcal{B}_G$ comme :
    $$(g \circ f)(e_j) = \sum_{i=1}^n c_{i,j} g_i$$
    Notre objectif est de montrer que $c_{i,j} = \sum_{k=1}^p a_{i,k} b_{k,j}$.

2.  **Étape 1 : Calcul de $(g \circ f)(e_j)$ en utilisant la définition de $f$**
    Nous commençons par l'expression de $(g \circ f)(e_j)$ :
    $$(g \circ f)(e_j) = g(f(e_j))$$
    En utilisant l'expression de $f(e_j)$ donnée par $(**)$ :
    $$(g \circ f)(e_j) = g\left(\sum_{k=1}^p b_{k,j} f_k\right)$$

3.  **Étape 2 (Transition micro-calculatoire) : Utilisation de la linéarité de $g$**
    Puisque $g$ est une application linéaire, elle respecte la somme et la multiplication par un scalaire. Nous pouvons donc "sortir" les scalaires $b_{k,j}$ de l'application $g$ et décomposer la somme :
    $$(g \circ f)(e_j) = \sum_{k=1}^p b_{k,j} g(f_k)$$

4.  **Étape 3 (Transition micro-calculatoire) : Utilisation de la définition de $g$**
    Maintenant, nous utilisons l'expression de $g(f_k)$ donnée par $(*)$ :
    $$(g \circ f)(e_j) = \sum_{k=1}^p b_{k,j} \left(\sum_{i=1}^n a_{i,k} g_i\right)$$

5.  **Étape 4 (Transition micro-calculatoire) : Réarrangement des sommes**
    Nous avons une somme de sommes. Nous pouvons intervertir l'ordre des sommations :
    $$(g \circ f)(e_j) = \sum_{k=1}^p \sum_{i=1}^n b_{k,j} a_{i,k} g_i$$
    Pour regrouper les termes selon les vecteurs de base $g_i$, nous réorganisons la somme :
    $$(g \circ f)(e_j) = \sum_{i=1}^n \left(\sum_{k=1}^p a_{i,k} b_{k,j}\right) g_i$$

6.  **Conclusion :**
    Par identification avec la définition de la matrice de $(g \circ f)$, c'est-à-dire $(g \circ f)(e_j) = \sum_{i=1}^n c_{i,j} g_i$, nous obtenons que le coefficient $c_{i,j}$ de la matrice $\text{Mat}_{\mathcal{B}_E, \mathcal{B}_G}(g \circ f)$ est :
    $$c_{i,j} = \sum_{k=1}^p a_{i,k} b_{k,j}$$
    Cette expression est précisément la définition du coefficient $(i,j)$ du produit matriciel $AB$.
    Par conséquent, nous avons démontré que $\text{Mat}_{\mathcal{B}_E, \mathcal{B}_G}(g \circ f) = \text{Mat}_{\mathcal{B}_F, \mathcal{B}_G}(g) \times \text{Mat}_{\mathcal{B}_E, \mathcal{B}_F}(f)$.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe (Inversion de matrice 2x2)
**Énoncé :** Soit la matrice $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \in \mathcal{M}_2(\mathbb{R})$.
1.  Calculer le déterminant de $A$.
2.  Déterminer si $A$ est inversible.
3.  Si oui, calculer $A^{-1}$ en utilisant la méthode du pivot de Gauss (ou méthode de l'élimination de Gauss-Jordan).
**Correction Détaillée :**
*   *Analyse de l'énoncé :* L'exercice demande de vérifier l'inversibilité d'une matrice $2 \times 2$ via son déterminant, puis de calculer son inverse en utilisant une méthode systématique.
*   *Résolution pas-à-pas :*
    1.  **Calcul du déterminant de $A$ :**
        Pour une matrice $2 \times 2$, $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, le déterminant est $\det A = ad - bc$.
        Pour $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, nous avons :
        $$\det A = (1 \times 4) - (2 \times 3)$$
        $$\det A = 4 - 6$$
        $$\det A = -2$$
    2.  **Détermination de l'inversibilité de $A$ :**
        Une matrice carrée est inversible si et seulement si son déterminant est non nul.
        Puisque $\det A = -2 \neq 0$, la matrice $A$ est inversible.
    3.  **Calcul de $A^{-1}$ par la méthode du pivot de Gauss :**
        Nous formons la matrice augmentée $(A | I_2)$ et nous appliquons des opérations élémentaires sur les lignes pour transformer $A$ en $I_2$. La matrice $I_2$ sera alors transformée en $A^{-1}$.
        La matrice augmentée est :
        $$\left( \begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 4 & 0 & 1 \end{array} \right)$$
        *   **Étape 1 : Éliminer le coefficient sous le pivot de la première colonne.**
            Nous effectuons l'opération $L_2 \leftarrow L_2 - 3L_1$ :
            $$L_2 \text{ (nouvelle)} = (3 - 3 \times 1, \quad 4 - 3 \times 2, \quad 0 - 3 \times 1, \quad 1 - 3 \times 0)$$
            $$L_2 \text{ (nouvelle)} = (0, \quad -2, \quad -3, \quad 1)$$
            La matrice augmentée devient :
            $$\left( \begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & -2 & -3 & 1 \end{array} \right)$$
        *   **Étape 2 : Normaliser le pivot de la deuxième colonne.**
            Nous voulons que le deuxième pivot soit 1. Nous effectuons l'opération $L_2 \leftarrow -\frac{1}{2} L_2$ :
            $$L_2 \text{ (nouvelle)} = (-\frac{1}{2} \times 0, \quad -\frac{1}{2} \times (-2), \quad -\frac{1}{2} \times (-3), \quad -\frac{1}{2} \times 1)$$
            $$L_2 \text{ (nouvelle)} = (0, \quad 1, \quad \frac{3}{2}, \quad -\frac{1}{2})$$
            La matrice augmentée devient :
            $$\left( \begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & \frac{3}{2} & -\frac{1}{2} \end{array} \right)$$
        *   **Étape 3 : Éliminer le coefficient au-dessus du pivot de la deuxième colonne.**
            Nous effectuons l'opération $L_1 \leftarrow L_1 - 2L_2$ :
            $$L_1 \text{ (nouvelle)} = (1 - 2 \times 0, \quad 2 - 2 \times 1, \quad 1 - 2 \times \frac{3}{2}, \quad 0 - 2 \times (-\frac{1}{2}))$$
            $$L_1 \text{ (nouvelle)} = (1, \quad 0, \quad 1 - 3, \quad 0 + 1)$$
            $$L_1 \text{ (nouvelle)} = (1, \quad 0, \quad -2, \quad 1)$$
            La matrice augmentée devient :
            $$\left( \begin{array}{cc|cc} 1 & 0 & -2 & 1 \\ 0 & 1 & \frac{3}{2} & -\frac{1}{2} \end{array} \right)$$
        La partie gauche est maintenant la matrice identité $I_2$. La partie droite est l'inverse de $A$.
**Conclusion :** $A^{-1} = \begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix}$.
Pour vérifier, on peut calculer $A A^{-1}$:
$A A^{-1} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix} = \begin{pmatrix} 1(-2) + 2(\frac{3}{2}) & 1(1) + 2(-\frac{1}{2}) \\ 3(-2) + 4(\frac{3}{2}) & 3(1) + 4(-\frac{1}{2}) \end{pmatrix} = \begin{pmatrix} -2 + 3 & 1 - 1 \\ -6 + 6 & 3 - 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2$. La vérification est concluante.

### Exercice 2 : Niveau Avancé (Noyau et Rang matriciel)
**Énoncé :** Soit la matrice $M = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{pmatrix} \in \mathcal{M}_3(\mathbb{R})$.
1.  Déterminer le rang de $M$.
2.  Déterminer une base du noyau de $M$.
3.  Vérifier le théorème du rang pour cette matrice.
**Correction Détaillée :**
*   *Analyse de l'énoncé :* Cet exercice demande de trouver le rang et le noyau d'une matrice $3 \times 3$. Le rang est le nombre de lignes (ou colonnes) linéairement indépendantes, et le noyau est l'ensemble des vecteurs qui sont transformés en vecteur nul par la matrice. La méthode la plus efficace est l'échelonnement de la matrice.
*   *Résolution pas-à-pas :*
    1.  **Détermination du rang de $M$ par échelonnement :**
        Nous allons appliquer des opérations élémentaires sur les lignes de $M$ pour la transformer en une matrice échelonnée. Le rang sera alors le nombre de lignes non nulles (ou de pivots).
        $$M = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{pmatrix}$$
        *   **Étape 1 : Annuler les coefficients sous le premier pivot (1ère colonne, 1ère ligne).**
            Opérations : $L_2 \leftarrow L_2 - L_1$ et $L_3 \leftarrow L_3 - 2L_1$.
            $$L_2 \text{ (nouvelle)} = (1-1, \quad 2-1, \quad 3-1) = (0, \quad 1, \quad 2)$$
            $$L_3 \text{ (nouvelle)} = (2-2\times 1, \quad 3-2\times 1, \quad 4-2\times 1) = (0, \quad 1, \quad 2)$$
            La matrice devient :
            $$\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{pmatrix}$$
        *   **Étape 2 : Annuler les coefficients sous le deuxième pivot (2ème colonne, 2ème ligne).**
            Opération : $L_3 \leftarrow L_3 - L_2$.
            $$L_3 \text{ (nouvelle)} = (0-0, \quad 1-1, \quad 2-2) = (0, \quad 0, \quad 0)$$
            La matrice échelonnée est :
            $$M' = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{pmatrix}$$
        Le nombre de lignes non nulles (ou de pivots) dans la matrice échelonnée $M'$ est 2 (les pivots sont 1 et 1).
        Donc, le rang de $M$ est $\text{rg } M = 2$.

    2.  **Détermination d'une base du noyau de $M$ :**
        Le noyau de $M$, noté $\ker M$, est l'ensemble des vecteurs $X = \begin{pmatrix} x \\ y \\ z \end{pmatrix} \in \mathbb{R}^3$ tels que $MX = 0$.
        La résolution du système linéaire $MX=0$ est équivalente à la résolution du système $M'X=0$ (car les opérations élémentaires sur les lignes ne changent pas le noyau).
        Le système $M'X=0$ s'écrit :
        $$\begin{cases} 1x + 1y + 1z = 0 \quad (Eq. 1) \\ 0x + 1y + 2z = 0 \quad (Eq. 2) \\ 0x + 0y + 0z = 0 \quad (Eq. 3) \end{cases}$$
        À partir de $(Eq. 2)$, nous avons $y + 2z = 0$, ce qui implique $y = -2z$.
        Substituons cette expression de $y$ dans $(Eq. 1)$ :
        $$x + (-2z) + z = 0$$
        $$x - z = 0$$
        $$x = z$$
        Les solutions sont donc de la forme $X = \begin{pmatrix} z \\ -2z \\ z \end{pmatrix}$ pour tout $z \in \mathbb{R}$.
        Nous pouvons factoriser $z$ :
        $$X = z \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix}$$
        Le noyau de $M$ est l'ensemble des multiples du vecteur $\begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix}$.
        Une base du noyau de $M$ est donc le singleton $\left\{ \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix} \right\}$.

    3.  **Vérification du théorème du rang :**
        Le théorème du rang stipule que pour une application linéaire $f: E \to F$ (ou une matrice $A \in \mathcal{M}_{n,p}(\mathbb{K})$), on a $\dim E = \dim(\ker f) + \text{rg } f$.
        Dans notre cas, $M$ est une matrice $3 \times 3$, donc elle représente une application linéaire de $\mathbb{R}^3$ vers $\mathbb{R}^3$. La dimension de l'espace de départ $E = \mathbb{R}^3$ est $p=3$.
        Nous avons trouvé :
        -   $\text{rg } M = 2$
        -   $\dim(\ker M) = 1$ (car le noyau est engendré par un seul vecteur non nul, donc sa dimension est 1).
        Vérifions le théorème du rang :
        $$\dim E = \dim(\ker M) + \text{rg } M$$
        $$3 = 1 + 2$$
        $$3 = 3$$
        L'égalité est vérifiée, ce qui confirme nos calculs.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
-   **Le Pont Théorique :** En Intelligence Artificielle, et plus particulièrement dans les réseaux de neurones profonds, le calcul matriciel est le cœur battant de toutes les opérations. Chaque couche d'un réseau de neurones effectue une transformation linéaire sur ses entrées, suivie d'une activation non linéaire. Ces transformations linéaires sont précisément représentées par des **matrices de poids**. Les "poids" et les "biais" d'un réseau de neurones sont des coefficients matriciels et vectoriels qui sont ajustés pendant l'entraînement. L'inférence (le processus de faire une prédiction avec un modèle entraîné) n'est rien d'autre qu'une succession de multiplications matricielles et d'additions vectorielles.
-   **Exemple Concret :**
    *   **Inférence et Entraînement :** Considérons une couche dense (ou *fully connected*) d'un réseau de neurones. Si l'entrée est un vecteur $x \in \mathbb{R}^p$ et la sortie est un vecteur $h \in \mathbb{R}^n$, la transformation linéaire est donnée par $h = Wx + b$, où $W \in \mathcal{M}_{n,p}(\mathbb{R})$ est la matrice des poids et $b \in \mathbb{R}^n$ est le vecteur de biais. La multiplication matricielle $Wx$ est l'opération fondamentale. Lors de l'entraînement, les gradients sont calculés via la règle de la chaîne, qui implique également des multiplications matricielles (ou des produits de Jacobi, qui sont des généralisations matricielles).
    *   **Accélération GPU :** Les unités de traitement graphique (GPU) sont devenues indispensables pour l'entraînement des modèles d'IA car leur architecture parallèle est spécifiquement optimisée pour effectuer des millions de multiplications matricielles en virgule flottante par seconde (FLOPS). C'est la raison principale de leur efficacité pour les calculs massifs requis par les réseaux de neurones.
    *   **Optimisation des Grands Modèles (LLM) :** Les grands modèles de langage (LLM) comme GPT-3 ou Llama ont des milliards de paramètres, principalement stockés dans d'énormes matrices de poids. Pour les adapter à des tâches spécifiques (fine-tuning) sans avoir à entraîner tout le modèle, des techniques comme **LoRA (Low-Rank Adaptation)** sont utilisées. LoRA propose de ne pas modifier directement la matrice de poids $W$ d'origine, mais d'ajouter une petite matrice de "mise à jour" $W' = W + BA$, où $B \in \mathcal{M}_{n,r}(\mathbb{R})$ et $A \in \mathcal{M}_{r,p}(\mathbb{R})$ avec $r \ll \min(n,p)$. Le produit $BA$ est une matrice de rang faible (au plus $r$). Au lieu d'apprendre $n \times p$ paramètres pour $W'$, on n'apprend que $n \times r + r \times p$ paramètres pour $B$ et $A$, ce qui réduit drastiquement le nombre de paramètres à entraîner et la mémoire requise, tout en conservant une grande partie de la performance. C'est une application directe et sophistiquée des concepts de rang et de produit matriciel.

## 6. Liens Sémantiques & Maillage Obsidian
-   **Concepts Précédents requis :** [[Jalon-7 (Espaces vectoriels abstraits)]], [[Jalon-8 (Applications linéaires)]]
-   **Concepts Futurs dépendants :** [[Jalon 10 (Changements de base)]], [[Jalon 29 (Éléments propres)]], [[Jalon 43 (Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.)]]
