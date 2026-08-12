# Exercice 4 : Équations différentielles : Formulation intégrale et complétude
**Niveau :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
On s'intéresse à l'équation différentielle $y'(t) = k y(t)$ sur l'intervalle $[0, 1]$ avec $y(0) = y_0$, où $k \in \mathbb{R}$.
1. Réécrire cette équation sous la forme d'une équation de point fixe $y = T(y)$ faisant intervenir un opérateur intégral $T$.
2. Sur l'espace $E = C([0, 1], \mathbb{R})$ muni de la norme $\|y\|_\infty = \max_{t\in[0,1]} |y(t)|$, déterminer sous quelle condition sur $k$ l'opérateur $T$ est contractant.
3. Pour échapper à cette restriction sur $k$, on définit une norme à poids $\|y\|_L = \max_{t\in[0,1]} |y(t) e^{-Lt}|$ pour $L > 0$. Démontrer que pour un choix approprié de $L$, l'opérateur $T$ devient contractant indépendamment de la taille de $k$.

**Démonstration pas à pas :**
1. En intégrant l'équation de $0$ à $t$, le théorème fondamental de l'analyse donne :
   $y(t) - y(0) = \int_0^t y'(s) ds = \int_0^t k y(s) ds$
   Soit l'opérateur $T : E \to E$ défini par $(Ty)(t) = y_0 + \int_0^t k y(s) ds$. L'EDO équivaut à $y = T(y)$.
2. Évaluons $\|Tu - Tv\|_\infty$ pour $u, v \in E$ :
   $|(Tu)(t) - (Tv)(t)| = \left| \int_0^t k (u(s) - v(s)) ds \right| \leq \int_0^t |k| |u(s) - v(s)| ds$
   Puisque $|u(s) - v(s)| \leq \|u - v\|_\infty$ pour tout $s$, on a :
   $|(Tu)(t) - (Tv)(t)| \leq |k| \|u - v\|_\infty \int_0^t 1 ds = |k| t \|u - v\|_\infty \leq |k| \|u - v\|_\infty$
   On prend le max sur $t \in [0, 1]$, et on obtient $\|Tu - Tv\|_\infty \leq |k| \|u - v\|_\infty$.
   Pour que $T$ soit contractant pour cette norme usuelle, il faut impérativement $|k| < 1$.
3. Considérons la norme à poids $\|y\|_L$. L'équivalence avec la norme infinie est évidente car $e^{-L} \|y\|_\infty \leq \|y\|_L \leq \|y\|_\infty$, et $E$ reste donc un espace de Banach pour $\|\cdot\|_L$.
   Évaluons l'action de $T$ :
   $e^{-Lt} |(Tu)(t) - (Tv)(t)| \leq e^{-Lt} \int_0^t |k| |u(s) - v(s)| ds$
   Insérons le poids à l'intérieur de l'intégrale :
   $e^{-Lt} \int_0^t |k| e^{Ls} \left( |u(s) - v(s)| e^{-Ls} \right) ds \leq e^{-Lt} \int_0^t |k| e^{Ls} \|u - v\|_L ds$
   Calculons l'intégrale résiduelle : $\int_0^t e^{Ls} ds = \frac{e^{Lt} - 1}{L} \leq \frac{e^{Lt}}{L}$.
   D'où : $e^{-Lt} |(Tu)(t) - (Tv)(t)| \leq e^{-Lt} |k| \|u - v\|_L \frac{e^{Lt}}{L} = \frac{|k|}{L} \|u - v\|_L$.
   Si l'on choisit un scalaire strict $L > |k|$ (par exemple $L = 2|k|$), le rapport de contraction est $\frac{|k|}{L} < 1$.
   $T$ est donc strictement contractant pour cette norme de Bielecki, ce qui garantit l'existence et l'unicité globale de l'exponentielle (qui est le point fixe) pour tout $k \in \mathbb{R}$.
