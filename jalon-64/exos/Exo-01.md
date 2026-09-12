# Exercice 1 : Monotonie de la mesure extérieure

**Difficulté :** $\bigstar\star\star\star\star$

Démontrer rigoureusement à partir de la définition que si $A \subset B \subset \mathbb{R}$, alors $\lambda^*(A) \le \lambda^*(B)$.

**Correction Détaillée :**
Par définition, $\lambda^*(B) = \inf \left\lbrace \sum_{n=1}^\infty \ell(I_n) \mid B \subset \bigcup_{n=1}^\infty I_n \right\rbrace$.
Soit $(I_n)$ un recouvrement dénombrable ouvert arbitraire de $B$. Puisque $A \subset B$, ce même recouvrement $(I_n)$ recouvre également $A$. Ainsi, l'ensemble des recouvrements de $B$ est inclus dans l'ensemble des recouvrements de $A$. L'infimum sur un surensemble est nécessairement plus petit ou égal. D'où $\lambda^*(A) \le \lambda^*(B)$.
