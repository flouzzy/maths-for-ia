\subsection*{Exercice 6 : Non-séparabilité de $L^\infty$ \quad $\bigstar\bigstar\bigstar$}
**Énoncé :**
On considère l'espace $L^\infty(\mathbb{R})$.
Pour tout $a \in \mathbb{R}$, on pose $f_a = \mathbf{1}_{[a, a+1]}$.
Montrer que $L^\infty(\mathbb{R})$ n'est pas séparable.

**Correction détaillée :**
1. L'espace $L^\infty$ est muni de la norme $\|f\|_\infty = \text{ess sup} |f(x)|$.
2. Considérons la famille de fonctions $(f_a)_{a \in \mathbb{R}}$.
3. Pour $a \neq b$, l'intersection des supports de $f_a$ et $f_b$ (les intervalles $[a, a+1]$ et $[b, b+1]$) a au plus un élément commun (ou un segment si $|a-b|<1$). Si $0 < |a-b| < 1$, alors la fonction $f_a - f_b$ prend la valeur $1$ sur $[a, b[$ (si $a<b$) et $-1$ sur $]a+1, b+1]$.
   Dans tous les cas, pour $a \neq b$, on a $\|f_a - f_b\|_\infty = 1$.
4. Les boules ouvertes de rayon $1/2$ centrées sur les $f_a$, notées $B(f_a, 1/2)$, sont disjointes car si $g \in B(f_a, 1/2) \cap B(f_b, 1/2)$, on aurait $\|f_a - f_b\|_\infty \le \|f_a - g\|_\infty + \|g - f_b\|_\infty < 1/2 + 1/2 = 1$, ce qui est absurde.
5. Il y a une infinité non dénombrable (indexée par $\mathbb{R}$) de ces boules disjointes. Tout ensemble dense doit posséder au moins un élément dans chaque boule, donc doit être au moins non dénombrable.
   Par conséquent, $L^\infty(\mathbb{R})$ n'est pas séparable. \qed
