---
uuid: exo-08
title: Exercice 8 - Formule du Laplacien
---

# Exercice 8 : Démonstration de la Formule Fondamentale du Laplacien

**Énoncé :**
Soit $G = (V,E)$ un graphe non orienté avec $n = |V|$ sommets, de matrice d'adjacence $A$ et de matrice des degrés $D$. Le laplacien est $L = D - A$.
Démontrer méticuleusement que pour tout vecteur $x = (x_1, \dots, x_n)^T \in \mathbb{R}^n$,
$$x^T L x = \sum_{\{i,j\} \in E} (x_i - x_j)^2$$
En déduire que $L$ est semi-définie positive.

**Correction Détaillée :**

*   *Analyse de l'énoncé :* Il s'agit de développer l'expression matricielle pour retomber sur une somme de carrés. Il faut faire attention au fait que $G$ est non orienté et ne possède pas de boucles.

*   *Résolution pas-à-pas :*
1. **Initialisation :**
   Exprimons $x^T L x$ composante par composante.
   $L$ est une matrice $n \times n$. On sait que :
   $x^T L x = \sum_{i=1}^n \sum_{j=1}^n L_{ij} x_i x_j$

2. **Étape 1 : Séparation des termes diagonaux et hors diagonale :**
   $x^T L x = \sum_{i=1}^n L_{ii} x_i^2 + \sum_{i=1}^n \sum_{\substack{j=1 \\ j \neq i}}^n L_{ij} x_i x_j$

3. **Étape 2 : Remplacement par les coefficients de $D$ et $A$ :**
   Par définition de $L = D - A$, nous avons :
   - Sur la diagonale ($i = j$) : $L_{ii} = D_{ii} - A_{ii}$. Comme il n'y a pas de boucles, $A_{ii} = 0$, donc $L_{ii} = D_{ii} = d_i$ (le degré du sommet $i$).
   - Hors diagonale ($i \neq j$) : $L_{ij} = D_{ij} - A_{ij}$. Or $D$ est diagonale, donc $D_{ij} = 0$. Ainsi $L_{ij} = -A_{ij}$.
   En remplaçant, on obtient :
   $x^T L x = \sum_{i=1}^n d_i x_i^2 - \sum_{i=1}^n \sum_{\substack{j=1 \\ j \neq i}}^n A_{ij} x_i x_j$

4. **Étape 3 : Reformulation des termes :**
   Le degré $d_i$ est le nombre de voisins de $i$, qui s'écrit formellement :
   $d_i = \sum_{j=1}^n A_{ij}$ (la somme sur $j$ de $A_{ij}$ compte 1 pour chaque voisin).
   Nous pouvons donc réécrire le premier terme :
   $\sum_{i=1}^n d_i x_i^2 = \sum_{i=1}^n \left( \sum_{j=1}^n A_{ij} \right) x_i^2 = \sum_{i=1}^n \sum_{j=1}^n A_{ij} x_i^2$

   L'expression devient :
   $x^T L x = \sum_{i=1}^n \sum_{j=1}^n A_{ij} x_i^2 - \sum_{i=1}^n \sum_{j=1}^n A_{ij} x_i x_j$
   (Ici on a ajouté $j=i$ dans la deuxième somme, car $A_{ii}=0$, donc on ne change pas la valeur totale).

5. **Étape 4 : Symétrie et regroupement :**
   On a donc :
   $x^T L x = \sum_{i=1}^n \sum_{j=1}^n A_{ij} (x_i^2 - x_i x_j)$

   Étant donné que le graphe est non orienté, $A_{ij} = A_{ji}$. On peut échanger les indices $i$ et $j$ sans changer la valeur de la somme :
   $x^T L x = \sum_{j=1}^n \sum_{i=1}^n A_{ji} (x_j^2 - x_j x_i) = \sum_{i=1}^n \sum_{j=1}^n A_{ij} (x_j^2 - x_i x_j)$

   On peut alors faire la moyenne des deux expressions obtenues :
   $x^T L x = \frac{1}{2} x^T L x + \frac{1}{2} x^T L x$
   $x^T L x = \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n A_{ij} (x_i^2 - x_i x_j) + \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n A_{ij} (x_j^2 - x_i x_j)$
   $x^T L x = \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n A_{ij} \left( x_i^2 - x_i x_j + x_j^2 - x_i x_j \right)$
   $x^T L x = \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n A_{ij} (x_i^2 - 2 x_i x_j + x_j^2)$
   $x^T L x = \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n A_{ij} (x_i - x_j)^2$

6. **Conclusion :**
   La somme double $\sum_{i=1}^n \sum_{j=1}^n$ compte chaque arête $\{i,j\}$ deux fois : une fois pour $A_{ij}$ et une fois pour $A_{ji}$. Puisque $A_{ij}=1$ si et seulement si $\{i,j\} \in E$, et que le facteur $\frac{1}{2}$ corrige le double comptage, on a finalement :
   $$x^T L x = \sum_{\{i,j\} \in E} (x_i - x_j)^2$$

   Comme $(x_i - x_j)^2 \geq 0$ pour tous $x_i, x_j \in \mathbb{R}$, on a $x^T L x \geq 0$ pour tout $x \in \mathbb{R}^n$.
   La matrice $L$ est par conséquent semi-définie positive.
