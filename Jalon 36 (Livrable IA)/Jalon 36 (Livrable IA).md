---
uuid: "jalon-36"
title: "Livrable IA T3 : Décomposition en valeurs singulières (SVD) et compression d'image"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/compression
prev: "[[Jalon 35 (Caractérisation séquentielle des ouverts).md]]"
next: "[[Jalon 37 (Intégrale de Riemann sur un segment).md]]"
---

# Jalon 36 : Livrable IA T3 : Décomposition en valeurs singulières (SVD) et compression d'image

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous ayez une photo numérique. C'est en fait une grille géante de nombres (des pixels). La **SVD** est un outil magique qui permet de décomposer cette photo complexe en une somme de "couches" de plus en plus simples. Les premières couches contiennent les formes principales (les visages, les horizons), tandis que les dernières couches ne contiennent que des détails insignifiants ou du bruit. Pour compresser l'image, on décide simplement de jeter les couches de détails et de ne garder que les couches essentielles.
- **Le "Pourquoi on a inventé ça" :** Contrairement à la diagonalisation classique, qui ne marche que pour les matrices carrées et très spéciales, la SVD fonctionne sur **n'importe quelle matrice**, même rectangulaire. C'est le "couteau suisse" ultime de l'algèbre linéaire pour extraire l'information importante d'un jeu de données.
- **Visualisation :** Toute transformation géométrique (une matrice $A$) peut être vue comme la succession de trois étapes :
    1. Une première rotation (on tourne l'image).
    2. Un étirement selon les axes principaux (on déforme l'image pour en faire une ellipse).
    3. Une seconde rotation (on tourne à nouveau l'image finale).

## 2. Formalisation & Rigueur Académique

### A. Théorème de la Décomposition en Valeurs Singulières (SVD)

Soit $A \in \mathcal{M}_{m,n}(\mathbb{R})$ une matrice réelle de taille $m \times n$.

> **Théorème Fondamental (SVD) :**
> Il existe une matrice orthogonale $U \in \mathcal{M}_m(\mathbb{R})$, une matrice orthogonale $V \in \mathcal{M}_n(\mathbb{R})$ et une matrice "diagonale" $\Sigma \in \mathcal{M}_{m,n}(\mathbb{R})$ telles que :
> $$A = U \Sigma V^T$$
> Les coefficients diagonaux $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_p \ge 0$ (où $p = \min(m, n)$) de $\Sigma$ sont appelés les **valeurs singulières** de $A$.

> **Propriétés des matrices de la SVD :**
> - Les colonnes de $U$ ($u_i$) sont les **vecteurs singuliers à gauche**. Ce sont les vecteurs propres de $A A^T$.
> - Les colonnes de $V$ ($v_i$) sont les **vecteurs singuliers à droite**. Ce sont les vecteurs propres de $A^T A$.
> - Les valeurs singulières $\sigma_i$ sont les racines carrées des valeurs propres non nulles de $A^T A$ (ou de $A A^T$).

### B. Approximation de Rang Faible (Théorème d'Eckart-Young)

> **Théorème :**
> Soit $k < \text{rg}(A)$. La meilleure approximation de $A$ par une matrice de rang $k$ (au sens de la norme de Frobenius) est donnée par :
> $$A_k = \sum_{i=1}^k \sigma_i u_i v_i^T$$
> On ne conserve que les $k$ plus grandes valeurs singulières.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration de l'existence de la SVD (Cas $m \ge n$)

1. **Construction de V :**
   Considérons la matrice $S = A^T A \in \mathcal{M}_n(\mathbb{R})$. $S$ est une matrice symétrique réelle car $S^T = (A^T A)^T = A^T A = S$. De plus, $S$ est semi-définie positive car $x^T S x = \|Ax\|^2 \ge 0$.
   D'après le **théorème spectral** (Jalon 32), il existe une base orthonormée de vecteurs propres $(v_1, \dots, v_n)$ associée aux valeurs propres $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n \ge 0$.
   Posons $V = [v_1 | \dots | v_n]$. $V$ est orthogonale.

2. **Calcul des valeurs singulières :**
   Posons $\sigma_i = \sqrt{\lambda_i}$. Soit $r$ le rang de $A$, tel que $\sigma_1 \ge \dots \ge \sigma_r > 0$ et $\sigma_{r+1} = \dots = \sigma_n = 0$.

3. **Construction de U :**
   Pour $i \in \{1, \dots, r\}$, définissons $u_i = \frac{1}{\sigma_i} A v_i$.
   Vérifions que les $u_i$ sont orthonormés :
   $$\langle u_i, u_j \rangle = \frac{1}{\sigma_i \sigma_j} (A v_i)^T (A v_j) = \frac{1}{\sigma_i \sigma_j} v_i^T (A^T A) v_j = \frac{1}{\sigma_i \sigma_j} v_i^T (\lambda_j v_j) = \frac{\lambda_j}{\sigma_i \sigma_j} \delta_{ij} = \delta_{ij}$$
   On complète $(u_1, \dots, u_r)$ en une base orthonormée de $\mathbb{R}^m$ pour former la matrice $U$.

4. **Vérification de la décomposition :**
   Par construction, $A v_i = \sigma_i u_i$ pour $i \le r$ et $A v_i = 0$ pour $i > r$.
   Cela se traduit matriciellement par $A V = U \Sigma$, soit $A = U \Sigma V^T$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Calcul de SVD d'une matrice 2x2
**Énoncé :** Trouver la SVD de $A = \begin{pmatrix} 3 & 0 \\ 0 & -2 \end{pmatrix}$.

**Correction Détaillée :**
1. **$A^T A = \begin{pmatrix} 9 & 0 \\ 0 & 4 \end{pmatrix}$**. Valeurs propres $\lambda_1=9, \lambda_2=4$.
2. **Valeurs singulières :** $\sigma_1 = \sqrt{9}=3, \sigma_2 = \sqrt{4}=2$.
3. **Vecteurs singuliers à droite (V) :** $v_1 = (1, 0), v_2 = (0, 1)$. Donc $V = I_2$.
4. **Vecteurs singuliers à gauche (U) :**
   $u_1 = \frac{1}{\sigma_1} A v_1 = \frac{1}{3} \begin{pmatrix} 3 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
   $u_2 = \frac{1}{\sigma_2} A v_2 = \frac{1}{2} \begin{pmatrix} 0 \\ -2 \end{pmatrix} = \begin{pmatrix} 0 \\ -1 \end{pmatrix}$.
5. **Résultat :** $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}^T$.

### Exercice 2 : Compression d'image théorique
**Énoncé :** Une image de $1000 \times 1000$ pixels consomme $10^6$ coefficients. Si on garde 50 valeurs singulières, quel est le taux de compression ?

**Correction Détaillée :**
* *Matrices stockées :* $U_k$ ($1000 \times 50$), $\Sigma_k$ ($50$), $V_k$ ($1000 \times 50$).
* *Nombre de coefficients :* $1000 \times 50 + 50 + 1000 \times 50 \approx 100,000$.
* *Ratio :* $100,000 / 1,000,000 = 1/10$.
**Conclusion :** On a réduit le poids de l'image par 10 en ne gardant que les 50 structures les plus importantes.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** La SVD est la base mathématique de la **PCA** (Analyse en Composantes Principales) mais aussi de la **Réduction de Dimension**. Elle permet de projeter des données de haute dimension vers un espace plus petit en perdant le minimum d'information.
- **Exemple Concret :**
    - **Compression d'Image :** Dans les formats comme JPEG (via la DCT, proche de la SVD), on élimine les hautes fréquences (petites valeurs singulières).
    - **Systèmes de Recommandation (Netflix) :** La matrice "Utilisateurs x Films" est décomposée par SVD. Les vecteurs $u_i$ représentent des profils d'utilisateurs types et $v_i$ des genres de films types. On peut alors prédire une note en faisant un produit scalaire dans cet espace réduit (Latent Semantic Analysis).
    - **Stabilité des Réseaux de Neurones :** On analyse le spectre des valeurs singulières des matrices de poids pour éviter l'explosion ou la disparition du gradient.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 32 (Preuve complète du théorème spectral pour les endomorphismes symétriques.).md]], [[Jalon 33 (Formes quadratiques).md]]
- **Concepts Futurs dépendants :** [[Jalon 48 (Livrable IA).md]], [[Jalon 143 (Théorie spectrale des graphes).md]]
