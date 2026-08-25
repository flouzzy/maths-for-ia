## Exercice 7 : Linéarité (Cas partiel) \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :** Soient $s, t \in \mathcal{S}_+$ deux fonctions simples. Montrer par un calcul direct que $\int (s + t) d\mu = \int s d\mu + \int t d\mu$.

**Correction Détaillée :**
1. Soit $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ et $t = \sum_{j=1}^m b_j \mathbf{1}_{B_j}$, où les $(A_i)$ forment une partition de $X$, et les $(B_j)$ forment une partition de $X$.
2. Les ensembles $C_{i,j} = A_i \cap B_j$ (pour $1 \le i \le n$, $1 \le j \le m$) forment une nouvelle partition plus fine de $X$.
3. Sur chaque sous-ensemble $C_{i,j}$, les fonctions sont constantes : $s$ y vaut $a_i$, $t$ y vaut $b_j$, et donc $s+t$ y vaut $a_i + b_j$.
4. On peut réécrire $s$ et $t$ en utilisant cette partition commune :
   $$s = \sum_{i=1}^n \sum_{j=1}^m a_i \mathbf{1}_{C_{i,j}} \quad \text{et} \quad t = \sum_{i=1}^n \sum_{j=1}^m b_j \mathbf{1}_{C_{i,j}}$$
5. L'intégrale de $s+t$ est :
   $$\int (s+t) d\mu = \sum_{i,j} (a_i + b_j) \mu(C_{i,j}) = \sum_{i,j} a_i \mu(C_{i,j}) + \sum_{i,j} b_j \mu(C_{i,j})$$
6. D'autre part, comme les $(B_j)$ partitonnent $X$, $\sum_j \mu(C_{i,j}) = \sum_j \mu(A_i \cap B_j) = \mu(A_i)$. De même $\sum_i \mu(C_{i,j}) = \mu(B_j)$.
7. Ainsi, $\sum_{i,j} a_i \mu(C_{i,j}) = \sum_i a_i \mu(A_i) = \int s d\mu$, et $\sum_{i,j} b_j \mu(C_{i,j}) = \sum_j b_j \mu(B_j) = \int t d\mu$.
8. On obtient bien $\int (s+t) d\mu = \int s d\mu + \int t d\mu$.
