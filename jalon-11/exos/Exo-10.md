# Exercice 10: Polynômes de Lagrange et dualité
## Énoncé
Dans $E = \mathbb{R}_{n-1}[X]$, on se donne $n$ scalaires distincts $a_1, \dots, a_n$. Montrer que les formes linéaires d'évaluation $\phi_i(P) = P(a_i)$ forment une base de $E^*$.

## Correction détaillée
1. **Étape 1:** La dimension de $E$ est $n$, donc $\dim E^* = n$. Pour démontrer qu'une famille de $n$ vecteurs forme une base, il suffit de montrer que la famille $(\phi_1, \dots, \phi_n)$ est libre.
2. **Étape 2:** Supposons une combinaison linéaire nulle: $\sum_{i=1}^n \lambda_i \phi_i = 0$. Cela signifie que pour tout polynôme $P \in E$, $\sum_{i=1}^n \lambda_i P(a_i) = 0$.
3. **Étape 3:** On introduit les polynômes interpolateurs de Lagrange $L_j(X) = \prod_{k \neq j} \frac{X-a_k}{a_j-a_k}$. Ce sont des éléments de $E$ car leur degré est exactement $n-1$.
4. **Étape 4:** Par construction, $L_j(a_i) = \delta_{ij}$ (vaut 1 si $i=j$, 0 sinon).
5. **Étape 5:** Évaluons la combinaison linéaire nulle sur le polynôme $L_j$ :
   $$0 = \sum_{i=1}^n \lambda_i \phi_i(L_j) = \sum_{i=1}^n \lambda_i L_j(a_i) = \lambda_j$$
6. **Conclusion:** Pour tout indice $j$, on obtient $\lambda_j = 0$. La famille est donc libre, et c'est par conséquent une base. Les polynômes $(L_j)$ forment précisément la base antéduale associée.
