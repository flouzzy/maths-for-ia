# Exercice 6: Indépendance de formes linéaires et polynômes d'interpolation
## Énoncé
Soient $a, b, c$ trois réels distincts. On considère l'espace $E = \mathbb{R}_2[X]$.
On définit les formes linéaires $\varphi_a(P) = P(a)$, $\varphi_b(P) = P(b)$ et $\varphi_c(P) = P(c)$.
Montrer que la famille $(\varphi_a, \varphi_b, \varphi_c)$ est une base de $E^*$. En déduire l'existence et l'unicité des polynômes d'interpolation de Lagrange.


## Correction détaillée
1. **Base de $E^*$ :**
   L'espace $E = \mathbb{R}_2[X]$ est de dimension 3. Son dual $E^*$ est également de dimension 3.
   Il suffit de montrer que la famille de 3 vecteurs $(\varphi_a, \varphi_b, \varphi_c)$ est libre dans $E^*$.
   Soient $\lambda_1, \lambda_2, \lambda_3 \in \mathbb{R}$ tels que $\lambda_1 \varphi_a + \lambda_2 \varphi_b + \lambda_3 \varphi_c = 0_{E^*}$.
   Cela signifie que pour tout polynôme $P \in \mathbb{R}_2[X]$ :
   $\lambda_1 P(a) + \lambda_2 P(b) + \lambda_3 P(c) = 0$.
   Choisissons astucieusement des polynômes pour isoler les coefficients.
   - Posons $P_a(X) = (X-b)(X-c)$. $P_a \in E$.
     L'équation devient $\lambda_1 P_a(a) + \lambda_2(0) + \lambda_3(0) = 0$.
     Comme $a, b, c$ sont distincts, $P_a(a) = (a-b)(a-c) \neq 0$.
     Donc $\lambda_1 = 0$.
   - En choisissant $P_b(X) = (X-a)(X-c)$, on obtient de même $\lambda_2 = 0$.
   - En choisissant $P_c(X) = (X-a)(X-b)$, on obtient $\lambda_3 = 0$.
   La famille est libre. Étant de cardinal 3 dans un espace de dimension 3, c'est une base de $E^*$.

2. **Polynômes de Lagrange :**
   Puisque $(\varphi_a, \varphi_b, \varphi_c)$ est une base de $E^*$, elle correspond à la base duale d'une unique base de $E$, notons-la $(L_a, L_b, L_c)$.
   Par définition de la dualité bidirectionnelle en dimension finie, cette base de $E$ doit vérifier :
   $\varphi_i(L_j) = \delta_{i,j}$.
   C'est-à-dire :
   - $L_a(a) = 1$, $L_a(b) = 0$, $L_a(c) = 0$
   - $L_b(a) = 0$, $L_b(b) = 1$, $L_b(c) = 0$
   - $L_c(a) = 0$, $L_c(b) = 0$, $L_c(c) = 1$
   L'existence et l'unicité de cette base $(L_a, L_b, L_c)$ de polynômes (les polynômes de Lagrange) découlent directement de l'isomorphisme de dualité.
