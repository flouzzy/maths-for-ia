# Exercice 8 : Un sous-ensemble non mesurable (Construction de Vitali)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

Sur l'intervalle $[0, 1]$, on définit la relation d'équivalence $x \sim y \iff x - y \in \mathbb{Q}$. En utilisant l'axiome du choix, soit $V$ un ensemble contenant exactement un représentant de chaque classe d'équivalence. Montrer que $V$ n'est pas Lebesgue-mesurable.

**Correction Détaillée :**
Supposons par l'absurde que $V$ est mesurable.
Considérons les rationnels $q_n$ dans $[-1, 1]$. Définissons les translatés $V_n = V + q_n$.
Les ensembles $V_n$ sont mutuellement disjoints. En effet, si $x \in V_n \cap V_m$, alors $x = v_1 + q_n = v_2 + q_m$, d'où $v_1 - v_2 = q_m - q_n \in \mathbb{Q}$. Ainsi $v_1 \sim v_2$. Puisque $V$ ne contient qu'un représentant par classe, $v_1 = v_2$, d'où $q_n = q_m$ et $n = m$.
De plus, on a $[0, 1] \subset \bigcup V_n \subset [-1, 2]$.
Si $V$ est mesurable, alors par invariance par translation $\lambda(V_n) = \lambda(V)$.
Par $\sigma$-additivité sur cette union disjointe :
$$1 \le \sum_{n=1}^\infty \lambda(V) \le 3$$
Si $\lambda(V) = 0$, la somme vaut 0, ce qui contredit $1 \le 0$.
Si $\lambda(V) > 0$, la somme vaut $+\infty$, ce qui contredit $\infty \le 3$.
Dans tous les cas, une contradiction émerge. Ainsi, $V$ ne peut pas être mesurable.
