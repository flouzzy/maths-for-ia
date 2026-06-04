---
uuid: "jalon-9"
title: "Calcul matriciel, opérations, inversibilité et représentations des applications linéaires"
year: 1
trimester: 1
tags:
  - math/algebre-lineaire
  - ia/poids-reseaux
prev: "[[Jalon 8 (Applications linéaires).md]]"
next: "[[Jalon 10 (Changements de base).md]]"
---

# Jalon 9 : Calcul matriciel, opérations, inversibilité et représentations des applications linéaires

## 1. L'Intuition Première (Niveau 12 ans)
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez un tableau de commande pour une usine de peinture. Les colonnes sont les pigments (Rouge, Bleu, Jaune) et les lignes sont les produits finis (Peinture Murs, Peinture Portes). Chaque case du tableau vous dit "combien de ce pigment il faut pour ce produit". Une **matrice**, c'est exactement ça : un tableau de nombres qui sert de "recette" pour transformer une entrée en sortie.
  - La **Multiplication** de matrices, c'est comme combiner deux usines : la sortie de la première usine (pigments) devient l'entrée de la deuxième (peinture).
  - L'**Inversibilité**, c'est savoir si on peut "désassembler" la peinture pour retrouver exactement les pigments de départ sans erreur.
- **Le "Pourquoi on a inventé ça" :** Écrire des listes de transformations pour des milliers de vecteurs prendrait des pages. Les matrices permettent de compresser toute une application linéaire en un seul bloc rectangulaire et d'effectuer des calculs massifs très rapidement.
- **Visualisation :** Une matrice $2 \times 2$ peut être vue comme une déformation de l'espace : elle prend le carré unité et l'étire en un parallélogramme. Si la matrice n'est pas inversible, elle écrase le carré en une simple ligne ou un point (perte d'une dimension).

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soient $n, p \in \mathbb{N}^*$.
1. **Matrice ($M \in \mathcal{M}_{n,p}(\mathbb{K})$) :** Tableau de $n$ lignes et $p$ colonnes à coefficients dans $\mathbb{K}$. On note $A = (a_{i,j})$ où $1 \le i \le n$ (indice de ligne) et $1 \le j \le p$ (indice de colonne).
2. **Produit Matriciel :** Soit $A \in \mathcal{M}_{n,p}(\mathbb{K})$ et $B \in \mathcal{M}_{p,q}(\mathbb{K})$. Le produit $C = AB \in \mathcal{M}_{n,q}(\mathbb{K})$ est défini par :
   $$c_{i,j} = \sum_{k=1}^p a_{i,k} b_{k,j}$$
3. **Inversibilité :** Une matrice carrée $A \in \mathcal{M}_n(\mathbb{K})$ est inversible s'il existe $B \in \mathcal{M}_n(\mathbb{K})$ telle que $AB = BA = I_n$, où $I_n$ est la matrice identité.
4. **Représentation d'une application linéaire :** Soit $f \in \mathcal{L}(E, F)$. Soient $\mathcal{B}_E = (e_1, ..., e_p)$ une base de $E$ et $\mathcal{B}_F = (f_1, ..., f_n)$ une base de $F$. La matrice de $f$ relativement à ces bases, notée $\text{Mat}_{\mathcal{B}_E, \mathcal{B}_F}(f)$, est la matrice dont la $j$-ème colonne est constituée des coordonnées de $f(e_j)$ dans la base $\mathcal{B}_F$.

### B. Théorèmes, Propositions & Lemmes
> **Théorème de l'Isomorphisme de $\mathcal{M}_{n,p}(\mathbb{K})$ :**
> L'application $\Phi : f \mapsto \text{Mat}_{\mathcal{B}_E, \mathcal{B}_F}(f)$ est un isomorphisme d'espaces vectoriels entre $\mathcal{L}(E, F)$ et $\mathcal{M}_{n,p}(\mathbb{K})$.
> De plus, pour la composition : $\text{Mat}(g \circ f) = \text{Mat}(g) \times \text{Mat}(f)$.

> **Caractérisation de l'inversibilité :**
> $A$ est inversible $\iff f$ est un isomorphisme $\iff \det(A) \neq 0 \iff \text{rg}(A) = n$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Matrice d'une composée et produit matriciel
Soient $f : E \to F$ et $g : F \to G$ deux applications linéaires. Soient $\mathcal{B}_E, \mathcal{B}_F, \mathcal{B}_G$ des bases respectives de $E, F$ et $G$.
Montrons que $\text{Mat}_{\mathcal{B}_E, \mathcal{B}_G}(g \circ f) = \text{Mat}_{\mathcal{B}_F, \mathcal{B}_G}(g) \times \text{Mat}_{\mathcal{B}_E, \mathcal{B}_F}(f)$.

1. **Initialisation / Cadre :**
   - Soit $A = \text{Mat}_{\mathcal{B}_F, \mathcal{B}_G}(g) = (a_{i,k}) \in \mathcal{M}_{n,p}$.
   - Soit $B = \text{Mat}_{\mathcal{B}_E, \mathcal{B}_F}(f) = (b_{k,j}) \in \mathcal{M}_{p,q}$.
   - Soient $\mathcal{B}_E = (e_j)_{1 \le j \le q}$, $\mathcal{B}_F = (f_k)_{1 \le k \le p}$, $\mathcal{B}_G = (g_i)_{1 \le i \le n}$.

