# Exercice 5 : Densité des fonctions en escalier $\bigstar\bigstar\bigstar\star\star$
Montrer que l'ensemble des fonctions en escalier sur $I_1 = [0,1]$ est dense dans $L^1([0,1])$.

\textbf{Correction détaillée}
Par définition de l'intégrale de Lebesgue, les fonctions étagées (combinaisons linéaires d'indicatrices d'ensembles mesurables) sont denses dans $L^1$.
Un sous-ensemble mesurable $A$ peut être approché en mesure par des unions finies d'intervalles ouverts.
L'indicatrice d'un intervalle est une fonction en escalier.
Donc, pour toute fonction intégrable $f \in L^1([0,1])$ et $\epsilon > 0$, il existe une fonction étagée $\phi = \sum_{i=1}^n c_i \mathbb{I}_{A_i}$ telle que $\|f - \phi\|_1 < \epsilon/2$.
Ensuite, pour chaque $A_i$, il existe une union finie d'intervalles $U_i$ telle que $m(A_i \Delta U_i) < \epsilon / (2n|c_i|)$.
La fonction $\psi = \sum_{i=1}^n c_i \mathbb{I}_{U_i}$ est en escalier.
Par l'inégalité triangulaire, $\|f - \psi\|_1 \le \|f - \phi\|_1 + \|\phi - \psi\|_1 \le \epsilon/2 + \sum |c_i| m(A_i \Delta U_i) < \epsilon$.
