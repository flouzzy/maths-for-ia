# Exercice 2 : Opérations algébriques sur les fonctions étagées

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Soient $s_1$ et $s_2$ deux fonctions étagées sur un espace mesurable $(X, \mathcal{A})$. Démontrer en construisant explicitement les ensembles que la somme $s_1 + s_2$ et le produit $s_1 s_2$ sont des fonctions étagées.

**Démonstration :**
Par définition, une fonction est étagée si elle est mesurable et prend un nombre fini de valeurs.
Soit $s_1 = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i}$ et $s_2 = \sum_{j=1}^m \beta_j \mathbf{1}_{B_j}$ les représentations canoniques de $s_1$ et $s_2$.
Ici, les familles $(A_i)_{1 \leq i \leq n}$ et $(B_j)_{1 \leq j \leq m}$ sont des partitions mesurables de $X$.
Considérons l'intersection de ces partitions : pour tout $i \in \{1, \dots, n\}$ et $j \in \{1, \dots, m\}$, on pose $C_{i,j} = A_i \cap B_j$.
Puisque $A_i \in \mathcal{A}$ et $B_j \in \mathcal{A}$, et que $\mathcal{A}$ est une tribu (stable par intersection finie), chaque ensemble $C_{i,j}$ est mesurable.
De plus, la famille $(C_{i,j})_{i,j}$ forme une partition de $X$ :
- Ils sont disjoints : si $(i, j) \neq (i', j')$, par exemple $i \neq i'$, alors $C_{i,j} \cap C_{i',j'} \subseteq A_i \cap A_{i'} = \emptyset$.
- Leur union couvre $X$ : $\bigcup_{i,j} C_{i,j} = \bigcup_{i} (A_i \cap (\bigcup_j B_j)) = \bigcup_i (A_i \cap X) = \bigcup_i A_i = X$.
Sur chaque sous-ensemble de partition $C_{i,j}$, la fonction $s_1$ vaut constamment $\alpha_i$ et la fonction $s_2$ vaut constamment $\beta_j$.
Par conséquent, pour tout $x \in C_{i,j}$, on a $(s_1 + s_2)(x) = \alpha_i + \beta_j$.
Nous pouvons donc écrire la somme sous la forme d'une combinaison linéaire finie d'indicatrices sur des ensembles mesurables :
$$s_1 + s_2 = \sum_{i=1}^n \sum_{j=1}^m (\alpha_i + \beta_j) \mathbf{1}_{C_{i,j}}$$
Cette somme ne prend qu'un nombre fini de valeurs (au maximum $n \times m$) et s'appuie sur une partition mesurable. C'est donc une fonction étagée.
Le raisonnement est strictement identique pour le produit :
$$s_1 s_2 = \sum_{i=1}^n \sum_{j=1}^m (\alpha_i \beta_j) \mathbf{1}_{C_{i,j}}$$
Le produit $s_1 s_2$ est donc également une fonction étagée.
