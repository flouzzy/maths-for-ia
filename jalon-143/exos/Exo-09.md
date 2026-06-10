---
uuid: exo-09
title: Exercice 9 - Multiplicité de la valeur propre zéro
---

# Exercice 9 : Multiplicité de la valeur propre 0 et Composantes Connexes

**Énoncé :**
Soit $G = (V, E)$ un graphe non orienté et $L$ son laplacien.
Prouver que la multiplicité de la valeur propre $0$ de la matrice $L$ est exactement égale au nombre de composantes connexes de $G$, noté $k$. (Zéro ellipse mathématique exigée).

**Correction Détaillée :**

*   *Analyse de l'énoncé :* Cet exercice est fondamental en théorie spectrale des graphes. Nous devons faire le lien entre le noyau de $L$ (les vecteurs $x$ tels que $Lx = 0$) et la structure en composantes connexes.
*   *Résolution pas-à-pas :*

1. **Initialisation et caractérisation de $Lx=0$ :**
   Soit $x \in \mathbb{R}^n$. Dire que $0$ est valeur propre de $L$ revient à dire que le noyau $\ker(L)$ n'est pas réduit au vecteur nul.
   Nous savons par la forme quadratique (démontrée dans l'exercice précédent) que :
   $x^T L x = \sum_{\{i,j\} \in E} (x_i - x_j)^2$

   Supposons $x \in \ker(L)$. Alors $Lx = 0$, donc $x^T L x = x^T 0 = 0$.
   Cela donne l'équation :
   $\sum_{\{i,j\} \in E} (x_i - x_j)^2 = 0$

2. **Étape 1 : Implication sur les arêtes :**
   La somme ci-dessus est une somme de termes positifs ou nuls (des carrés réels).
   Une somme de nombres positifs ou nuls est égale à $0$ si et seulement si chaque terme de la somme est égal à $0$.
   Ainsi, pour chaque arête $\{i,j\} \in E$, nous devons avoir $(x_i - x_j)^2 = 0$, ce qui équivaut à $x_i = x_j$.

3. **Étape 2 : Extension aux composantes connexes :**
   Si deux sommets $u$ et $v$ appartiennent à la même composante connexe, il existe un chemin $u = v_0, v_1, v_2, \dots, v_m = v$ dans $G$ reliant $u$ à $v$.
   Puisque $\{v_k, v_{k+1}\} \in E$ pour tout $k$, nous avons :
   $x_{v_0} = x_{v_1} = x_{v_2} = \dots = x_{v_m}$
   Par conséquent, $x_u = x_v$.
   Cela signifie que le vecteur $x$ doit être constant sur chaque composante connexe du graphe $G$.

4. **Étape 3 : Dimension du noyau :**
   Supposons que le graphe $G$ possède $k$ composantes connexes, notées $C_1, C_2, \dots, C_k$.
   D'après ce qui précède, un vecteur $x = (x_1, \dots, x_n)^T$ appartient au noyau de $L$ si et seulement si $x_i$ ne dépend que de la composante connexe à laquelle $i$ appartient.
   Ainsi, il existe des constantes $c_1, c_2, \dots, c_k \in \mathbb{R}$ telles que :
   Pour tout $i \in V$, si $i \in C_m$, alors $x_i = c_m$.

5. **Étape 4 : Construction d'une base du noyau :**
   Définissons $k$ vecteurs indicatrices $u^{(1)}, u^{(2)}, \dots, u^{(k)} \in \mathbb{R}^n$ associés aux $k$ composantes connexes :
   Pour $m \in \{1, \dots, k\}$, la composante $i$ de $u^{(m)}$ est définie par :
   $$u^{(m)}_i = \begin{cases} 1 & \text{si } i \in C_m \\ 0 & \text{sinon} \end{cases}$$

   Tout vecteur $x \in \ker(L)$ peut donc s'écrire de manière unique comme une combinaison linéaire de ces vecteurs indicatrices :
   $x = c_1 u^{(1)} + c_2 u^{(2)} + \dots + c_k u^{(k)}$

6. **Conclusion :**
   La famille $\{u^{(1)}, \dots, u^{(k)}\}$ est une famille génératrice de $\ker(L)$.
   De plus, comme les composantes connexes $C_m$ sont deux à deux disjointes, les vecteurs $u^{(m)}$ ont des supports disjoints, ils sont donc linéairement indépendants.
   Ainsi, $\{u^{(1)}, \dots, u^{(k)}\}$ forme une base de $\ker(L)$.
   La dimension du noyau de $L$, qui correspond à la multiplicité géométrique (et donc algébrique, puisque $L$ est symétrique) de la valeur propre $0$, est exactement la dimension de cet espace, soit $k$.
   La démonstration est achevée.
