\subsection*{Exercice 5 : Séparabilité de $L^p$ pour $1 \le p < \infty$ \quad $\bigstar\bigstar\bigstar$}
**Énoncé :**
Montrer que l'espace $L^p(\mathbb{R})$ est séparable (il admet un sous-ensemble dénombrable dense) pour $1 \le p < \infty$.

**Correction détaillée :**
1. D'après l'exercice précédent, l'espace $C_c(\mathbb{R})$ des fonctions continues à support compact est dense dans $L^p(\mathbb{R})$.
2. On considère l'ensemble $D$ des fonctions en escalier dont les intervalles sont à bornes rationnelles et dont les valeurs sont rationnelles.
   Toute fonction en escalier s'écrit $\sum q_i \mathbf{1}_{[a_i, b_i[}$. L'ensemble des bornes $(a_i, b_i) \in \mathbb{Q}^2$ et $q_i \in \mathbb{Q}$ est dénombrable. Donc $D$ est dénombrable.
3. Soit $f \in C_c(\mathbb{R})$. Elle est uniformément continue car à support compact. Pour tout $\varepsilon > 0$, on peut approcher $f$ uniformément à $\varepsilon$ près par une fonction en escalier $g$ (en découpant le support en intervalles suffisamment petits).
   On peut ensuite approcher $g$ par une fonction $h \in D$ en prenant des bornes rationnelles très proches de celles de $g$ et des valeurs rationnelles très proches des hauteurs de $g$.
4. L'approximation uniforme sur un support compact $K$ implique l'approximation dans $L^p$ puisque $\int_K |f-h|^p \le \varepsilon^p \mu(K)$.
   Ainsi, $D$ est dense dans $C_c(\mathbb{R})$ (pour la norme $L^p$) et donc dense dans $L^p(\mathbb{R})$.
   L'espace $L^p(\mathbb{R})$ est donc séparable. \qed
