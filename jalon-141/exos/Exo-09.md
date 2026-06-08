# Exercice 9 : Rôle de l'union Bound
**Énoncé :** Démontrer le lemme de la borne de l'union pour la probabilité de l'événement suprémum sur un ensemble fini d'événements.
**Correction Détaillée :**
* *Analyse de l'énoncé :* Montrer $P(\cup_{k=1}^m A_k) \le \sum P(A_k)$.
* *Résolution pas-à-pas :*
Soit une collection finie d'événements $A_1, A_2, \dots, A_m$ dans un espace probabilisé $(\Omega, \mathcal{A}, P)$.
On procède par récurrence sur $m$.
**Initialisation :** Pour $m=2$. $A_1 \cup A_2 = A_1 \cup (A_2 \setminus A_1)$.
Puisque $A_1$ et $A_2 \setminus A_1$ sont disjoints, par l'axiome d'additivité des probabilités :
$$P(A_1 \cup A_2) = P(A_1) + P(A_2 \setminus A_1)$$
Or, $A_2 \setminus A_1 \subseteq A_2$. Par monotonie de la mesure de probabilité, $P(A_2 \setminus A_1) \le P(A_2)$.
Donc :
$$P(A_1 \cup A_2) \le P(A_1) + P(A_2)$$
L'hypothèse est vraie au rang 2.

**Hérédité :** Supposons la propriété vraie au rang $m$. Soit $m+1$ événements.
$$P\left( \bigcup_{k=1}^{m+1} A_k \right) = P\left( \left( \bigcup_{k=1}^m A_k \right) \cup A_{m+1} \right)$$
Par la propriété au rang 2 :
$$P\left( \bigcup_{k=1}^{m+1} A_k \right) \le P\left( \bigcup_{k=1}^m A_k \right) + P(A_{m+1})$$
Par l'hypothèse de récurrence sur l'union des $m$ événements :
$$P\left( \bigcup_{k=1}^{m+1} A_k \right) \le \sum_{k=1}^m P(A_k) + P(A_{m+1}) = \sum_{k=1}^{m+1} P(A_k)$$
La propriété est démontrée. Ceci justifie le passage $P(\sup_{f \in \mathcal{F}_n} |P_n(f)-P(f)| > t) \le \sum_{f} P(|P_n(f)-P(f)| > t)$ dans la preuve conditionnelle de Vapnik. $\blacksquare$
