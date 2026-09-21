\subsection*{Exercice 7 : Opérateur de décalage dans $L^p$ \quad $\bigstar\bigstar\star$}
**Énoncé :**
Pour $f \in L^p(\mathbb{R})$ ($1 \le p < \infty$) et $h \in \mathbb{R}$, on définit la translation $\tau_h f(x) = f(x-h)$.
Montrer que l'application $h \mapsto \tau_h f$ est continue de $\mathbb{R}$ dans $L^p(\mathbb{R})$, c'est-à-dire $\lim_{h \to 0} \|\tau_h f - f\|_p = 0$.

**Correction détaillée :**
1. On prouve d'abord le résultat pour une fonction $g \in C_c(\mathbb{R})$.
   Soit $K$ le support de $g$. $g$ est uniformément continue, donc $\lim_{h \to 0} \| \tau_h g - g\|_\infty = 0$.
   De plus, pour $h$ assez petit (ex: $|h| \le 1$), les fonctions $\tau_h g - g$ sont à support inclus dans un même compact $K_1 = K + [-1, 1]$.
   $\|\tau_h g - g\|_p^p \le \|\tau_h g - g\|_\infty^p \mu(K_1)$. Comme $\mu(K_1) < \infty$, la norme tend vers 0.
2. Pour $f \in L^p(\mathbb{R})$ quelconque, par densité de $C_c(\mathbb{R})$, il existe $g \in C_c(\mathbb{R})$ telle que $\|f - g\|_p < \varepsilon/3$.
3. On utilise l'inégalité triangulaire :
   $\|\tau_h f - f\|_p \le \|\tau_h f - \tau_h g\|_p + \|\tau_h g - g\|_p + \|g - f\|_p$.
   L'opérateur de translation conserve la norme (mesure invariante), donc $\|\tau_h f - \tau_h g\|_p = \|f - g\|_p < \varepsilon/3$.
4. Pour $h$ suffisamment petit, $\|\tau_h g - g\|_p < \varepsilon/3$ (d'après l'étape 1).
   On a alors $\|\tau_h f - f\|_p < \varepsilon/3 + \varepsilon/3 + \varepsilon/3 = \varepsilon$.
   La translation est donc un opérateur uniformément continu sur $L^p(\mathbb{R})$. \qed