2. **Étape 1 : Expression des images des vecteurs de base**
   Par définition de la matrice d'une application :
   - $f(e_j) = \sum_{k=1}^p b_{k,j} f_k$ (1)
   - $g(f_k) = \sum_{i=1}^n a_{i,k} g_i$ (2)

3. **Étape 2 : Calcul de $(g \circ f)(e_j)$**
   $(g \circ f)(e_j) = g(f(e_j))$
   En utilisant (1) : $g(\sum_{k=1}^p b_{k,j} f_k)$
   Par linéarité de $g$ : $\sum_{k=1}^p b_{k,j} g(f_k)$
   En utilisant (2) : $\sum_{k=1}^p b_{k,j} \left( \sum_{i=1}^n a_{i,k} g_i \right)$

4. **Étape 3 : Interversion des sommes**
   $(g \circ f)(e_j) = \sum_{k=1}^p \sum_{i=1}^n b_{k,j} a_{i,k} g_i$
   $(g \circ f)(e_j) = \sum_{i=1}^n \left( \sum_{k=1}^p a_{i,k} b_{k,j} \right) g_i$

5. **Conclusion :**
   Le coefficient à la ligne $i$ et colonne $j$ de la matrice de $g \circ f$ est donc $c_{i,j} = \sum_{k=1}^p a_{i,k} b_{k,j}$.
   C'est précisément la définition du produit matriciel $AB$.
   L'égalité $\text{Mat}(g \circ f) = \text{Mat}(g) \times \text{Mat}(f)$ est démontrée.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe (Inversion de matrice 2x2)
**Énoncé :** Soit $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$. Calculer $\det A$ et déterminer $A^{-1}$ par la méthode du pivot de Gauss.
**Correction Détaillée :**
1. **Déterminant :** $\det A = (1 \times 4) - (2 \times 3) = 4 - 6 = -2$. Comme $\det A \neq 0$, $A$ est inversible.
2. **Pivot de Gauss :** On accole l'identité : $\left( \begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 4 & 0 & 1 \end{array} \right)$
3. $L_2 \leftarrow L_2 - 3L_1$ : $\left( \begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & -2 & -3 & 1 \end{array} \right)$
4. $L_2 \leftarrow -1/2 L_2$ : $\left( \begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & 3/2 & -1/2 \end{array} \right)$
5. $L_1 \leftarrow L_1 - 2L_2$ : $\left( \begin{array}{cc|cc} 1 & 0 & 1 - 2(3/2) & 0 - 2(-1/2) \\ 0 & 1 & 3/2 & -1/2 \end{array} \right)$
   $\left( \begin{array}{cc|cc} 1 & 0 & -2 & 1 \\ 0 & 1 & 1.5 & -0.5 \end{array} \right)$
**Conclusion :** $A^{-1} = \begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix}$.

### Exercice 2 : Niveau Avancé (Noyau et Rang matriciel)
**Énoncé :** Soit $M = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{pmatrix}$. Déterminer le rang de $M$ et une base de son noyau.
**Correction Détaillée :**
1. **Échelonnement :**
   - $L_2 \leftarrow L_2 - L_1 : \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 2 & 3 & 4 \end{pmatrix}$
   - $L_3 \leftarrow L_3 - 2L_1 : \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{pmatrix}$
   - $L_3 \leftarrow L_3 - L_2 : \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{pmatrix}$
2. **Rang :** Il y a 2 pivots non nuls. Donc $\text{rg } M = 2$.
3. **Noyau :** Résolvons $MX = 0 \iff \begin{cases} x+y+z=0 \\ y+2z=0 \end{cases}$
   - $y = -2z$
   - $x + (-2z) + z = 0 \implies x = z$
   - $X = \begin{pmatrix} z \\ -2z \\ z \end{pmatrix} = z \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix}$
**Conclusion :** $\ker M = \text{Vect}((1, -2, 1))$. Sa dimension est 1, ce qui concorde avec le théorème du rang ($3 = 2 + 1$).

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** En IA, les **poids d'un réseau de neurones** sont stockés sous forme de matrices. L'inférence (le passage d'une donnée dans le réseau) n'est rien d'autre qu'une suite de multiplications matricielles.
- **Exemple Concret :** L'entraînement des modèles sur **GPU** (unités de traitement graphique) est extrêmement rapide car ces puces sont conçues pour effectuer des millions de **produits matriciels** en parallèle. Chaque couche $h_{l+1} = \sigma(W_l h_l + b_l)$ utilise une matrice de poids $W_l$. Si $W_l$ est de grande taille, on utilise des techniques de **factorisation de matrice** (comme LoRA - Low-Rank Adaptation) pour n'apprendre qu'une petite partie de la matrice, ce qui permet de fine-tuner des modèles géants (LLM) sur du matériel grand public.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 7 (Espaces vectoriels abstraits)]], [[Jalon 8 (Applications linéaires)]]
- **Concepts Futurs dépendants :** [[Jalon 10 (Changements de base)]], [[Jalon 29 (Éléments propres)]], [[Jalon 43 (Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.)]]
