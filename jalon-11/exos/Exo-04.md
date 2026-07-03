# Exercice 4: Base duale avec changement de base
## Énoncé
Soit $E = \mathbb{R}^3$ et sa base canonique $\mathcal{B} = (e_1, e_2, e_3)$. On considère les vecteurs :
$u_1 = (1, 1, 1)$, $u_2 = (1, 1, 0)$, $u_3 = (1, 0, 0)$
1. Montrer que $\mathcal{C} = (u_1, u_2, u_3)$ est une base de $E$.
2. Déterminer les formes linéaires constituant la base duale $\mathcal{C}^* = (u_1^*, u_2^*, u_3^*)$ exprimées dans la base duale $\mathcal{B}^* = (e_1^*, e_2^*, e_3^*)$.


## Correction détaillée
1. **Base de $E$ :**
   La dimension de $\mathbb{R}^3$ est 3. Il suffit de montrer que la famille $(u_1, u_2, u_3)$ est libre.
   Soient $\lambda_1, \lambda_2, \lambda_3 \in \mathbb{R}$ tels que $\lambda_1 u_1 + \lambda_2 u_2 + \lambda_3 u_3 = (0, 0, 0)$.
   $(\lambda_1 + \lambda_2 + \lambda_3, \lambda_1 + \lambda_2, \lambda_1) = (0, 0, 0)$
   Ce qui donne le système échelonné :
   $\lambda_1 = 0$
   $\lambda_1 + \lambda_2 = 0 \implies \lambda_2 = 0$
   $\lambda_1 + \lambda_2 + \lambda_3 = 0 \implies \lambda_3 = 0$
   La famille est libre et contient 3 vecteurs, c'est une base de $E$.

2. **Recherche de la base duale $\mathcal{C}^*$ :**
   Soit $\varphi(x, y, z) = ax + by + cz = a e_1^* + b e_2^* + c e_3^*$.
   Cherchons $u_1^*$ tel que $u_1^*(u_1)=1, u_1^*(u_2)=0, u_1^*(u_3)=0$.
   $u_1^*(1,0,0) = a = 0$
   $u_1^*(1,1,0) = a + b = 0 \implies b = 0$
   $u_1^*(1,1,1) = a + b + c = 1 \implies c = 1$
   Donc $u_1^* = e_3^*$.

   Cherchons $u_2^*$ tel que $u_2^*(u_1)=0, u_2^*(u_2)=1, u_2^*(u_3)=0$.
   $u_2^*(1,0,0) = a = 0$
   $u_2^*(1,1,0) = a + b = 1 \implies b = 1$
   $u_2^*(1,1,1) = a + b + c = 0 \implies 0 + 1 + c = 0 \implies c = -1$
   Donc $u_2^* = e_2^* - e_3^*$.

   Cherchons $u_3^*$ tel que $u_3^*(u_1)=0, u_3^*(u_2)=0, u_3^*(u_3)=1$.
   $u_3^*(1,0,0) = a = 1$
   $u_3^*(1,1,0) = a + b = 0 \implies 1 + b = 0 \implies b = -1$
   $u_3^*(1,1,1) = a + b + c = 0 \implies 1 - 1 + c = 0 \implies c = 0$
   Donc $u_3^* = e_1^* - e_2^*$.

   Conclusion : La base duale est $(e_3^*, e_2^* - e_3^*, e_1^* - e_2^*)$.
