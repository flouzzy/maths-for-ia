```yaml
uuid: e1f2a3b4-c5d6-7890-1234-567890abcdef
title: "Exercice 3 : Forme quadratique du Laplacien combinatoire et coupures"
```

# Exercice 3 : Forme quadratique du Laplacien combinatoire et coupures

Mes chers étudiants,

Poursuivons notre exploration de la théorie spectrale des graphes en nous penchant sur une propriété fondamentale du Laplacien combinatoire et son lien direct avec la notion de coupure. Cette relation est la pierre angulaire de nombreuses applications, notamment en partitionnement de graphes et en clustering spectral.

---

## Question 1 : Forme quadratique du Laplacien combinatoire

Soit $G=(V,E)$ un graphe simple, non orienté, avec $n = |V|$ sommets. On note $A$ sa matrice d'adjacence et $D$ sa matrice des degrés (matrice diagonale où $D_{uu} = d_u$, le degré du sommet $u$). Le Laplacien combinatoire de $G$ est défini par $L = D - A$.

Montrer que pour tout vecteur $x = (x_1, \dots, x_n)^T \in \mathbb{R}^n$, la forme quadratique associée au Laplacien combinatoire est donnée par :
$$x^T L x = \sum_{(u,v) \in E} (x_u - x_v)^2$$
où la somme est effectuée sur toutes les arêtes $(u,v)$ du graphe $G$.

---

## Question 2 : Application aux coupures de graphes

Soit $G=(V,E)$ un graphe simple, non orienté. Une coupure $(S, \bar{S})$ est une partition des sommets $V$ en deux sous-ensembles non vides $S$ et $\bar{S} = V \setminus S$. La valeur d'une coupure, notée $cut(S, \bar{S})$, est le nombre d'arêtes ayant une extrémité dans $S$ et l'autre dans $\bar{S}$.

Considérons un vecteur de coupure $x_S \in \mathbb{R}^n$ défini par :
$$ (x_S)_u = \begin{cases} 1 & \text{si } u \in S \\ -1 & \text{si } u \in \bar{S} \end{cases} $$

a) Calculer $x_S^T L x_S$ en utilisant la formule établie à la Question 1.

b) Montrer que $x_S^T L x_S = 4 \cdot cut(S, \bar{S})$.

c) Discuter brièvement l'intérêt de cette relation pour l'étude des coupures de graphes, en particulier en lien avec le problème de la coupure minimale (Min-Cut) et les méthodes spectrales.

---

## Correction détaillée

### Correction de la Question 1

Nous voulons montrer que $x^T L x = \sum_{(u,v) \in E} (x_u - x_v)^2$.

Partons de la définition de $L = D - A$.
Alors, la forme quadratique $x^T L x$ peut s'écrire :
$$x^T L x = x^T (D - A) x = x^T D x - x^T A x$$

Calculons chaque terme séparément :

1.  **Terme $x^T D x$ :**
    La matrice $D$ est diagonale, avec $D_{uu} = d_u$ (degré du sommet $u$) et $D_{uv} = 0$ pour $u \neq v$.
    $$x^T D x = \sum_{u \in V} D_{uu} x_u^2 = \sum_{u \in V} d_u x_u^2$$
    Le degré $d_u$ est le nombre d'arêtes incidentes à $u$. On peut donc réécrire la somme en considérant chaque arête. Chaque arête $(u,v)$ contribue à $d_u$ et à $d_v$.
    Ainsi, on peut exprimer $\sum_{u \in V} d_u x_u^2$ comme une somme sur les arêtes :
    $$ \sum_{u \in V} d_u x_u^2 = \sum_{u \in V} \sum_{v \in V, (u,v) \in E} x_u^2 $$
    Dans cette double somme, pour chaque arête $(u,v)$, le terme $x_u^2$ apparaît une fois (quand $u$ est le premier indice) et le terme $x_v^2$ apparaît une fois (quand $v$ est le premier indice). Donc, on peut regrouper les termes par arête :
    $$ \sum_{u \in V} d_u x_u^2 = \sum_{(u,v) \in E} (x_u^2 + x_v^2) $$

2.  **Terme $x^T A x$ :**
    La matrice d'adjacence $A$ a $A_{uv} = 1$ si $(u,v) \in E$ et $A_{uv} = 0$ sinon. Puisque le graphe est non orienté, $A$ est symétrique ($A_{uv} = A_{vu}$).
    $$x^T A x = \sum_{u \in V} \sum_{v \in V} A_{uv} x_u x_v$$
    Puisque $A_{uu}=0$ (graphe simple, pas de boucles) et $A_{uv}=A_{vu}=1$ pour les arêtes, chaque arête $(u,v)$ contribue deux fois à la somme (une fois pour $A_{uv}x_u x_v$ et une fois pour $A_{vu}x_v x_u$).
    $$x^T A x = \sum_{(u,v) \in E} 2 x_u x_v$$

Maintenant, combinons les deux termes :
$$x^T L x = \sum_{(u,v) \in E} (x_u^2 + x_v^2) - \sum_{(u,v) \in E} 2 x_u x_v$$
En regroupant les termes sous une seule somme :
$$x^T L x = \sum_{(u,v) \in E} (x_u^2 - 2 x_u x_v + x_v^2)$$
Nous reconnaissons l'identité remarquable $(a-b)^2 = a^2 - 2ab + b^2$ :
$$x^T L x = \sum_{(u,v) \in E} (x_u - x_v)^2$$
Ceci conclut la démonstration de la Question 1.

