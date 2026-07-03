---
uuid: "exo-11-03"
title: "Exercice 3: Base duale d'une famille de polynômes"
---
# Exercice 3: Base duale d'une famille de polynômes (Difficulté $\star \star \star$)

## Énoncé
Dans l'espace vectoriel $E = \mathbb{R}_2[X]$ des polynômes de degré inférieur ou égal à 2, on considère la famille $\mathcal{B} = (P_0, P_1, P_2)$ où $P_0(X) = 1$, $P_1(X) = X-1$, et $P_2(X) = (X-1)^2$. Montrer que $\mathcal{B}$ est une base et déterminer la base duale $\mathcal{B}^* = (P_0^*, P_1^*, P_2^*)$.

## Correction détaillée

1. **Démonstration de la liberté de $\mathcal{B}$ :**
   Soient $\lambda_0, \lambda_1, \lambda_2 \in \mathbb{R}$ tels que $\lambda_0 P_0 + \lambda_1 P_1 + \lambda_2 P_2 = 0_E$.
   Cela signifie que pour tout réel $x$, le polynôme s'annule :
   $$\lambda_0 + \lambda_1(x-1) + \lambda_2(x-1)^2 = 0$$
   L'évaluation en $x=1$ donne : $\lambda_0 = 0$.
   En dérivant l'expression polynomiale formellement, nous obtenons :
   $$\lambda_1 + 2\lambda_2(x-1) = 0$$
   L'évaluation en $x=1$ de la dérivée donne : $\lambda_1 = 0$.
   En dérivant une seconde fois : $2\lambda_2 = 0 \implies \lambda_2 = 0$.
   La famille est libre. De cardinal 3 dans un espace de dimension 3, elle constitue une base.

2. **Recherche de la base duale via les évaluations (formule de Taylor) :**
   Par la formule de Taylor pour les polynômes, tout polynôme $P \in \mathbb{R}_2[X]$ peut s'écrire autour du point $a=1$ :
   $$P(X) = P(1) + P'(1)(X-1) + \frac{P''(1)}{2}(X-1)^2$$
   Substituons avec les vecteurs de notre base :
   $$P(X) = P(1) P_0(X) + P'(1) P_1(X) + \frac{P''(1)}{2} P_2(X)$$
   Par identification avec la décomposition unique dans la base $\mathcal{B}$ : $P = P_0^*(P) P_0 + P_1^*(P) P_1 + P_2^*(P) P_2$, nous identifions les formes coordonnées.

3. **Vérification de l'action des formes trouvées sur la base :**
   - Soit $P_0^*(P) = P(1)$. On a $P_0^*(P_0) = 1$, $P_0^*(P_1) = 0$, $P_0^*(P_2) = 0$. C'est correct.
   - Soit $P_1^*(P) = P'(1)$. On a $P_1^*(P_0) = 0$, $P_1^*(P_1) = 1$, $P_1^*(P_2) = 2 \times 0 = 0$. C'est correct.
   - Soit $P_2^*(P) = \frac{1}{2}P''(1)$. On a $P_2^*(P_0) = 0$, $P_2^*(P_1) = 0$, $P_2^*(P_2) = \frac{1}{2} \times 2 = 1$. C'est correct.

**Conclusion :**
La base duale $(P_0^*, P_1^*, P_2^*)$ est formellement caractérisée par les applications : $P \mapsto P(1)$, $P \mapsto P'(1)$ et $P \mapsto \frac{P''(1)}{2}$.