### Correction de la Question 2

a) **Calcul de $x_S^T L x_S$ :**
Nous utilisons la formule établie à la Question 1 : $x_S^T L x_S = \sum_{(u,v) \in E} ((x_S)_u - (x_S)_v)^2$.
Considérons une arête $(u,v) \in E$. Il y a trois cas possibles pour les positions des sommets $u$ et $v$ par rapport à la coupure $(S, \bar{S})$ :

1.  **Les deux sommets sont dans $S$ :** $u \in S$ et $v \in S$.
    Alors $(x_S)_u = 1$ et $(x_S)_v = 1$.
    Le terme correspondant dans la somme est $((x_S)_u - (x_S)_v)^2 = (1 - 1)^2 = 0^2 = 0$.

2.  **Les deux sommets sont dans $\bar{S}$ :** $u \in \bar{S}$ et $v \in \bar{S}$.
    Alors $(x_S)_u = -1$ et $(x_S)_v = -1$.
    Le terme correspondant dans la somme est $((x_S)_u - (x_S)_v)^2 = (-1 - (-1))^2 = 0^2 = 0$.

3.  **Les sommets sont dans des ensembles différents :** $u \in S$ et $v \in \bar{S}$ (ou vice-versa).
    Alors $(x_S)_u = 1$ et $(x_S)_v = -1$.
    Le terme correspondant dans la somme est $((x_S)_u - (x_S)_v)^2 = (1 - (-1))^2 = (1 + 1)^2 = 2^2 = 4$.

En résumé, seuls les arêtes qui traversent la coupure (c'est-à-dire les arêtes ayant une extrémité dans $S$ et l'autre dans $\bar{S}$) contribuent à la somme, et chaque telle arête contribue une valeur de 4.
Donc, $x_S^T L x_S = \sum_{(u,v) \in E \text{ s.t. } u \in S, v \in \bar{S}} 4$.

b) **Démonstration de $x_S^T L x_S = 4 \cdot cut(S, \bar{S})$ :**
D'après le calcul précédent, $x_S^T L x_S = \sum_{(u,v) \in E \text{ s.t. } u \in S, v \in \bar{S}} 4$.
Le nombre d'arêtes $(u,v)$ telles que $u \in S$ et $v \in \bar{S}$ est précisément la définition de la valeur de la coupure $cut(S, \bar{S})$.
Par conséquent :
$$x_S^T L x_S = 4 \cdot cut(S, \bar{S})$$
Ceci démontre la relation.

c) **Intérêt de cette relation pour l'étude des coupures de graphes :**

Cette relation est d'une importance capitale pour plusieurs raisons :

1.  **Évaluation des coupures :** Elle montre que la forme quadratique du Laplacien combinatoire, évaluée sur un vecteur de coupure binaire spécifique, est directement proportionnelle à la valeur de la coupure. Cela signifie que minimiser $x_S^T L x_S$ pour de tels vecteurs $x_S$ est équivalent à résoudre le problème de la coupure minimale (Min-Cut). Le problème Min-Cut est un problème d'optimisation combinatoire qui, bien que polynomial pour des graphes non pondérés, devient NP-difficile pour des variantes plus complexes ou si l'on cherche des partitions en plus de deux ensembles.

2.  **Relaxation spectrale :** Le problème de la coupure minimale est difficile car le vecteur $x_S$ est contraint à prendre des valeurs discrètes ($+1$ ou $-1$). La théorie spectrale des graphes propose une approche de relaxation. Au lieu de chercher $x_S$ parmi les vecteurs binaires, on cherche un vecteur $x \in \mathbb{R}^n$ qui minimise $x^T L x$ sous des contraintes plus souples, par exemple $x \perp \mathbf{1}$ (où $\mathbf{1}$ est le vecteur de tous les uns) et $\|x\|^2 = n$.
    Le minimum de $x^T L x$ sous ces contraintes est la deuxième plus petite valeur propre du Laplacien, $\lambda_2(L)$ (appelée valeur propre de Fiedler), et le vecteur $x$ qui l'atteint est le vecteur propre de Fiedler.

3.  **Heuristique pour le Min-Cut et le partitionnement :** Bien que le vecteur propre de Fiedler ne soit pas un vecteur binaire, ses composantes peuvent être utilisées pour partitionner le graphe. Par exemple, on peut séparer les sommets en deux ensembles en fonction du signe de leurs composantes dans le vecteur de Fiedler (les sommets $u$ avec $(x_F)_u > 0$ d'un côté, et ceux avec $(x_F)_u \le 0$ de l'autre). Cette méthode, connue sous le nom de partitionnement spectral, fournit souvent des coupures de bonne qualité, même si elles ne sont pas garanties optimales au sens du Min-Cut combinatoire. Elle est à la base de nombreux algorithmes de clustering spectral.

En somme, cette relation fondamentale établit un pont entre une quantité algébrique (la forme quadratique du Laplacien) et une propriété combinatoire du graphe (la valeur d'une coupure), ouvrant la voie à l'utilisation d'outils de l'algèbre linéaire pour l'analyse et l'optimisation des structures de graphes.
